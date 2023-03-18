from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    username = CharField(max_length=150, default="", unique=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    @property
    def fullname(self):
        return self.get_full_name()
