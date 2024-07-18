from django.db import models
from quizes.models import QuizSubject

class Question(models.Model):
    context = models.CharField(max_length=4000, null=True, blank=True)
    question = models.CharField(max_length=1501, null=True, blank=True)
    quiz_subject = models.ForeignKey(QuizSubject, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.quiz_subject}, {self.context}"
    
    # def get_answers(self):
    #     return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=1500)    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(null=True, blank=True)
    

    def __str__(self):
        return f"question: answer {self.text}"
    

