#api_fetch.py
import requests
from requests.structures import CaseInsensitiveDict

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
            "apiKey": "cffbc02463704e22ba33c259df8bcf75"
        }
        try:
            resp = requests.get(url, headers=headers, params=params)
            if resp.status_code == 200:
                return resp.json()
            else:
                return None
        except requests.RequestException:
            return None

    @staticmethod
    def fetch_ntas_alerts():
        url = "https://api.example.com/ntas/alerts"
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                return resp.json()
            else:
                return None
        except requests.RequestException:
            return None

    @staticmethod
    def get_current_weather(address):
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": "2e82b4c18182476895132928231106",
            "q": address,
            "aqi": "yes"
        }
        try:
            resp = requests.get(url, params=params)
            if resp.status_code == 200:
                return resp.json()
            else:
                return None
        except requests.RequestException:
            return None

    @staticmethod
    def get_astronomy_data(address):
        url = "http://api.weatherapi.com/v1/astronomy.json"
        params = {
            "key": "2e82b4c18182476895132928231106",
            "q": address,
            "dt": "Current"
        }
        try:
            resp = requests.get(url, params=params)
            if resp.status_code == 200:
                return resp.json()
            else:
                return None
        except requests.RequestException:
            return None

    @staticmethod
    def get_tidal_data(address):
        url = "https://api.example.com/tidal"
        params = {
            "address": address
        }
        try:
            resp = requests.get(url, params=params)
            if resp.status_code == 200:
                return resp.json()
            else:
                return None
        except requests.RequestException:
            return None
            
