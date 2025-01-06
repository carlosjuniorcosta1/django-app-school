from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ..models import QuizSubject
from questions.models import Question, Answer
from django.core.paginator import Paginator


class QuizListView(ListView):
    model = QuizSubject
    fields = ['quiz_subject']
    template_name = "quizes/enem/main_quiz.html"




class QuizExamListView(ListView):
    model = QuizSubject
    fields = ['quiz_subject']
    template_name = "quizes/exams/list_exam_quizes.html"

