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