from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        AUTHOR = "AUTHOR", "Author"
        READER = "READER", "Reader"

    role = models.CharField(max_length=10, choices=Role.choices)

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_author(self):
        return self.role == self.Role.AUTHOR

    @property
    def is_reader(self):
        return self.role == self.Role.READER

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, role="READER", **extra_fields):
        if not username:
            raise ValueError("Username required")

        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('role', 'ADMIN')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
