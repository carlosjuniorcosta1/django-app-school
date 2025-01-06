
from rest_framework import generics
from .models import Question, Answer
from quizes.models import QuizSubject
from questions.api.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy



class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer



class QuestionDeleteView(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer(instance)
        question_data = serializer.data
        
        self.perform_destroy(instance)
        
        return Response(
            {
                "message": "Questão e respostas deletadas com sucesso",
                "deleted_question": question_data
            }, 
            status=status.HTTP_200_OK
        )
    

class QuestionUpdateView(UpdateView):
    model = Question
    fields = ['context']  
    template_name = 'quizes/exams/update_question.html' 
    success_url = reverse_lazy('quizes:portuguese-language-quiz')  


class QuestionFormView(TemplateView):
    template_name = 'quizes/exams/create_question_exam.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = QuizSubject.objects.all()
        return context
