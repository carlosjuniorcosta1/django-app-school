from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_columnist', 'presentation', 
                    'user_picture', 'is_artist', 'is_teacher', 'user_instagram', 'user_facebook', 
                    'user_youtube', 'user_linkedin', 'is_essay_editor', 'is_premium', 'has_accepted_terms']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_columnist', 'presentation', 'user_picture', 'is_artist', 
                           'is_teacher', 'user_instagram', 'user_youtube', 'user_linkedin', 
                           'user_facebook', 'is_essay_editor', 'is_premium', 'has_accepted_terms')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_columnist', 'presentation', 'user_picture', 'is_artist', 
                           'is_teacher', 'user_instagram',  'user_youbue', 'user_linkedin',
                             'user_facebook', 'is_essay_editor', 'is_premium', 'has_accepeted_terms')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)