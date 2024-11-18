
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from ..models import Essay
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import base64
from django.core.files.base import ContentFile


class ListEssayForEditors(ListView):
    model = Essay
    template_name = 'review_essay/review_essay_list.html'
    context_object_name = 'essays'

    def get_queryset(self):
        queryset = Essay.objects.filter(is_finished=False)
        return queryset
     
class UpdateEssayEditor(UpdateView):
    model = Essay
    fields = ["c1", "about_c1", "c2", "about_c2", "c3", "about_c3", "c4", "about_c4", "c5",
               "about_c5", "correction_image", "audio_feedback", 
               'is_reviewed', 'is_finished', 'total_grade'] 
    template_name = "review_essay/review_essay_edit_essay.html"
    success_url = reverse_lazy('review_essay:list_essay_editors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['essay'] = self.object
        return context

    def form_valid(self, form): 


        correction_image = self.request.FILES.get('correction_image')  

        if correction_image:
            form.instance.correction_image = correction_image 

        if 'mark_as_reviewed' in self.request.POST:
            form.instance.is_reviewed = True    
        if 'mark_as_finished' in self.request.POST:
            form.instance.is_finished = True
            form.instance.is_reviewed = True
      
        return super().form_valid(form)
