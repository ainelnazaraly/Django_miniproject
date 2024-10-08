from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = ['title', 
    'content', 
    'created_at', 
    'author'
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display = [
        'content', 
        'created_at', 
        'post', 
        'author'
    ]
# Register your models here.
