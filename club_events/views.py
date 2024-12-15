from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from calendar import HTMLCalendar
import calendar

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from calendar_utils import CalendarUtils
from club_events.classes.printer import Printer
from club_events.models import Event, Venue
from club_events.forms import VenueForm, EventForm


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


def home(request, year: int = CalendarUtils.current_year(), month: str = CalendarUtils.current_month()):
    month_num = list(calendar.month_name).index(month.title())
    return render(request, 'events/home.html', {
        'year': year,
        'month': month,
        'my_calendar': HTMLCalendar().formatmonth(year, month_num),
    })


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/event_list.html'
    ordering = ['event_date_time']


class VenueCreateView(StaffRequiredMixin, CreateView):
    model = Venue
    template_name = 'events/add_venue.html'
    form_class = VenueForm

    def get_success_url(self):
        messages.success(self.request, 'Venue added successfully')
        return reverse_lazy('home')


class EventCreateView(StaffRequiredMixin, CreateView):
    model = Event
    template_name = 'events/add_event.html'
    form_class = EventForm

    def get_success_url(self):
        messages.success(self.request, 'Venue added successfully')
        return reverse_lazy('home')


class VenueListView(ListView):
    model = Venue
    context_object_name = 'venues'
    template_name = 'events/venue.html'


class VenueDetailView(DetailView):
    model = Venue
    context_object_name = 'venue'
    template_name = 'events/show_venue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = (Venue.objects.get(pk=self.kwargs['pk'])
                             .event_set.all()
                             .filter(event_date_time__gt=datetime.now())
                             .order_by('event_date_time'))
        return context


class SearchVenueList(ListView):
    model = Venue
    context_object_name = 'venues'
    template_name = 'events/search_venue.html'
    ordering = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searched"] = self.request.GET.get("q")
        context["all_venues"] = self.model.objects.all().order_by(self.ordering)
        return context

    def get_queryset(self):
        return Venue.objects.filter(name__icontains=self.request.GET['q'])


def venue_download(request, extension: str):
    printer = Printer()
    match extension:
        case 'pdf':
            return printer.pdf()
        case 'txt':
            return printer.txt()
        case 'csv':
            return printer.csv()
        case _:
            return printer.txt()


class AdminApprovalCreateView(StaffRequiredMixin, ListView):
    model = Event
    fields = '__all__'
    template_name = 'events/admin_approval.html'
    context_object_name = 'events'
    ordering = 'event_date_time'

    def post(self, request, *args, **kwargs):
        events = Event.objects.all().order_by('event_date_time')
        event_id_list = request.POST.getlist('approve_status')
        events.update(approved=False)

        for event_id in event_id_list:
            Event.objects.filter(pk=int(event_id)).update(approved=True)
        return self.get_success_url()

    def get_success_url(self):
        messages.success(self.request, "Events approval updated")
        return redirect(reverse_lazy('admin_approval'))
