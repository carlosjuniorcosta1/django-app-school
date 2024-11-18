from django.urls import path
from .views.editors_view import ListEssayForEditors,  UpdateEssayEditor
from .views.user_crud_view import CreateEssayReview, DetailEssay, UpdateEssay, ListUserEssay, DetailUserReviewedEssay

app_name = 'review_essay'

urlpatterns = [
    path('submit_essay/', CreateEssayReview.as_view(), name="submit_essay"),
    path('list_essay/', ListEssayForEditors.as_view(), name='list_essay_editors'),
    path('detail_essay/<int:pk>/', DetailEssay.as_view(), name="detail_essay"),
    path('update_essay/<int:pk>/', UpdateEssay.as_view(), name='update_essay'),
    path('update_essay_editors/<int:pk>/', UpdateEssayEditor.as_view(), name='update_essay_editors'),
    path('list_user_essays/', ListUserEssay.as_view(), name="list_user_essays"),
    path('detail_reviewed_essay/<int:pk>/', DetailUserReviewedEssay.as_view(), name='detail_reviewed_essay'),

]