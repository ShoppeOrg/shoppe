from django.db import models
from django.db.models.fields import DateTimeField, CharField, DecimalField, IntegerField, TextField
from django.core.validators import  MinValueValidator

class Product(models.Model):
    name = CharField(max_length=150, unique=True)
    price = DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    amount = IntegerField(default=0, validators=[MinValueValidator(0)])
    description = TextField(default="")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<Product {self.id}: ({self.name})>'
    @property
    def in_stock(self):
        return self.amount != 0


