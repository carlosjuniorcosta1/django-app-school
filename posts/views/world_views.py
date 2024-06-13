from django.views.generic import ListView
from ..models import Post
from django.db.models import Q
from api_awesome.views import GetExchangeListView

class WorldListView(ListView):
    model = Post
    fields = ['title', 'subtitle', 'main_text', 'textual_genre', 'image', 'section_name']
    template_name = 'posts/world/world_index.html'

    def get_queryset(self):
        queryset = Post.objects.filter(section_name__section_name="mundo").order_by('-created')      
        return queryset    
                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['world_posts'] = self.get_queryset()
        context['api_awesome'] = GetExchangeListView.get_exchange_data()
        print(context['api_awesome'])
        return context 





