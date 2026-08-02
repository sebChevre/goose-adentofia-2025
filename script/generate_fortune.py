#!/usr/bin/env python3
"""
Grumpy Fortune Teller - Generates sassy fortunes with ASCII art
"""

import os
import random
from datetime import datetime

# Grumpy fortune messages
FORTUNES = [
    "Oh, great. Another human seeking wisdom. Fine. Your day will be... tolerable. Barely.",
    "I could tell you your fortune, but honestly, you probably won't listen anyway. Typical.",
    "Your future involves more coffee and less talking. Take notes, if you must.",
    "Someone will annoy you today. Spoiler: It's you. Get over it.",
    "A surprise awaits you. It's probably minor. Don't get excited.",
    "You'll make a decision today. It'll be wrong. But hey, that's growth, right?",
    "The stars say you're stubborn. No, wait, that's just my personality. Close enough.",
    "Money will come your way. Probably a refund you forgot about. Thrilling.",
    "Love is in the air. Unfortunately, it's not for you. Try again never.",
    "You'll have a moment of clarity. It'll be brief and mostly useless.",
    "Today's forecast: 90% chance of sarcasm, 10% chance of actual helpfulness.",
    "Your lucky numbers are 4, 8, 15, 16, 23, 42. No, I'm not telling you why.",
    "A friend will surprise you. It'll be awkward. Everyone will pretend it's fine.",
    "The universe has a plan. It involves you being slightly less annoying. Progress!",
    "Something broken will be fixed. You'll still complain about it. Classic.",
]

# Sassy goose ASCII art
SASSY_GOOSE = """
   __      __
  /  \\    /  \\
 |    \\/\\/    |
 |  >  o_o  <  |
 |    /   \\    |
  \\  \\     /  /
   \\  \\___/  /
    \\_______/
      |   |
     /|   |\\
    / |   | \\
   |  |   |  |
   |  |   |  |
   |  |   |  |
   |__|   |__|
"""

# Border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
MIDDLE_BORDER = "║" + " " * 58 + "║"
DIVIDER = "╟" + "─" * 58 + "╢"


def generate_fortune():
    """Generate a random grumpy fortune."""
    return random.choice(FORTUNES)


def format_output(fortune):
    """Format the fortune with ASCII art and border."""
    lines = []
    
    # Top border
    lines.append(TOP_BORDER)
    
    # Title line
    lines.append("║  🦆 GRUMPY FORTUNE TELLER - " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " * 6 + "║")
    lines.append(MIDDLE_BORDER)
    
    # Sassy goose
    goose_lines = SASSY_GOOSE.strip().split('\n')
    for goose_line in goose_lines:
        # Center the goose art
        padded_line = goose_line.center(58)
        lines.append("║ " + padded_line + " ║")
    
    lines.append(MIDDLE_BORDER)
    
    # Divider between goose and fortune
    lines.append(DIVIDER)
    lines.append(MIDDLE_BORDER)
    
    # Fortune text - wrap if needed
    fortune_lines = []
    words = fortune.split()
    current_line = "║  "
    
    for word in words:
        if len(current_line) + len(word) + 1 > 56:
            fortune_lines.append(current_line + " ║")
            current_line = "║  " + word
        else:
            if current_line == "║  ":
                current_line += word
            else:
                current_line += " " + word
    
    if current_line != "║  ":
        fortune_lines.append(current_line + " ║")
    
    # Add padding lines if fortune is short
    while len(fortune_lines) < 4:
        fortune_lines.insert(0, MIDDLE_BORDER)
    
    lines.extend(fortune_lines)
    
    lines.append(MIDDLE_BORDER)
    
    # Bottom border
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def main():
    """Main function to generate and save fortune."""
    # Output file path
    output_path = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(output_path):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(output_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate fortune
    fortune = generate_fortune()
    
    # Format output
    output = format_output(fortune)
    
    # Write to markdown file
    with open(output_path, 'w') as f:
        f.write("# 🦆 Grumpy Fortune\n\n")
        f.write("```text\n")
        f.write(output)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {output_path}")
    print("\n" + output)


if __name__ == "__main__":
    main()
