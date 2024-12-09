from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from calendar import HTMLCalendar
import calendar

from django.urls import reverse_lazy
from django.views.generic import CreateView

from calendar_utils import CalendarUtils
from .models import Event, Venue
from .forms import VenueForm


def home(request, year: int = CalendarUtils.current_year(), month: str = CalendarUtils.current_month()):
    month_num = list(calendar.month_name).index(month.title())
    return render(request, 'home.html', {
        'year': year,
        'month': month,
        'my_calendar': HTMLCalendar().formatmonth(year, month_num),
    })


def all_events(request):
    events = Event.objects.all().order_by('event_date_time')
    return render(request, 'event_list.html', {
        'events': events,
    })


def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venue added successfully')
            return redirect(reverse_lazy('add_venue'))
        else:
            messages.error(request, form.errors)
    return render(request, 'add_venue.html', {
        'form': VenueForm,
    })


class VenueCreateView(CreateView):
    model = Venue
    template_name = 'add_venue.html'
    form_class = VenueForm
    success_message = 'Venue added successfully'

    def get_success_url(self):
        return redirect(reverse_lazy('add_venue'))

    # success_url = redirect(reverse_lazy('add_venue'))
