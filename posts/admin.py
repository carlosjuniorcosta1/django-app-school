from django.contrib import admin
from .models import Post, Genre, Section, Chapter

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1  # Número de capítulos adicionais exibidos por padrão

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]
    list_display = ('title', 'user', 'textual_genre', 'created', 'status')
    list_filter = ('textual_genre', 'status', 'created')

# Registrando os outros modelos
admin.site.register(Genre)
admin.site.register(Section)
