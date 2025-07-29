import random
import json
import os
from config import PACKET_SPEED, GAME_WIDTH, GAME_HEIGHT, COLOR_SAFE_PACKET, COLOR_THREAT_PACKET

class Packet:
    def __init__(self, is_threat=False):
        self.is_threat = is_threat
        self.protocol_data = self._load_packet_data(is_threat)
        self.name = self.protocol_data['name']
        self.description = self.protocol_data['description']
        self.color = COLOR_THREAT_PACKET if is_threat else COLOR_SAFE_PACKET
        self.size = 20 # Small square representing the packet

        # Initial position (will be updated by NetworkGrid or GameLogic)
        self.x = 0
        self.y = 0
        self.dx = PACKET_SPEED # Movement direction x
        self.dy = 0 # Movement direction y (for now, simple horizontal movement)

    def _load_packet_data(self, is_threat):
        script_dir = os.path.dirname(__file__) # Get current script directory
        data_dir = os.path.join(script_dir, '..', 'data')

        if is_threat:
            file_path = os.path.join(data_dir, 'threats.json')
        else:
            file_path = os.path.join(data_dir, 'protocols.json')

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return random.choice(data)
        except FileNotFoundError:
            print(f"Error: Data file not found at {file_path}")
            # Fallback in case of error
            return {"name": "UNKNOWN", "description": "N/A"}

    def update(self):
        self.x += self.dx
        self.y += self.dy
        # Basic boundary check (will be more complex with grid paths)
        if self.x > GAME_WIDTH + self.size: # If packet goes off screen to the right
            return True # Indicate that it's off screen
        return False

    def get_rect(self):
        # Returns a simple rect for drawing and collision detection
        return (self.x, self.y, self.size, self.size)
