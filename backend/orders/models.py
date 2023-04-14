from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from products.models import Product

from .statuses import OrderStatus


class Order(models.Model):
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    goods = models.ManyToManyField(Product, through="OrderProduct")
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
