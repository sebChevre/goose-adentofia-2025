#!/usr/bin/env python3
"""
Fortune Generator - Introspective Sassy Goose Edition
Generates a fortune from a fictional fortune teller with an introspective mood.
Features a sassy goose in ASCII art with the fortune above it.
"""

import os
import shutil
import random
from datetime import datetime

# Introspective fortune messages
FORTUNES = [
    "The quiet moments within hold the answers you seek. Listen to your own voice.",
    "Your journey is not about reaching destinations, but understanding the path itself.",
    "What you seek is already within you. The reflection you need is in your own eyes.",
    "True wisdom comes from sitting with uncertainty. Embrace the questions.",
    "The person you're becoming is worth more than the person you're leaving behind.",
    "Your greatest teacher has been walking beside you in the mirror all along.",
    "In the stillness between thoughts, your soul whispers its deepest truths.",
    "The wounds you carry are not weaknesses—they are maps of where you've grown.",
    "Sometimes the bravest thing is to simply be, without needing to become.",
    "Your story is still being written. The best chapters are yet to unfold.",
    "The light you search for outside has been illuminating your path from within.",
    "Reflection is not dwelling—it is gathering wisdom to move forward with purpose.",
    "The answers you seek are not in the stars, but in the quiet spaces of your heart.",
    "Your capacity for growth exceeds any obstacle standing before you today.",
    "The journey inward is the only one that truly matters. Everything else is scenery.",
]

# Sassy goose ASCII art - looking unimpressed but wise
SASSY_GOOSE = """
      _
     (.)>  *raises eyebrow*
    /   \\
   | O O |   "Oh, you want wisdom?
    \\ ^ /    Fine. Here's the thing..."
     V V
    /| |\\
   /_|_|_\\
  /  | |  \\
 |   | |   |
 |   | |   |  *crosses wings*
 \\___| |___/
     | |
     | |    "Now go figure it out yourself."
    /   \\
   |     |
   |     |
  /       \\
"""

# ASCII border characters
TOP_BORDER = "╔" + "═" * 60 + "╗"
BOTTOM_BORDER = "╚" + "═" * 60 + "╝"
MIDDLE_BORDER = "╠" + "═" * 60 + "╣"
SIDE_BORDER = "║"


def generate_fortune():
    """Generate a random introspective fortune."""
    return random.choice(FORTUNES)


def format_fortune_output(fortune):
    """Format the fortune with ASCII art and borders."""
    lines = []
    border_width = 60
    
    # Top border
    lines.append(TOP_BORDER)
    
    # Header
    title = "INTROSPECTIVE FORTUNE - SASSY GOOSE EDITION"
    lines.append(f"{SIDE_BORDER}  {title:^56} {SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}  {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):^56} {SIDE_BORDER}")
    lines.append(MIDDLE_BORDER)
    
    # Fortune section header
    lines.append(f"{SIDE_BORDER}  {'YOUR FORTUNE AWAITS...':^56} {SIDE_BORDER}")
    lines.append(MIDDLE_BORDER)
    
    # Fortune text - wrap if needed
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 54:
            current_line += (" " if current_line else "") + word
        else:
            if current_line:
                lines.append(f"{SIDE_BORDER}  {current_line:<54} {SIDE_BORDER}")
            current_line = word
    if current_line:
        lines.append(f"{SIDE_BORDER}  {current_line:<54} {SIDE_BORDER}")
    
    # Divider between fortune and goose
    lines.append(MIDDLE_BORDER)
    
    # Goose section header
    lines.append(f"{SIDE_BORDER}  {'YOUR WISE (AND SARCASTIC) GUIDE':^56} {SIDE_BORDER}")
    lines.append(MIDDLE_BORDER)
    
    # Add the sassy goose ASCII art
    goose_lines = SASSY_GOOSE.strip().split('\n')
    for g_line in goose_lines:
        # Center the goose art within the border
        centered = g_line.center(56)
        lines.append(f"{SIDE_BORDER}  {centered[:54]}  {SIDE_BORDER}")
    
    # Bottom border
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def manage_old_fortune():
    """Move existing fortune.md to old folder if it exists."""
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Generate unique name for old file with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        
        # Move the file
        shutil.move(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")


def main():
    """Main function to generate and save the fortune."""
    # Generate the fortune
    fortune = generate_fortune()
    
    # Format the output
    output = format_fortune_output(fortune)
    
    # Manage old fortune file
    manage_old_fortune()
    
    # Write to fortune.md
    with open("fortune.md", "w") as f:
        f.write(output)
    
    print("Fortune generated successfully!")
    print("\n" + output)


if __name__ == "__main__":
    main()
