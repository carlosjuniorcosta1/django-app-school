from django import forms


class PostFilterForm(forms.Form):
    filter_choices = [
        ('main_text', 'Palavra'),
        ('title', 'Título'),
        ('textual_genre', 'Gênero'),
        ('section_name', 'Seção'),
        ('user', 'Colunista')
    ]
    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar por", initial='')
    search_term = forms.CharField(required=False, label="Buscar")