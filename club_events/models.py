from django.contrib.auth.models import User
from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=20, blank=True, null=True)
    web = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class VenueGallery(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.venue


class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date_time = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, related_name='attendees', blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
