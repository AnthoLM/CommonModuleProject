#from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, AgeCategory, EventCategory
from .serializers import EventSerializer, AgeCategorySerializer, EventCategorySerializer
#from rest_framework import generics
#from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
#Not sure all those imports are needed but the tutorial used them at some points and I don't have the brain to know which one does what. 
#I've commented the ones I'm not sure about.
#I'm purposedly typing long sentences because otherwise it's all copilote writing for me and I hate it. 

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        
        'event': reverse('event-list', request=request, format=format),
        'ageCategory': reverse('ageCategory-list', request=request, format=format),
        'eventCategory': reverse('eventCategory-list', request=request, format=format)
    })


class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer


    def perform_create(self, serializer):
        serializer.save()


class AgeCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = AgeCategory.objects.all()
    serializer_class = AgeCategorySerializer


    def perform_create(self, serializer):
        serializer.save()
