from django.views.generic import ListView
from ..models import Post
from posts.forms.brazil_form import BrazilForm
from django.db.models import Q


class BrazilListView(ListView):
    model = Post
    fields = ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 'section_name']
    template_name = "posts/brazil/brazil_index.html"

    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="brasil", status="approved").order_by('-created')

        form = BrazilForm(self.request.GET)
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
        context['brazil_posts'] = self.get_queryset()
        context['form'] = BrazilForm(self.request.GET)

        return context 





