from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from ..models import QuizSubject
from questions.models import Question, Answer
from quizes.forms.enem_quiz_question_form import QuestionForm

class QuestionListView(ListView):
    model = QuizSubject
    template_name = "quizes/question_list.html"

    def get_queryset(self) -> QuerySet:
        queryset = Question.objects.all()
        form = QuestionForm(self.request.GET)
        if form.is_valid():
            filter_by = form.cleaned_data.get('filter_by')
            search_term = form.cleaned_data.get('search_term')

            if filter_by == "year":
                queryset = queryset.filter(year__icontains=search_term)
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['questions'] = self.get_queryset()
        context['form'] = QuestionForm(self.request.GET)  
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
