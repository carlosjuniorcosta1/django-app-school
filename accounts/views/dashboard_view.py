from ..models import CustomUser as User 
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post


class UserPostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'registration/dashboard.html'
    context_object_name = 'user_posts'

    def get_queryset(self):
        queryset = Post.objects.filter(user=self.request.user).order_by('-created')
        print(queryset)  
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context 

    