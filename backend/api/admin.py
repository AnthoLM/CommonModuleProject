from django.contrib import admin

from .models import Message, Place, PlaceCommentary, EventCommentary, Event, Registered_to_Event


@admin.register(Message)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('subject', 'body')


@admin.register(Place)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'city', 'npa', 'user')
    list_filter = ('city', 'npa')
    search_fields = ('name', 'city', 'address', 'npa', 'user')

@admin.register(PlaceCommentary)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'place', 'content', 'date')
    list_filter = ('user', 'place', 'date')
    search_fields = ('user', 'place', 'content', 'date')

@admin.register(EventCommentary)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'event', 'content', 'date')
    list_filter = ('user', 'event', 'date')
    search_fields = ('user', 'event', 'content', 'date')

@admin.register(Event)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'startDate', 'endDate', 'place', 'user', 'maxParticipants')
    list_filter = ('startDate', 'endDate', 'place', 'user')
    search_fields = ('name', 'description', 'startDate', 'endDate', 'place', 'user', 'maxParticipants')

@admin.register(Registered_to_Event)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'event')
    list_filter = ('user', 'event')
    search_fields = ('user', 'event')

