from django.shortcuts import render
from calendar import HTMLCalendar
import calendar
from calendar_utils import CalendarUtils
from .models import Event

def home(request, year: int = CalendarUtils.current_year(), month: str = CalendarUtils.current_month()):
    month_num = list(calendar.month_name).index(month.title())
    return render(request, 'home.html', {
        'year': year,
        'month': month,
        'my_calendar': HTMLCalendar().formatmonth(year, month_num),
    })


def all_events(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {
        'events': events,
    })
