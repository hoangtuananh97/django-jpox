import os
import time

from django.contrib.auth.models import AbstractUser
from django.db import models

from api.base.upload_path import upload_avatar_path


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.FileField(upload_to=upload_avatar_path, null=True, verbose_name="Avatar file", )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ("email",)

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
