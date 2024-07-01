from django.urls import path 
from .views import (
    QuizListView,
    quiz_view
)

app_name = 'quizes'

urlpatterns = [
         path('main', QuizListView.as_view(), name = 'main-view'),
         path('main/<int:pk>', quiz_view, name='quiz-view')
     ]
