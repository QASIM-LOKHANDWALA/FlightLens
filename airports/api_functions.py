import os
from dotenv import load_dotenv
import requests
import random

class AirportAPI:
  def __init__(self):
    load_dotenv()
    self.airport_api_key = os.getenv('AVIATIONSTACK_API_KEY')
    self.base_url = 'https://api.aviationstack.com/v1/'
    
  def get_airports(self):
    url = f'{self.base_url}airports'
    params = {
      'access_key': self.airport_api_key
    }
    response = requests.get(url, params=params)
    if response.ok:
      data = response.json()['data']
      shuffle_data = random.shuffle(data)
      return data[:10]
    else:
      print('Error:', response.status_code)
      return []