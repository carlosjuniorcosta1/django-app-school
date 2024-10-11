from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from accounts.models import CustomUser as User 
from django.core.exceptions import ValidationError



class Essay(models.Model):
    essay_image = models.ImageField(upload_to="images/", 
                              validators=
                              [FileExtensionValidator(allowed_extensions=
                                                       ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_reviewed = models.BooleanField(default=False)
    essay_topic = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}, tema: {self.essay_topic}'
    


    