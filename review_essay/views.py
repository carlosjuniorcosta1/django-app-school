from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Essay
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
import base64



class CreateEssayReview(LoginRequiredMixin, CreateView):
    model = Essay
    template_name = 'review_essay/review_essay_post.html'
    fields = ['essay_image', 'essay_topic']
    success_url = reverse_lazy('review_essay:submit_essay')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_essays = Essay.objects.filter(user=self.request.user, is_reviewed=False)
        context['has_pending_essay'] = pending_essays.exists()
        context['essay'] = pending_essays.first() if pending_essays.exists() else None  
        return context 


class ListEssayForEditors(ListView):
    model = Essay
    template_name = 'review_essay/review_essay_list.html'
    context_object_name = 'essays'

    def get_queryset(self):
        queryset = Essay.objects.filter(is_reviewed=False)
        return queryset

class UpdateEssay(UpdateView):
    model = Essay
    template_name = "review_essay/review_essay_post.html"
    success_url = reverse_lazy('review_essay:submit_essay')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Reenviar ou corrigir"

        return context 
    
class DetailEssay(DetailView):
    model = Essay
    template_name = "review_essay/review_essay_detail.html"
    context_object_name = "essay"


class UpdateEssayEditor(UpdateView):
    model = Essay
    fields = ["c1", "about_c1", "c2", "about_c2", "c3", "about_c3", "c4", "about_c4", "c5", "about_c5", "correction_image"] 
    template_name = "review_essay/review_essay_edit_essay.html"
    success_url = reverse_lazy('review_essay:list_essay_editors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['essay'] = self.object
        return context

    def form_valid(self, form):
        correction_image_data = self.request.POST.get("correction_image")
        print(f"Imagem recebida: {correction_image_data}")  # Exibe os primeiros 100 caracteres para verificar
        if correction_image_data:
            format, imgstr = correction_image_data.split(';base64,') 
            ext = format.split('/')[-1]  # Pega a extensão da imagem
            image_file = ContentFile(base64.b64decode(imgstr), name=f'correction.{ext}')
            form.instance.correction_image = image_file  # Salva a imagem no modelo
        return super().form_valid(form)

    
