from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

app_name = 'posts'

urlpatterns = [
    path('postlist/', views.list_posts, name = "lists_posts"),
    path('thank_you/', views.thank_you, name="thank_you"),
    # path('create/', views.create_post, name="create_post"),
    path('list_texts/', PostListView.as_view(), name = "list_texts"),
    path('detail_text/<int:pk>/', PostDetailView.as_view(), name='detail_text'),
    path('create_post/', PostCreateView.as_view(), name="create_post"),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name='update_post')


]