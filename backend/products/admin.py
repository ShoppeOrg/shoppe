from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import StackedInline

from .models import Product
from .models import ProductInventory


class InventoryInline(StackedInline):
    model = ProductInventory
    exclude = ["sold_qty"]


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["id", "name", "display_price"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "description"]
    ordering = ["name", "price"]
    list_per_page = 10
    inlines = [
        InventoryInline,
    ]
