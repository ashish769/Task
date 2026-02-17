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
