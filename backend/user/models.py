from functools import partial

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models import CharField
from random_username.generate import UsernameGenerator


random_name = partial(UsernameGenerator().generate_username, num_digits=3)


class UserManager(UserManager):
    def create(self, *args, **kwargs):
        if "username" not in kwargs:
            kwargs["username"] = random_name()
        return super().create(*args, **kwargs)


class User(AbstractUser):
    # objects = UserManager()

    username = CharField(
        max_length=150,
        unique=True,
    )

    @property
    def fullname(self):
        return self.get_full_name()
