from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
# import pygame.mixer # Comment out this line

from ui.main_menu import MainMenu
from ui.game_screen import GameScreen
from ui.settings_menu import SettingsMenu
from ui.about_screen import AboutScreen
from ui.help_screen import HelpScreen
from ui.game_over_screen import GameOverScreen
from ui.pause_menu import PauseMenu 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packet Hunter")
        self.resize(1024, 768) 
        self.setMinimumSize(1024, 768) 

        self.setWindowIcon(QIcon("assets/icons/game_icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.stacked_layout = QStackedLayout(self.central_widget)
        
        self._setup_ui()
        self._connect_signals()
        # self._load_music() # Comment out this line
        # self._play_background_music() # Comment out this line

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

        self.game_over_screen.restart_game_signal.connect(self._show_game_screen)
        self.game_over_screen.back_to_main_menu_signal.connect(self._show_main_menu)

        self.pause_menu.resume_game_signal.connect(self._resume_game)
        self.pause_menu.restart_game_signal.connect(self._restart_game_from_pause)
        self.pause_menu.back_to_main_menu_signal.connect(self._show_main_menu)

    def _load_music(self): # Keep the method, but comment out its content
        pass # Commented out try/except block
        # try:
        #     pygame.mixer.music.load("assets/sounds/background_music.mp3")
        #     print("Background music loaded.")
        # except pygame.error as e:
        #     print(f"Could not load background music: {e}")

    def _play_background_music(self): # Keep the method, but comment out its content
        pass # Commented out if/try/except block
        # if pygame.mixer.music.get_busy():
        #     pygame.mixer.music.stop()
        # try:
        #     pygame.mixer.music.play(-1) # -1 means loop indefinitely
        #     print("Background music playing.")
        # except pygame.error as e:
        #     print(f"Could not play background music: {e}")

    def _stop_background_music(self): # Keep the method, but comment out its content
        pass # Commented out if block
        # if pygame.mixer.music.get_busy():
        #     pygame.mixer.music.stop()
        #     print("Background music stopped.")

    def closeEvent(self, event): # Override close event, remove music stop call
        # self._stop_background_music() # Comment out this line
        super().closeEvent(event)

    def _show_game_screen(self):
        self.stacked_layout.setCurrentWidget(self.game_screen)
        self.game_screen.start_game_loop()

    def _show_main_menu(self):
        self.game_screen.stop_game_loop()
        self.stacked_layout.setCurrentWidget(self.main_menu)
        # self._play_background_music() # Comment out this line

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
        # self._play_sound_effect("game_over.wav") # Comment out this line

    def _show_pause_menu(self): 
        self.stacked_layout.setCurrentWidget(self.pause_menu)
        # if pygame.mixer.music.get_busy(): # Comment out this block
        #     pygame.mixer.music.pause()

    def _resume_game(self): 
        self.stacked_layout.setCurrentWidget(self.game_screen)
        self.game_screen.resume_game()
        # if pygame.mixer.music.get_paused(): # Comment out this block
        #     pygame.mixer.music.unpause()
        
    def _restart_game_from_pause(self): 
        self.stacked_layout.setCurrentWidget(self.game_screen)
        self.game_screen.start_game_loop() 
        # if pygame.mixer.music.get_paused(): # Comment out this block
        #     pygame.mixer.music.unpause()

    def _play_sound_effect(self, filename): # Keep the method, but comment out its content
        pass # Commented out try/except block
        # try:
        #     sound = pygame.mixer.Sound(f"assets/sounds/{filename}")
        #     sound.play()
        # except pygame.error as e:
        #     print(f"Could not play sound effect {filename}: {e}")
