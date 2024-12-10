from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>', views.home, name='home'),
    path('venue_text/', views.venue_text, name='venue_text'),
    path('venue_csv/', views.venue_csv, name='venue_csv'),

    path('events/', views.EventListView.as_view(), name='event_list'),
    # path('add_venue/', views.add_venue, name='add_venue'),
    path('add_venue/', views.VenueCreateView.as_view(), name='add_venue'),
    path('list_venues/', views.VenueListView.as_view(), name='list_venues'),
    path('show_venue/<int:pk>', views.VenueDetailView.as_view(), name='show_venue'),

    # path('search_venue/', views.search_venue, name='search_venue'),
    path('search_venue/', views.SearchVenueList.as_view(), name='search_venue')


]
