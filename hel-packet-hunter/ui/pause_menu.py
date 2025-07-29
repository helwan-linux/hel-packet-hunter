# ui/pause_menu.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

class PauseMenu(QWidget):
    resume_game_signal = pyqtSignal()
    restart_game_signal = pyqtSignal()
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(20) # Add some spacing

        title_label = QLabel("Game Paused")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("title_label") # For CSS styling
        main_layout.addWidget(title_label)

        resume_button = QPushButton("Resume Game")
        resume_button.clicked.connect(self.resume_game_signal.emit)
        resume_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(resume_button, alignment=Qt.AlignmentFlag.AlignCenter)

        restart_button = QPushButton("Restart Game")
        restart_button.clicked.connect(self.restart_game_signal.emit)
        restart_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_menu_button = QPushButton("Main Menu")
        main_menu_button.clicked.connect(self.back_to_main_menu_signal.emit)
        main_menu_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(main_menu_button, alignment=Qt.AlignmentFlag.AlignCenter)
