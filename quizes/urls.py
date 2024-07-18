from django.urls import path 
# from .views.view_quiz_js import (
#     QuizListView,
#     quiz_view,
#     quiz_data_view,
#     save_quiz_view
# )
from .views.view_quiz_dj import QuizListViewDj, QuizDetailDj

app_name = 'quizes'

urlpatterns = [
        #  path('main', QuizListView.as_view(), name = 'main-view'),
        #  path('main/<int:pk>', quiz_view, name='quiz-view'),
        # path('main/<int:pk>/save', save_quiz_view, name='save-view'),

        # path('main/<int:pk>/data', quiz_data_view, name='quiz-data-view'),
        path('list', QuizListViewDj.as_view(), name='list-quiz-dj' ),
        path('detail/<int:pk>', QuizDetailDj.as_view(), name="detail-quiz-dj")

     ]
