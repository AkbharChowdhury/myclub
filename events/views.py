import calendar
from calendar import HTMLCalendar
from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

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


# def all_events(request):
#     event_list = Event.objects.all()
#     return render(request, 'event_list.html', {'event_list': event_list})


class EventListView(ListView):
    template_name = 'event_list.html'
    model = Event


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

    def get_success_url(self):
        return reversed('add_venue')


class VenueUpdateView(UpdateView):
    model = Venue
    context_object_name = 'post'
    template_name = 'update_venue.html'
    fields = '__all__'
    success_message = 'venue updated'.title()

    def get_success_url(self):
        return reversed('list_venue')


class EventDeleteView(DeleteView):
    model = Event
    # context_object_name = 'post'
    # template_name = 'update_venue.html'
    # fields = '__all__'
    success_message = 'event deleted'.title()
    template_name = "event_delete.html"
    success_url = '/'
    #
    # def get_success_url(self):
    #     return reversed('list_events')


# def list_venues(request):
#     venue_list = Venue.objects.all()
#     return render(request, 'venue.html', {'venue_list': venue_list})
class VenueListView(ListView):
    template_name = 'venue.html'
    model = Venue


def show_venue(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    return render(request, 'show_venue.html', {'venue': venue})


class VenueDetailView(DetailView):
    # specify the model to use
    model = Venue
    template_name = 'show_venue.html'


def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'search_venue.html', {'searched': searched, 'venues': venues})
    return render(request, 'search_venue.html', {})
