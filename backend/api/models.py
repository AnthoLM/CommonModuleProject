from django.db import models

# Create your models here.
class Event(models.Model):
    #All the blanking is to make the fields optional in the admin panel.
    #From the front end, the fields will be required. The users must not be able to click on the send button without filling the fields.
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    dateDebut = models.DateTimeField(null=True)
    dateFin = models.DateTimeField(null=True)
    allDay = models.BooleanField(default=False)
    streetName = models.CharField(max_length=100, default="", blank=True)
    streetNumber = models.CharField(max_length=10, default="", blank=True)
    AgeCategory = models.ForeignKey('AgeCategory', on_delete=models.CASCADE, null=True) #Will probably need a related name
    EventCategory = models.ForeignKey('EventCategory', on_delete=models.CASCADE, null=True) #Will probably need a related name
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE, null=True) # One to many relationship (One user can have many events)
    #This need works and can not be used as is. 
    #The owner field actually doesn't work because the user is not logged in when the event is created.
    
    class Meta:
        ordering = ['dateDebut']
    def __str__(self):
        return self.title

class AgeCategory(models.Model):
    #There is a possibility to create the categories already here and not in the admin panel, same for the event categories
    name = models.CharField(max_length=100)
    minAge = models.IntegerField(null=True)

    class Meta:
        ordering = ['minAge']
    def __str__(self):
        return self.name

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name