from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Essay
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



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
        essays = Essay.objects.all()
        return essays


class DetailEssay(DetailView):
    model = Essay
    template_name = "review_essay/review_essay_detail.html"
    context_object_name = "essay"


class UpdateEssay(UpdateView):
    model = Essay
    fields = ['essay_topic', 'essay_image']
    template_name = "review_essay/review_essay_post.html"
    success_url = reverse_lazy('review_essay:list_essay_editors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Reenviar ou corrigir"

        return context 





    
