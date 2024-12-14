from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('club_events.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'MyClub Admin'
admin.site.site_title = 'MyClub Admin'
admin.site.index_title = 'Welcome to the admin site'
