import os
from dotenv import load_dotenv
import requests

class FlightAPI:
  def __init__(self):
    load_dotenv()
    self.bearer_token = self.get_token()
    self.base_url = 'https://test.api.amadeus.com/v1'
    
  def get_token(self):
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    data = {
      'grant_type': 'client_credentials',
      'client_id': os.getenv('CLIENT_ID'),
      'client_secret': os.getenv('CLIENT_SECRET')
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
      return response.json()['access_token']
    else:
      return None
  
  def search_by_city_code(self, city_code, date):
    url = f'{self.base_url}/shopping/flight-destinations'
    headers = {
      'Authorization': f'Bearer {self.bearer_token}'
    }
    params = {
      'origin': city_code,
      'departureDate': date,
    }
    response = requests.get(url, headers=headers,params=params)
    if response.status_code == 401:
      self.bearer_token = self.get_token()
      headers['Authorization'] = f'Bearer {self.bearer_token}'
      response = requests.get(url, headers=headers,params=params)
    return response.json()
    