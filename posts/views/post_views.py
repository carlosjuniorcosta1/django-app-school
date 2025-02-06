from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post, Chapter
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from posts.forms.post_form import PostFilterForm
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from posts.forms.chapter_form import ChapterFilterForm
from django.shortcuts import get_object_or_404


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 
              'section_name', 'image_illustrator', 'is_asking_for_illustration']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        if self.request.user.is_columnist or self.request.user.is_superuser:
            form.instance.status = 'approved'
        else:
            form.instance.status = 'pending'
        
        response = super().form_valid(form)

        if form.instance.textual_genre.textual_genre.lower() == 'fanfic':
            Chapter.objects.create(
                post=self.object,
                title=self.object.title,
                content=self.object.main_text
            )
        
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_artist': user.is_artist,
            'is_columnist': user.is_columnist,
        })
        return context

    def get_success_url(self):
        return reverse('posts:detail_text', kwargs={'pk': self.object.pk})


class PostListView(ListView):
    model = Post
    ordering = ['-created']

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
         
            elif filter_by == 'user':
                queryset = queryset.filter(user__first_name__icontains=search_term)
                
            elif filter_by == 'title_main_text':
                queryset = queryset.filter(
                    Q(title__icontains=search_term) |
                    Q(main_text__icontains=search_term)
                )
        queryset = queryset[:25] 

        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostFilterForm(self.request.GET)
        return context 
    
  
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        
        if post.textual_genre.textual_genre.lower() == 'fanfic':
            chapters = Chapter.objects.filter(post=post).order_by('chapter_number')
            context['post_chapters'] = chapters
            context['has_continuation'] = chapters.count() > 1
            
            selected_chapter_id = self.request.GET.get('chapter_id')
            if selected_chapter_id:
                selected_chapter = get_object_or_404(chapters, id=selected_chapter_id)
                context['selected_chapter_id'] = int(selected_chapter_id)
                context['selected_chapter'] = selected_chapter
        else:
            context['has_continuation'] = False

        context['post_user'] = post.user
        context['user_is_authenticated'] = self.request.user.is_authenticated
        context['post_created'] = post.created
        context['post_updated'] = post.updated
        context['is_illustration_done'] = post.is_illustration_done
        context['is_asking_for_illustration'] = post.is_asking_for_illustration
        context['subtitle_illustrator'] = post.subtitle_illustrator
        context['post_image'] = post.image

        if post.is_illustration_done:
            context['illustrator'] = post.illustrator
            context['illustrator_instagram'] = post.illustrator.user_instagram
            context['illustrator_linkedin'] = post.illustrator.user_linkedin
        
        context['post_textual_genre'] = post.textual_genre

        context['post_section_name'] = post.section_name
        
        return context




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
    
    
class ChapterCreateView(CreateView, LoginRequiredMixin):
    model = Chapter
    fields = ['title', 'content']
    template_name = 'posts/create_chapter.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['post_id'])
        next_chapter_number = Chapter.objects.filter(post=post).count() + 1
        context['next_chapter_number'] = next_chapter_number
        context['user'] = post.user
        context['fanfic_title'] = post.title
        context['content'] = post.main_text

        return context

    def get_success_url(self):
        return reverse('posts:detail_text', kwargs={'pk': self.object.post.pk})

    


