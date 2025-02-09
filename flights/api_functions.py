import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightAPI:
    def __init__(self):
        load_dotenv()
        self.amadeus_client_id = os.getenv("CLIENT_ID")
        self.amadeus_client_secret = os.getenv("CLIENT_SECRET")
        self.token = self._get_amadeus_token()

    def _get_amadeus_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_client_id,
            "client_secret": self.amadeus_client_secret,
        }
        response = requests.post(url, data=data)
        response_data = response.json()
        return response_data.get("access_token")

    def search_flights(self, origin, destination, date):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": date,
            "adults": 1,
            "max": 5,
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json().get("data", [])

    def get_flight_details(self, flight_number):
        url = f"https://test.api.amadeus.com/v2/schedule/flights/{flight_number}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json().get("data")

    def get_nearest_airport(self, lat, lon):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/airports"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {"latitude": lat, "longitude": lon, "radius": 100, "sort": "relevance"}
        response = requests.get(url, headers=headers, params=params)
        
        print("Got nearest airports : ", response.json())
        
        if response.ok:
            data = response.json().get("data", [])
            return data[0] if data else None
        return None
