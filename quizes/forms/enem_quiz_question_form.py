from django import forms 

class QuestionForm(forms.Form):
    filter_choices = [
        ('word', 'Palavra'),
        ('year', 'Ano'), 
    ]

    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar", initial="")
    search_term = forms.CharField(required=False, label="Buscar")