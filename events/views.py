import calendar

from django.shortcuts import render
from calendar import HTMLCalendar
import calendar
from datetime import datetime
from .models import Event


def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    name = 'john'.title()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)
    print(month_num)
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
