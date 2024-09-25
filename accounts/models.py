from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator



class CustomUser(AbstractUser):
    is_columnist = models.BooleanField(default=False)
    presentation = models.CharField(max_length=100, blank=False, null=False)
    user_picture =  models.ImageField(null=True, blank=True, upload_to="images/", 
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])])

    def __str__(self):
        return self.username