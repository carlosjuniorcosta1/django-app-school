
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from ..models import Post
from django.db.models import Q
from api_awesome.views import GetExchangeListView
from posts.forms.world_form import WorldForm


class SportListView(ListView):
    model = Post
    fields = ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 'section_name']
    template_name = "posts/sports/sports_index.html"

    def get_queryset(self):
        return super().get_queryset()



    
