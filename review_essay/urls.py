from django.urls import path
from .views import CreateEssayReview, ListEssayForEditors, DetailEssay, UpdateEssay, UpdateEssayEditor

app_name = 'review_essay'

urlpatterns = [
    path('submit_essay/', CreateEssayReview.as_view(), name="submit_essay"),
    path('list_essay/', ListEssayForEditors.as_view(), name='list_essay_editors'),
    path('detail_essay/<int:pk>/', DetailEssay.as_view(), name="detail_essay"),
    path('update_essay/<int:pk>/', UpdateEssay.as_view(), name='update_essay'),
    path('update_essay_editors/<int:pk>/', UpdateEssayEditor.as_view(), name='update_essay_editors')
]