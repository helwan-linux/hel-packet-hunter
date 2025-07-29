# ui/settings_menu.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

class SettingsMenu(QWidget):
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(20) # Add some spacing

        title_label = QLabel("Settings")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("title_label") # For CSS styling
        main_layout.addWidget(title_label)

        # You can add actual settings widgets here later if needed
        temp_setting_label = QLabel("No settings available yet.")
        temp_setting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(temp_setting_label)

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.back_to_main_menu_signal.emit)
        back_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
