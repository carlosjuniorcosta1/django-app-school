from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import CustomUser as User 
from django.core.validators import MaxValueValidator

class Essay(models.Model):
    essay_image = models.ImageField(upload_to="images/", 
                              validators=
                              [FileExtensionValidator(allowed_extensions=
                                                       ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_reviewed = models.BooleanField(default=False)
    essay_topic = models.CharField(max_length=200)
    c1 = models.IntegerField(validators=[MaxValueValidator(200)], blank=True, null=True)
    about_c1 = models.CharField(max_length=500, blank=True, null=True)
    c2 = models.IntegerField(validators=[MaxValueValidator(200)], blank=True, null=True)
    about_c2 = models.CharField(max_length=500, blank=True, null=True)
    c3 = models.IntegerField(validators=[MaxValueValidator(200)], blank=True, null=True)
    about_c3 = models.CharField(max_length=500, blank=True, null=True)
    c4 = models.IntegerField(validators=[MaxValueValidator(200)], blank=True, null=True)
    about_c4 = models.CharField(max_length=500, blank=True, null=True)
    c5 = models.IntegerField(validators=[MaxValueValidator(200)], blank=True, null=True)
    about_c5 = models.CharField(max_length=500, blank=True, null=True)  
    correction_image = models.ImageField(upload_to="images/", 
                              validators=
                              [FileExtensionValidator(allowed_extensions=
                                                       ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])], blank=True, null=True)
    total_grade = models.IntegerField(blank=True, null=True)
    is_finished = models.BooleanField(null=True, blank=True)


    audio_feedback = models.FileField(upload_to="audio/", 
                             validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])], 
                             blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}, tema: {self.essay_topic}, total: {self.total_grade}'
    


    def save(self, *args, **kwargs):
        self.total_grade = sum(filter(None, [self.c1, self.c2, self.c3, self.c4, self.c5]))
        super(Essay, self).save(*args, **kwargs)

# class EssayGrade(models.Model):
#     essay_id = models.ForeignKey(Essay,on_delete=models.CASCADE)
  

#     def __str__(self):
#         return f'C1:{self.c1}'



    