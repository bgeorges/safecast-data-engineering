import requests

def fetch_data(api_url):
    response = requests.get(api_url)
    return response.json()
