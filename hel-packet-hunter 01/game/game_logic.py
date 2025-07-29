import random
from PyQt6.QtCore import pyqtSignal, QObject 
from game.sniffer import SnifferAgent
from game.packet import Packet
from config import (
    GAME_WIDTH, GAME_HEIGHT, PACKET_SPEED, FPS,
    POINTS_PER_SAFE_DETECT, POINTS_PER_THREAT_DETECT, POINTS_PER_THREAT_MISSED,
    MIN_SCORE_FOR_GAME_OVER, MAX_MISSED_THREATS_FOR_GAME_OVER,
    LEVEL_UP_SCORE, THREAT_CHANCE_INCREASE_PER_LEVEL,
    PACKET_SPEED_INCREASE_PER_LEVEL, TIME_BETWEEN_PACKETS_DECREASE_PER_LEVEL
)

class GameLogic(QObject): 
    game_over_signal = pyqtSignal(int, int, int) 
    level_up_signal = pyqtSignal(int) 
    packet_intercepted_signal = pyqtSignal(bool) # New: True for threat, False for safe
    threat_missed_signal = pyqtSignal() # New: Signal when a threat is missed

    def __init__(self):
        super().__init__() 
        self.sniffer = SnifferAgent()
        self.packets = []
        self.score = 0
        self.level = 1
        self.missed_threats_count = 0
        self.game_over = False
        
        self.packet_spawn_timer = 0
        self.base_time_between_packets = FPS * 2 
        self.current_time_between_packets = self.base_time_between_packets
        self.current_packet_speed = PACKET_SPEED
        self.current_threat_chance = 0.3 

        self.level_up_progress = 0 

    def reset_game(self):
        self.sniffer = SnifferAgent()
        self.packets = []
        self.score = 0
        self.level = 1
        self.missed_threats_count = 0
        self.game_over = False
        self.packet_spawn_timer = 0
        self.current_time_between_packets = self.base_time_between_packets
        self.current_packet_speed = PACKET_SPEED
        self.current_threat_chance = 0.3
        self.level_up_progress = 0
        print("Game reset!")

    def update(self):
        if self.game_over:
            return

        if self.level_up_progress >= LEVEL_UP_SCORE:
            self._level_up()

        self.packet_spawn_timer += 1
        if self.packet_spawn_timer >= self.current_time_between_packets:
            self.spawn_packet()
            self.packet_spawn_timer = 0

        packets_to_remove = []
        for packet in self.packets:
            packet.dx = self.current_packet_speed 
            if packet.update(): 
                packets_to_remove.append(packet)
                if packet.is_threat:
                    self.score += POINTS_PER_THREAT_MISSED
                    self.missed_threats_count += 1
                    self.threat_missed_signal.emit() # Emit signal for missed threat
                    print(f"Missed threat! {POINTS_PER_THREAT_MISSED} points. Missed: {self.missed_threats_count}. Score: {self.score}")
            
        for packet in packets_to_remove:
            self.packets.remove(packet)

        if self.score <= MIN_SCORE_FOR_GAME_OVER or \
           self.missed_threats_count >= MAX_MISSED_THREATS_FOR_GAME_OVER:
            self._game_over()

    def spawn_packet(self):
        is_threat = random.random() < self.current_threat_chance
        new_packet = Packet(is_threat=is_threat)
        
        new_packet.x = -new_packet.size
        new_packet.y = random.randint(50, GAME_HEIGHT - 50 - new_packet.size)
        
        self.packets.append(new_packet)

    def handle_sniffer_movement(self, dx, dy):
        self.sniffer.move(dx, dy)

    def intercept_packet(self):
        sniffer_rect = self.sniffer.get_rect()
        intercepted_packet = None

        for packet in self.packets:
            packet_rect = packet.get_rect()
            
            if (sniffer_rect[0] < packet_rect[0] + packet_rect[2] and
                sniffer_rect[0] + sniffer_rect[2] > packet_rect[0] and
                sniffer_rect[1] < packet_rect[1] + packet_rect[3] and
                sniffer_rect[1] + sniffer_rect[3] > packet_rect[1]):
                
                intercepted_packet = packet
                break

        if intercepted_packet:
            print(f"Intercepted: {intercepted_packet.name} (Threat: {intercepted_packet.is_threat}) - {intercepted_packet.description}")
            if intercepted_packet.is_threat:
                self.score += POINTS_PER_THREAT_DETECT
                self.level_up_progress += POINTS_PER_THREAT_DETECT 
            else:
                self.score += POINTS_PER_SAFE_DETECT
            
            self.packet_intercepted_signal.emit(intercepted_packet.is_threat) # Emit signal here
            self.packets.remove(intercepted_packet)
            return intercepted_packet
        return None

    def _level_up(self):
        self.level += 1
        self.level_up_progress = 0 
        self.current_packet_speed += PACKET_SPEED_INCREASE_PER_LEVEL
        self.current_threat_chance = min(0.9, self.current_threat_chance + THREAT_CHANCE_INCREASE_PER_LEVEL) 
        self.current_time_between_packets *= TIME_BETWEEN_PACKETS_DECREASE_PER_LEVEL
        print(f"LEVEL UP! New Level: {self.level}, Packet Speed: {self.current_packet_speed:.1f}, Threat Chance: {self.current_threat_chance:.2f}")
        self.level_up_signal.emit(self.level) 

    def _game_over(self):
        self.game_over = True
        print(f"GAME OVER! Final Score: {self.score}, Level Reached: {self.level}, Missed Threats: {self.missed_threats_count}")
        self.game_over_signal.emit(self.score, self.level, self.missed_threats_count)
