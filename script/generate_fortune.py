#!/usr/bin/env python3
"""
Sarcastic Fortune Teller - Generates sassy fortunes from a judgmental goose.
"""

import os
import random
from datetime import datetime

# Sarcastic fortunes
FORTUNES = [
    "Ah yes, your future looks... well, let's just say 'interesting' is one word for it.",
    "The stars say you'll make a decision today. Probably the wrong one, but hey, confidence!",
    "I see great things in your future. By 'great,' I mean 'memorably disastrous.'",
    "Your lucky numbers are 0, 0, 0, 0, 0, and 'have you tried turning it off and on?'",
    "The universe has a plan for you. Unfortunately, it involves more paperwork.",
    "A mysterious stranger will enter your life. They'll probably disappoint you.",
    "Your future self is judging your current choices. Hard.",
    "The stars align! Too bad you'll still forget to drink water today.",
    "Love is in the air. Or maybe it's just allergies. Let's go with allergies.",
    "You will achieve your dreams! Eventually. After several 'learning experiences.'",
    "The cosmos whisper your name. They're mostly gossiping, but still.",
    "A golden opportunity awaits! *cough* It's probably a scam.",
    "Your charisma is off the charts! Shame about your decision-making skills.",
    "The future holds adventure! By adventure, I mean 'unexpected inconveniences.'",
    "You'll meet someone special. They'll special in annoying you, mostly.",
]

# Sassy goose ASCII art
GOOSE_ART = """
   __
  /  \\
 | o o|
 |  ^ |  *judgmental squint*
 | \\_/ |
  \\___/
   | |
   | |
  /   \\
 /     \\
|       |
|  ___  |
| |   | |
| |___| |
|_______|
"""

# Border characters
TOP_BORDER = "╔" + "═" * 68 + "╗"
BOTTOM_BORDER = "╚" + "═" * 68 + "╝"
SIDE_BORDER = "║"
DIVIDER = "╟" + "─" * 68 + "╢"


def generate_fortune():
    """Generate a sarcastic fortune with ASCII art."""
    fortune = random.choice(FORTUNES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the fortune card
    lines = []
    lines.append(TOP_BORDER)
    lines.append(f"{SIDE_BORDER}{'🔮 SARCASTIC FORTUNE TELLER 🔮':^66}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{'Generated on: ' + timestamp:^66}{SIDE_BORDER}")
    lines.append(SIDE_BORDER + " " * 66 + SIDE_BORDER)
    lines.append(DIVIDER)
    lines.append(SIDE_BORDER + " " * 66 + SIDE_BORDER)
    
    # Add fortune text (wrapped)
    fortune_lines = []
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 64:
            current_line += (" " if current_line else "") + word
        else:
            fortune_lines.append(current_line)
            current_line = word
    if current_line:
        fortune_lines.append(current_line)
    
    for line in fortune_lines:
        lines.append(f"{SIDE_BORDER} {line:^64}{SIDE_BORDER}")
    
    lines.append(SIDE_BORDER + " " * 66 + SIDE_BORDER)
    lines.append(DIVIDER)
    
    # Add goose art (centered)
    for line in GOOSE_ART.split('\n'):
        if line.strip():
            lines.append(f"{SIDE_BORDER} {line:^64}{SIDE_BORDER}")
        else:
            lines.append(f"{SIDE_BORDER}{' ' * 66}{SIDE_BORDER}")
    
    lines.append(SIDE_BORDER + " " * 66 + SIDE_BORDER)
    lines.append(DIVIDER)
    quote_text = "💀 \"Trust me, I'm a goose.\" 💀"
    lines.append(f"{SIDE_BORDER}{quote_text:^66}{SIDE_BORDER}")
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def main():
    """Main function to generate and save fortune."""
    # Generate the fortune
    fortune_content = generate_fortune()
    
    # Check if fortune.md exists and move it to /old folder
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
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write new fortune to fortune.md
    with open(fortune_path, 'w') as f:
        f.write(fortune_content)
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + fortune_content)


if __name__ == "__main__":
    main()
