from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from posts.forms.post_form import PostFilterForm
from django.shortcuts import render
from django.db.models import Q


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 'section_name', 'image_illustrator', 'is_asking_for_illustration']
    success_url = reverse_lazy("posts:detail_text")

    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.request.user.is_columnist or self.request.user.is_superuser:
            form.instance.status = 'approved'
        else:
            form.instance.status = 'pending'

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['username'] = user.username
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['post'] = self.object
        context['is_artist'] = user.is_artist
        context['is_columnist'] = user.is_columnist
        context['is_artist'] = user.is_artist
        context['is_post_created'] = hasattr(self, 'object') and self.object is not None

        
        return context
    def get_success_url(self):
        return reverse('posts:detail_text', kwargs={'pk': self.object.pk})


class PostListView(ListView):
    model = Post
    ordering = ['-created']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status='approved')

        search_term = self.request.GET.get('search_term')
        filter_by = self.request.GET.get('filter_by')

        if search_term and filter_by:
            if filter_by == 'title':
                queryset = queryset.filter(title__icontains=search_term)         
            elif filter_by == 'textual_genre':
                queryset = queryset.filter(textual_genre__textual_genre__icontains=search_term)
            elif filter_by == 'section_name':
                queryset = queryset.filter(section_name__section_name__icontains=search_term)
            elif filter_by == 'main_text':
                queryset = queryset.filter(main_text__icontains=search_term)
            elif filter_by == 'user':
                queryset = queryset.filter(user__first_name__icontains=search_term)

        return queryset

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostFilterForm(self.request.GET)
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
    fields =  ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 
               'section_name',  "is_asking_for_illustration", 'subtitle_illustrator']
    template_name = 'posts/post_update.html'
    
    def get_success_url(self):
        print(f"Post updated with ID:{ self.object.pk}")  

        return reverse('posts:detail_text', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        self.object = form.save(commit=False) 
        self.object.updated = timezone.now()  
        self.object.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_illustration_done'] = self.object.is_illustration_done 
        return context

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list_texts')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


 
        

