from django.shortcuts import render, get_object_or_404
from . forms import PostForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post
from django.urls import reverse_lazy

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

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("posts:thank_you")



class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"

