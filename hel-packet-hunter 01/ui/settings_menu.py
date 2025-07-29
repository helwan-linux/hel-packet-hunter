from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSlider
from PyQt6.QtCore import pyqtSignal, Qt

class SettingsMenu(QWidget):
    back_to_main_menu_signal = pyqtSignal()
    # Add other signals for settings changes here later (e.g., volume_changed_signal)

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("Settings")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #66BB6A;") # Styling
        layout.addWidget(title_label)

        layout.addSpacing(30)

        # Example setting: Volume control (just a placeholder slider for now)
        volume_label = QLabel("Volume:")
        volume_label.setStyleSheet("font-size: 18px;")
        volume_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(volume_label)

        volume_slider = QSlider(Qt.Orientation.Horizontal)
        volume_slider.setRange(0, 100)
        volume_slider.setValue(75) # Default volume
        volume_slider.setFixedSize(300, 30)
        # volume_slider.valueChanged.connect(self.volume_changed_signal.emit) # Connect to a signal later
        layout.addWidget(volume_slider, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacing(50)

        back_button = QPushButton("Back to Main Menu")
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(self.back_to_main_menu_signal.emit)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
