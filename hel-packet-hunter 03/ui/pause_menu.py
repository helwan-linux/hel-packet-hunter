from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

class PauseMenu(QWidget):
    resume_game_signal = pyqtSignal()
    restart_game_signal = pyqtSignal()
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgba(0, 0, 0, 180);") # Semi-transparent dark background
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("PAUSED")
        title_label.setFont(QFont("Arial", 48, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #FFFFFF;") # White color
        layout.addWidget(title_label)

        layout.addSpacing(40)

        resume_button = QPushButton("Resume Game")
        resume_button.setFixedSize(200, 50)
        resume_button.clicked.connect(self.resume_game_signal.emit)
        layout.addWidget(resume_button, alignment=Qt.AlignmentFlag.AlignCenter)

        restart_button = QPushButton("Restart Level")
        restart_button.setFixedSize(200, 50)
        restart_button.clicked.connect(self.restart_game_signal.emit)
        layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_menu_button = QPushButton("Main Menu")
        main_menu_button.setFixedSize(200, 50)
        main_menu_button.clicked.connect(self.back_to_main_menu_signal.emit)
        layout.addWidget(main_menu_button, alignment=Qt.AlignmentFlag.AlignCenter)
