from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from ..models import Post


class ListCorpus(ListView):
    model = Post
    template_name = 'posts/linguistics/list_corpus.html'
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.values('textual_genre__textual_genre').distinct()
        return queryset




