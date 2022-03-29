from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    jinsi = models.BooleanField(default=True, blank=True)
    tel_raqam = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='uploadUser', blank=True)
    kasbi = models.CharField(max_length=100, blank=True)
    uz_haqida = models.TextField(null=True, blank=True)
    teligram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username


class Contact(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    subject = models.TextField()
    messages = models.TextField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
