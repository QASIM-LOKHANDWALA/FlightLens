from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='landing_page'),
    path('flights/',include('flights.urls')),
    path('airports/',include('airports.urls')),
]
