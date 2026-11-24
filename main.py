"""One Emoji, One Smile."""
import os

# A sunflower: bright, friendly from anyone, and reads the same at every age.
EMOJI = "\U0001F33B"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EMOJI)
