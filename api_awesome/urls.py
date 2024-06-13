from django.urls import path
from .views import GetExchangeListView


app_name = 'api_currencies'

urlpatterns = [
    path('api_awesome_exchange/', GetExchangeListView.as_view(), name = "get_exchange")

]