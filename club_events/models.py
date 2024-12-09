from django.contrib.auth.models import User
from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    web = models.URLField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date_time = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, related_name='attendees', blank=True)

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
