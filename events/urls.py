
from django.urls import path
# . means current directory
from . import views

from .views import VenueCreateView



urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>', views.home, name='home'),
    path('events/', views.all_events, name='list-events'),
    # path('add_venue', views.add_venue, name='add_venue'),
    path('add_venue', VenueCreateView.as_view(), name='add_venue'),

]
