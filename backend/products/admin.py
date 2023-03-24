from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["id", "name", "display_price"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "description"]
    ordering = ["name", "price"]
