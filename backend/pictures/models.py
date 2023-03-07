from django.db.models import Model, CharField, ImageField, DateTimeField
from uuid import uuid4


class Picture(Model):
    title = CharField(max_length=150, default="", blank=True)
    picture = ImageField(max_length=150, upload_to="uploaded/%Y/%m")
    uploaded_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
