from django.db import models
from quizes.models import QuizSubject
from accounts.models import CustomUser as User

class Result(models.Model):
    quiz = models.ForeignKey(QuizSubject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.pk})"