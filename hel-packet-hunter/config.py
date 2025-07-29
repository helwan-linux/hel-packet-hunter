# config.py

# Game dimensions
GAME_WIDTH = 800
GAME_HEIGHT = 600
INFO_PANEL_WIDTH = 250 # Increased for better info display
TOTAL_WIDTH = GAME_WIDTH + INFO_PANEL_WIDTH
TOTAL_HEIGHT = GAME_HEIGHT

# Colors (RGB tuples)
COLOR_BACKGROUND = (26, 26, 46) # Dark Blue/Purple
COLOR_GRID_LINES = (50, 50, 70) # Slightly lighter purple
COLOR_SNIFFER = (0, 150, 255) # Bright Blue
COLOR_SAFE_PACKET = (0, 255, 0) # Green
COLOR_THREAT_PACKET = (255, 0, 0) # Red
COLOR_TEXT_NORMAL = (224, 224, 224) # Light Gray
COLOR_TEXT_HIGHLIGHT = (255, 255, 0) # Yellow

# Sniffer settings
SNIFFER_SIZE = 50
SNIFFER_SPEED = 10 # Pixels per move

# Packet settings
PACKET_SIZE = 40
PACKET_SPEED_INITIAL = 2 # Pixels per update
PACKET_SPAWN_INTERVAL_INITIAL = 1500 # Milliseconds
PACKET_SPAWN_INTERVAL_MIN = 500 # Minimum spawn interval

# Game settings
FPS = 60
SCORE_SAFE_PACKET = 5
SCORE_THREAT_PACKET = 10
PENALTY_MISSED_THREAT = 15
LEVEL_UP_SCORE_THRESHOLD = 100 # Score needed to level up
MAX_MISSED_THREATS = 5 # Game over if missed threats reach this
