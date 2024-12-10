from django.db import models
from quizes.models import QuizSubject

class Question(models.Model):
    context = models.CharField(max_length=5000, null=True, blank=True)
    question = models.CharField(max_length=1705, null=True, blank=True)
    quiz_subject = models.ForeignKey(QuizSubject, on_delete=models.CASCADE, null=True, blank=True)
    question_image = models.TextField(blank=True, null=True)
    year= models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    has_image = models.BooleanField(blank=True, default=0, null=True)

    def __str__(self):
        return f" Questão {self.id}, ano: {self.year}, ({self.quiz_subject}): {self.context[:500]}  {self.question}"
    
    def get_answers(self):
        return self.answer_set.all()
    
    def get_image_urls(self):
        if self.question_image:
            return self.question_image.split(',')  
        return []

class Answer(models.Model):
    text = models.CharField(max_length=2501)    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(null=True, blank=True)
    has_image_alt = models.BooleanField(blank=True, null=True)   
    alternative = models.CharField(max_length=1, blank=True, null=True)
    answer_image = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"question: answer {self.text[:200]}"
    

