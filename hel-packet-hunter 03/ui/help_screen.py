from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

class HelpScreen(QWidget):
    back_to_main_menu_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title_label = QLabel("How to Play: Packet Hunter")
        title_label.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #1E88E5;") # Blueish color for title
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        layout.addSpacing(20)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        
        help_content_widget = QWidget(scroll_area)
        help_content_layout = QVBoxLayout(help_content_widget)
        help_content_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        help_text = QLabel(
            "<h3>Objective:</h3>"
            "Your goal as the **Sniffer Agent** is to analyze network packets and "
            "intercept **malicious threats** while letting **safe packets** pass.\n\n"
            
            "<h3>Controls:</h3>"
            "- Use **Arrow Keys** (↑↓←→) to move your Sniffer Agent around the network grid.\n"
            "- Press **Spacebar** or **Enter** to analyze/intercept a packet that your Sniffer is currently on.\n\n"
            
            "<h3>Packet Types:</h3>"
            "- **Safe Packets (Green):** Standard network traffic (e.g., HTTP, DNS, TCP). Let them pass! "
            "Intercepting a safe packet will result in a **penalty**.\n"
            "- **Threat Packets (Red):** Malicious activity (e.g., DDoS, ARP Spoof, SQL Injection). "
            "You **must intercept** these quickly! Successfully intercepting a threat earns you **points**.\n\n"
            
            "<h3>Scoring:</h3>"
            "- **+10 points:** For each successfully intercepted threat.\n"
            "- **-5 points:** For intercepting a safe packet (False Positive).\n"
            "- **-15 points:** For letting a threat packet pass (Missed Threat).\n\n"
            
            "<h3>Good luck, Sniffer Agent!</h3>"
        )
        help_text.setFont(QFont("Arial", 12))
        # Changed text color to a dark gray for better contrast
        help_text.setStyleSheet("color: #333333; padding: 10px;") 
        help_text.setWordWrap(True)
        help_text.setAlignment(Qt.AlignmentFlag.AlignLeft)

        help_content_layout.addWidget(help_text)
        help_content_widget.setLayout(help_content_layout)
        scroll_area.setWidget(help_content_widget)
        
        layout.addWidget(scroll_area)

        layout.addSpacing(30)

        back_button = QPushButton("Back to Main Menu")
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(self.back_to_main_menu_signal.emit)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
