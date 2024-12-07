from django.shortcuts import render
from calendar import month_name, HTMLCalendar
import datetime
import calendar
import datetime


# def home(request):
#     return render(request,'home.html',{})
def home(request, year: int = datetime.date.year, month: str = "march"):
    month_num = list(calendar.month_name).index(month.title())
    return render(request, 'home.html', {
        'year': year,
        'month': month,
        'my_calendar': HTMLCalendar().formatmonth(year, month_num),
    })
