from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import ApiBncc
from api_bncc.forms.list_bncc_form import ListBnccForm

class ApiBnccListView(ListView):
    model = ApiBncc
    fields = ['cur_comp', 'k_obj', 'whole_skill']
    template_name = 'api/api_bncc/bncc_list.html'

    def get_queryset(self):
        queryset =  queryset = super().get_queryset()

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
        context['form'] = ListBnccForm(self.request.GET)
        return context 
        


        





# Create your views here.
