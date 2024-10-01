from django import forms
from questions.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['context', 'question', 'quiz_subject', 'question_image']
        widgets = {
            'context': forms.TextInput(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control'}),
            'quiz_subject': forms.Select(attrs={'class': 'form-control'}),
            'question_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o URL da imagem'}),  # Alterado para URL

        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct', 'alternative', 'answer_image']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'alternative': forms.Textarea(attrs={'class': 'form-control'})


        }
