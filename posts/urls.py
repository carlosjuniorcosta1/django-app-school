from django.urls import path
from posts.views import post_views
from .views.post_views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views.opinion_views import OpinionListView, OpinionStudentsListView
from .views.brazil_views import BrazilListView
from .views.world_views import WorldListView
from .views.culture.culture_views import CultureListView
from .views.culture.cinema_views import CultureCineListView
from .views.culture.literature_views import CultureLiteratureListView
from .views.culture.games_views import CultureGamesListView
from .views.culture.food_views import CultureFoodListView
from .views.culture.arts_views import CultureArtsListView
from .views.health_views import HealthListView
from .views.ilustrattor_views import ListIllustrationsAsked, UpdateIllustration, DetailIllustration


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
    path('culture_news/', CultureListView.as_view(), name="index_culture"),
    path('culture_news/cinema', CultureCineListView.as_view(), name="list_cinema" ), 
    path('culture_news/literature', CultureLiteratureListView.as_view(), name="list_literature"),
    path('culture_news/games', CultureGamesListView.as_view(), name="list_games"),
    path('health_news/', HealthListView.as_view(), name="index_health"),
    path('food_recipe_news/', CultureFoodListView.as_view(), name="list_food"),
    path('arts_students_users/', CultureArtsListView.as_view(), name="list_arts"),
    path('illustrations_asked/', ListIllustrationsAsked.as_view(), name='illustrations_asked'),
    path('illustrations_asked/update/<int:pk>/', UpdateIllustration.as_view(), name='update_image_illustration'),
    path('illustrations_asked/detail/<int:pk>/', DetailIllustration.as_view(), name="detail_illustration"),

]