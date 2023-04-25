from django.contrib import admin
from .models import Event, AgeCategory, EventCategory

admin.site.register(Event)
admin.site.register(AgeCategory)
admin.site.register(EventCategory)

# Register your models here.
