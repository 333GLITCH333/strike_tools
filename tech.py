# tech.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class TechPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tech Panel")
        self.setGeometry(200, 200, 400, 300)

        # Create and customize UI elements for the Tech Panel
        label = QLabel("Tech Panel")
        label.setAlignment(Qt.AlignCenter)

        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.jpg")  # Replace "logo.jpg" with the path to your logo image
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        close_app_button = QPushButton("CLOSE APP")
        close_app_button.setStyleSheet(
            "background-color: red; color: white; font-weight: bold; font-size: 20px; padding: 10px;"
        )
        close_app_button.clicked.connect(self.close)

        # Add the UI elements to the layout of the Tech Panel
        tech_layout = QVBoxLayout()
        tech_layout.addWidget(label)
        tech_layout.addWidget(logo_label)
        tech_layout.addWidget(close_app_button)

        self.setLayout(tech_layout)  # Set the layout for the Tech Panel

# END TECH.PY
