from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Picture


@admin.register(Picture)
class PictureAdmin(ModelAdmin):
    list_display = ["title", "image_preview"]
