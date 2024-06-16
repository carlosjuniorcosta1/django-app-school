from django import forms


class ListBnccForm(forms.Form):
    filter_choices = [
        ('cur_comp', 'Matéria'),
        ('k_obj', 'Objeto do conhecimento'),
        ('skill', 'Habilidade'),
        ('description', 'Descritor')
    ]

    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar", initial='')
    search_term = forms.CharField(required=False, label="Buscar")

