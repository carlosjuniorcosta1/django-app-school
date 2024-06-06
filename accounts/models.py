from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_columnist = models.BooleanField(default=False)
    presentation = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.username