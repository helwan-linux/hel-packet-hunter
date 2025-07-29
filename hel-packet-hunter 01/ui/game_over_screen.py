from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

class GameOverScreen(QWidget):
    restart_game_signal = pyqtSignal()
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()
    
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("GAME OVER!")
        title_label.setFont(QFont("Arial", 48, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #FF0000;") # Red color for game over
        layout.addWidget(title_label)

        layout.addSpacing(30)

        self.final_score_label = QLabel("Final Score: 0")
        self.final_score_label.setFont(QFont("Arial", 28))
        self.final_score_label.setStyleSheet("color: #FFFFFF;")
        layout.addWidget(self.final_score_label)

        self.level_reached_label = QLabel("Level Reached: 1")
        self.level_reached_label.setFont(QFont("Arial", 22))
        self.level_reached_label.setStyleSheet("color: #CCCCCC;")
        layout.addWidget(self.level_reached_label)

        self.missed_threats_label = QLabel("Missed Threats: 0")
        self.missed_threats_label.setFont(QFont("Arial", 22))
        self.missed_threats_label.setStyleSheet("color: #CCCCCC;")
        layout.addWidget(self.missed_threats_label)

        layout.addSpacing(50)

        restart_button = QPushButton("Play Again")
        restart_button.setFixedSize(200, 50)
        restart_button.clicked.connect(self.restart_game_signal.emit)
        layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)

        back_button = QPushButton("Main Menu")
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(self.back_to_main_menu_signal.emit)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def set_final_stats(self, score, level, missed_threats):
        self.final_score_label.setText(f"Final Score: {score}")
        self.level_reached_label.setText(f"Level Reached: {level}")
        self.missed_threats_label.setText(f"Missed Threats: {missed_threats}")
