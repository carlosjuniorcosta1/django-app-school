from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import os
from accounts.models import CustomUser as User
 
class Genre(models.Model):
    genre_choices = [
        ('reportagem', 'Reportagem'),
        ('noticia', 'Notícia'),
        ('artigo', 'Artigo'),
        ('fanfic', 'Fanfic'),
        ('conto', 'Conto'),
        ('resenha', 'Resenha'),
        ('receita', 'Receita'),
        ('cronica', 'Crônica'),
        ('resumo', 'Resumo'),
        ('tirinha', 'Tirinha'), 
        ('ilustracao', 'Ilustração')
        
      ]
    textual_genre = models.CharField(max_length=30, choices=genre_choices, blank=True, null=True)

    def __str__(self):
      return self.get_textual_genre_display()
    
    def get_textual_genre_names (self):
      return self.textual_genre

 
class Section(models.Model):
    section_choices = [
            ('saude', 'Saúde'),
            ('opiniao', 'Opinião'),
            ('mundo', 'Mundo'),
            ('brasil', 'Brasil'),
            ('cultura_lazer', 'Cultura e Lazer'),
            ('enem', 'Enem'), 
            ('professor', 'Professor')

      ]
    subsection_choices = [
       ('literatura', 'Literatura'), 
       ('cinema_tv', 'Cinema e TV'),
       ('games', 'Jogos'),
       ('comida', 'Comida'),
       ('artes', 'Ilustrações')
    ]
    
    section_name = models.CharField(max_length=50, choices=section_choices)
    subsection_name = models.CharField(max_length=50, choices=subsection_choices, blank=True, null=True)

    def __str__(self):
        if not self.subsection_name:
           return self.get_section_name_display()
        else:
           return f'{self.get_subsection()}'
    
    def get_section_names(self):
       return self.section_name
    
    def get_subsection(self):
        if self.subsection_name:
            return dict(self.subsection_choices).get(self.subsection_name)
        return None
       

class Post(models.Model):
    status_choices = (
    ('pending', 'Pendente'),
    ('approved', 'Aprovado'),
    ('rejected', 'Rejeitado'),
    )
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(null=True, blank=True)
    textual_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    post_views = models.IntegerField(default=0)
    image = models.ImageField(blank=True, upload_to="images/", 
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])])
    section_name = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    image_illustrator =  models.ImageField(null=True, blank=True, upload_to="images/", 
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])])

    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    is_asking_for_illustration = models.BooleanField(null=True, blank=True, default=False)
    is_illustration_done = models.BooleanField(default=False, null=True, blank=True)
    illustrator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='illustrated_posts')
    subtitle_illustrator = models.CharField(max_length=35, blank=True, null=True)

   
    def __str__(self):
        return f"{self.status}, {self.user.first_name} {self.user.last_name}, {self.section_name}, {self.textual_genre}, Asking for illustration: {self.is_asking_for_illustration} Illustration done: {self.is_illustration_done}, Title: {self.title}"
  
    def clean(self):
      super().clean()
      if self.image:
        max_size = 2 * 1024 * 1024  
        if self.image.size > max_size:
            raise ValidationError("A imagem não pode ser maior que 2MB")
 
    
    

    



