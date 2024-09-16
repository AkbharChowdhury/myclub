import calendar
from calendar import HTMLCalendar
from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Event, Venue
from django.shortcuts import get_object_or_404


def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    name = 'john'.title()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)
    cal = HTMLCalendar().formatmonth(year, month_num)
    now = datetime.now()
    current_year = now.year
    return render(request, 'home.html',
                  {
                      'year': year,
                      'month': month,
                      'name': name,
                      'cal': cal,
                      'current_year': current_year,
                  })


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'event_list.html', {'event_list': event_list})


# def add_venue(request):
#     is_submitted = False
#     if request.method == 'POST':
#         form = VenueForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect('/add_venue?is_submitted=True')
#         else:
#             is_submitted = True
#
#     form = VenueForm
#     return render(request, 'add_venue.html', {'form': form, 'is_submitted': is_submitted})


class VenueCreateView(SuccessMessageMixin, CreateView):
    model = Venue
    context_object_name = 'venue'
    template_name = 'add_venue.html'
    fields = '__all__'
    success_message = f'venue created'.title()
    success_url = 'add_venue'


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'venue.html', {'venue_list': venue_list})


def show_venue(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    return render(request, 'show_venue.html', {'venue': venue})


def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'search_venue.html', {'searched': searched, 'venues': venues})
    return render(request, 'search_venue.html', {})
