#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic flair
FORTUNES = [
    "The stars whisper of adventures waiting beyond your horizon, dear seeker.",
    "A unexpected joy approaches on wings of chance—keep your heart open.",
    "The universe conspires to bring you what you truly need, not what you want.",
    "Like a river finding its course, your path will reveal itself in time.",
    "Patience is the key that unlocks doors you've been pounding upon.",
    "The moon's reflection shows not what is, but what could be yours.",
    "A conversation you've been avoiding holds the answer you seek.",
    "The seeds you planted in darkness will bloom in unexpected light.",
    "Trust the whispers of your intuition—they know the way home.",
    "What you seek is also seeking you, and it draws near.",
]

# ASCII art of a sassy goose
GOOSE_ART = """
   __      __
  /  \\    /  \\
 |    \\//    |
 |  O      O  |
 |     <      |
  \\\\  \\\\____/  /
   \\\\        /
    \\\\______/
    /|    |\\\\
   / |    | \\\\
  /  |    |  \\\\
     |    |
     |    |
    /      \\\\
   |        |
   |        |
   |        |
"""

def create_fortune_display():
    """Create the visually appealing fortune display with ASCII art."""
    fortune = random.choice(FORTUNES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the fortune box
    border = "╔" + "═" * 40 + "╗"
    middle = "║" + " " * 40 + "║"
    bottom = "╚" + "═" * 40 + "╝"
    
    # Build the display
    lines = []
    lines.append(border)
    lines.append("║" + "  ✨ POETIC FORTUNE ✨".ljust(38) + "║")
    lines.append(middle)
    lines.append("║" + "  " + fortune.ljust(36) + "║")
    lines.append(middle)
    lines.append("║" + "  ──────────────────────────────".ljust(38) + "║")
    lines.append("║" + "  " + "DIVIDER".center(36) + "║")
    lines.append("║" + "  ──────────────────────────────".ljust(38) + "║")
    lines.append(middle)
    
    # Add the sassy goose
    goose_lines = GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        lines.append("║" + line.center(40) + "║")
    
    lines.append(middle)
    lines.append("║" + "  Generated: " + timestamp.ljust(26) + "║")
    lines.append(bottom)
    
    return '\n'.join(lines)

def manage_fortune_file():
    """Move existing fortune.md to old folder if it exists."""
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to: {old_path}")
    
    return fortune_path

def main():
    """Main function to generate and save the fortune."""
    print("🔮 Consulting the mystical forces...")
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Manage existing file
    output_path = manage_fortune_file()
    
    # Write to fortune.md
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(fortune_display)
        f.write('\n')
    
    print(f"\n✨ Your fortune has been written to: {output_path}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
