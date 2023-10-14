from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django.db import models
from products.models import Product

from .statuses import OrderStatus


class PhoneNumberValidator(RegexValidator):
    regex = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"


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


class Address(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, blank=True, null=True
    )
    phone_number = models.CharField(validators=[PhoneNumberValidator()])
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    building = models.CharField(max_length=4)
    flat_number = models.CharField(max_length=5, blank=True, null=True)
