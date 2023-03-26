from functools import partial

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from random_username.generate import UsernameGenerator


class User(AbstractUser):
    username = CharField(
        max_length=150,
        default=partial(UsernameGenerator().generate_username, num_digits=3),
        unique=True,
    )

    @property
    def fullname(self):
        return self.get_full_name()
