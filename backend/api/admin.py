from django.contrib import admin

from .models import Message, Place


@admin.register(Message)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('subject', 'body')


@admin.register(Place)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'city',
                    'latitude', 'longitude', 'country')
    list_filter = ('city', 'country')
    search_fields = ('name', 'city', 'country')
