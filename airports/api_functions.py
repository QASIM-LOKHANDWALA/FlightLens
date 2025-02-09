import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta 

class AirportAPI:
    def __init__(self):
        load_dotenv()
        self.aviation_api_key = os.getenv('AVIATIONSTACK_API_KEY')
        self.aviation_base_url = 'https://api.aviationstack.com/v1/'
        self.amadeus_client_id = os.getenv("CLIENT_ID")
        self.amadeus_client_secret = os.getenv("CLIENT_SECRET")
        self._amadeus_token = None
        self._token_expiry = None

    def _get_amadeus_token(self):
        if not self._amadeus_token or not self._token_expiry or datetime.now() >= self._token_expiry:
            url = "https://test.api.amadeus.com/v1/security/oauth2/token"
            data = {
                "grant_type": "client_credentials",
                "client_id": self.amadeus_client_id,
                "client_secret": self.amadeus_client_secret,
            }
            response = requests.post(url, data=data)
            response_data = response.json()
            self._amadeus_token = response_data.get("access_token")
            self._token_expiry = datetime.now() + timedelta(seconds=response_data.get("expires_in", 1800))
        return self._amadeus_token

    def get_airports(self, limit = 10, country = None):
        params = {
            'access_key': self.aviation_api_key,
            'limit': limit
        }
        if country:
            params['country_iso2'] = country

        response = requests.get(f'{self.aviation_base_url}airports', params=params)
        if response.ok:
            data = response.json().get('data', [])
            return data[:limit]
        return []

    def search_airports(self, query):
        params = {
            'access_key': self.aviation_api_key,
            'search': query
        }
        response = requests.get(f'{self.aviation_base_url}airports', params=params)
        if response.ok:
            return response.json().get('data', [])
        return []

    def get_nearby_airports(self, lat, lon, radius = 100):
        try:
            token = self._get_amadeus_token()
            headers = {"Authorization": f"Bearer {token}"}
            url = f"https://test.api.amadeus.com/v1/reference-data/locations/airports"
            params = {
                "latitude": lat,
                "longitude": lon,
                "radius": radius
            }
            response = requests.get(url, headers=headers, params=params)
            if response.ok:
                return response.json().get("data", [])
            else:
                print(f"Amadeus API Error: {response.status_code} - {response.text}")
            return []
        except Exception as e:
            print(f"Error in get_nearby_airports: {str(e)}")
            return []