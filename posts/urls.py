from django.urls import path
from posts.views import post_views
from .views.post_views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views.opinion_views import OpinionListView, OpinionStudentsListView
from .views.brazil_views import BrazilListView
from .views.world_views import WorldListView
from .views.cuisine_views import CuisineListView
from .views.sport_views import SportListView

app_name = 'posts'

urlpatterns = [
    path('list_texts_main/', PostListView.as_view(), name = "list_texts"),
    path('detail_text_main/<int:pk>/', PostDetailView.as_view(), name='detail_text'),
    path('create_post_main/', PostCreateView.as_view(), name="create_post"),
    path('update_post_main/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('delete_post_main/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('opinion/', OpinionListView.as_view(), name = "index_opinion"),
    path('opinion_students/', OpinionStudentsListView.as_view(), name='list_opinion_students'),
    path('brazil_news/', BrazilListView.as_view(), name= "index_brazil"),
    path('world_news/', WorldListView.as_view(), name="index_world"),
    path('cuisine_news/', CuisineListView.as_view(), name="index_cuisine"),
    path('sports_news', SportListView.as_view(), name="index_sport")

]