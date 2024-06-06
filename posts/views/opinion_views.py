from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from accounts.models import CustomUser as User
from posts.forms import PostOpinionForm, PostOpinionStudentsForm



class OpinionListView(ListView):
    model = Post    
    paginate_by = 4
    template_name = "posts/opinion/opinion_index.html"
    ordering = ['-created']
    
    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="opiniao", user__is_columnist=True ).order_by('-created')  

        search_term = self.request.GET.get('search_term')
        filter_by = self.request.GET.get('filter_by')

        if search_term and filter_by:
            if filter_by == 'title':
                queryset = queryset.filter(title__icontains=search_term)
            elif filter_by == 'user':
                queryset = queryset.filter(user__first_name__icontains=search_term)
            elif filter_by == 'main_text':
                queryset = queryset.filter(main_text__icontains=search_term)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opinion_posts'] = self.get_queryset()
        context['form'] =  PostOpinionForm(self.request.GET)
        return context 
    
class OpinionStudentsListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'posts/opinion/opinion_students_list.html'
    ordering = ['-created']

    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name='opiniao', user__is_columnist=False).order_by('-created')

        search_term = self.request.GET.get('search_term')
        filter_by = self.request.GET.get('filter_by')

        if search_term and filter_by:
            if filter_by == 'title':
                queryset = queryset.filter_by(title__icontains=search_term)
            elif filter_by == "main_text":
                queryset = queryset.filter_by(main_text__icontains=search_term)
            elif filter_by == "user":
                queryset = queryset.filter_by(user__first_name__icontains=search_term)

        return queryset 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opinion_students'] = self.get_queryset()
        context['form'] = PostOpinionStudentsForm(self.request.GET)
        return context
    
    
        

    


    
       
       


