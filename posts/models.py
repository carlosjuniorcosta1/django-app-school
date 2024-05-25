from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} --{self.created}"
    

    
    



