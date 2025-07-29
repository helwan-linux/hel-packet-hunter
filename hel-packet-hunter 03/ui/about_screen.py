from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

class AboutScreen(QWidget):
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("About Packet Hunter")
        title_label.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #FFC107;") # Yellowish color for title
        layout.addWidget(title_label)

        layout.addSpacing(20)

        info_text = QLabel(
            "Packet Hunter is an educational game designed to introduce players to "
            "network packet analysis and cybersecurity threats in a fun, interactive way.\n\n"
            "Developed with Python and PyQt6.\n\n"
            "Version: 0.1\n\n"
            "Copyright © 2025 Your Name/Organization"
        )
        info_text.setFont(QFont("Arial", 12))
        # Changed text color to a dark gray for better contrast
        info_text.setStyleSheet("color: #333333;") 
        info_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_text.setWordWrap(True)
        layout.addWidget(info_text)

        layout.addSpacing(50)

        back_button = QPushButton("Back to Main Menu")
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(self.back_to_main_menu_signal.emit)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
