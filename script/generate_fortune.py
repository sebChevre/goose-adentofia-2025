#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic flair
FORTUNES = [
    "The stars whisper of adventures yet unexplored, where courage meets destiny.",
    "A surprise awaits around the corner, wrapped in mystery and delight.",
    "Your path leads to unexpected joy, found in the simplest of moments.",
    "The universe aligns to bring you clarity where once there was fog.",
    "An old friend will return with news that brightens your darkest hour.",
    "Creativity flows through you like a river—let it carve new channels.",
    "Patience will be rewarded with a harvest more bountiful than imagined.",
    "The answer you seek lies not in the distance, but within your own heart.",
    "A small risk today paves the way for a magnificent tomorrow.",
    "The goose knows: sometimes the wildest path leads home.",
]

# ASCII art of a sassy goose
GOOSE_ALTERNATIVES = [
    """
      __
    <(o )___
     ( ._> /
      \\___/
    /|   |\\
   (_|   |_)
    /|   |\\
   / |   | \\
  /  |   |  \\
 /   |   |   \\
/____|___|____\\
  (SASSY MODE)
""",
    """
      __
    <(o )___
     ( ._> /
      \\___/
    /|   |\\
   (_|   |_)
    /|   |\\
   / |   | \\
  /  |   |  \\
 /   |   |   \\
/____|___|____\\
  (MYSTIC MODE)
""",
    """
      __
    <(o )___
     ( ._> /
      \\___/
    /|   |\\
   (_|   |_)
    /|   |\\
   / |   | \\
  /  |   |  \\
 /   |   |   \\
/____|___|____\\
  (WISDOM MODE)
""",
]

def generate_fortune():
    """Generate a fortune with poetic mood and sassy goose."""
    fortune = random.choice(FORTUNES)
    goose = random.choice(GOOSE_ALTERNATIVES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the fortune card with border
    border = "+" + "-" * 58 + "+"
    divider = "|" + "=" * 58 + "|"
    
    lines = []
    lines.append(border)
    lines.append("|" + " " * 58 + "|")
    lines.append("|" + "  ✨ POETIC FORTUNE OF THE DAY ✨".center(58) + "|")
    lines.append("|" + " " * 58 + "|")
    lines.append(divider)
    lines.append("|" + " " * 58 + "|")
    
    # Add fortune text (wrapped to fit)
    fortune_lines = []
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 56:
            current_line += " " + word if current_line else word
        else:
            fortune_lines.append(current_line)
            current_line = word
    if current_line:
        fortune_lines.append(current_line)
    
    for line in fortune_lines:
        lines.append("|" + "  " + line + " " * (54 - len(line)) + "|")
    
    lines.append("|" + " " * 58 + "|")
    lines.append(divider)
    lines.append("|" + " " * 58 + "|")
    
    # Add goose art (centered)
    goose_lines = goose.strip().split('\n')
    for line in goose_lines:
        centered = line.center(58)
        lines.append("|" + centered + "|")
    
    lines.append("|" + " " * 58 + "|")
    lines.append(border)
    lines.append("")
    lines.append(f"Generated: {timestamp}")
    lines.append("May the cosmic winds guide your path... 🪿✨")
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save fortune."""
    # Generate the fortune
    fortune_content = generate_fortune()
    
    # Check if fortune.md exists
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        import shutil
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        shutil.move(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write the new fortune
    with open(fortune_path, 'w') as f:
        f.write(fortune_content)
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + fortune_content)

if __name__ == "__main__":
    main()
