from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, permissions, status
from .models import Message, Place, PlaceCommentary, EventCommentary, Event
from .serializers import UserSerializer, GroupSerializer, MessageSerializer, ReadPlaceSerializer, PostPlaceSerializer, ReadPlaceCommentarySerializer, PostPlaceCommentarySerializer, ReadEventCommentarySerializer, PostEventCommentarySerializer, ReadEventSerializer, PostEventSerializer
from django.utils import timezone
from rest_framework.response import Response

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
    permissions_classes = [permissions.IsAuthenticated]

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

class PlaceCommentaryViewSet(viewsets.ModelViewSet):
    queryset = PlaceCommentary.objects.all()
    serializer_class = ReadPlaceCommentarySerializer
    permissions_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"] :
            return PostPlaceCommentarySerializer
        return ReadPlaceCommentarySerializer
    
class EventCommentaryViewSet(viewsets.ModelViewSet):
    queryset = EventCommentary.objects.all()
    serializer_class = ReadEventCommentarySerializer
    permissions_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"] :
            return PostEventCommentarySerializer
        return ReadEventCommentarySerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = ReadEventSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return PostEventSerializer
        return ReadEventSerializer
    
    def register(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if event.users_registered.filter(pk=user.pk).exists():
            # User is already registered for the event
            return Response({'detail': 'User is already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)

        if event.users_registered.count() >= event.maxParticipants:
            # Maximum number of participants reached
            return Response({'detail': 'Maximum number of participants reached for this event.'}, status=status.HTTP_400_BAD_REQUEST)

        event.users_registered.add(user)
        event.save()

        # Update the registration count
        registration_count = event.users_registered.count()

        return Response({'detail': 'User successfully registered for the event.', 'registration_count': registration_count}, status=status.HTTP_200_OK)
    