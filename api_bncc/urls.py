from django.urls import path
from .views import ApiBnccListView


app_name = 'api_bncc'

urlpatterns = [
    path('list_bncc', ApiBnccListView.as_view(), name='list_bncc')
    
]