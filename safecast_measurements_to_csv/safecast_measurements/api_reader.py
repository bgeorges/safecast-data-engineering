import requests
from config import Config


def fetch_data():
    api_url = Config.get('safecast_api_url')
    response = requests.get(api_url)
    return response.json()
