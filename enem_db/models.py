from django.db import models

class EnemDb(models.Model):
    number = models.IntegerField()
    context = models.CharField(max_length=4000)
    question = models.CharField(max_length=1500)
    alt_a = models.CharField(max_length=1500)
    alt_b = models.CharField(max_length=1500)
    alt_c = models.CharField(max_length=1500)
    alt_d = models.CharField(max_length=1500)
    alt_e = models.CharField(max_length=1500)
    correct = models.CharField(max_length=1)
    context_images = models.CharField(max_length=500)
    subject = models.CharField(max_length=10)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.subject}, {self.year}, correct: {self.correct}"







