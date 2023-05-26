from django.contrib import admin

from .models import Message, Place, Commentary


@admin.register(Message)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('subject', 'body')


@admin.register(Place)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'city', 'npa', 'user')
    list_filter = ('city', 'npa')
    # Try to delete name and address
    search_fields = ('name', 'city', 'address', 'npa', 'user')

@admin.register(Commentary)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'place', 'content', 'date')
    list_filter = ('user', 'place', 'date')
    search_fields = ('user', 'place', 'content', 'date')
