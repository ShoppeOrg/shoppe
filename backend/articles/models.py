from api.settings import AUTH_USER_MODEL
from django.core.validators import validate_slug
from django.db.models import (
    Model, CharField, TextField, DateTimeField, ManyToManyField, ForeignKey, BooleanField, PROTECT
)
from datetime import datetime

class ArticleCategory(Model):

    name = CharField(primary_key=True, unique=True, max_length=50)

    class Meta:
        db_table = "articles_article_category"
        verbose_name = "category"
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<ArticleCategory {self}>"


class Article(Model):

    title = CharField(max_length=255)
    slug = CharField(primary_key=True, max_length=260, validators=[validate_slug])
    data = TextField(default="")
    author = ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=PROTECT,
    )
    categories = ManyToManyField(
        to=ArticleCategory,
        related_name="articles",
    )
    is_published = BooleanField(default=False)
    published_at = DateTimeField(null=True)
    is_scheduled = BooleanField(default=False)
    scheduled_at = DateTimeField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.slug

    def __repr__(self):
        return f"<Article {self}>"
