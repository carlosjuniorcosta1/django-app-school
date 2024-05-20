from django import forms
from . models import Posts


class PostsForm(forms.ModelForm):
    model = Posts
    fields = "__all__"

    
