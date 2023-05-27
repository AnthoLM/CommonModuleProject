from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, permissions
from .models import Message, Place, Commentary, Event
from .serializers import UserSerializer, GroupSerializer, MessageSerializer, ReadPlaceSerializer, PostPlaceSerializer, ReadCommentarySerializer, PostCommentarySerializer, ReadEventSerializer, PostEventSerializer
from django.utils import timezone

current_time = timezone.now()

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # SHOULD IMPLEMENT CUSTOM PERMISSIONS FOR OBJECT LEVEL SECURITY
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = ReadPlaceSerializer
    permissions_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Place.objects.all()
        city = self.request.query_params.get('city', None)
        npa = self.request.query_params.get('npa', None)
        if city is not None and npa is not None:
            queryset = queryset.filter(city=city, npa=npa)
        elif city is not None:
            queryset = queryset.filter(city=city)
        elif npa is not None:
            queryset = queryset.filter(npa=npa)
        return queryset
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return PostPlaceSerializer
        return ReadPlaceSerializer

    # SHOULD IMPLEMENT CUSTOM PERMISSIONS FOR OBJECT LEVEL SECURITY

class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = ReadCommentarySerializer
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"] :
            return PostCommentarySerializer
        return ReadCommentarySerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = ReadEventSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return PostEventSerializer
        return ReadEventSerializer
    