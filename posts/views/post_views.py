from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone



class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 'section_name']
    success_url = reverse_lazy("posts:detail_text")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['username'] = user.username
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name   
        return context
    def get_success_url(self):
        return reverse('posts:detail_text', kwargs={'pk': self.object.pk})


class PostListView(ListView):
    model = Post
    ordering = ['-created']
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context['object_list']:
            print(f"titulo do post '{post.title}': {post.section_name}")
        return context



class PostDetailView(DetailView):
    model = Post
    # def get_object(self):
    #     post = super().get_object()
    #     post.post_views += 1
    #     post.save()
    #     return post 


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields =  ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 'section_name']

    
    def get_success_url(self):
        print(f"Post updated with ID:{ self.object.pk}")  

        return reverse('posts:detail_text', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        self.object = form.save(commit=False) 
        self.object.updated = timezone.now()  
        self.object.save()
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list_texts')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)



 
        

