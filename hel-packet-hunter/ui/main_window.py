# ui/main_window.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
import pygame.mixer # تأكد من أن هذا السطر غير معلق لإعادة تفعيل Pygame mixer

from ui.main_menu import MainMenu
from ui.game_screen import GameScreen
from ui.settings_menu import SettingsMenu
from ui.about_screen import AboutScreen
from ui.help_screen import HelpScreen
from ui.game_over_screen import GameOverScreen
from ui.pause_menu import PauseMenu
from config import TOTAL_WIDTH, TOTAL_HEIGHT

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packet Hunter")
        self.resize(TOTAL_WIDTH, TOTAL_HEIGHT)
        self.setMinimumSize(QSize(TOTAL_WIDTH, TOTAL_HEIGHT))

        try:
            pygame.mixer.init()
            print("Pygame mixer initialized successfully.")
        except Exception as e:
            print(f"Error initializing Pygame mixer: {e}")

        try:
            with open("style.qss", "r") as f:
                _style = f.read()
                self.setStyleSheet(_style)
            print("Stylesheet loaded successfully.")
        except FileNotFoundError:
            print("Error: style.qss not found! UI might not be styled correctly.")
        except Exception as e:
            print(f"Error loading stylesheet: {e}")

        self.setWindowIcon(QIcon("assets/icons/game_icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.stacked_layout = QStackedLayout(self.central_widget)

        self._setup_ui()
        self._connect_signals()
        self._load_music() # تأكد أن هذا السطر غير معلق
        self._play_background_music() # تأكد أن هذا السطر غير معلق

    def _setup_ui(self):
        self.main_menu = MainMenu()
        self.game_screen = GameScreen()
        self.settings_menu = SettingsMenu()
        self.about_screen = AboutScreen()
        self.help_screen = HelpScreen()
        self.game_over_screen = GameOverScreen()
        self.pause_menu = PauseMenu()

        self.stacked_layout.addWidget(self.main_menu)
        self.stacked_layout.addWidget(self.game_screen)
        self.stacked_layout.addWidget(self.settings_menu)
        self.stacked_layout.addWidget(self.about_screen)
        self.stacked_layout.addWidget(self.help_screen)
        self.stacked_layout.addWidget(self.game_over_screen)
        self.stacked_layout.addWidget(self.pause_menu)

        self.stacked_layout.setCurrentWidget(self.main_menu)

    def _connect_signals(self):
        self.main_menu.start_game_signal.connect(self._show_game_screen)
        self.main_menu.settings_signal.connect(self._show_settings_screen)
        self.main_menu.about_signal.connect(self._show_about_screen)
        self.main_menu.help_signal.connect(self._show_help_screen)
        self.main_menu.exit_game_signal.connect(self.close)

        self.settings_menu.back_to_main_menu_signal.connect(self._show_main_menu)
        self.about_screen.back_to_main_menu_signal.connect(self._show_main_menu)
        self.help_screen.back_to_main_menu_signal.connect(self._show_main_menu)

        self.game_screen.game_over_signal.connect(self._show_game_over_screen)
        self.game_screen.pause_game_signal.connect(self._show_pause_menu)

        self.game_over_screen.restart_game_signal.connect(self._show_game_screen_and_restart)
        self.game_over_screen.back_to_main_menu_signal.connect(self._show_main_menu)

        self.pause_menu.resume_game_signal.connect(self._resume_game)
        self.pause_menu.restart_game_signal.connect(self._restart_game_from_pause)
        self.pause_menu.back_to_main_menu_signal.connect(self._show_main_menu)

    def _load_music(self):
        try:
            pygame.mixer.music.load("assets/sounds/background_music.mp3")
            print("Background music loaded.")
        except pygame.error as e:
            print(f"Could not load background music: {e}")

    def _play_background_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        try:
            pygame.mixer.music.play(-1)
            print("Background music playing.")
        except pygame.error as e:
            print(f"Could not play background music: {e}")

    def _stop_background_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            print("Background music stopped.")

    def closeEvent(self, event):
        self._stop_background_music()
        pygame.mixer.quit()
        super().closeEvent(event)

    def _show_game_screen(self):
        self.stacked_layout.setCurrentWidget(self.game_screen)
        self.game_screen.start_game_loop()
        if not pygame.mixer.music.get_busy(): # تأكد أنها غير مشغولة قبل البدء
            self._play_background_music()
        pygame.mixer.music.set_volume(1.0)

    def _show_game_screen_and_restart(self):
        self.stacked_layout.setCurrentWidget(self.game_screen)
        self.game_screen.start_game_loop()
        pygame.mixer.music.set_volume(1.0) # تأكد من ضبط الصوت

    def _show_main_menu(self):
        self.game_screen.stop_game_loop()
        self.stacked_layout.setCurrentWidget(self.main_menu)
        self._play_background_music()

    def _show_settings_screen(self):
        self.stacked_layout.setCurrentWidget(self.settings_menu)

    def _show_about_screen(self):
        self.stacked_layout.setCurrentWidget(self.about_screen)

    def _show_help_screen(self):
        self.stacked_layout.setCurrentWidget(self.help_screen)

    def _show_game_over_screen(self, final_score, level_reached, missed_threats):
        self.game_screen.stop_game_loop()
        self.game_over_screen.set_final_stats(final_score, level_reached, missed_threats)
        self.stacked_layout.setCurrentWidget(self.game_over_screen)

    def _show_pause_menu(self):
        self.stacked_layout.setCurrentWidget(self.pause_menu)
        if pygame.mixer.music.get_busy(): # هذا جيد، check if playing to pause
            pygame.mixer.music.pause()

    def _resume_game(self):
        self.stacked_layout.setCurrentWidget(self.game_screen)
        self.game_screen.resume_game()
        # تمت إزالة شرط get_paused() هنا لتجنب الخطأ
        pygame.mixer.music.unpause() # استئناف الموسيقى مباشرة

    def _restart_game_from_pause(self):
        self.stacked_layout.setCurrentWidget(self.game_screen)
        self.game_screen.start_game_loop() # هذا سيعيد ضبط اللعبة ويبدأها من جديد، ويتعامل مع الموسيقى
        # تمت إزالة شرط get_paused() واستدعاء unpause() هنا
        # لأنه عند start_game_loop()، الموسيقى ستبدأ مجددًا من _play_background_music في _show_game_screen
