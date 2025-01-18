
from rest_framework import generics
from .models import Question, Answer
from quizes.models import QuizSubject
from questions.api.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.contrib import messages




class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


    def create(self, request, *args, **kwargs):
        print(request.FILES.get("question_image"))  
        return super().create(request, *args, **kwargs)

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
    fields = ['context', 'question', 'quiz_subject', 'question_image', 'year', 'examining_board']  
    template_name = 'quizes/exams/update_question.html' 
    success_url = reverse_lazy('quizes:portuguese-language-quiz')  # Pode ser alterado caso não queira redirecionar para essa URL por padrão.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        AnswerFormset = inlineformset_factory(
            Question, 
            Answer,
            fields=['text', 'is_correct',  'alternative', 'answer_image'],
            extra=1,
            can_delete=True
        )
        if self.request.POST:
            context['answer_formset'] = AnswerFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['answer_formset'] = AnswerFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        answer_formset = context['answer_formset']
        if form.is_valid() and answer_formset.is_valid():
            self.object = form.save()
            answer_formset.instance = self.object
            answer_formset.save()

            redirect_to = self.request.POST.get('redirect_to')
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect(self.success_url) 
        else:
            return self.form_invalid(form)
        
class QuestionCreateView(CreateView):
    model = Question
    fields = ['context', 'question', 'quiz_subject', 'question_image', 'year', 'examining_board']  # Campos do modelo de pergunta
    template_name = 'quizes/exams/create_question_exam.html'
    success_url = reverse_lazy('questions:create-new-question')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        AnswerFormset = inlineformset_factory(
            Question,
            Answer,
            fields=['text', 'is_correct', 'alternative', 'answer_image'],  
            extra=1,
            can_delete=True
        )
        if self.request.POST:
            context['answer_formset'] = AnswerFormset(self.request.POST, self.request.FILES)
        else:
            context['answer_formset'] = AnswerFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        answer_formset = context['answer_formset']
        if form.is_valid() and answer_formset.is_valid():
            self.object = form.save()
            answer_formset.instance = self.object
            answer_formset.save()
            messages.success(self.request, "Questão criada com sucesso!")



            redirect_to = self.request.POST.get('redirect_to')
            if redirect_to:
                return redirect(redirect_to)
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class QuestionFormView(TemplateView):
    template_name = 'quizes/exams/create_question_exam.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = QuizSubject.objects.all()
        return context
