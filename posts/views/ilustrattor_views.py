from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from posts.forms.post_form import PostFilterForm
from django.shortcuts import render
from django.db.models import Q


class ListIllustrationsAsked(ListView):
    model = Post 
    template_name = 'posts/illustrations/list_illustrations.html'
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.filter(is_asking_for_illustration=True, is_illustration_done=False)
     
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['illustrated_posts'] = Post.objects.filter(is_illustration_done=True, illustrator=self.request.user)
        return context
     
class DetailIllustration(DetailView):
    model = Post

    

class UpdateIllustration(UpdateView):
    model = Post 
    fields = ['image', 'is_illustration_done', 'illustrator']
    template_name = 'posts/illustrations/update_image_illustration.html'
    success_url = reverse_lazy('posts:detail_text')
    context_object_name = "posts"

    def get_success_url(self):
        return reverse_lazy('posts:detail_text', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.illustrator = self.request.user
        return super().form_valid(form)
    




    
    


    

