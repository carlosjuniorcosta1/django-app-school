from django.views.generic import ListView
from posts.models import Post
from accounts.models import CustomUser as User 


class UserSharedPostsListView(ListView):
    model = Post
    template_name = 'user_posts/list_user_posts.html'
    context_object_name = "posts"

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user_id=user_id, status__in= ['approved', 'pending']).order_by('-created')

