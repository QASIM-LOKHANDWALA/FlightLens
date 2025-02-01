from django.urls import path
from .views import home,nearby_airports

urlpatterns = [
  path('', home, name='airport_home'),
  path("nearby/", nearby_airports, name="nearby_airports"),
]
