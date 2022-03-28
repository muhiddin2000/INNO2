from django.contrib import admin
from .models import Post, Comment


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'about', 'body', 'image', 'create_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'messages', 'create_at']
