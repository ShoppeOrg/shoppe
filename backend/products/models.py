from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import ForeignKey, DateTimeField, CharField, DecimalField, IntegerField, TextField, CASCADE
from django.contrib.auth import get_user_model


class Product(models.Model):
    name = CharField(max_length=150, unique=True)
    price = DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    main_image = models.ForeignKey(
        to="pictures.Picture",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    images = models.ManyToManyField(
        to="pictures.Picture",
        related_name="products",
    )
    description = TextField(default="")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Product {self.id}: ({self})>"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        obj, created = ProductInventory.objects.get_or_create(product=self)
        obj.save()

    @property
    def in_stock(self):
        return self.inventory.quantity != 0


class ProductInventory(models.Model):

    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="inventory",
    )
    quantity = IntegerField(default=0, null=False, validators=[MinValueValidator(0)])
    sold_qty = IntegerField(default=0, null=False, validators=[MinValueValidator(0)])
    created_at = DateTimeField(auto_now_add=True, null=False)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = "products_product_inventory"
        ordering = ['-updated_at']

    def __repr__(self):
        return f"<Inventory of {self}>"


class Review(models.Model):

    user = ForeignKey(
        to=get_user_model(),
        on_delete=CASCADE
    )
    rating = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])