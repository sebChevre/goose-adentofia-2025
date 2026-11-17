#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic mood
FORTUNES = [
    "The stars whisper that your courage will bloom like dawn's first light, \nleading you to treasures hidden in plain sight.",
    "A journey awaits where shadows dance with opportunity—\ntrust your heart, for it knows the way.",
    "The winds of change carry whispers of joy,\nand laughter shall be your compass soon.",
    "Like a river finding its path through stone,\nyour persistence will carve wonders yet unknown.",
    "The moon watches over dreams you've yet to speak,\nand soon they'll bloom into something remarkable.",
    "A chance encounter shall spark a flame of inspiration,\nburning bright with possibilities.",
    "The ancient quills of fate have written this:\nyour kindness will return multiplied tenfold.",
    "Beneath the canopy of tomorrow's stars,\nyou'll discover strength you never knew you held.",
    "The universe conspires in your favor,\nfor you are exactly where you need to be.",
    "Like autumn leaves that paint the sky in gold,\nyour efforts will reveal their beauty in time."
]

# Sassy Goose ASCII Art
GOOSE_ART = """
  __      __
 / /\\    / /\\
|  |\\__/|  |
|  |    |  |
 \\ \\  __\\ /
  \\ \\/      \\
   \\        )
    \\      /
     \\____/
    /      \\
   |  O  O  |
   |   ∆    |  *sassy*
   |  \\__/  |
   \\        /
    \\______/
"""

def create_border(text, width=60):
    """Create an ASCII border around text."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    
    lines = text.split('\n')
    result = [top_bottom]
    
    for line in lines:
        # Pad line to fit within border
        padded = line.ljust(width - 2)[:width - 2]
        result.append("║ " + padded + " ║")
    
    result.append(top_bottom)
    return '\n'.join(result)

def generate_fortune_output():
    """Generate the complete fortune output with goose and border."""
    fortune = random.choice(FORTUNES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the content
    content_parts = [
        "",
        "  ✦  POETIC FORTUNE  ✦",
        "",
        f"  {fortune}",
        "",
        "  ──────────────────────────────────────────────────────────",
        "",
        "  Your Guide to Wisdom:",
        GOOSE_ART,
        f"  {timestamp}",
        ""
    ]
    
    content = '\n'.join(content_parts)
    return create_border(content)

def main():
    """Main function to generate and save fortune."""
    output_file = "fortune.md"
    old_dir = "old"
    
    # Check if fortune.md already exists
    if os.path.exists(output_file):
        # Create old directory if it doesn't exist
        os.makedirs(old_dir, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_dir, f"fortune_{timestamp}.md")
        os.rename(output_file, old_file)
        print(f"Moved existing fortune.md to {old_file}")
    
    # Generate the fortune
    fortune_content = generate_fortune_output()
    
    # Write to fortune.md
    with open(output_file, 'w') as f:
        f.write(fortune_content)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + fortune_content)

if __name__ == "__main__":
    main()
