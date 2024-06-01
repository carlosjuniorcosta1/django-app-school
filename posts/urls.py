from django.urls import path
from posts.views import post_views
from .views.post_views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views.opinion_views import OpinionListView

app_name = 'posts'

urlpatterns = [
    path('list_texts_main/', PostListView.as_view(), name = "list_texts"),
    path('detail_text_main/<int:pk>/', PostDetailView.as_view(), name='detail_text'),
    path('create_post_main/', PostCreateView.as_view(), name="create_post"),
    path('update_post_main/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('delete_post_main/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('opinion/', OpinionListView.as_view(), name = "index_opinion")

]