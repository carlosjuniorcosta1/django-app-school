from django.urls import path 

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'), 
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"
    ),
          name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

]