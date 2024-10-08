from django.urls import path
# . means current directory
from . import views

from .views import VenueCreateView, VenueUpdateView, EventListView, VenueListView, VenueDetailView, EventDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>', views.home, name='home'),
    # path('events/', views.all_events, name='list_events'),
    path('events/', EventListView.as_view(), name='list_events'),
    # EventListView
    # path('add_venue', views.add_venue, name='add_venue'),
    path('add_venue', VenueCreateView.as_view(), name='add_venue'),
    path('list_venues/', VenueListView.as_view(), name='list_venue'),
    # path('show_venue/', views.show_venue, name='show_venue'),
    # path('show_venue/<int:venue_id>', VenueDetailView.as_view(), name='show_venue'),
    # path('show_venue/<int:venue_id>', VenueDetailView.as_view(), name='show_venue'),
    path("show_venue/<int:pk>/", VenueDetailView.as_view(), name="show_venue"),

    path('search_venues', views.search_venues, name='search_venues'),
    path('venue/<int:pk>/update', VenueUpdateView.as_view(), name='update_venue'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='delete_event'),

    # path('venue/<int:pk>/delete', EventDeleteView.as_view(), name='delete_venue'),

]
