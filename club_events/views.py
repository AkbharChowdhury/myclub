from django.contrib import messages
from django.shortcuts import render
from calendar import HTMLCalendar
import calendar

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from calendar_utils import CalendarUtils
from club_events.printer import Printer
from .models import Event, Venue
from .forms import VenueForm


def home(request, year: int = CalendarUtils.current_year(), month: str = CalendarUtils.current_month()):
    month_num = list(calendar.month_name).index(month.title())
    return render(request, 'home.html', {
        'year': year,
        'month': month,
        'my_calendar': HTMLCalendar().formatmonth(year, month_num),
    })


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event_list.html'
    ordering = ['event_date_time']


# def all_events(request):
#     return render(request, 'event_list.html', {
#         'events': Event.objects.all().order_by('event_date_time'),
#     })

class VenueCreateView(CreateView):
    model = Venue
    template_name = 'add_venue.html'
    form_class = VenueForm

    def get_success_url(self):
        messages.success(self.request, 'Venue added successfully')
        return reverse_lazy('home')


class VenueListView(ListView):
    model = Venue
    context_object_name = 'venues'
    template_name = 'venue.html'
    # ordering = ['event_date_time']


def list_venues(request):
    return render(request, 'venue.html', {
        'venues': Venue.objects.all(),
    })


class VenueDetailView(DetailView):
    model = Venue
    context_object_name = 'venue'
    template_name = 'show_venue.html'


class SearchVenueList(ListView):
    model = Venue
    context_object_name = 'venues'
    template_name = 'search_venue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searched"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        return Venue.objects.filter(name__icontains=self.request.GET['q'])


def venue_text(request):
    return Printer().text_file()


def venue_csv(request):
    return Printer().csv()


def venue_pdf(request):
    return Printer().pdf()
