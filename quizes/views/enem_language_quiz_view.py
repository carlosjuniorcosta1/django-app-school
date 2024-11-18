from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ..models import QuizSubject
from questions.models import Question, Answer
from quizes.forms.enem_quiz_question_form import QuestionForm
from django.db.models import Q

class EnemLanguageQuizListView(ListView):
    model = QuizSubject
    template_name = "quizes/enem/enem_language_quiz.html"
    paginate_by = 1  # Número de questões a serem paginadas se nenhum filtro for aplicado

    def get_queryset(self) -> QuerySet:
     
        queryset = Question.objects.filter(quiz_subject=1)  # Ajuste conforme necessário para a consulta inicial
        form = QuestionForm(self.request.GET)

        if form.is_valid():
            filter_by = form.cleaned_data.get('filter_by')
            search_term = form.cleaned_data.get('search_term')

            # Aplica o filtro de acordo com o critério selecionado
            if filter_by == "year":
                queryset = queryset.filter(year__icontains=search_term)
            elif filter_by == 'word':
                queryset = queryset.filter(
                    Q(context__icontains=search_term) |
                    Q(question__icontains=search_term)
                )
            elif filter_by == "id":
                queryset = queryset.filter(id=search_term)

        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    
        context = super().get_context_data(**kwargs)
        questions = self.get_queryset()
        form = QuestionForm(self.request.GET)        
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

        context['form'] = form  
        context['total_questions'] = questions.count()  
        context['is_filter_used'] = is_filter_used
        context['is_premium'] = self.request.user.is_premium


        return context

    def post(self, request, *args, **kwargs):
        """
        Processa as respostas enviadas pelo usuário e exibe o resultado com base nas respostas selecionadas.
        """
        quiz = QuizSubject.objects.get(pk=self.kwargs.get('pk'))
        questions = quiz.question_set.all()  # Obtém todas as questões do quiz atual
        submitted_answers = {}

        for question in questions:
            selected_answer_id = request.POST.get(f"question{question.id}", None)
            if selected_answer_id:
                try:
                    selected_answer = Answer.objects.get(id=selected_answer_id)
                    submitted_answers[question.context] = {
                        'selected': selected_answer.text,
                        'correct': selected_answer.is_correct
                    }
                    # Log para depuração
                    print(f"Pergunta: {question.context} - Resposta Selecionada: {selected_answer.text} - Correta: {selected_answer.is_correct}")
                except Answer.DoesNotExist:
                    print(f"Erro: A resposta com ID {selected_answer_id} não foi encontrada.")

        context = self.get_context_data()
        context['submitted_answers'] = submitted_answers

        return render(request, self.template_name, context)
