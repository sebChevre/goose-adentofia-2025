#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic flair
FORTUNES = [
    "The stars whisper of adventures waiting just beyond your horizon. Dare to step forward.",
    "A creative spark ignites within you—let it guide you to unexpected wonders.",
    "Patience shall be your companion, for the finest treasures bloom in their own time.",
    "An old friendship shall rekindle, bringing warmth to your autumn days.",
    "The universe conspires to bring you a moment of pure, unbridled joy.",
    "Your words carry magic today—speak them with confidence and kindness.",
    "A surprise awaits you where you least expect it. Keep your eyes wide open.",
    "The path ahead may twist, but each turn reveals a new gift.",
    "Trust your intuition—it knows the way even when the road seems dark.",
    "Something beautiful is growing in the shadows of your doubts. Nurture it.",
]

# Sassy goose ASCII art
GOOSE_ART = """
   __
  /  \\
 |    |
 |    |
  \\__/
   ||
   ||    /\\
   ||   /  \\
   ||  |    |
   ||   \\__/
   ||
  _||_
 (____)
"""

GOOSE_ART_SASSY = """
    __
   /  \\
  | o o|
  |  < |   HONK!
  \\__/
   ||
   ||    /\\
   ||   /  \\
   ||  |    |
   ||   \\__/
   ||
  _||_
 (____)
"""

GOOSE_ART_MISCHIEVOUS = """
   __
  /  \\
 | ^ ^|
 |    |   *wink*
  \\__/
   ||
   ||    /\\
   ||   /  \\
   ||  |    |
   ||   \\__/
   ||
  _||_
 (____)
"""

def generate_fortune():
    """Generate a random fortune with ASCII art."""
    fortune = random.choice(FORTUNES)
    
    # Choose a random goose art style
    goose_variants = [GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_MISCHIEVOUS]
    goose = random.choice(goose_variants)
    
    # Get current date
    date_str = datetime.now().strftime("%B %d, %Y")
    
    # Build the fortune card with border
    border = "╔" + "═" * 58 + "╗"
    bottom = "╚" + "═" * 58 + "╝"
    side = "║"
    
    lines = []
    lines.append(border)
    lines.append(f"{side}{'✨ POETIC FORTUNE ✨':^56}{side}")
    lines.append(f"{side}{'🌙 ' + date_str + ' 🌙':^56}{side}")
    lines.append(side + "═" * 58 + side)
    lines.append(side)
    
    # Add fortune text (wrapped)
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 54:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(f"{side} {current_line:<54}{side}")
            current_line = word
    if current_line:
        lines.append(f"{side} {current_line:<54}{side}")
    
    lines.append(side)
    lines.append(side + "─" * 58 + side)
    lines.append(side)
    
    # Add goose art (centered)
    for goose_line in goose.strip().split('\n'):
        # Center the goose art within the border
        centered = goose_line.center(56)
        lines.append(f"{side} {centered:<54}{side}")
    
    lines.append(side)
    lines.append(bottom)
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save fortune."""
    # Generate the fortune
    fortune_content = generate_fortune()
    
    # Output file path (current directory)
    output_file = "fortune.md"
    
    # Check if file exists and move to old folder
    if os.path.exists(output_file):
        old_folder = "old"
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing fortune to: {old_path}")
    
    # Write new fortune to file
    with open(output_file, 'w') as f:
        f.write(f"# Daily Fortune\n\n")
        f.write(f"```text\n{fortune_content}\n```\n")
    
    print(f"Fortune generated and saved to: {output_file}")
    print("\n" + fortune_content)

if __name__ == "__main__":
    main()
