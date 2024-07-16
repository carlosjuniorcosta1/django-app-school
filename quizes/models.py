from django.db import models
import random


DIFF_CHOICES = ( 
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120, null=True, blank=True)
    number_of_questions = models.IntegerField( null=True, blank=True)
    time = models.IntegerField(help_text="Duração em minutos", null=True, blank = True)
    required_score_to_pass = models.IntegerField(help_text="Pontuação requerida em %", null=True, blank=True)
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]
        # return self.question_set.all()[:self.number_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizes'