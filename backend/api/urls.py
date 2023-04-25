from api.views import EventViewSet, api_root, EventCategoryViewSet, AgeCategoryViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


event_list = EventViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
event_detail = EventViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

eventcategory_list = EventCategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
eventcategory_detail = EventCategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

agecategory_list = AgeCategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
agecategory_detail = AgeCategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('event/', event_list, name='event-list'),
    path('event/<int:pk>/', event_detail, name='event-detail'),
    path('ageCategory/', agecategory_list, name='agecategory-list'),
    path('ageCategory/<int:pk>/', agecategory_detail, name='agecategory-detail'),
    path('eventCategory/', eventcategory_list, name='eventcategory-list'),
    path('eventCategory/<int:pk>/', eventcategory_detail, name='eventcategory-detail'),
])

