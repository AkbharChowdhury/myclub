from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>', views.home, name='home'),
    path('venue_download/<str:extension>', views.venue_download, name='venue_download'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    # path('add_venue/', views.add_venue, name='add_venue'),
    path('add_venue/', views.VenueCreateView.as_view(), name='add_venue'),
    path('add_event/', views.EventCreateView.as_view(), name='add_event'),

    path('list_venues/', views.VenueListView.as_view(), name='list_venues'),
    path('show_venue/<int:pk>', views.VenueDetailView.as_view(), name='show_venue'),

    # path('search_venue/', views.search_venue, name='search_venue'),
    path('search_venue/', views.SearchVenueList.as_view(), name='search_venue'),
    # path('admin_approval/', views.admin_approval, name='admin_approval'),
    path('admin_approval/', views.AdminApprovalCreateView.as_view(), name='admin_approval'),


]
