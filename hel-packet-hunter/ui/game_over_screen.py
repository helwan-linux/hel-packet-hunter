# ui/game_over_screen.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

class GameOverScreen(QWidget):
    restart_game_signal = pyqtSignal()
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(20) # Add some spacing

        self.title_label = QLabel("GAME OVER!")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label") # For CSS styling
        main_layout.addWidget(self.title_label)

        self.score_label = QLabel("Final Score: 0")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.score_label)

        self.level_label = QLabel("Level Reached: 1")
        self.level_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.level_label)

        self.missed_threats_label = QLabel("Missed Threats: 0")
        self.missed_threats_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.missed_threats_label)

        restart_button = QPushButton("Restart Game")
        restart_button.clicked.connect(self.restart_game_signal.emit)
        restart_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_menu_button = QPushButton("Main Menu")
        main_menu_button.clicked.connect(self.back_to_main_menu_signal.emit)
        main_menu_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(main_menu_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def set_final_stats(self, score, level, missed_threats):
        self.score_label.setText(f"Final Score: {score}")
        self.level_label.setText(f"Level Reached: {level}")
        self.missed_threats_label.setText(f"Missed Threats: {missed_threats}")
