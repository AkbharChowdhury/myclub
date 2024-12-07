from django.shortcuts import render
from calendar import month_name, HTMLCalendar
import datetime
import calendar
import datetime


# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

def home(request, year: int = datetime.date.year, month: str = "Jan"):
    month_num = list(calendar.month_name).index(month.title())
    return render(request, 'home.html', {
        'year': year,
        'month': month,
        'my_calendar': HTMLCalendar().formatmonth(year, month_num),
    })
