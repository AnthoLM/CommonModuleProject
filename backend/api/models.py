from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    npa = models.IntegerField(default='0001')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'
