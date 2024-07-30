from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ..models import QuizSubject
from questions.models import Question, Answer
from django.core.paginator import Paginator


class QuizListViewDj(ListView):
    model = QuizSubject
    fields = ['quiz_subject']
    template_name = "quizes/main_quiz_dj.html"

class QuizDetailDj(DetailView):
    model = QuizSubject
    template_name = "quizes/quiz_detail_dj.html" 

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        quiz = self.get_object()
        
        questions = quiz.question_set.all()      
      
        paginator = Paginator(questions, 50)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)        
      
        context['questions'] = page_obj
        context['quiz'] = quiz
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        quiz = self.object
        questions = quiz.question_set.all()
        submitted_answers = {}

        for question in questions:
            selected_answer_id = request.POST.get(f"question{question.id}", None)
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                submitted_answers[question.context] = {
                    'selected': selected_answer.text,
                    'correct': selected_answer.is_correct
                }
                print(f"Pergunta: {question.context} - Resposta Selecionada: {selected_answer.text} - Correta: {selected_answer.is_correct}")

        context = self.get_context_data()
        context['submitted_answers'] = submitted_answers

        return render(request, self.template_name, context)
