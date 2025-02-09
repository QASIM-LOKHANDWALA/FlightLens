from django.urls import path
from . import views

urlpatterns = [
    path('', views.flights_home, name='flights_home'),
    path('search/', views.flight_search, name='flight_search'),
    path('details/<str:flight_number>/', views.flight_details, name='flight_details'),
    path('tracking/', views.flight_tracking, name='flight_tracking'),
    path('nearest_airport/', views.nearest_airport, name='nearest_airport'),
]
