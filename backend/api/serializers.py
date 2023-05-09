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

    city = serializers.SerializerMethodField()
    npa = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('name', 'address', 'city', 'npa')

    def get_city(self, obj):
        return obj.city

    def get_npa(self, obj):
        return obj.npa
