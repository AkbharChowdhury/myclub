from django.contrib import admin

from .models import Event, MyClubUser, Venue
admin.site.register(Event)
admin.site.register(MyClubUser)
admin.site.register(Venue)
