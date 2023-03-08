from django.db.models import Model, CharField, ImageField, DateTimeField
from django.core.validators import FileExtensionValidator
from django.conf import settings
from uuid import uuid4


class Picture(Model):
    title = CharField(max_length=150, default="", blank=True)
    picture = ImageField(
        max_length=150, upload_to="uploaded/%Y/%m", validators=[
            FileExtensionValidator(settings.ALLOWED_FILE_EXTENSIONS)
        ]
    )
    uploaded_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def save(self, *args, **kwargs):
        _, ext = self.picture.name.split(".")
        self.picture.name = f"{uuid4()}.{ext}"
        return super().save(*args, **kwargs)
