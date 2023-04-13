from functools import partial

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from random_username.generate import UsernameGenerator


random_name = partial(UsernameGenerator().generate_username, num_digits=3)


class User(AbstractUser):
    username = CharField(
        max_length=150,
        default=random_name,
        unique=True,
    )

    @property
    def fullname(self):
        return self.get_full_name()
