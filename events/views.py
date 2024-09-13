import calendar

from django.shortcuts import render
from calendar import HTMLCalendar
import calendar
from datetime import datetime, timedelta


def home(request, year, month):
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
