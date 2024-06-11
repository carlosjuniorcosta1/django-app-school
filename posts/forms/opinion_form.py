from django import forms

class PostOpinionForm(forms.Form):
    filter_choices = [
        ('user', 'Colunista'),
        ('main_text', 'Palavra no texto'),
        ('title', 'Título')
    ]
    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar por", initial='')
    search_term = forms.CharField(required=False, label="Buscar")


class PostOpinionStudentsForm(forms.Form):
    filter_choices = [
        ('user', 'Autor'),
        ('main_text', 'Palavra no texto'),
        ('title', 'Título')
    ]
    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar por", initial='')
    search_term = forms.CharField(required=False, label="Buscar")


