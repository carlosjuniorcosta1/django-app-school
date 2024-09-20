from django.urls import path 
from .views import IndexListView, about

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('about', about, name='about')
    ]