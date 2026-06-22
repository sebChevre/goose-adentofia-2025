#!/usr/bin/env python3
"""
Fortune Generator - Grumpy Fortune Teller Edition
Generates a fortune from a fictional grumpy fortune teller with ASCII art.
"""

import os
import shutil
import random
from datetime import datetime

# Grumpy fortune messages
FORTUNES = [
    "Ugh, fine. Your future looks... tolerable. Don't get used to it.",
    "Whatever. You'll find what you're looking for, but only because I said so.",
    "Hmph. The stars say you'll succeed, but I'm not impressed by your chances.",
    "Oh joy, another person wanting a fortune. Fine - success is coming, grudgingly.",
    "Look, your path is clear. Don't waste it complaining like I am right now.",
    "The universe whispers your name. I'm rolling my eyes. You'll be fine, apparently.",
    "Ugh, you're going to make a big decision soon. Try not to mess it up.",
    "Fine, fine! Your luck is about to turn. Don't expect me to celebrate.",
    "Whatever you're worried about, it'll work out. Happy now? Go away.",
    "The fates decree... you'll survive. Thrive, even. Disappointingly for me.",
    "Sigh. Someone special will enter your life. Try not to scare them off.",
    "Your hard work will pay off. I guess that's good news. There, I said it.",
    "Ugh, you'll face a challenge. You'll overcome it. Can I go back to sleep now?",
    "Fine! Abundance is coming your way. Don't spend it all on nonsense.",
    "The universe has a plan. I have a headache. Both involve you somehow.",
]

# Sassy goose ASCII art
GRUMPY_GOOSE = """
   __      __
  /  \\____/  \\
 |  O      O  |
 |     <      |  *sigh*
  \\  \\____/  /
   \\        /
    \\______/
     |    |
     |    |  Ugh, another fortune?
    /      \\
   |        |
   |        |
  /          \\
"""

# ASCII border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
MIDDLE_BORDER = "╠" + "═" * 58 + "╣"
SIDE_BORDER = "║"


def generate_fortune():
    """Generate a random grumpy fortune."""
    return random.choice(FORTUNES)


def format_fortune_output(fortune):
    """Format the fortune with ASCII art and borders."""
    lines = []
    
    # Top border
    lines.append(TOP_BORDER)
    
    # Header
    lines.append(f"{SIDE_BORDER}  {'GRUMPY FORTUNE TELLER - FORTUNE OF THE DAY':^54} {SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}  {'Generated: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'):^54} {SIDE_BORDER}")
    lines.append(TOP_BORDER.replace("╔", "╠").replace("╗", "╣"))
    
    # Fortune section
    fortune_lines = fortune.split('\n')
    for f_line in fortune_lines:
        # Pad or truncate to fit within border
        padded = f_line[:52].ljust(52)
        lines.append(f"{SIDE_BORDER}  {padded}  {SIDE_BORDER}")
    
    # Divider
    lines.append(MIDDLE_BORDER)
    
    # Goose section header
    lines.append(f"{SIDE_BORDER}  {'YOUR GUIDE THROUGH THE MYSTERIES (RELUCTANTLY)':^54} {SIDE_BORDER}")
    lines.append(MIDDLE_BORDER)
    
    # Add the sassy goose ASCII art (centered)
    goose_lines = GRUMPY_GOOSE.strip().split('\n')
    for g_line in goose_lines:
        # Center the goose art within the border
        centered = g_line.center(54)
        lines.append(f"{SIDE_BORDER}  {centered[:52]}  {SIDE_BORDER}")
    
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
