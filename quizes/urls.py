from django.urls import path 

from .views.questions_view import  QuestionListView
from .views.quiz_view import QuizListView
from .views.enem_language_quiz_view import EnemLanguageQuizListView
from .views.enem_math_quiz_view import EnemMathQuizListView
from .views.enem_human_sciences_quiz_view import EnemHumanSciencesQuizListView
from .views.enem_natural_sciences_quiz_view import EnemNaturalSciencesQuizListView
from .views.create_question_view import QuestionCreateView
from .views.enem_human_sciences_ajax import EnemHumanSciencesQuizAjaxListView
from .views.enem_natural_sciences_ajax import EnemNaturalSciencesQuizAjaxListView
from .views.enem_language_ajax import EnemLanguagesQuizAjaxListView
from .views.enem_math_ajax import EnemMathQuizAjaxListView
from .views.portuguese_language_view import PortugueseLanguageQuizListView
from .views.portuguese_language_ajax import PortugueseLanguageQuizAjaxListView


app_name = 'quizes'

urlpatterns = [
        path('list', QuizListView.as_view(), name='list-quiz-dj' ),
        path('list/questions', QuestionListView.as_view(), name="list-questions"),
        path('list/questions/language', EnemLanguageQuizListView.as_view(), name="enem-language-quiz" ),
        path('list/questions/math', EnemMathQuizListView.as_view(), name="enem-math-quiz"),
        path('list/questions/human_sciences', EnemHumanSciencesQuizListView.as_view(), name="enem-human-sciences-quiz"),
        path('list/questions/natural_sciences', EnemNaturalSciencesQuizListView.as_view(), name="enem-natural-sciences-quiz"),
        path('create_question', QuestionCreateView.as_view(), name='create_question'),
        path('human_sciences/filtered', EnemHumanSciencesQuizAjaxListView.as_view(), name='enem-human-sciences-quiz-ajax'),
        path('natural_sciences/filtered', EnemNaturalSciencesQuizAjaxListView.as_view(), name='enem-natural-sciences-quiz-ajax'),
        path('languages/filtered', EnemLanguagesQuizAjaxListView.as_view(), name='enem-languages-quiz-ajax'),
        path('math/filtered', EnemMathQuizAjaxListView.as_view(), name='enem-math-quiz-ajax'),
        path('list/questions/portuguese', PortugueseLanguageQuizListView.as_view(), name='portuguese-language-quiz'),
        path('portuguese/filtered', PortugueseLanguageQuizAjaxListView.as_view(), name='portuguese-language-quiz-ajax'),






     ]
