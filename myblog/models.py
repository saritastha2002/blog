from django.db import models
from django.urls import reverse


# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    
    