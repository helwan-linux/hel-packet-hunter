# game/packet.py

from config import COLOR_SAFE_PACKET, COLOR_THREAT_PACKET

class Packet:
    def __init__(self, x, y, width, height, speed, is_threat, color, name, description):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.is_threat = is_threat
        self.color = color
        self.name = name
        self.description = description

    def move(self):
        self.y += self.speed

    def get_rect(self):
        return (self.x, self.y, self.width, self.height)
