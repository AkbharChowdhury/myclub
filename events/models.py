from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=100)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=100)
    web = models.URLField('Website Address')
    email = models.EmailField('Email Address')

    def __str__(self):
        return self.name.title()


class MyClubUser(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    email = models.EmailField('User Email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.title()


class Event(models.Model):
    name = models.CharField('Event Name', max_length=200)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    # venue = models.CharField(max_length=200)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, related_name='attendees', blank=True)

    def __str__(self):
        return self.name.title()
