from django.shortcuts import render
from django.http import JsonResponse
from .api_functions import FlightAPI

def flights_home(request):
  
  return render(request, 'flights/flights_home.html') 

def flight_search(request):
  if request.method == "POST":
    origin = request.POST.get("origin")
    destination = request.POST.get("destination")
    date = request.POST.get("date")

    flight_api = FlightAPI()
    flights = flight_api.search_flights(origin, destination, date)

    return render(request, "flights/flight_results.html", {"flights": flights})
  return render(request, "flights/flight_search.html")

def flight_details(request, flight_number):
  flight_api = FlightAPI()
  details = flight_api.get_flight_details(flight_number)
  
  if details is None:
    return JsonResponse({"error": "Flight details not available."}, status=404)
  
  return render(request, "flights/flight_details.html", {"details": details})

def flight_tracking(request):
  return render(request, "flights/flight_tracking.html")

def nearest_airport(request):
  flight_api = FlightAPI()
  lat = request.GET.get("lat")
  lon = request.GET.get("lon")
  if not lat or not lon:
    return JsonResponse({"error": "Latitude and longitude are required"}, status=400)

  try:
    flight_api = FlightAPI()
    nearest_airport = flight_api.get_nearest_airport(float(lat), float(lon))
    return JsonResponse({"nearest_airport": nearest_airport})
  except Exception as e:
    print(e)
    return JsonResponse({"error": str(e)}, status=500)