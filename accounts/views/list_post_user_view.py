from django.views.generic import ListView
from posts.models import Post
from accounts.models import CustomUser as User 


class UserSharedPostsListView(ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user_id=user_id, status__in= ['approved']).order_by('-created')

  

        