from django import forms
from django.contrib.auth.models import User
from django_flatpickr.widgets import DateTimePickerInput

from .models import Venue, Event


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


class EventForm(forms.ModelForm):
    # attendees = forms.MultiValueField(queryset=User.objects.filter(is_staff=True))
    # attendees = forms.MultiValueField(queryset=User.objects.filter(is_staff=True), fields=)
    attendees = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_active=True), widget=forms.CheckboxSelectMultiple())
    manager = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    event_date_time = forms.DateTimeField()

    # https://stackoverflow.com/questions/74043096/django-crispy-form-filter-by-is-staff
    class Meta:
        model = Event
        fields = '__all__'
