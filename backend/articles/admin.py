from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Article


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ["slug"]
