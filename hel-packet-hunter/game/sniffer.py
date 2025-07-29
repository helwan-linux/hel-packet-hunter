# game/sniffer.py

from PyQt6.QtCore import QRect

class Sniffer:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy, game_width, game_height):
        # Update position
        self.x += dx
        self.y += dy

        # Keep sniffer within game boundaries
        self.x = max(0, min(self.x, game_width - self.width))
        self.y = max(game_height - self.height * 2, min(self.y, game_height - self.height)) # Keep sniffer in lower half

    def get_rect(self):
        return (self.x, self.y, self.width, self.height)

    def check_collision(self, packet):
        sniffer_rect = QRect(self.x, self.y, self.width, self.height)
        packet_rect = QRect(packet.x, packet.y, packet.width, packet.height)
        return sniffer_rect.intersects(packet_rect)
