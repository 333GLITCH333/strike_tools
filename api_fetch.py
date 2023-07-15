#api_fetch.py
import requests

class APIFetcher:
    @staticmethod
    def fetch_image(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.content
        except requests.RequestException as e:
            # Handle or log the exception
            print(f"Failed to fetch image: {e}")
        return None

    @staticmethod
    def fetch_data(url, headers=None, params=None):
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                return response.json()
        except requests.RequestException as e:
            # Handle or log the exception
            print(f"Failed to fetch data: {e}")
        return None

    @staticmethod
    def fetch_geocode(address):
        url = "https://api.geoapify.com/v1/geocode/search"
        params = {
            "text": address,
            "format": "json",
            "apiKey": "YOUR_API_KEY"  # Replace with your actual API key
        }
        return APIFetcher.fetch_data(url, params=params)

    @staticmethod
    def fetch_ntas_alerts():
        url = "https://api.example.com/ntas/alerts"
        return APIFetcher.fetch_data(url)

    @staticmethod
    def get_current_weather(address):
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": "2e82b4c18182476895132928231106",
            "q": address
        }
        return APIFetcher.fetch_data(url, params=params)

    @staticmethod
    def get_astronomy_data(address):
        url = "http://api.weatherapi.com/v1/astronomy.json"
        params = {
            "key": "2e82b4c18182476895132928231106",
            "q": address,
            "dt": "Current"
        }
        return APIFetcher.fetch_data(url, params=params)

    @staticmethod
    def get_tidal_data(address):
        url = "https://api.example.com/tidal"
        params = {
            "address": address
        }
        return APIFetcher.fetch_data(url, params=params)
        
