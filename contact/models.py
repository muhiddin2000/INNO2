from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    subject = models.TextField()
    messages = models.TextField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
