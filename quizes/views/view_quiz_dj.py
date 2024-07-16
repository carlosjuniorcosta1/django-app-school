from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ..models import Quiz
from questions.models import Question, Answer

class QuizListViewDj(ListView):
    model = Quiz
    fields = ['name', 'topic', 'number_of_questions', 'time', 'required_score_to_pass', 'difficulty']
    template_name = "quizes/main_quiz_dj.html"

class QuizDetailDj(DetailView):
    model = Quiz
    template_name = "quizes/quiz_detail_dj.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        quiz = self.get_object()
        context['questions'] = quiz.question_set.all()
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
                submitted_answers[question.text] = {
                    'selected': selected_answer.text,
                    'correct': selected_answer.correct
                }
                print(f"Pergunta: {question.text} - Resposta Selecionada: {selected_answer.text} - Correta: {selected_answer.correct}")

        context = self.get_context_data()
        context['submitted_answers'] = submitted_answers

        return render(request, self.template_name, context)
