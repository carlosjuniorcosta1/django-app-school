from django import forms

class PostOpinionForm(forms.Form):
    filter_choices = [
        ('title_main_text', 'Palavra'),
        ('user', 'Colunista'),
        ('title', 'Título')
    ]
    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar por", initial='')
    search_term = forms.CharField(required=False, label="Buscar")

class PostOpinionStudentsForm(forms.Form):
    filter_choices = [
        ('title_main_text', 'Palavra'),
        ('user', 'Autor'),
        ('title', 'Título')
    ]
    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar por", initial='')
    search_term = forms.CharField(required=False, label="Buscar")


