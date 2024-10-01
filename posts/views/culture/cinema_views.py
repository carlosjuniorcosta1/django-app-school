from django.views.generic import ListView
from ...models import Post
from posts.forms.culture_form import CultureForm
from django.db.models import Q


class CultureCineListView(ListView):
    model = Post
    template_name = "posts/culture/culture_cinema.html"
    
    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="cultura_lazer",
                                       section_name__subsection_name="cinema_tv",
                                        textual_genre__textual_genre__in=['resenha', 'resumo', 'cronica', 'reportagem']
                                        , status="approved").order_by('-created')
        form = CultureForm(self.request.GET)
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
        context['culture_cinema_posts'] = self.get_queryset()
        context['form'] = CultureForm(self.request.GET)

        return context 





