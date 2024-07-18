from django.db import models

class EnemDb(models.Model):
    number = models.IntegerField()
    context = models.CharField(max_length=4000, null=True, blank=True)
    question = models.CharField(max_length=1500, null=True, blank=True)
    alt_a = models.CharField(max_length=1500, null=True, blank=True)
    alt_b = models.CharField(max_length=1500, null=True, blank=True)
    alt_c = models.CharField(max_length=1500, null=True, blank=True)
    alt_d = models.CharField(max_length=1500, null=True, blank=True)
    alt_e = models.CharField(max_length=1500, null=True, blank=True)
    correct = models.CharField(max_length=1, null=True, blank=True)
    context_images = models.CharField(max_length=500, null=True, blank=True)
    subject = models.CharField(max_length=10, null=True, blank=True)
    subject_code = models.IntegerField(null=True, blank=True)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.subject}, {self.year}, correct: {self.correct}"







