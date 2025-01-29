from django.shortcuts import render,HttpResponse
from .api_functions import FlightAPI

def search(request):
  api_class = FlightAPI()
  if request.method == "POST":
    city_code = request.POST.get('city_code')
    date = request.POST.get('date')
    data = api_class.search_by_city_code(city_code, date)
    print(data)
  return HttpResponse('Hii')