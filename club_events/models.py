from django.db import models


class Venue(models.Model):
    name = models.CharField(name='venue name'.title(), max_length=255)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(name='zip code'.title(), max_length=15)
    phone = models.CharField(name='contact phone'.title(), max_length=20)
    web = models.URLField(name='web address'.title())
    email = models.EmailField(name='email address'.title(), max_length=200)



class Event(models.Model):
    name = models.CharField(name='event name'.title(), max_length=120)
    event_date = models.DateTimeField(name='event date'.title())
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
