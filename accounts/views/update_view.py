from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from ..models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['user_picture', 'presentation', 'user_instagram', 'user_linkedin', 'user_youtube', 'user_facebook']  
    template_name = 'registration/dashboard.html'
    success_url = reverse_lazy('accounts:dashboard')  

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)
    
    def form_valid(self, form):
        if not self.request.FILES.get('user_picture'):
            form.instance.user_picture = self.get_object().user_picture
        return super().form_valid(form)

    
