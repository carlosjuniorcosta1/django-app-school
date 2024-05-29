from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('list_texts/', PostListView.as_view(), name = "list_texts"),
    path('detail_text/<int:pk>/', PostDetailView.as_view(), name='detail_text'),
    path('create_post/', PostCreateView.as_view(), name="create_post"),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),



]