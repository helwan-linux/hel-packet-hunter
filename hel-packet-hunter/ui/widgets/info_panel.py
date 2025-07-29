# ui/widgets/info_panel.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from config import INFO_PANEL_WIDTH, TOTAL_HEIGHT, COLOR_TEXT_NORMAL, COLOR_TEXT_HIGHLIGHT, COLOR_SAFE_PACKET, COLOR_THREAT_PACKET

class InfoPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(INFO_PANEL_WIDTH)
        self.setFixedHeight(TOTAL_HEIGHT) # Set height to match main window
        self.setObjectName("info_panel") # For CSS styling

        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(10)

        title_label = QLabel("Packet Info")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        self.packet_name_label = QLabel("N/A")
        self.packet_name_label.setObjectName("packet_name_label") # For CSS styling
        self.packet_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.packet_name_label)

        self.packet_desc_label = QLabel("Waiting for packet...")
        self.packet_desc_label.setObjectName("packet_desc_label") # For CSS styling
        self.packet_desc_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.packet_desc_label.setWordWrap(True)
        layout.addWidget(self.packet_desc_label)

        layout.addStretch(1) # Pushes content to the top

    def update_info(self, packet_info):
        if packet_info:
            packet_type = packet_info.get('type', 'unknown')
            score_change = packet_info.get('score_change', 0)

            # Update packet name and description
            self.packet_name_label.setText(f"Type: {packet_info['name']}")
            self.packet_desc_label.setText(f"Description: {packet_info['description']}")

            # Apply color based on packet type
            if packet_type == 'threat':
                self.packet_name_label.setStyleSheet(f"color: rgb{COLOR_THREAT_PACKET};")
                self.packet_desc_label.setStyleSheet(f"color: rgb{COLOR_THREAT_PACKET};")
            elif packet_type == 'safe':
                self.packet_name_label.setStyleSheet(f"color: rgb{COLOR_SAFE_PACKET};")
                self.packet_desc_label.setStyleSheet(f"color: rgb{COLOR_SAFE_PACKET};")
            else:
                self.packet_name_label.setStyleSheet(f"color: rgb{COLOR_TEXT_NORMAL};")
                self.packet_desc_label.setStyleSheet(f"color: rgb{COLOR_TEXT_NORMAL};")
        else:
            # Reset to default when no packet is intercepted
            self.packet_name_label.setText("N/A")
            self.packet_desc_label.setText("Waiting for packet...")
            self.packet_name_label.setStyleSheet(f"color: rgb{COLOR_TEXT_NORMAL};")
            self.packet_desc_label.setStyleSheet(f"color: rgb{COLOR_TEXT_NORMAL};")
