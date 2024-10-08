from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField( default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model): 
    content = models.TextField(blank=True)
    created_at = models.DateTimeField( default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
# Create your models here.
