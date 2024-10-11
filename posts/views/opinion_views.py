from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post
from django.utils import timezone
from accounts.models import CustomUser as User
from posts.forms.opinion_form import PostOpinionForm, PostOpinionStudentsForm
from django.db.models import Q



class OpinionListView(ListView):
    model = Post    
    paginate_by = 4
    template_name = "posts/opinion/opinion_index.html"
    ordering = ['-created']
    
    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="opiniao", user__is_columnist=True, status="approved" ).order_by('-created')  
        form = PostOpinionForm(self.request.GET)

        if form.is_valid():
            filter_by = form.cleaned_data.get('filter_by')
            search_term = form.cleaned_data.get('search_term')

            if filter_by == 'title':
                queryset = queryset.filter(title__icontains=search_term)
            elif filter_by == 'user':
                queryset = queryset.filter(user__first_name__icontains=search_term)
            elif filter_by == 'title_main_text':
                queryset = queryset.filter(
                    Q(title__icontains=search_term) |
                    Q(main_text__icontains=search_term)                )

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
        queryset = Post.objects.filter(section_name__section_name='opiniao', user__is_columnist=False, status="approved").order_by('-created')
        form = PostOpinionForm(self.request.GET)     
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            filter_by = form.cleaned_data.get('filter_by')

            if filter_by == 'title':
                queryset = queryset.filter(title__icontains=search_term)
            
            elif filter_by == 'title_main_text':
                queryset = queryset.filter(
                    Q(title__icontains=search_term) |
                    Q(main_text__icontains=search_term)
                )       
            elif filter_by == "user":
                queryset = queryset.filter(user__first_name__icontains=search_term)

        return queryset 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opinion_students'] = self.get_queryset()
        context['form'] = PostOpinionStudentsForm(self.request.GET)
        return context
    
    
        

    


    
       
       


