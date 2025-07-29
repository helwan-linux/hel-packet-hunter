from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal, Qt

class MainMenu(QWidget):
    start_game_signal = pyqtSignal()
    settings_signal = pyqtSignal()
    about_signal = pyqtSignal() # New signal
    help_signal = pyqtSignal()   # New signal
    exit_game_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("Packet Hunter")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 48px; font-weight: bold; color: #4CAF50;")
        layout.addWidget(title_label)

        layout.addSpacing(50)

        start_button = QPushButton("Start Game")
        start_button.setFixedSize(200, 50)
        start_button.clicked.connect(self.start_game_signal.emit)
        layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        settings_button = QPushButton("Settings")
        settings_button.setFixedSize(200, 50)
        settings_button.clicked.connect(self.settings_signal.emit)
        layout.addWidget(settings_button, alignment=Qt.AlignmentFlag.AlignCenter)

        about_button = QPushButton("About") # New button
        about_button.setFixedSize(200, 50)
        about_button.clicked.connect(self.about_signal.emit)
        layout.addWidget(about_button, alignment=Qt.AlignmentFlag.AlignCenter)

        help_button = QPushButton("Help") # New button
        help_button.setFixedSize(200, 50)
        help_button.clicked.connect(self.help_signal.emit)
        layout.addWidget(help_button, alignment=Qt.AlignmentFlag.AlignCenter)

        exit_button = QPushButton("Exit")
        exit_button.setFixedSize(200, 50)
        exit_button.clicked.connect(self.exit_game_signal.emit)
        layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter)
