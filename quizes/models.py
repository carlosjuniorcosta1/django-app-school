from django.db import models
import random

class QuizSubject(models.Model):
    quiz_subject = models.CharField(max_length=25)
    quiz_subject_hum = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.quiz_subject}"
    
    def get_questions(self):     
        return self.question_set.all()
    
    class Meta:
        verbose_name_plural = 'Quizes'