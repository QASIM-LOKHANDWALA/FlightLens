from django.shortcuts import render
from .api_functions import AirportAPI

airport_api = AirportAPI()

# Create your views here.
def home(request):
  airports = airport_api.get_airports()
  return render(request, 'airports/airport_home.html')