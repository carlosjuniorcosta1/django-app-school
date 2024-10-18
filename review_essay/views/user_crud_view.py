from django.views.generic import ListView, CreateView, DetailView, UpdateView
from ..models import Essay
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

class UpdateEssay(UpdateView):
    model = Essay
    template_name = "review_essay/review_essay_post.html"
    success_url = reverse_lazy('review_essay:submit_essay')
    fields = ['essay_topic', 'essay_image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Reenviar ou corrigir"

        return context 
    
    
class DetailEssay(DetailView):
    model = Essay
    template_name = "review_essay/review_essay_detail.html"
    context_object_name = "essay"


class ListUserEssay(ListView):
    model = Essay
    template_name = "review_essay/review_essay_list_user_essays.html"

    def get_queryset(self):
        queryset = Essay.objects.filter(user=self.request.user, is_finished=True)
        return queryset
    
class DetailUserReviewedEssay(DetailView):
    template_name = 'review_essay/review_detail_corrected_essay.html'
    model = Essay



    
