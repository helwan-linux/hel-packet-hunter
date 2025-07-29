# Game Settings
GAME_WIDTH = 1024
GAME_HEIGHT = 768
FPS = 60
PACKET_SPEED = 2 # Pixels per game loop update

# Sniffer Settings
SNIFFER_SIZE = 30 # Size of the Sniffer (e.g., 30x30 pixels)
SNIFFER_SPEED = 5 # Pixels per movement step

# Colors (RGB tuples)
COLOR_BACKGROUND = (30, 30, 30) # Dark gray
COLOR_GRID_LINES = (50, 50, 50) # Slightly lighter gray
COLOR_SAFE_PACKET = (0, 255, 0) # Green
COLOR_THREAT_PACKET = (255, 0, 0) # Red
COLOR_SNIFFER = (0, 191, 255) # Deep Sky Blue
COLOR_TEXT_NORMAL = (255, 255, 255) # White
COLOR_TEXT_INFO = (0, 255, 255) # Cyan

# Game Logic
POINTS_PER_SAFE_DETECT = -5 # Penalty for false positive
POINTS_PER_THREAT_DETECT = 10 # Reward for correct threat detection
POINTS_PER_THREAT_MISSED = -15 # Penalty for missed threat

# Game Over Conditions
MIN_SCORE_FOR_GAME_OVER = -50 # Game over if score drops below this
MAX_MISSED_THREATS_FOR_GAME_OVER = 5 # Game over if this many threats are missed

# Level Progression (New)
LEVEL_UP_SCORE = 100 # Score needed to advance to next level
THREAT_CHANCE_INCREASE_PER_LEVEL = 0.05 # How much threat chance increases per level
PACKET_SPEED_INCREASE_PER_LEVEL = 0.5 # How much packet speed increases per level
TIME_BETWEEN_PACKETS_DECREASE_PER_LEVEL = 0.9 # Multiplier: 0.9 means 10% faster (e.g., 2s -> 1.8s)
