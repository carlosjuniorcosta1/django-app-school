from django.db import models
from quizes.models import QuizSubject
from accounts.models import CustomUser as User

class Question(models.Model):
    context = models.CharField(max_length=5000, null=True, blank=True)
    question = models.CharField(max_length=1705, null=True, blank=True)
    quiz_subject = models.ForeignKey(QuizSubject, on_delete=models.CASCADE, null=True, blank=True)
    question_image = models.ImageField(blank=True, null=True, upload_to="questions/")
    year= models.IntegerField(blank=True, null=True)
    examining_board = models.CharField(max_length=100, blank=True, null=True)

    """
    def __str__(self):
        return f" Questão {self.id},banca {self.examining_board}, ano: {self.year}, ({self.quiz_subject}): {self.context[:500]}  {self.question}"
    """
    def get_answers(self):
        return self.answer_set.all()
    """
    def get_image_urls(self):
        if self.question_image:
            return self.question_image.split(',')  
        return []
    """

class Answer(models.Model):
    text = models.CharField(max_length=2501, blank=True, null=True)    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(null=True, blank=True)
    alternative = models.CharField(max_length=1, blank=True, null=True)
    answer_image = models.ImageField(blank=True, null=True, upload_to=("quizes/images/answers"))

    def count_alternatives(self):
        if self.question:
            return self.question.answer_set.count()
        return 0

    def save(self, *args, **kwargs):
        if not self.alternative:  
            existing_answers = self.question.answer_set.count()  
            self.alternative = chr(97 + existing_answers)
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"question: answer {self.text[:200]}"
    





