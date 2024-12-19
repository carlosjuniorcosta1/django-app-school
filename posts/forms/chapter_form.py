from django import forms

class ChapterFilterForm(forms.Form):
    filter_choices = [
      
        ('chapter_number', 'Número'),
    ]
    filter_by = forms.ChoiceField(choices=filter_choices, label="Filtrar por")
    search_term = forms.CharField(required=False, label="Buscar")