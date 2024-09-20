from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from ..models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['user_picture', 'presentation']  
    template_name = 'registration/dashboard.html'
    success_url = reverse_lazy('dashboard')  

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk) 
    
    from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from ..models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['user_picture', 'presentation']
    template_name = 'registration/dashboard.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def form_valid(self, form):
        form.instance.user_picture = self.request.FILES.get('user_picture') 
        return super().form_valid(form)

    
