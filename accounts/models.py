from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class CustomUser(AbstractUser):
    is_columnist = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_essay_editor = models.BooleanField(default=False)
    presentation = models.CharField(max_length=100, blank=False, null=False)
    user_picture =  models.ImageField(null=True, blank=True, upload_to="images/", 
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])])
    user_instagram = models.URLField( null=True, blank=True)
    user_linkedin = models.URLField( null=True, blank=True)
    user_youtube = models.URLField( null=True, blank=True)
    user_facebook = models.URLField(null=True, blank=True)
    is_premium = models.BooleanField(null=True, blank=True)
    has_accepted_terms = models.BooleanField(default=False)



    def __str__(self):
        return self.username