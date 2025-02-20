from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank = True, null= True)
    def __str__(self): 
        return f"{self.user.username}'s Profile"

class Follow(models.Model): 
    follower = models.ForeignKey(User, related_name = 'following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name = 'followers', on_delete=models.CASCADE)
# Create your models here.
