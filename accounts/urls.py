from django.urls import path 

from .views import login_logout_view
from django.contrib.auth import views as auth_views
from .views.update_view import UpdateProfileView

urlpatterns = [
    path('login', login_logout_view.login, name='login'),
    path('register', login_logout_view.register, name='register'),
    path('logout', login_logout_view.logout, name='logout'),
    path('dashboard', login_logout_view.dashboard, name='dashboard'), 
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"
    ),
          name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('update_profile',UpdateProfileView.as_view(), name="update_profile" )

]