from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #CreatedPlace - udpatedPlace + date


class Place(models.Model):
    #pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    npa = models.IntegerField(default='0001')

    def __str__(self):
        return self.name
