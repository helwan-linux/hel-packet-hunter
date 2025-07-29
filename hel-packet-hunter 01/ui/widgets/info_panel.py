from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor

class InfoPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(250) # Set a fixed width for the info panel
        self.setStyleSheet("background-color: #333333; border: 1px solid #555555; padding: 10px;") # Basic styling

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.title_label = QLabel("Packet Info")
        self.title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #66BB6A;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.layout.addSpacing(10)

        self.name_label = QLabel("Name: N/A")
        self.name_label.setFont(QFont("Arial", 12))
        self.name_label.setStyleSheet("color: #FFFFFF;")
        self.layout.addWidget(self.name_label)

        self.type_label = QLabel("Type: N/A")
        self.type_label.setFont(QFont("Arial", 12))
        self.type_label.setStyleSheet("color: #FFFFFF;")
        self.layout.addWidget(self.type_label)
        
        self.description_label = QLabel("Description: N/A")
        self.description_label.setFont(QFont("Arial", 11))
        self.description_label.setStyleSheet("color: #CCCCCC;")
        self.description_label.setWordWrap(True) # Allow text to wrap
        self.layout.addWidget(self.description_label)
        
        self.layout.addStretch(1) # Pushes content to the top

    def update_info(self, packet=None):
        if packet:
            self.title_label.setText("Intercepted Packet")
            self.name_label.setText(f"Name: {packet.name}")
            self.type_label.setText(f"Type: {'Threat' if packet.is_threat else 'Safe'}")
            self.description_label.setText(f"Description: {packet.description}")
            if packet.is_threat:
                self.title_label.setStyleSheet("color: #FF6666;") # Red for threat
            else:
                self.title_label.setStyleSheet("color: #66BB6A;") # Green for safe
        else:
            self.title_label.setText("Packet Info")
            self.name_label.setText("Name: N/A")
            self.type_label.setText("Type: N/A")
            self.description_label.setText("Description: N/A")
            self.title_label.setStyleSheet("color: #66BB6A;") # Default color
