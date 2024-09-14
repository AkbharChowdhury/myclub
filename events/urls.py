
from django.urls import path
# . means current directory
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>', views.home, name='home'),
    path('events/', views.all_events, name='list-events'),

]
