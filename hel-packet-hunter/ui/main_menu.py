# ui/main_menu.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

class MainMenu(QWidget):
    start_game_signal = pyqtSignal()
    settings_signal = pyqtSignal()
    about_signal = pyqtSignal()
    help_signal = pyqtSignal()
    exit_game_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(15) # Add some spacing between buttons

        title_label = QLabel("Packet Hunter")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("title_label") # For CSS styling
        main_layout.addWidget(title_label)

        # Buttons
        start_button = QPushButton("Start Game")
        start_button.clicked.connect(self.start_game_signal.emit)
        start_button.setObjectName("start_button") # Special ID for CSS
        start_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        settings_button = QPushButton("Settings")
        settings_button.clicked.connect(self.settings_signal.emit)
        settings_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(settings_button, alignment=Qt.AlignmentFlag.AlignCenter)

        about_button = QPushButton("About")
        about_button.clicked.connect(self.about_signal.emit)
        about_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(about_button, alignment=Qt.AlignmentFlag.AlignCenter)

        help_button = QPushButton("Help")
        help_button.clicked.connect(self.help_signal.emit)
        help_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(help_button, alignment=Qt.AlignmentFlag.AlignCenter)

        exit_button = QPushButton("Exit Game")
        exit_button.clicked.connect(self.exit_game_signal.emit)
        exit_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter)
