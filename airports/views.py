from django.shortcuts import render
from django.http import JsonResponse
from .api_functions import AirportAPI
from django.core.cache import cache
from django.views.decorators.cache import cache_page

airport_api = AirportAPI()

@cache_page(60 * 15)
def home(request):
    country = request.GET.get('country')
    airports = airport_api.get_airports(country=country)
    context = {
        'airports': airports,
        'error': 'Error fetching airports' if not airports else None
    }
    return render(request, 'airports/airport_home.html', context)

def nearby_airports(request):
    print("Nearby airports view called")
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    radius = request.GET.get("radius", 100)

    print(f"lat={lat}, lon={lon}, radius={radius}")

    if not lat or not lon:
        print("Missing coordinates")
        return JsonResponse({"error": "Latitude and Longitude required"}, status=400)

    try:
        airports = airport_api.get_nearby_airports(float(lat), float(lon), int(radius))
        return JsonResponse({"data": airports})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def search_airports(request):
    query = request.GET.get('q')
    if not query:
        return JsonResponse({"error": "Search query required"}, status=400)
    
    results = airport_api.search_airports(query)
    return JsonResponse({"data": results})
