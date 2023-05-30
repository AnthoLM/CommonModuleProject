from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Message, Place, PlaceCommentary, EventCommentary, Event, Registered_to_Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk', 'created_date', 'updated_date')


class PostPlaceSerializer(serializers.HyperlinkedModelSerializer):

    createdDate = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Place
        fields = ('pk','name', 'address', 'city', 'npa','createdDate', 'user')

    def get_event_ids(self, obj):
        events = obj.events.all()
        return [event.id for event in events]

    # Test can be deleted in the future
    def create(self, validated_data):
        events_data = validated_data.pop('events', [])
        place = Place.objects.create(
            name=validated_data['name'],
            address=validated_data['address'],
            city=validated_data['city'],
            npa=validated_data['npa'],
            user=self.context['request'].user
        )
        place.events.set(events_data)
        return place
    
    def get_event_ids(self, obj):
        events = obj.event_set.all()
        return [event.id for event in events]

    # Test can be deleted in the future
    def update(self, instance, validated_data):
        events_data = validated_data.pop('events', [])
        instance.pk = validated_data.get('pk', instance.pk)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.npa = validated_data.get('npa', instance.npa)
        instance.save()
        instance.events.set(events_data)
        return instance

    def get_city(self, obj):
        return obj.city

    def get_npa(self, obj):
        return obj.npa
    

class ReadPlaceSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Place
        fields = ('pk','name', 'address', 'city', 'npa','createdDate', 'user')

    def get_event_ids(self, obj):
        events = obj.events.all()
        return [event.id for event in events]

class PostPlaceCommentarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PlaceCommentary
        fields = ['id', 'user', 'place', 'content', 'date']


class ReadPlaceCommentarySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = PlaceCommentary
        fields = ['id', 'user', 'place', 'content', 'date']


class ReadEventCommentarySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = EventCommentary
        fields = ['id', 'user', 'event', 'content', 'date']

class PostEventCommentarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EventCommentary
        fields = ['id', 'user', 'event', 'content', 'date']



class ReadEventSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    place = PostPlaceSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'startDate', 'endDate', 'place', 'user', 'maxParticipants']

class PostEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'startDate', 'endDate', 'place', 'user', 'maxParticipants']

class Registered_to_EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registered_to_Event
        fields = ['id', 'user', 'event']