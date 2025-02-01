import os
from dotenv import load_dotenv
import requests
from django.shortcuts import render
from django.http import JsonResponse
from .api_functions import AirportAPI

airport_api = AirportAPI()
load_dotenv()
def get_amadeus_token():
  url = "https://test.api.amadeus.com/v1/security/oauth2/token"
  data = {
    "grant_type": "client_credentials",
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
  }
  response = requests.post(url, data=data)
  return response.json().get("access_token")

def nearby_airports(request):
  lat = request.GET.get("lat")
  lon = request.GET.get("lon")

  if not lat or not lon:
      return JsonResponse({"error": "Latitude and Longitude required"}, status=400)

  token = get_amadeus_token()
  headers = {"Authorization": f"Bearer {token}"}
  
  url = f"https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude={lat}&longitude={lon}&radius=100"

  response = requests.get(url, headers=headers)

  if response.status_code != 200:
    return JsonResponse({"error": "Failed to fetch airports"}, status=response.status_code)

  return JsonResponse(response.json().get("data", []), safe=False)


# Create your views here.
def home(request):
  airports = airport_api.get_airports()
  if airports:
    context = {
      'airports': airports
    }
  else:
    context = {
      'airports': [],
      'error': 'Error fetching airports'
    }
  return render(request, 'airports/airport_home.html',context)