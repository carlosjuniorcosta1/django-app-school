from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import ElementarySchoolBncc, HighSchoolBncc
from api_bncc.forms.list_bncc_form import ListBnccFormElSchool

class ElementarySchoolBnccListView(ListView):
    template_name = 'api/api_bncc/bncc_list_es.html'
    

    def get_queryset(self):
        queryset =  ElementarySchoolBncc.objects.all()

        materia = self.request.GET.get('materia')
        ano = self.request.GET.get('ano')
        if materia:
            queryset = queryset.filter(cur_comp__icontains=materia)        
        if ano:
            year_field = f'es{ano}'
            queryset = queryset.filter(**{year_field:True})
            queryset = queryset.order_by('-' + year_field)


        return queryset

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materia = self.request.GET.get('materia')

        context['show_columns_port'] = materia == 'portugues'
        context['show_columns_english'] = materia == 'ingles'
        
        context['api_bncc'] = self.get_queryset()
        context['form'] = ListBnccFormElSchool(self.request.GET)
        return context 
        
class HighSchoolBnccListView(ListView):
    template_name = 'api/api_bncc/bncc_list_hs.html'

    def get_queryset(self):
        queryset = HighSchoolBncc.objects.all()
        materia = self.request.GET.get('materia')

        if materia:
            queryset = queryset.filter(cur_comp__icontains=materia)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materia = self.request.GET.get('materia')

        context['api_bncc_hs'] = self.get_queryset()

        return context



    




        





