from django import forms


class ListBnccForm(forms.Form):
    filter_choices = [
        ('cur_comp', 'Matéria'),
        ('k_obj', 'Objeto do conhecimento'),
        ('whole_skill', 'Habilidade')
    ]

    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar", initial='', widget=forms.RadioSelect)
    search_term = forms.CharField(required=False, label="Buscar")

