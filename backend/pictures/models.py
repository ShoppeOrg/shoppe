from uuid import uuid4

from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ImageField
from django.db.models import Model
from django.utils.safestring import mark_safe


class Picture(Model):
    title = CharField(max_length=150, default="", blank=True)
    picture = ImageField(
        max_length=150,
        upload_to="uploaded/%Y/%m",
        validators=[FileExtensionValidator(settings.ALLOWED_FILE_EXTENSIONS)],
    )
    uploaded_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    @property
    def url(self):
        return self.picture.url

    def image_tag(self):  # new
        return mark_safe(
            '<img src="/images/%s" width="150" height="150" />' % self.picture
        )

    def save(self, *args, **kwargs):
        _, ext = self.picture.name.split(".")
        self.picture.name = f"{uuid4()}.{ext}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.picture.name
