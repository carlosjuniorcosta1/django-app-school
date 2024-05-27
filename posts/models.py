from django.db import models
from django.contrib.auth.models import User 

  
class Genre(models.Model):
    genre_choices = [
        ('reportagem', 'Reportagem'),
        ('noticia', 'Notícia'),
        ('artigo_opiniao', 'Artigo de opinião'),
        ('fanfic', 'Fanfic') 
      ]
    textual_genre = models.CharField(max_length=30, choices=genre_choices)
    
    def __str__(self):
        return self.textual_genre
    
class Post(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    textual_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.user.username} {self.textual_genre}-{self.created}"
    

    



