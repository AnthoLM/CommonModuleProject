from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Message, Place


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Place
        fields = ('pk','name', 'address', 'city', 'npa')

    # Test can be deleted in the future
    def create(self, validated_data):
        place = Place.objects.create(
            name=validated_data['name'],
            address=validated_data['address'],
            city=validated_data['city'],
            npa=validated_data['npa']
        )
        return place
    
    def delete(self, instance):
        instance.delete()

    # Test can be deleted in the future
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.npa = validated_data.get('npa', instance.npa)
        instance.save()
        return instance

    def get_city(self, obj):
        return obj.city

    def get_npa(self, obj):
        return obj.npa
