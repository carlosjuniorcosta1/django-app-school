from django import forms
from . models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control-lg mb-5 rounded',
                'placeholder': "Enter the title",   
                'id': 'idTitle'             
            }), 
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control-lg mb-2 rounded',
                'placeholder': "Enter the subtitle",
                'id': 'idSubtitle'
            }),
            'main_text': forms.Textarea(attrs={
                'class': 'form-control mb-2 rounded border shadow bg-light',
                'placeholder': "Enter the main text",
                "rows": 15,
                'id': 'idMainText'
            })

        }




    

    
