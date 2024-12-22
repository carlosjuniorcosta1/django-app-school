from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from ..models import QuizSubject
from questions.models import Question, Answer
from quizes.forms.enem_quiz_question_form import QuestionForm, QuestionExamForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render


class PortugueseLanguageQuizListView(ListView):
    model = QuizSubject
    template_name = "quizes/exams/portuguese_language_quiz.html"
    quiz_subject_id = 5
    paginate_by = 1

    def get_queryset(self) -> QuerySet:
        queryset = Question.objects.filter(quiz_subject=self.quiz_subject_id)
        form = QuestionExamForm(self.request.GET)
        if form.is_valid():
            filter_by = form.cleaned_data.get('filter_by')
            search_term = form.cleaned_data.get('search_term')

            if filter_by == "examining_board":
                queryset = queryset.filter(year__icontains=search_term)
            elif filter_by == 'word':
                queryset = queryset.filter(
                    Q(context__icontains=search_term) |
                    Q(question__icontains=search_term)
                )
            elif filter_by == "id":
                queryset = queryset.filter(id=search_term )
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        questions = self.get_queryset()
        form = QuestionExamForm(self.request.GET)       

        is_filter_used = form.is_valid() and (form.cleaned_data.get('filter_by') and form.cleaned_data.get('search_term'))
        if is_filter_used:
            context['questions'] = questions

        else:
            paginator = Paginator(questions, self.paginate_by)

            page = self.request.GET.get('page')
            try:
                questions_paginated = paginator.page(page)
            except PageNotAnInteger:
                questions_paginated = paginator.page(1)
            except EmptyPage:
                questions_paginated = paginator.page(paginator.num_pages)            
            context['questions'] = questions_paginated 
        context['form'] = QuestionExamForm(self.request.GET)
        context['total_questions'] = questions.count()
        context['is_filter_used'] = is_filter_used
        context['is_premium'] = self.request.user.is_premium


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
        context = self.get_context_data()
        context['submitted_answers'] = submitted_answers

        return render(request, self.template_name, context)
    