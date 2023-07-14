#strike_tools.py
from PyQt5.QtMultimedia import QSoundEffect
import os
import requests
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QMessageBox, QApplication, QWidget, QInputDialog, QLabel

from ui_components import LogoLabel, ImageLabel, CloseAppButton, NTASAlertsButton, ImageButton, AddressInput
from api_fetch import APIFetcher


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.startup_sound = QSoundEffect()
        self.startup_sound.setSource(QUrl.fromLocalFile(os.path.abspath("startup_sound.wav")))

        self.button_sound = QSoundEffect()
        self.button_sound.setSource(QUrl.fromLocalFile("0x15.wav"))

        self.close_button_sound = QSoundEffect()
        self.close_button_sound.setSource(QUrl.fromLocalFile("0x66.wav"))

        self.startup_sound.play()

        self.close_app_sound = QSoundEffect()

        self.address_input = AddressInput()

        self.setWindowTitle("Strike Tools")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()
        self.logo_label = LogoLabel()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(script_dir, "logo.jpg")
        self.logo_label.setPixmap(QPixmap(logo_path))
        layout.addWidget(self.logo_label, alignment=Qt.AlignTop)
        self.image_label = ImageLabel()
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        image_url = "https://tripcheck.com/RoadCams/cams/Yaquina%20Bay%20Bridge%20N_pid2778.JPG"
        image_data = APIFetcher().fetch_image(image_url)
        if image_data:
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            scaled_pixmap = pixmap.scaledToWidth(1000)
            self.image_label.setPixmap(scaled_pixmap)

        button_layout = QHBoxLayout()
        self.geocode_button = ImageButton("geocode.jpg")
        self.geocode_button.clicked.connect(self.handle_geocode_button_click)
        geocode_label = QLabel("Geocode")
        button_layout.addWidget(geocode_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.geocode_button, alignment=Qt.AlignCenter)
        self.geocode_button.setFont(QFont("", -1, QFont.Bold))

        self.maps_button = ImageButton("maps.jpg")
        self.maps_button.clicked.connect(self.handle_maps_button_click)
        maps_label = QLabel("Maps")
        button_layout.addWidget(maps_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.maps_button, alignment=Qt.AlignCenter)
        self.maps_button.setFont(QFont("", -1, QFont.Bold))

        self.deals_button = ImageButton("deals.jpg")
        self.deals_button.clicked.connect(self.handle_deals_button_click)
        deals_label = QLabel("Deals")
        button_layout.addWidget(deals_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.deals_button, alignment=Qt.AlignCenter)
        self.deals_button.setFont(QFont("", -1, QFont.Bold))

        layout.addLayout(button_layout)
        self.ntas_alerts_button = NTASAlertsButton()
        self.ntas_alerts_button.setText("NTAS Alerts")
        self.ntas_alerts_button.clicked.connect(self.handle_ntas_alerts_button_click)
        self.ntas_alerts_button.setFont(QFont("", -1, QFont.Bold))
        layout.addWidget(self.ntas_alerts_button)

        self.current_weather_button = QPushButton("Local Weather")
        self.current_weather_button.clicked.connect(self.handle_current_weather_button_click)
        self.current_weather_button.setFont(QFont("", -1, QFont.Bold))
        layout.addWidget(self.current_weather_button)

        self.astro_data_button = QPushButton("Local Astro Data")
        self.astro_data_button.clicked.connect(self.handle_astro_data_button_click)
        self.astro_data_button.setFont(QFont("", -1, QFont.Bold))
        layout.addWidget(self.astro_data_button)

        self.tidal_data_button = QPushButton("Local Tidal Data")
        self.tidal_data_button.clicked.connect(self.handle_tidal_data_button_click)
        self.tidal_data_button.setFont(QFont("", -1, QFont.Bold))
        layout.addWidget(self.tidal_data_button)

        self.close_app_button = CloseAppButton()
        self.close_app_button.clicked.connect(self.close_app)
        self.close_app_button.setFont(QFont("", -1, QFont.Bold))
        layout.addWidget(self.close_app_button, alignment=Qt.AlignBottom)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def handle_geocode_button_click(self):
        address, ok = QInputDialog.getText(self, "Enter Address", "Address:", QLineEdit.Normal, "")

        if ok:
            if not address:
                QMessageBox.warning(self, "Error", "Please enter an address.")
                return

            geocode_data = APIFetcher().fetch_geocode(address)
            if geocode_data and "results" in geocode_data and len(geocode_data["results"]) > 0:
                lon = geocode_data["results"][0]["lon"]
                lat = geocode_data["results"][0]["lat"]
                self.lat_lon_output.setPlainText(f"Longitude: {lon}\nLatitude: {lat}")
            else:
                QMessageBox.warning(self, "Error", "Geocode API request failed.")

    def handle_maps_button_click(self):
        address = self.address_input.text()

        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        maps_url = f"https://www.google.com/maps/search/?api=1&query={address}"
        webbrowser.open(maps_url)

    def handle_deals_button_click(self):
        address = self.address_input.text()

        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        deals_url = f"https://www.example.com/deals?location={address}"
        webbrowser.open(deals_url)

    def handle_ntas_alerts_button_click(self):
        APIFetcher().fetch_ntas_alerts()

    def handle_current_weather_button_click(self):
        address = self.address_input.text()

        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        weather_data = APIFetcher().get_current_weather(address)
        if weather_data:
            temperature = weather_data['current']['temp_c']
            humidity = weather_data['current']['humidity']
            self.weather_output.setPlainText(f"Temperature: {temperature}°C\nHumidity: {humidity}%")
        else:
            QMessageBox.warning(self, "Error", "Weather API request failed.")

    def handle_astro_data_button_click(self):
        address = self.address_input.text()

        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        astro_data = APIFetcher().get_astronomy_data(address)
        if astro_data:
            sunrise = astro_data['astronomy']['astro']['sunrise']
            sunset = astro_data['astronomy']['astro']['sunset']
            self.astro_data_output.setPlainText(f"Sunrise: {sunrise}\nSunset: {sunset}")
        else:
            QMessageBox.warning(self, "Error", "Astro Data API request failed.")

    def handle_tidal_data_button_click(self):
        address = self.address_input.text()

        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        tidal_data = APIFetcher().get_tidal_data(address)
        if tidal_data:
            tide_height = tidal_data['tide']['height']
            tide_time = tidal_data['tide']['time']
            self.tidal_data_output.setPlainText(f"Tide Height: {tide_height}\nTide Time: {tide_time}")
        else:
            QMessageBox.warning(self, "Error", "Tidal Data API request failed.")

    def close_app(self):
        self.close_app_sound.play()
        confirm = QMessageBox.question(
            self, "Confirmation", "Are you sure you want to close the app?", QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication([])
    weather_app = WeatherApp()
    weather_app.show()
    app.exec_()
