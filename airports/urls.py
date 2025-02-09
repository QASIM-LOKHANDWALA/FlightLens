from django.urls import path
from .views import home, nearby_airports, search_airports

urlpatterns = [
    path('', home, name='airport_home'),
    path('nearby/', nearby_airports, name='nearby_airports'),
    path('search/', search_airports, name='search_airports'),
]