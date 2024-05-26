from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def list_posts(request):
    return render(request, 'posts/post_example.html')

def thank_you(request):
    return render(request,'posts/thank_you.html' )


# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             new_post = form.save()
        
#             return render(request, "posts/create_post.html",  {'form': form, 'preview_post': new_post})
#     else:
#         form = PostForm()

#     return render(request, 'posts/create_post.html', {'form': form})

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'subtitle', 'main_text']
    success_url = reverse_lazy("posts:list_texts")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    ordering = ['-created']

class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    



 
        

