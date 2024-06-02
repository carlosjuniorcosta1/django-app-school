from django.db import models
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import os
 
class Genre(models.Model):
    genre_choices = [
        ('reportagem', 'Reportagem'),
        ('noticia', 'Notícia'),
        ('artigo', 'Artigo de opinião'),
        ('fanfic', 'Fanfic'),
        ('conto', 'Conto'),
        ('resenha', 'Resenha'),
        ('receitas', 'Receitas'),
        ('resumo', 'Resumo')

      ]
    textual_genre = models.CharField(max_length=30, choices=genre_choices, blank=True, null=True)
    
    def __str__(self):
         return self.textual_genre
    
class Section(models.Model):
    section_choices = [
            ('saude', 'Saúde'),
            ('opiniao', 'Opinião'),
            ('mundo', 'Mundo'),
            ('brasil', 'Brasil'),
            ('gastronomia', 'Gastronomia'),
            ('cultura_lazer', 'Cultura e Lazer'),
            ('esportes', 'Esportes'),
            ('enem', 'Enem'), 
            ('professor', 'Professor')

      ]
    
    section_name = models.CharField(max_length=50, choices=section_choices)

    def __str__(self):
        return self.section_name
       


    
class Post(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(null=True, blank=True)
    textual_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    post_views = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="images/", 
                                      validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
)
    section_name = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return f"{self.user.username} {self.textual_genre}-{self.created}"
  
    def clean(self):
      super().clean()
      if self.image:
        max_size = 2 * 1024 * 1024  
        if self.image.size > max_size:
            raise ValidationError("A imagem não pode ser maior que 2MB")
    
    
    

    



