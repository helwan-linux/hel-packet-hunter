from pydub import AudioSegment
import os

# Define the output directory
output_dir = "assets/sounds"
os.makedirs(output_dir, exist_ok=True) # Create directory if it doesn't exist

# Define the list of dummy sound files needed
dummy_sounds = {
    "background_music.mp3": 5000,  # 5 seconds of silence for music
    "intercept_safe.wav": 500,     # 0.5 seconds for effect
    "intercept_threat.wav": 500,
    "level_up.wav": 750,
    "game_over.wav": 1000,
    "threat_missed.wav": 500,
}

print(f"Creating dummy sound files in: {os.path.abspath(output_dir)}")

for filename, duration_ms in dummy_sounds.items():
    filepath = os.path.join(output_dir, filename)
    # Create an empty (silent) audio segment
    silent_audio = AudioSegment.silent(duration=duration_ms)
    
    # Export the silent audio to the specified file
    try:
        silent_audio.export(filepath, format=filename.split('.')[-1])
        print(f"Created: {filepath} ({duration_ms}ms silent)")
    except Exception as e:
        print(f"Error creating {filepath}: {e}")
        print("Make sure 'ffmpeg' is installed and its path is added to system environment variables.")

print("\nDummy sound creation complete. You can now run your game.")
print("Remember to replace these dummy files with actual sound files later for full audio experience!")
