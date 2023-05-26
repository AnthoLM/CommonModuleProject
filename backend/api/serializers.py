from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Message, Place, Commentary


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

    class Meta:
        model = Place
        fields = ('pk','name', 'address', 'city', 'npa', 'user')

    # Test can be deleted in the future
    def create(self, validated_data):
        place = Place.objects.create(
            name=validated_data['name'],
            address=validated_data['address'],
            city=validated_data['city'],
            npa=validated_data['npa']
        )
        return place

    # Test can be deleted in the future
    def update(self, instance, validated_data):
        instance.pk = validated_data.get('pk', instance.pk)
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
    
class ReadPlaceSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Place
        fields = ('pk','name', 'address', 'city', 'npa', 'user')

class ReadCommentarySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Commentary
        fields = ['id', 'user', 'place', 'content', 'date']

class PostCommentarySerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = Commentary
        fields = ['id', 'user', 'place', 'content', 'date']