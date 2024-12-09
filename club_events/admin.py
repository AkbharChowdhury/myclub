from django.contrib import admin
from .models import Venue, Event, MyClubUser

# admin.site.register(Venue)
# admin.site.register(Event)
admin.site.register(MyClubUser)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    search_fields = ('name', 'address')
    ordering = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date_time', 'description', 'manager')
    list_display = ('name', 'event_date_time', 'venue')
    list_filter = ('event_date_time', 'venue')
    ordering = ['event_date_time']
