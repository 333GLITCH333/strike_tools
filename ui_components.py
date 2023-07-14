#ui_components.py
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QLineEdit, QInputDialog

class AddressInput(QLineEdit):
    def __init__(self):
        super().__init__()

class GeocodeButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("geocode.jpg"))
        self.setIconSize(QSize(150, 150))
        self.setStyleSheet("padding: 0px; margin-bottom: 10px;")

class MapsButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("maps.jpg"))
        self.setIconSize(QSize(150, 150))
        self.setStyleSheet("padding: 0px; margin-bottom: 10px;")

class DealsButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("deals.jpg"))
        self.setIconSize(QSize(150, 150))
        self.setStyleSheet("padding: 0px; margin-bottom: 10px;")

class NTASAlertsButton(QPushButton):
    def __init__(self):
        super().__init__()

class CurrentWeatherButton(QPushButton):
    def __init__(self):
        super().__init__()

class AstroDataButton(QPushButton):
    def __init__(self):
        super().__init__()

class TidalDataButton(QPushButton):
    def __init__(self):
        super().__init__()

class CloseAppButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("CLOSE APP")
        self.setStyleSheet(
            "background-color: red; color: white; font-weight: bold; font-size: 50px;padding: 45px;"
        )

class LogoLabel(QLabel):
    def __init__(self):
        super().__init__()

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

class WeatherOutput(QLabel):
    def __init__(self):
        super().__init__()

class AstroDataOutput(QLabel):
    def __init__(self):
        super().__init__()

class TidalDataOutput(QLabel):
    def __init__(self):
        super().__init__()
