from django.urls import path 
# from .views.view_quiz_js import (
#     QuizListView,
#     quiz_view,
#     quiz_data_view,
#     save_quiz_view
# )
from .views.questions_view import  QuestionListView
from .views.quiz_view import QuizListView
from .views.enem_language_quiz_view import EnemLanguageQuizListView
from .views.enem_math_quiz_view import EnemMathQuizListView
from .views.enem_human_sciences_quiz_view import EnemHumanSciencesQuizListView
from .views.enem_natural_sciences_quiz_view import EnemNaturalSciencesQuizListView


app_name = 'quizes'

urlpatterns = [
        #  path('main', QuizListView.as_view(), name = 'main-view'),
        #  path('main/<int:pk>', quiz_view, name='quiz-view'),
        # path('main/<int:pk>/save', save_quiz_view, name='save-view'),

        # path('main/<int:pk>/data', quiz_data_view, name='quiz-data-view'),
        path('list', QuizListView.as_view(), name='list-quiz-dj' ),
        path('list/questions', QuestionListView.as_view(), name="list-questions"),
        path('list/questions/language', EnemLanguageQuizListView.as_view(), name="enem-language-quiz" ),
        path('list/questions/math', EnemMathQuizListView.as_view(), name="enem-math-quiz"),
        path('list/questions/human_sciences', EnemHumanSciencesQuizListView.as_view(), name="enem-human-sciences-quiz"),
        path('list/questions/natural_sciences', EnemNaturalSciencesQuizListView.as_view(), name="enem-natural-sciences-quiz"),



     ]
