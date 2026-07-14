#!/usr/bin/env python3
"""
Grumpy Fortune Teller - Generates fortunes with a sassy goose attitude
"""

import os
import random
from datetime import datetime

# Sassy goose ASCII art
SASSY_GOOSE = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

# Alternative grumpier goose variations
GRUMPY_GOOSE_VARIATIONS = [
    """
      __
    <(o )___
     ( ._> /
      \\___/
    """,
    """
      _
    <(o )
     ( .>
      \\/
    """,
    """
      __
    <(x )___
     ( .> /
      \\/\\/
    """
]

# Grumpy fortune messages
FORTUNES = [
    "Ugh, fine. Your future is... adequately predictable. Happy now?",
    "I suppose you want a fortune? Alright: Someone will annoy you less than I am today.",
    "Your destiny? *sigh* You'll survive. Barely.",
    "Oh wow, a fortune. Groundbreaking. You'll encounter something mildly interesting soon.",
    "Fine, fine! Your luck is... tolerable. Like finding a seat on a crowded bus.",
    "I'm only doing this once. Your future involves less me, which is good for everyone.",
    "Hmph. The stars say you'll do something reasonable today. Don't get used to it.",
    "Congratulations! Your fortune is... adequate. Like a lukewarm sandwich.",
    "Ugh. You'll meet someone who tolerates you as much as I tolerate this job.",
    "Fine! Something mildly amusing will happen. Try not to get your hopes up.",
    "Your future holds... *checks notes*... normalcy. Thrilling, I know.",
    "Oh joy, another fortune. You'll make it through today. Somehow.",
    "The universe whispers... *mutter*... you're doing okay. There, happy?",
    "Fine! Your luck is slightly above 'miserable'. Progress!",
    "I hate this. Your fortune: You'll find something you lost. Eventually."
]

# Border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
SIDE_BORDER = "║"
DIVIDER = "╟" + "─" * 58 + "╢"


def generate_fortune():
    """Generate a grumpy fortune from the sassy goose fortune teller."""
    return random.choice(FORTUNES)


def get_goose_art():
    """Return a random grumpy goose ASCII art."""
    return random.choice(GRUMPY_GOOSE_VARIATIONS)


def create_fortune_display():
    """Create the full fortune display with border, goose, and fortune."""
    goose_art = get_goose_art()
    fortune = generate_fortune()
    
    # Get timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the display
    lines = []
    lines.append(TOP_BORDER)
    lines.append(f"{SIDE_BORDER}{'GRUMPY FORTUNE TELLER'.center(56)}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{'Sassy Goose Edition'.center(56)}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{'-' * 56}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{goose_art.center(56)}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{DIVIDER[1:-1].center(56)}{SIDE_BORDER}")
    
    # Add fortune with proper spacing
    fortune_lines = fortune.split('\n')
    for fl in fortune_lines:
        lines.append(f"{SIDE_BORDER}{fl.center(56)}{SIDE_BORDER}")
    
    lines.append(f"{SIDE_BORDER}{'-' * 56}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{timestamp.center(56)}{SIDE_BORDER}")
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def move_existing_fortune():
    """Move existing fortune.md to old folder if it exists."""
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"fortune_{timestamp}.md"
        backup_path = os.path.join(old_folder, backup_name)
        
        # Move the file
        os.rename(fortune_path, backup_path)
        print(f"Moved existing fortune.md to {backup_path}")


def main():
    """Main function to generate fortune and save to file."""
    # Move existing fortune file if present
    move_existing_fortune()
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Write to fortune.md
    with open("fortune.md", "w") as f:
        f.write(fortune_display)
        f.write("\n")
    
    print("Fortune generated successfully!")
    print("\n" + fortune_display)


if __name__ == "__main__":
    main()
