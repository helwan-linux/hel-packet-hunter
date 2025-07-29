import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
# import pygame.mixer # Comment out this line

if __name__ == "__main__":
    # Initialize pygame mixer
    # pygame.mixer.init() # Comment out this line

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
