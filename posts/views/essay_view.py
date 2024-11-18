from django.views.generic import ListView, CreateView, DetailView, UpdateView
from posts.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.forms.essay_index_form import EssayIndexForm
from django.db.models import Q


class IndexEssayListView(ListView):
    model = Post 
    template_name = "posts/review_essay_posts/review_essay_index.html"

       
    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="redacao", status="approved").order_by('-created')

        form = EssayIndexForm(self.request.GET)
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
        context['essay_posts'] = self.get_queryset()
        context['form'] = EssayIndexForm(self.request.GET)

        return context 


    

    



