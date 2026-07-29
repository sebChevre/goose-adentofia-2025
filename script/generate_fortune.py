#!/usr/bin/env python3
"""
Fortune Generator - A Sassy Goose Fortune Teller
Generates poetic fortunes with ASCII art flair
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic mood
FORTUNES = [
    "The stars whisper that your courage shall bloom like dawn's first light, \nand opportunities shall find you where least expected.",
    "A mystery unfolds before you, like petals opening to the moon—\ntrust your intuition, for it sees what eyes cannot.",
    "The winds of change carry whispers of prosperity,\nbut beware: the path winds through shadows before reaching gold.",
    "Three doors stand before you, yet only one bears the mark of destiny.\nChoose with wisdom, not haste.",
    "An old friend shall return bearing gifts you forgot you needed,\nand laughter shall echo where silence once dwelt.",
    "The river of fate flows swift today—hold tight to your convictions,\nfor the current tests all who seek the other shore.",
    "A secret long buried shall surface like a pearl from the deep,\nrevealing truths that set you free.",
    "The cosmos aligns in your favor, dear seeker,\nbut remember: even the mightiest oak began as a humble acorn.",
    "Beware the siren's song of easy paths,\nfor treasure lies only where effort has watered the soil.",
    "Your path crosses with destiny's messenger within three days.\nListen closely to what is said, and what is left unsaid.",
]

# ASCII art of a sassy goose
GOOSE_ART = """
       _._
      (o.o)  *sassy honk*
       |=|
      __|__
     //.=.\\\\
    // | \\\\
   ((  |  ))
    \\\\ | //
     \\\\|//
      | |
     /   \\\\
    (     )
     \\___/
"""

def generate_fortune():
    """Generate a random fortune with poetic flair."""
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the full fortune display with border, art, and divider."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the display
    border_top = "╔" + "═" * 58 + "╗"
    border_bottom = "╚" + "═" * 58 + "╝"
    border_side = "║"
    divider = "├" + "─" * 58 + "┤"
    
    lines = []
    lines.append(border_top)
    lines.append(border_side + "  🌙 THE SASSY GOOSE FORTUNE TELLER 🌙".center(56) + border_side)
    lines.append(border_side + f"  {timestamp}".center(56) + border_side)
    lines.append(border_side + " " * 58 + border_side)
    lines.append(border_side + "  Your Fortune Awaits...".center(56) + border_side)
    lines.append(border_side + " " * 58 + border_side)
    
    # Add fortune text (wrapped)
    for line in fortune.split('\n'):
        lines.append(border_side + f"  {line}".center(56) + border_side)
    
    lines.append(border_side + " " * 58 + border_side)
    lines.append(divider)
    lines.append(border_side + " " * 58 + border_side)
    lines.append(border_side + "  The Sassy Goose Speaks:".center(56) + border_side)
    lines.append(border_side + " " * 58 + border_side)
    
    # Add goose art (centered approximately)
    goose_lines = GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        # Center the goose art
        padded_line = line.center(56)
        lines.append(border_side + padded_line + border_side)
    
    lines.append(border_side + " " * 58 + border_side)
    lines.append(border_side + "  Honk if you believe! 🪿".center(56) + border_side)
    lines.append(border_bottom)
    
    return '\n'.join(lines)

def save_fortune(content, output_path):
    """Save fortune to markdown file, backing up existing file."""
    # Check if output file exists
    if os.path.exists(output_path):
        # Create old directory if it doesn't exist
        old_dir = os.path.join(os.path.dirname(output_path) or '.', 'old')
        os.makedirs(old_dir, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"fortune_{timestamp}.md"
        backup_path = os.path.join(old_dir, backup_name)
        os.rename(output_path, backup_path)
        print(f"✓ Backed up existing fortune to: {backup_path}")
    
    # Write new fortune
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 🌙 Sassy Goose Fortune 🌙\n\n")
        f.write("```text\n")
        f.write(content)
        f.write("\n```\n")
    
    print(f"✓ Fortune saved to: {output_path}")

def main():
    """Main function to generate and save fortune."""
    # Output path (current directory)
    output_path = os.path.join(os.getcwd(), 'fortune.md')
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Print to console
    print("\n")
    print(fortune_display)
    print("\n")
    
    # Save to markdown file
    save_fortune(fortune_display, output_path)

if __name__ == "__main__":
    main()
