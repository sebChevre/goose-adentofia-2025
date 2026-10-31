#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose companion
"""

import os
import random
from datetime import datetime

# Sassy Goose ASCII Art
SASSY_GOOSE = """
        __
      <(o )___
       ( ._> /
        \\___/
"""

SASSY_GOOSE_LARGE = """
           __
         <(o )___
          ( ._> /
           \\___/
         __
       <(o )___
        ( ._> /
         \\___/
"""

# Wise Fortune Teller ASCII Art
WISE_GOOSE = """
    .---.
   /     \\
  |  o o  |   Wisdom flows from the feathers of age
   \\  ^  /    The ancient goose knows all secrets
  /'-----'\\
  \\_______/
"""

# Fortune messages with wise/sassy tone
FORTUNES = [
    "The winds of change blow favorably in your direction. Embrace the unexpected journey ahead.",
    "A feather in your path today signals good fortune. What you seek is already on its way.",
    "The stars align with the wisdom of ancient geese. Your patience will be rewarded soon.",
    "An opportunity approaches on quiet wings. Be ready to spread your own when the moment comes.",
    "The moon whispers secrets to those who listen. Trust your intuition in the days to come.",
    "A challenge awaits, but you have the strength to soar above it like a goose in flight.",
    "The universe conspires to bring you what you need. Keep your heart open to receive it.",
    "Wisdom comes from those who have flown many migrations. Seek counsel from your elders.",
    "A surprising turn of events will lead you to unexpected joy. Embrace the detour.",
    "The river of life flows toward your destiny. Trust in its current and swim with purpose.",
    "Your hard work is about to bear fruit. The harvest season is closer than you think.",
    "A friend from the past will bring good news. Keep your ears perked for their call.",
    "The path ahead may seem unclear, but your inner compass is true. Follow your heart.",
    "Success comes to those who persist. Your wings are growing stronger with each challenge.",
    "The moon is full and your dreams are near. Take action tonight to make them reality.",
]

# Divider between goose and fortune
DIVIDER = "═══════════════════════════════════════════════════════════════"

def generate_fortune():
    """Generate a random fortune from the wise fortune teller."""
    return random.choice(FORTUNES)

def create_bordered_content(goose_art, fortune, width=60):
    """Create ASCII bordered content with the goose and fortune."""
    # Top border
    border_top = "╔" + "═" * width + "╗"
    border_bottom = "╚" + "═" * width + "╝"
    border_side = "║"
    
    lines = []
    lines.append(border_top)
    
    # Header
    header = "✨ ✨ THE WISE FORTUNE TELLER ✨ ✨"
    header = header.center(width)
    lines.append(border_side + header + border_side)
    lines.append(border_side + " " * width + border_side)
    
    # Goose art section (centered)
    goose_lines = goose_art.strip().split('\n')
    goose_width = max(len(line) for line in goose_lines)
    for line in goose_lines:
        centered = line.center(goose_width)
        padding = (width - goose_width) // 2
        lines.append(border_side + " " * padding + centered + " " * padding + border_side)
    
    lines.append(border_side + " " * width + border_side)
    
    # Divider
    divider = "─" * width
    lines.append(border_side + divider + border_side)
    lines.append(border_side + " " * width + border_side)
    
    # Fortune section
    fortune_lines = fortune.split('\n')
    for line in fortune_lines:
        wrapped = line.center(width)
        lines.append(border_side + wrapped + border_side)
    
    lines.append(border_side + " " * width + border_side)
    
    # Footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    footer = f"Fortune told on: {timestamp}"
    footer = footer.center(width)
    lines.append(border_side + footer + border_side)
    lines.append(border_side + " " * width + border_side)
    
    # Bottom border
    lines.append(border_bottom)
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save the fortune."""
    # Define paths
    current_dir = os.getcwd()
    fortune_file = os.path.join(current_dir, "fortune.md")
    old_folder = os.path.join(current_dir, "old")
    
    # Check if fortune.md already exists and move it to /old folder
    if os.path.exists(fortune_file):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        import shutil
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_folder, f"fortune_{timestamp}.md")
        shutil.move(fortune_file, old_file)
        print(f"Previous fortune.md moved to: {old_file}")
    
    # Generate the fortune
    fortune = generate_fortune()
    
    # Create the bordered content with sassy goose
    content = create_bordered_content(SASSY_GOOSE_LARGE, fortune)
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(content)
        f.write('\n')
    
    print("Fortune generated successfully!")
    print(f"Output saved to: {fortune_file}")
    print("\n" + content)

if __name__ == "__main__":
    main()
