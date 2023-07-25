#ui_elements.py
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit

class AddressInput(QLineEdit):
    pass

class ImageButton(QPushButton):
    def __init__(self, icon_path):
        super().__init__()
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(150, 150))
        self.setStyleSheet("padding: 0px; margin-bottom: 10px;")

    def setButtonStyle(self, style):
        self.setStyleSheet(style)

class NTASAlertsButton(QPushButton):
    def setButtonStyle(self, style):
        self.setStyleSheet(style)

class OutputLabel(QLabel):
    pass

class CloseAppButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("CLOSE APP")
        self.setStyleSheet(
            "background-color: red; color: white; font-weight: bold; font-size: 50px;padding: 45px;"
        )

    def setButtonStyle(self, style):
        self.setStyleSheet(style)

class LogoLabel(QLabel):
    def setLabelStyle(self, style):
        self.setStyleSheet(style)

class ImageLabel(QLabel):
    def setLabelStyle(self, style):
        self.setStyleSheet(style)

# END UI_ELEMENTS.PY
