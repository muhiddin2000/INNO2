from django.db import models
from contact.models import CustomUser
from django.contrib.contenttypes.models import ContentType


# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    count_seen = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title


# class CommentManager(models.Manager):
#     def all(self):
#         qs = super(CommentManager, self).filter(parent=None)
#         return qs
#
#     def filter_by_instance(self, instance):
#         content_type = ContentType.objects.get_for_model(instance.__class__)
#         obj_id = instance.id
#         qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
#         return qs


class Comment(models.Model):
    name = models.CharField(max_length=200)
    messages = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    # objects = CommentManager()

    def __str__(self):
        return self.name

    def children(self):  # replies
        return Comment.objects.filter(messages=self)

    @property
    def is_parent(self):
        if self.messages is not None:
            return False
        return True
