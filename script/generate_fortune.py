#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with poetic vibes
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic flair
FORTUNES = [
    "The stars whisper that your creativity will bloom like a rose in spring.",
    "A unexpected opportunity awaits you where least expected.",
    "Your path leads to joy, though clouds may pass before the sun emerges.",
    "The universe conspires to bring harmony to your weary soul.",
    "Adventure calls your name - dare to answer with an open heart.",
    "Wisdom comes to those who listen to the whispers of their dreams.",
    "A friendship deepens into something precious and enduring.",
    "The winds of change bring gifts you have yet to unwrap.",
    "Your courage will illuminate the darkest corners of doubt.",
    "Patience is the key that unlocks doors you've been seeking.",
]

# Sassy goose ASCII art
GOOSE_ART = """
     __
    /  \\
   |    |
   |    |    _
   |    |   (o>
   \\    /   //
    \\__/   (_\\
    / \\
   /   \\
  /     \\
 /       \\
|  SASSY  |
|  GOOSE  |
 \\_______/
"""

def generate_fortune():
    """Generate a random fortune with poetic mood."""
    return random.choice(FORTUNES)

def create_ascii_border(content, width=60):
    """Create an ASCII border around content."""
    top_border = "╔" + "═" * width + "╗"
    bottom_border = "╚" + "═" * width + "╝"
    # Split content into lines and add border to each
    lines = content.split('\n')
    bordered_lines = []
    for line in lines:
        # Pad the line to width and add side borders
        padded = line.ljust(width)[:width]
        bordered_lines.append("║" + padded + "║")
    return f"{top_border}\n" + "\n".join(bordered_lines) + f"\n{bottom_border}"

def main():
    # Generate fortune
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the fortune display
    divider = "─" * 56
    fortune_display = f"""
    ✨ POETIC FORTUNE ✨
    
    {fortune}
    
    {divider}
    
    {GOOSE_ART}
    
    Generated: {timestamp}
    """
    
    # Create bordered version
    bordered_content = create_ascii_border(fortune_display.strip(), 60)
    
    # Output file path
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists, move to old folder if so
    if os.path.exists(output_file):
        os.makedirs(old_folder, exist_ok=True)
        # Move existing file to old folder with timestamp
        old_filename = f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing {output_file} to {old_path}")
    
    # Write to markdown file
    with open(output_file, 'w') as f:
        f.write("# 🎴 Daily Fortune 🎴\n\n")
        f.write("```text\n")
        f.write(bordered_content)
        f.write("\n```\n")
    
    print(f"Fortune written to {output_file}")
    print("\n" + bordered_content)

if __name__ == "__main__":
    main()
