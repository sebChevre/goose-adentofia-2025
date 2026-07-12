#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective wisdom.
"""

import os
import random
from datetime import datetime

# Introspective fortunes
FORTUNES = [
    "The path you seek lies within the quiet spaces between your thoughts.",
    "Today, ask yourself not what the world needs, but what your soul whispers.",
    "The answers you pursue are already dancing in your mind's eye.",
    "Pause and breathe - the universe speaks loudest in silence.",
    "Your next breakthrough comes from embracing what you fear most.",
    "The mirror of introspection reveals treasures hidden from casual glance.",
    "What you've been avoiding holds the key to your next transformation.",
    "The wisdom you seek has been waiting patiently in your memories.",
    "Look not outward for validation, but inward for truth.",
    "The journey of a thousand miles begins with a single moment of self-awareness.",
    "Your intuition knows the way; you've only forgotten how to listen.",
    "The question you're afraid to ask is the one that will set you free.",
    "In the space between doubt and certainty, your true path awaits.",
    "The past is a teacher, not a prison - what lesson calls to you?",
    "Your greatest strength is hidden in what you consider your weakness."
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
    __/ /
   (___/
   /   \\
  |     |
  |     |
  \\_____/
"""

GOOSE_ART_SASSY = """
      __
    <(o )___
     ( ._> /
      \\___/
    __/ /
   (___/
   /   \\
  |     |
  |     |
  \\_____/
   ( )
  (   )
   \\_/
"""

GOOSE_ART_THOUGHTFUL = """
      __
    <(o )___
     ( ._> /
      \\___/
    __/ /
   (___/
   /   \\
  |     |
  |     |
  \\_____/
   ^ ^
  (   )
   \\_/
"""

# ASCII border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
MIDDLE_BORDER = "║" + " " * 58 + "║"
DIVIDER = "╟" + "─" * 58 + "╢"


def generate_fortune():
    """Generate a random introspective fortune."""
    return random.choice(FORTUNES)


def select_goose_art():
    """Select a random goose art style."""
    return random.choice([GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_THOUGHTFUL])


def create_fortune_display():
    """Create the full fortune display with border, fortune, divider, and goose."""
    fortune = generate_fortune()
    goose = select_goose_art()
    
    # Format the fortune to fit within the border
    lines = []
    words = fortune.split()
    current_line = "║ "
    
    for word in words:
        if len(current_line) + len(word) + 1 <= 56:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = "║ " + word + " "
    
    lines.append(current_line)
    # Pad remaining lines
    while len(lines) < 3:
        lines.append("║" + " " * 56 + "║")
    
    # Build the display
    display = []
    display.append(TOP_BORDER)
    display.append("║" + " " * 58 + "║")
    display.append("║" + "  🌙  INTROSPECTIVE FORTUNE  🌙  " + " " * 24 + "║")
    display.append("║" + " " * 58 + "║")
    
    for line in lines:
        display.append(line)
    
    display.append("║" + " " * 58 + "║")
    display.append(DIVIDER)
    display.append("║" + " " * 58 + "║")
    display.append("║" + "  🪿  SASSY GOOSE SAYS  🪿  " + " " * 26 + "║")
    display.append("║" + " " * 58 + "║")
    
    # Add goose art (centered)
    for art_line in goose.split('\n'):
        if art_line:
            padded = art_line.center(58)
            display.append("║" + padded + "║")
    
    # Fill remaining space
    while len(display) < 20:
        display.append("║" + " " * 58 + "║")
    
    display.append("║" + " " * 58 + "║")
    display.append(BOTTOM_BORDER)
    
    return '\n'.join(display)


def main():
    """Main function to generate fortune and save to file."""
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_output = f"# 🌙 Introspective Fortune 🌙\n\nGenerated: {timestamp}\n\n{fortune_display}\n"
    
    # Check if fortune.md exists and move to /old folder
    fortune_path = "fortune.md"
    if os.path.exists(fortune_path):
        old_folder = "old"
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp_suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp_suffix}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to: {old_path}")
    
    # Write new fortune to file
    with open(fortune_path, 'w') as f:
        f.write(full_output)
    
    print(f"Fortune generated and saved to: {fortune_path}")
    print("\n" + fortune_display)


if __name__ == "__main__":
    main()
