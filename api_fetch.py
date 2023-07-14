#api_fetch.py
import requests

class APIFetcher:
    @staticmethod
    def fetch_image(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return None

    @staticmethod
    def fetch_geocode(address):
        url = "https://api.geoapify.com/v1/geocode/search"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        params = {
            "text": address,
            "apiKey": "YOUR_GEOAPIFY_API_KEY"
        }
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None

    @staticmethod
    def fetch_ntas_alerts():
        url = "https://api.example.com/ntas/alerts"
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None

    @staticmethod
    def get_current_weather(address):
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": "YOUR_WEATHERAPI_API_KEY",
            "q": address,
            "aqi": "yes"
        }
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None

    @staticmethod
    def get_astronomy_data(address):
        url = "http://api.weatherapi.com/v1/astronomy.json"
        params = {
            "key": "YOUR_WEATHERAPI_API_KEY",
            "q": address,
            "dt": "Current"
        }
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None

    @staticmethod
    def get_tidal_data(address):
        url = "https://api.example.com/tidal"
        params = {
            "address": address
        }
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None
