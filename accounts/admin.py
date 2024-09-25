from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_columnist', 'presentation', 'user_picture']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_columnist', 'presentation', 'user_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_columnist', 'presentation', 'user_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)