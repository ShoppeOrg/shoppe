from django.contrib.auth import get_user_model
from django.db import models

from .statuses import OrderStatus


class Order(models.Model):
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
