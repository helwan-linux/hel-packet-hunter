from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QTimer, Qt, QRect, pyqtSignal
from PyQt6.QtGui import QPainter, QColor, QKeyEvent, QFont
# import pygame.mixer # Comment out this line

from game.game_logic import GameLogic
from ui.widgets.info_panel import InfoPanel
from config import COLOR_BACKGROUND, COLOR_GRID_LINES, COLOR_SNIFFER, COLOR_SAFE_PACKET, COLOR_THREAT_PACKET, COLOR_TEXT_NORMAL, FPS, GAME_WIDTH, GAME_HEIGHT

class GameScreen(QWidget):
    game_over_signal = pyqtSignal(int, int, int)
    pause_game_signal = pyqtSignal() 

    def __init__(self):
        super().__init__()
        self.game_logic = GameLogic()
        self.game_running = False
        self.is_paused = False 
        self.game_timer = QTimer(self)
        self.game_timer.timeout.connect(self._game_loop_update)
        
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus) 
        
        self._setup_ui()
        # self._load_sound_effects() # Comment out this line
        self._connect_game_logic_signals()

    def _setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.game_canvas = QWidget(self)
        self.game_canvas.paintEvent = self._custom_paint_event 
        self.game_canvas.setFixedSize(GAME_WIDTH, GAME_HEIGHT)
        
        main_layout.addWidget(self.game_canvas, 1)

        self.info_panel = InfoPanel()
        main_layout.addWidget(self.info_panel)

    def _load_sound_effects(self): # Keep the method, but comment out its content
        pass # Commented out try/except block
        # self.sounds = {}
        # try:
        #     self.sounds['intercept_safe'] = pygame.mixer.Sound("assets/sounds/intercept_safe.wav")
        #     self.sounds['intercept_threat'] = pygame.mixer.Sound("assets/sounds/intercept_threat.wav")
        #     self.sounds['level_up'] = pygame.mixer.Sound("assets/sounds/level_up.wav")
        #     self.sounds['threat_missed'] = pygame.mixer.Sound("assets/sounds/threat_missed.wav")
        #     print("Sound effects loaded.")
        # except pygame.error as e:
        #     print(f"Could not load sound effect: {e}")

    def _play_sound(self, sound_name): # Keep the method, but comment out its content
        pass # Commented out if block
        # if sound_name in self.sounds:
        #     try:
        #         self.sounds[sound_name].play()
        #     except pygame.error as e:
        #         print(f"Error playing sound {sound_name}: {e}")
        # else:
        #     print(f"Sound '{sound_name}' not found.")

    def _connect_game_logic_signals(self):
        self.game_logic.game_over_signal.connect(self.game_over_signal.emit)
        self.game_logic.level_up_signal.connect(self._on_level_up)
        self.game_logic.packet_intercepted_signal.connect(self._on_packet_intercepted)
        self.game_logic.threat_missed_signal.connect(self._on_threat_missed)

    def _on_level_up(self, level):
        print(f"UI: Level Up to Level {level}!")
        # self._play_sound('level_up') # Comment out this line

    def _on_packet_intercepted(self, is_threat):
        # if is_threat: # Comment out this block
        #     self._play_sound('intercept_threat')
        # else:
        #     self._play_sound('intercept_safe')
        pass

    def _on_threat_missed(self):
        # self._play_sound('threat_missed') # Comment out this line
        pass

    def _custom_paint_event(self, event):
        painter = QPainter(self.game_canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.fillRect(self.game_canvas.rect(), QColor(*COLOR_BACKGROUND))

        pen = painter.pen()
        pen.setColor(QColor(*COLOR_GRID_LINES))
        pen.setWidth(1)
        painter.setPen(pen)
        
        grid_spacing = 50
        for x in range(0, self.game_canvas.width(), grid_spacing):
            painter.drawLine(x, 0, x, self.game_canvas.height())
        for y in range(0, self.game_canvas.height(), grid_spacing):
            painter.drawLine(0, y, self.game_canvas.width(), y)

        sniffer_rect = self.game_logic.sniffer.get_rect()
        painter.setBrush(QColor(*COLOR_SNIFFER))
        painter.drawRect(QRect(sniffer_rect[0], sniffer_rect[1], sniffer_rect[2], sniffer_rect[3]))

        for packet in self.game_logic.packets:
            packet_rect = packet.get_rect()
            painter.setBrush(QColor(*packet.color))
            painter.drawRect(QRect(packet_rect[0], packet_rect[1], packet_rect[2], packet_rect[3]))
            
            painter.setPen(QColor(*COLOR_TEXT_NORMAL))
            packet_font = QFont()
            packet_font.setPointSize(10)
            painter.setFont(packet_font)
            painter.drawText(QRect(packet_rect[0], packet_rect[1] - 20, packet_rect[2], 20), 
                             Qt.AlignmentFlag.AlignCenter, packet.name)

        painter.setPen(QColor(*COLOR_TEXT_NORMAL))
        score_level_font = QFont()
        score_level_font.setPointSize(24)
        painter.setFont(score_level_font)
        painter.drawText(10, 30, f"Score: {self.game_logic.score}")
        painter.drawText(10, 60, f"Level: {self.game_logic.level}")
        painter.drawText(10, 90, f"Missed: {self.game_logic.missed_threats_count}")

        painter.end()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape: 
            if self.game_running and not self.game_logic.game_over:
                self.pause_game()
                self.pause_game_signal.emit() 
            return 

        if not self.game_logic.game_over and not self.is_paused: 
            if event.key() == Qt.Key.Key_Left:
                self.game_logic.handle_sniffer_movement(-1, 0)
            elif event.key() == Qt.Key.Key_Right:
                self.game_logic.handle_sniffer_movement(1, 0)
            elif event.key() == Qt.Key.Key_Up:
                self.game_logic.handle_sniffer_movement(0, -1)
            elif event.key() == Qt.Key.Key_Down:
                self.game_logic.handle_sniffer_movement(0, 1)
            elif event.key() == Qt.Key.Key_Space or event.key() == Qt.Key.Key_Return:
                intercepted = self.game_logic.intercept_packet()
                if intercepted:
                    self.info_panel.update_info(intercepted)
                else:
                    self.info_panel.update_info(None)
            
            self.game_canvas.update()

    def start_game_loop(self):
        self.game_logic.reset_game()
        self.is_paused = False 
        if not self.game_running:
            self.game_running = True
            self.game_timer.start(1000 // FPS) 
            self.setFocus()
            self.info_panel.update_info(None)

    def stop_game_loop(self):
        if self.game_running:
            self.game_running = False
            self.is_paused = False 
            self.game_timer.stop()

    def pause_game(self):
        if self.game_running and not self.is_paused:
            self.is_paused = True
            self.game_timer.stop() 
            print("Game Paused!")

    def resume_game(self):
        if self.game_running and self.is_paused:
            self.is_paused = False
            self.game_timer.start(1000 // FPS) 
            self.setFocus() 
            print("Game Resumed!")
    
    def _game_loop_update(self):
        if not self.is_paused: 
            self.game_logic.update()
            self.game_canvas.update()
