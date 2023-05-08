from django.db import models
import json


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def create_from_json(cls, json_data):
        place = cls(
            name=json_data['name'],
            address=json_data['address'],
            city=json_data['city'],
            latitude=float(json_data['lat']),
            longitude=float(json_data['lng']),
            country=json_data['country']
        )
        place.save()
        return place
