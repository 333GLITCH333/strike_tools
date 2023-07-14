import requests
from requests.structures import CaseInsensitiveDict


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

    def fetch_geocode(self, address):
        url = "https://api.geoapify.com/v1/geocode/search"
        headers = CaseInsensitiveDict({"Accept": "application/json"})
        params = {
            "text": address,
            "apiKey": "cffbc02463704e22ba33c259df8bcf75"
        }
        return self.fetch_data(url, headers, params)

    def fetch_ntas_alerts(self):
        url = "https://api.example.com/ntas/alerts"
        return self.fetch_data(url)

    def get_current_weather(self, address):
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": "2e82b4c18182476895132928231106",
            "q": address
        }
        return self.fetch_data(url, params=params)

    def get_astronomy_data(self, address):
        url = "http://api.weatherapi.com/v1/astronomy.json"
        params = {
            "key": "2e82b4c18182476895132928231106",
            "q": address,
            "dt": "Current"
        }
        return self.fetch_data(url, params=params)

    def get_tidal_data(self, address):
        url = "https://api.example.com/tidal"
        params = {
            "address": address
        }
        return self.fetch_data(url, params=params)
