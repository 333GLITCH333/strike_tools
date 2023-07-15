#ui_componentd.py
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


class NTASAlertsButton(QPushButton):
    pass


class OutputLabel(QLabel):
    pass


class CloseAppButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("CLOSE APP")
        self.setStyleSheet(
            "background-color: red; color: white; font-weight: bold; font-size: 50px;padding: 45px;"
        )


class LogoLabel(QLabel):
    pass


class ImageLabel(QLabel):
    pass
    
