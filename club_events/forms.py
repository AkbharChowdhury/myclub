from django import forms
from django.contrib.auth.models import User
from .models import Venue, Event


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


class EventForm(forms.ModelForm):
    attendees = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_active=True),
                                               widget=forms.CheckboxSelectMultiple())
    manager = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    event_date_time = forms.DateTimeField()

    class Meta:
        model = Event
        fields = '__all__'
