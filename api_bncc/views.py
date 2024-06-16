from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import ApiBncc
from api_bncc.forms.list_bncc_form import ListBnccForm

class ApiBnccListView(ListView):
    model = ApiBncc
    fields = ['cur_comp', 'k_obj', 'skill']
    template_name = 'api/api_bncc/bncc_list.html'

    def get_queryset(self):
        queryset =  queryset = super().get_queryset()

        form = ListBnccForm(self.request.GET)

        if form.is_valid():
            filter_by = form.cleaned_data.get('filter_by')
            search_term = form.cleaned_data.get('search_term')

            if filter_by == 'cur_comp':
                queryset = queryset.filter(cur_comp__icontains=search_term)
            elif filter_by == 'k_obj':
                queryset = queryset.filter(k_obj__icontains=search_term)
            elif filter_by == 'skill':
                queryset = queryset.filter(skill__icontains=search_term)
            
            return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_bncc'] = self.get_queryset()
        context['form'] = ListBnccForm(self.request.GET)
        return context 
        


        





# Create your views here.
