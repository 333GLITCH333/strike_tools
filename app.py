# app.py
import os
import webbrowser
from datetime import datetime
from PyQt5.QtCore import Qt, QUrl, QDateTime, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QApplication,
    QWidget,
    QInputDialog,
    QLabel,
    QPushButton,
    QDialog,
    QDialogButtonBox,
    QTextEdit,
)

from api import APIFetcher
from ui_elements import (
    LogoLabel,
    ImageLabel,
    CloseAppButton,
    NTASAlertsButton,
    ImageButton,
    AddressInput,
)

class ImageButton(QPushButton):
    def __init__(self, icon_path, size):
        super().__init__()
        self.setIcon(QIcon(icon_path))
        self.setIconSize(size)
        
class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Strike Tools")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.logo_label = LogoLabel()
        layout.addWidget(self.logo_label, alignment=Qt.AlignTop)
        self.image_label = ImageLabel()
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        
        layout.addStretch()

        button_font = QFont()
        button_font.setPointSize(18)
        button_font.setBold(True)

        button_layout = QHBoxLayout()
        
        self.ping_button = ImageButton("ping.jpg",QSize(100, 100))
        self.ping_button.clicked.connect(self.handle_ping_button_click)
        ping_label = QLabel("Ping\nMe")
        ping_label.setFont(button_font)
        button_layout.addWidget(ping_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.ping_button, alignment=Qt.AlignCenter)
        self.ping_button.setFont(button_font)
        
        self.geocode_button = ImageButton("geocode.jpg",QSize(100, 100))
        self.geocode_button.clicked.connect(self.handle_geocode_button_click)
        geocode_label = QLabel("Geo\nCode")
        geocode_label.setFont(button_font)
        button_layout.addWidget(geocode_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.geocode_button, alignment=Qt.AlignCenter)
        self.geocode_button.setFont(button_font)

        self.maps_button = ImageButton("maps.jpg",QSize(100, 100))
        self.maps_button.clicked.connect(self.handle_maps_button_click)
        maps_label = QLabel("Maps")
        maps_label.setFont(button_font)
        button_layout.addWidget(maps_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.maps_button, alignment=Qt.AlignCenter)
        self.maps_button.setFont(button_font)

        self.satimg_button = ImageButton("satimg.jpg",QSize(100, 100))
        self.satimg_button.clicked.connect(self.handle_satimg_button_click)
        satimg_label = QLabel("SAT\nIMG")
        satimg_label.setFont(button_font)
        button_layout.addWidget(satimg_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.satimg_button, alignment=Qt.AlignCenter)

        layout.addLayout(button_layout)
        self.ntas_alerts_button = NTASAlertsButton()
        self.ntas_alerts_button.setText("NTAS Alerts")
        self.ntas_alerts_button.clicked.connect(self.handle_ntas_alerts_button_click)
        self.ntas_alerts_button.setFont(button_font)
        layout.addWidget(self.ntas_alerts_button, alignment=Qt.AlignBottom)

        self.current_weather_button = QPushButton("Local Weather")
        self.current_weather_button.clicked.connect(self.handle_current_weather_button_click)
        
        self.current_weather_button.setFont(button_font)
        layout.addWidget(self.current_weather_button, alignment=Qt.AlignBottom)

        self.astro_data_button = QPushButton("Local Astro Data")
        self.astro_data_button.clicked.connect(self.handle_astro_data_button_click)
        self.astro_data_button.setFont(button_font)
        layout.addWidget(self.astro_data_button, alignment=Qt.AlignBottom)
        
        self.tidal_data_button = QPushButton("Local Tidal Data")
        self.tidal_data_button.clicked.connect(self.handle_tidal_data_button_click)
        self.tidal_data_button.setFont(button_font)
        layout.addWidget(self.tidal_data_button, alignment=Qt.AlignBottom)
        
        self.close_app_button = CloseAppButton()
        self.close_app_button.clicked.connect(self.close_app)
        self.close_app_button.setFont(button_font)
        layout.addWidget(self.close_app_button, alignment=Qt.AlignBottom)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.location_label = QLabel()
        self.location_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.location_label.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(self.location_label, alignment=Qt.AlignCenter)

        self.startup_sound = QSoundEffect()
        self.startup_sound.setSource(QUrl.fromLocalFile(os.path.abspath("startup_sound.wav")))

        self.button_sound = QSoundEffect()
        self.button_sound.setSource(QUrl.fromLocalFile("click.wav"))

        self.close_button_sound = QSoundEffect()
        self.close_button_sound.setSource(QUrl.fromLocalFile("close.wav"))

        self.startup_sound.play()

        self.close_app_sound = QSoundEffect()

        script_dir = os.path.dirname(os.path.abspath(__file__))

        logo_path = os.path.join(script_dir, "logo.jpg")
        self.logo_label.setPixmap(QPixmap(logo_path))

        image_url = "https://tripcheck.com/RoadCams/cams/Yaquina%20Bay%20Bridge%20N_pid2778.JPG"
        image_data = APIFetcher.fetch_image(image_url)
        if image_data:
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            scaled_pixmap = pixmap.scaledToWidth(1000)
            self.image_label.setPixmap(scaled_pixmap)
            
    def handle_ping_button_click(self):
        self.button_sound.play()
    
    def handle_geocode_button_click(self):
        self.button_sound.play()
        dialog = QDialog(self)
        dialog.setWindowTitle("Enter Address")

        layout = QVBoxLayout(dialog)

        label = QLabel("ENTER STREET ADDRESS FOR COORDINATES:")
        font = QFont()
        font.setBold(True)
        font.setPointSize(15)
        dialog.setFont(font)
        layout.addWidget(label)

        self.address_input = AddressInput()
        self.address_input.setFixedWidth(1000)
        layout.addWidget(self.address_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        if dialog.exec_() == QDialog.Accepted:
            address = self.address_input.text()
            if not address:
                QMessageBox.warning(self, "Error", "Please enter an address.")
                return

            geocode_data = APIFetcher.fetch_geocode(address)

            if geocode_data and "features" in geocode_data and len(geocode_data["features"]) > 0:
                location = geocode_data["features"][0]
                lon = location["geometry"]["coordinates"][0]
                lat = location["geometry"]["coordinates"][1]
                rounded_lon = round(lon, 6)  # Round longitude to 6 decimal places
                geocode_result = f"GEOCODED Longitude: {rounded_lon}\nGEOCODED Latitude: {lat}"

                clipboard = QApplication.clipboard()
                clipboard.setText(f"{rounded_lon}, {lat}")

                timestamp = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
                geocode_result += f"\nAddress: {address}\nTimestamp: {timestamp}"

                QMessageBox.information(self, "Geocode Result", geocode_result)
            else:
                QMessageBox.warning(self, "Error", "Geocode API request failed.")

    def handle_maps_button_click(self):
        self.button_sound.play()
        dialog = QInputDialog(self)
        dialog.setFixedWidth(1000)
        dialog.setWindowTitle("Enter Coordinates")
        font = QFont()
        font.setBold(True)
        font.setPointSize(15)
        dialog.setFont(font)
        dialog.setLabelText("ENTER LAT/LON (COMMA-SEPARATED):")
        dialog.setTextValue("LAT, LON")
        dialog.setOkButtonText("SHOW MAP")
        dialog.setCancelButtonText("CANCEL")
        dialog.setWindowModality(Qt.ApplicationModal)

        if dialog.exec_() == QInputDialog.Accepted:
            coordinates = dialog.textValue().split(",")
            if len(coordinates) != 2:
                QMessageBox.warning(self, "Error", "Invalid coordinates. Please enter latitude and longitude.")
                return

            lat, lon = coordinates[0].strip(), coordinates[1].strip()

            if not lat or not lon:
                QMessageBox.warning(self, "Error", "Invalid coordinates. Please enter latitude and longitude.")
                return

            map_url = f"https://maps.geoapify.com/v1/staticmap?style=osm-liberty&width=300&height=600&center=lonlat:{lat},{lon}&zoom=15.5&scaleFactor=2&pitch=20&marker=lonlat:{lat},{lon};color:%23ff0000;size:small;text:X&apiKey=8a2f8596c1d14ecc8dba0ddb787acdf4"
            webbrowser.open(map_url)

    def handle_satimg_button_click(self):
        self.button_sound.play()

    def handle_ntas_alerts_button_click(self):
        self.button_sound.play()
        APIFetcher.fetch_ntas_alerts()

    def handle_current_weather_button_click(self):
        self.button_sound.play()
        address = self.address_input.text()

        # Validate if address is provided
        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        weather_data = APIFetcher.get_current_weather(address)
        if weather_data:
            temperature = weather_data['current']['temp_c']
            humidity = weather_data['current']['humidity']
            QMessageBox.information(
                self,
                "Weather Information",
                f"Temperature: {temperature}°C\nHumidity: {humidity}%",
            )
        else:
            QMessageBox.warning(self, "Error", "Weather API request failed.")

    def handle_astro_data_button_click(self):
        self.button_sound.play()
        address = self.address_input.text()

        # Validate if address is provided
        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        astro_data = APIFetcher.get_astronomy_data(address)
        if astro_data:
            sunrise = astro_data['astronomy']['astro']['sunrise']
            sunset = astro_data['astronomy']['astro']['sunset']
            QMessageBox.information(
                self,
                "Astronomy Data",
                f"Sunrise: {sunrise}\nSunset: {sunset}",
            )
        else:
            QMessageBox.warning(self, "Error", "Astro Data API request failed.")

    def handle_tidal_data_button_click(self):
        self.button_sound.play()
        address = self.address_input.text()

        # Validate if address is provided
        if not address:
            QMessageBox.warning(self, "Error", "Please enter an address.")
            return

        tidal_data = APIFetcher.get_tidal_data(address)
        if tidal_data:
            tide_height = tidal_data['tide']['height']
            tide_time = tidal_data['tide']['time']
            QMessageBox.information(
                self,
                "Tidal Data",
                f"Tide Height: {tide_height}\nTide Time: {tide_time}",
            )
        else:
            QMessageBox.warning(self, "Error", "Tidal Data API request failed.")

    def close_app(self):
        self.close_button_sound.play()
        confirm = QMessageBox.question(
            self, "Confirmation", "Are you sure you want to close the app?", QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication([])
    weather_app = WeatherApp()
    weather_app.show()
    app.exec()

# END APP.PY