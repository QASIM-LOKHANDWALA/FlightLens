from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='landing_page'),
    path('user_auth/',include('user_auth.urls')),
    path('flights/',include('flights.urls')),
    path('airports/',include('airports.urls')),
]
