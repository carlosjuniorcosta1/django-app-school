from django import forms


class PostFilterForm(forms.Form):
    filter_choices = [
        ('title', 'Título'),
        ('textual_genre', 'Gênero'),
        ('section_name', 'Seção'),
        ('main_text', 'Palavra no texto')
    ]
    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar por", initial='')
    search_term = forms.CharField(required=False, label="Buscar")






    

    
