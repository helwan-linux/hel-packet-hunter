from config import SNIFFER_SIZE, SNIFFER_SPEED, GAME_WIDTH, GAME_HEIGHT, COLOR_SNIFFER

class SnifferAgent:
    def __init__(self):
        self.size = SNIFFER_SIZE
        # Initial position (center of the screen or specific grid point)
        self.x = GAME_WIDTH // 2 - self.size // 2
        self.y = GAME_HEIGHT // 2 - self.size // 2
        self.speed = SNIFFER_SPEED
        self.color = COLOR_SNIFFER

    def move(self, dx, dy):
        # Update position based on movement direction
        self.x += dx * self.speed
        self.y += dy * self.speed
        
        # Keep sniffer within game boundaries
        self.x = max(0, min(self.x, GAME_WIDTH - self.size))
        self.y = max(0, min(self.y, GAME_HEIGHT - self.size))

    def get_rect(self):
        # Returns a simple rect for drawing and collision detection
        return (self.x, self.y, self.size, self.size)

    def get_position(self):
        return (self.x, self.y)
