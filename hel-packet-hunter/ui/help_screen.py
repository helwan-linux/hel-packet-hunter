# ui/help_screen.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

class HelpScreen(QWidget):
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(20) # Add some spacing

        title_label = QLabel("How to Play")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("title_label") # For CSS styling
        main_layout.addWidget(title_label)

        help_text = QLabel(
            "Use the Arrow Keys (Left, Right, Up, Down) to move your Sniffer.\n\n"
            "Press Spacebar or Enter to intercept a packet.\n\n"
            "Intercept 'Safe' packets for points, but focus on intercepting 'Threat' packets to prevent damage.\n\n"
            "Avoid missing 'Threat' packets! Missing too many will result in Game Over.\n\n"
            "Good luck, Packet Hunter!"
        )
        help_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        help_text.setWordWrap(True)
        help_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        main_layout.addWidget(help_text)

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.back_to_main_menu_signal.emit)
        back_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
