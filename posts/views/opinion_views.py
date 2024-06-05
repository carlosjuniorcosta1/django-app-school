from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from accounts.models import CustomUser as User



class OpinionListView(ListView):
    model = Post    
    paginate_by = 4
    template_name = "posts/opinion/opinion_index.html"
    ordering = ['-created']
    
    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="opiniao", user__is_columnist=True ).order_by('-created')  

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opinion_posts'] = self.get_queryset()
        return context 
    


    
       
       


