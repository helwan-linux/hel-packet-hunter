# game/game_logic.py

import random
from PyQt6.QtCore import pyqtSignal, QObject
from game.sniffer import Sniffer
from game.packet import Packet
from config import (
    GAME_WIDTH, GAME_HEIGHT, SNIFFER_SIZE, PACKET_SIZE,
    PACKET_SPEED_INITIAL, PACKET_SPAWN_INTERVAL_INITIAL,
    PACKET_SPAWN_INTERVAL_MIN, SCORE_SAFE_PACKET, SCORE_THREAT_PACKET,
    PENALTY_MISSED_THREAT, LEVEL_UP_SCORE_THRESHOLD, MAX_MISSED_THREATS,
    COLOR_SAFE_PACKET, COLOR_THREAT_PACKET, FPS
)

class GameLogic(QObject):
    game_over_signal = pyqtSignal(int, int, int) # score, level, missed_threats
    level_up_signal = pyqtSignal(int) # new_level
    packet_intercepted_signal = pyqtSignal(bool) # is_threat
    threat_missed_signal = pyqtSignal() # No arguments needed, just a signal

    def __init__(self):
        super().__init__()
        # سيتم تهيئة هذه المتغيرات بشكل صحيح عند استدعاء reset_game
        self.sniffer = None
        self.packets = []
        self.score = 0
        self.level = 1
        self.missed_threats_count = 0
        self.game_over = False
        self.packet_spawn_timer = 0
        self.current_packet_spawn_interval = PACKET_SPAWN_INTERVAL_INITIAL
        self.current_packet_speed = PACKET_SPEED_INITIAL
        self.score_for_next_level = LEVEL_UP_SCORE_THRESHOLD

    def reset_game(self):
        self.sniffer = Sniffer(GAME_WIDTH // 2 - SNIFFER_SIZE // 2,
                               GAME_HEIGHT - SNIFFER_SIZE * 2,
                               SNIFFER_SIZE, SNIFFER_SIZE)
        self.packets = []
        self.score = 0
        self.level = 1
        self.missed_threats_count = 0
        self.game_over = False
        self.packet_spawn_timer = 0
        self.current_packet_spawn_interval = PACKET_SPAWN_INTERVAL_INITIAL
        self.current_packet_speed = PACKET_SPEED_INITIAL
        self.score_for_next_level = LEVEL_UP_SCORE_THRESHOLD
        print("Game logic reset successfully!") # تأكيد أن الريسيت تم

    def update(self):
        if self.game_over:
            return

        self._spawn_packets()
        self._move_packets()
        self._check_for_game_over()
        self._check_level_up()

    def _spawn_packets(self):
        # يجب أن تتأكد أن هذا يزداد بشكل ثابت مع الوقت الفعلي
        self.packet_spawn_timer += (1000 / FPS) # استخدم 1000 / FPS لزيادة الزمن بالمللي ثانية
        if self.packet_spawn_timer >= self.current_packet_spawn_interval:
            x_pos = random.randint(0, GAME_WIDTH - PACKET_SIZE)
            threat_chance = min(0.1 + (self.level * 0.05), 0.5)
            is_threat = random.random() < threat_chance
            
            packet_color = COLOR_THREAT_PACKET if is_threat else COLOR_SAFE_PACKET
            packet_name = "Threat" if is_threat else "Safe"
            packet_desc = "Malicious data detected!" if is_threat else "Legitimate data packet."

            new_packet = Packet(x_pos, 0, PACKET_SIZE, PACKET_SIZE,
                                self.current_packet_speed, is_threat,
                                packet_color, packet_name, packet_desc)
            self.packets.append(new_packet)
            self.packet_spawn_timer = 0
            print(f"Packet spawned at X:{x_pos}, is threat: {is_threat}") # هذا السطر الجديد

    def _move_packets(self):
        for packet in list(self.packets):
            packet.move()
            if packet.y > GAME_HEIGHT:
                if packet.is_threat:
                    self.missed_threats_count += 1
                    self.score -= PENALTY_MISSED_THREAT
                    self.threat_missed_signal.emit()
                self.packets.remove(packet)

    def intercept_packet(self):
        intercepted_packet_info = None
        for packet in list(self.packets):
            if self.sniffer.check_collision(packet):
                if packet.is_threat:
                    self.score += SCORE_THREAT_PACKET
                    intercepted_packet_info = {'name': "Threat Intercepted!", 'description': packet.description, 'type': 'threat', 'score_change': SCORE_THREAT_PACKET}
                else:
                    self.score += SCORE_SAFE_PACKET
                    intercepted_packet_info = {'name': "Safe Packet Intercepted!", 'description': packet.description, 'type': 'safe', 'score_change': SCORE_SAFE_PACKET}
                self.packet_intercepted_signal.emit(packet.is_threat)
                self.packets.remove(packet)
                return intercepted_packet_info

        return intercepted_packet_info

    def handle_sniffer_movement(self, dx, dy):
        if self.sniffer: # التأكد من تهيئة sniffer
            self.sniffer.move(dx, dy, GAME_WIDTH, GAME_HEIGHT)

    def _check_level_up(self):
        if self.score >= self.score_for_next_level and self.level < 10:
            self.level += 1
            self.score_for_next_level += LEVEL_UP_SCORE_THRESHOLD * self.level
            self.current_packet_speed += 0.5
            self.current_packet_spawn_interval = max(PACKET_SPAWN_INTERVAL_MIN, self.current_packet_spawn_interval - 50)
            self.level_up_signal.emit(self.level)

    def _check_for_game_over(self):
        if self.score < -50 or self.missed_threats_count >= MAX_MISSED_THREATS:
            if not self.game_over: # Emit signal only once
                self.game_over = True
                self.game_over_signal.emit(self.score, self.level, self.missed_threats_count)
