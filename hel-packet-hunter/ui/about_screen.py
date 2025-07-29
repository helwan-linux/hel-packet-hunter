# ui/about_screen.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

class AboutScreen(QWidget):
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(20) # Add some spacing

        title_label = QLabel("About Packet Hunter")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("title_label") # For CSS styling
        main_layout.addWidget(title_label)

        about_text = QLabel(
            "Packet Hunter is a cybersecurity-themed arcade game.\n\n"
            "Your mission is to intercept malicious data packets while letting safe ones pass through.\n\n"
            "Developed by [Your Name/Team Name] as a fun way to learn about network security basics."
        )
        about_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        about_text.setWordWrap(True)
        about_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        main_layout.addWidget(about_text)

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.back_to_main_menu_signal.emit)
        back_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
