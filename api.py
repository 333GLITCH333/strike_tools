#api.py
import requests
import xml.etree.ElementTree as ET

class APIFetcher:
    @staticmethod
    def fetch_image(url):
        # Fetches an image from the provided URL and returns its content
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return None

    @staticmethod
    def fetch_geocode(address):
        # Fetches geocode data for the provided address using the Geoapify API
        url = f"https://api.geoapify.com/v1/geocode/search?text={address}&apiKey=cffbc02463704e22ba33c259df8bcf75"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        return None

    @staticmethod
    def get_current_weather(address):
        # Retrieves the current weather data for the provided address using the WeatherAPI
        url = f"http://api.weatherapi.com/v1/current.json?key=2e82b4c18182476895132928231106&q=Waldport, OR&aqi=yes"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        return None
    @staticmethod
    def get_astronomy_data(address):
        # Implement your astronomy data API logic here
        # Make the appropriate API request to fetch astronomy data based on the provided address
        pass

    @staticmethod
    def get_tidal_data(address):
        # Implement your tidal data API logic here
        # Make the appropriate API request to fetch tidal data based on the provided address
        pass

    @staticmethod
    def fetch_ntas_alerts():
        # Fetches NTAS alerts from the DHS API
        url = "https://www.dhs.gov/ntas/1.1/feed.xml"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            alerts = APIFetcher.parse_ntas_alerts(data)
            return alerts
        return None

    @staticmethod
    def parse_ntas_alerts(xml_data):
        # Parse the XML data and extract the necessary NTAS alert information
        root = ET.fromstring(xml_data)
        alerts = []
        for alert_elem in root.iter("alert"):
            alert = {}
            alert["start"] = alert_elem.get("start")
            alert["end"] = alert_elem.get("end")
            alert["type"] = alert_elem.get("type")
            alert["href"] = alert_elem.get("href")
            alert["title"] = alert_elem.find("summary/h2").text
            alert["summary"] = alert_elem.find("summary/p").text
            alerts.append(alert)
        return alerts

# END API.PY
