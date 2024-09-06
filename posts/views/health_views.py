
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from ..models import Post
from django.db.models import Q
from api_awesome.views import GetExchangeListView
from posts.forms.health_form import HealthForm


class HealthListView(ListView):
    model = Post
    template_name = "posts/health/health_index.html"


    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="saude").order_by('-created')
        form = HealthForm(self.request.GET)
        if form.is_valid():
            filter_by = form.cleaned_data.get('filter_by')
            search_term = form.cleaned_data.get('search_term')
            if filter_by == 'title':
                queryset = queryset.filter(title__icontains=search_term)
            elif filter_by == 'title_main_text':
                queryset = queryset.filter(
                    Q(title__icontains=search_term) |
                    Q(main_text__icontains=search_term)
                )
            elif filter_by == 'user':
                queryset = queryset.filter(user__username__icontains=search_term)
        return queryset 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['health_posts'] = self.get_queryset()
        context['form'] = HealthForm(self.request.GET)
        return context 


    

            


        



    
