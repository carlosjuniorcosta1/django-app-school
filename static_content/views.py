from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render
from posts.models import Post
from .index_form import IndexForm
from django.db.models import Q

class IndexListView(ListView):
    model = Post
    template_name= "static_content/index.html"

    def get_queryset(self):
        queryset = Post.objects.all()   
        form = IndexForm(self.request.GET)
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
        context['latest_posts'] = Post.objects.exclude(section_name__section_name='opiniao').filter(status="approved").order_by('-created')[:4]
        context['carro_one_posts'] = Post.objects.exclude(section_name__section_name='opiniao').order_by('-created')[4:7]
        context['opinion_posts'] = Post.objects.filter(section_name__section_name='opiniao').filter(status="approved").order_by('-created')[:5]
        context['latest_posts_second_row'] = Post.objects.exclude(section_name__section_name='opiniao').filter(status="approved").order_by("-created")[7:11]
        context['carro_second_posts'] = Post.objects.exclude(section_name__section_name='opiniao').order_by('-created')[11:14]
                 
        context['form'] = IndexForm(self.request.GET) 
        return context 
    








def about(request):
    return render(request, 'static_content/about.html')
