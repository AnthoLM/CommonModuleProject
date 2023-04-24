from rest_framework import serializers
from api.models import Event, AgeCategory, EventCategory

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', "url", 'title', 'description', 'dateDebut', 'dateFin', 'allDay', 'streetName', 'streetNumber', 'AgeCategory', 'EventCategory', 'owner')

class AgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeCategory
        fields = ('id', "url", 'name', 'minAge')

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ('id', "url", 'name', 'description')
