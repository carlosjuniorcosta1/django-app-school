from django.urls import path
from .views import ElementarySchoolBnccListView, HighSchoolBnccListView


app_name = 'api_bncc'

urlpatterns = [
    path('list_bncc_es', ElementarySchoolBnccListView.as_view(), name='list-bncc-el-school'),
    path('list_bncc_hs', HighSchoolBnccListView.as_view(), name='list-bncc-hs-school')

    
]