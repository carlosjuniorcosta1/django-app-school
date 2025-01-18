from django.urls import path
from .views import QuestionListCreateView, AnswerListCreateView, QuestionDeleteView, QuestionUpdateView, QuestionFormView, QuestionCreateView


app_name = "questions"
urlpatterns = [
    path('api/create_question', QuestionListCreateView.as_view(), name='api-create-question'),
    path('api/create_answer', AnswerListCreateView.as_view(), name='api-create-answer'),
    path('api/<int:pk>/delete', QuestionDeleteView.as_view(), name='question-delete'),
    path('update/question/<int:pk>/', QuestionUpdateView.as_view(), name='update-question'),
    path('new/', QuestionFormView.as_view(), name='create-question'),
    path('create/', QuestionCreateView.as_view(), name='create-new-question'),




    


]
