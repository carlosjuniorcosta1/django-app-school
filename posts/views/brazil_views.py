from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from accounts.models import CustomUser as User
from posts.forms.opinion_form import PostOpinionForm, PostOpinionStudentsForm


class BrazilListView(ListView):
    model = Post
    fields = ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 'section_name']
    template_name = "posts/brazil/brazil_index.html"

    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="brasil").order_by('-created')

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brazil_posts'] = self.get_queryset()
        return context 





