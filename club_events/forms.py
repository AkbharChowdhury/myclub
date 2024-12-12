from django import forms
from django.contrib.auth.models import User

from .models import Venue, Event


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


class EventForm(forms.ModelForm):
    attendees = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    manager = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))

    # https://stackoverflow.com/questions/74043096/django-crispy-form-filter-by-is-staff
    class Meta:
        model = Event
        fields = '__all__'
