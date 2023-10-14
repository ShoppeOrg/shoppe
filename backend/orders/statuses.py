from django.db import models


class OrderStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    PROCESSING = "PROCESSING", "Processing"
    SHIPPED = "SHIPPED", "Shipped"
    DELIVERED = "DELIVERED", "Delivered"
    CANCELLED = "CANCELLED", "Cancelled"
    REFUNDED = "REFUNDED", "Refunded"
    ON_HOLD = "ON_HOLD", "On hold"
    BACKORDERED = "BACKORDERED", "Backordered"
    RETURNED = "RETURNED", "Returned"
    AWAITING_PICKUP = "AWAITING_PICKUP", "Awaiting pickup"
    COMPLETED = "COMPLETED", "Completed"
