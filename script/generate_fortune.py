#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic flair
FORTUNES = [
    "The stars align in your favor, dear seeker. A surprise awaits that will brighten your darkest hour.",
    "Patience is your ally now. Like a river carving stone, persistence will bring your desires to fruition.",
    "A friend from the past will cross your path again, bearing gifts of wisdom and joy.",
    "The winds of change blow gently. Embrace new beginnings with an open heart.",
    "Your creative spark will ignite something magnificent. Trust your intuition today.",
    "A small act of kindness will return to you multiplied, like seeds scattered by the wind.",
    "The moon whispers secrets of romance. Keep your eyes open for unexpected connections.",
    "Challenges ahead are but stepping stones. Each one brings you closer to your true path.",
    "Abundance flows toward you now. Be ready to receive with gratitude and grace.",
    "A word you speak today will echo through the lives of others. Choose it wisely.",
]

# Sassy Goose ASCII Art
GOOSE_ART = """
       __
      /  \\
     |    |
     |    |
      \\  /
       \\/
    __/\\__/__
   /         \\
  |  O     O  |
  |     <     |
  |    ___    |
   \\  \\___/  /
    \\_______/
    /       \\
   |  \\   /  |
   |   \\_/   |
   |  /   \\  |
   | |     | |
   | |     | |
   | |     | |
   | |     | |
   \\_|     |_\\
     |     |
     |     |
     |     |
    /       \\
   |   ___   |
   |  (___)  |
   |         |
   |_________|
"""

# Fortune Art (Crystal Ball)
FORTUNE_ART = """
      _
    (o)
   /   \\
  |     |
   \\___/
    | |
    | |
   /   \\
  |     |
   \\___/
"""


def generate_fortune():
    """Generate a random fortune with poetic mood."""
    return random.choice(FORTUNES)


def create_bordered_content(fortune, goose_art, fortune_art):
    """Create visually appealing bordered content with divider."""
    border_char = "═"
    side_char = "║"
    
    # Get the max width needed
    lines = fortune_art.split('\n') + [''] + goose_art.split('\n')
    max_width = max(len(line) for line in lines)
    
    # Create the fortune section
    fortune_lines = fortune.split('\n')
    fortune_width = max(len(line) for line in fortune_lines)
    
    # Build the complete content
    output = []
    
    # Top border
    output.append(border_char * (max_width + 4))
    
    # Fortune section header
    output.append(f"{side_char}  🌙 POETIC FORTUNE  🌙{' ' * (max_width - 23)}{side_char}")
    output.append(f"{side_char}  {border_char * 23}{' ' * (max_width - 23)}{side_char}")
    
    # Fortune text (centered)
    for line in fortune_lines:
        padding = (max_width - len(line)) // 2
        output.append(f"{side_char}{' ' * padding}{line}{' ' * (max_width - padding - len(line))}{side_char}")
    
    # Divider
    output.append(f"{side_char}  {border_char * 23}{' ' * (max_width - 23)}{side_char}")
    output.append(f"{side_char}  ✨ DIVIDER ✨{' ' * (max_width - 15)}{side_char}")
    output.append(f"{side_char}  {border_char * 23}{' ' * (max_width - 23)}{side_char}")
    
    # Goose section header
    output.append(f"{side_char}  🪿 SASSY GOOSE 🪿{' ' * (max_width - 19)}{side_char}")
    output.append(f"{side_char}  {border_char * 19}{' ' * (max_width - 19)}{side_char}")
    
    # Add fortune art and goose art
    art_lines = fortune_art.split('\n') + goose_art.split('\n')
    for line in art_lines:
        padding = (max_width - len(line)) // 2
        output.append(f"{side_char}{' ' * padding}{line}{' ' * (max_width - padding - len(line))}{side_char}")
    
    # Bottom border with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output.append(f"{side_char}  Generated: {timestamp}{' ' * (max_width - 24 - len(timestamp))}{side_char}")
    output.append(border_char * (max_width + 4))
    
    return '\n'.join(output)


def main():
    """Main function to generate and save fortune."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.dirname(script_dir)  # Current directory (parent of script)
    fortune_file = os.path.join(output_dir, 'fortune.md')
    old_dir = os.path.join(output_dir, 'old')
    
    # If fortune.md exists, move it to /old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_dir, exist_ok=True)
        # Get existing filename with counter if needed
        base_name = 'fortune.md'
        counter = 1
        while os.path.exists(os.path.join(old_dir, base_name)):
            name, ext = os.path.splitext(base_name)
            base_name = f"{name}_{counter}{ext}"
            counter += 1
        
        import shutil
        shutil.move(fortune_file, os.path.join(old_dir, base_name))
        print(f"Moved existing fortune.md to {old_dir}/{base_name}")
    
    # Generate fortune
    fortune = generate_fortune()
    
    # Create the formatted content
    content = create_bordered_content(fortune, GOOSE_ART, FORTUNE_ART)
    
    # Add markdown header
    markdown_content = f"""# 🔮 Fortune Teller's Prediction

{content}

---
*May the winds of fortune blow in your direction* 🌬️✨
"""
    
    # Write to fortune.md
    with open(fortune_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + "=" * 50)
    print("Your Fortune:")
    print(fortune)
    print("=" * 50)


if __name__ == "__main__":
    main()
