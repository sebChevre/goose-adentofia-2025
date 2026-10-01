#!/usr/bin/env python3
"""
Fortune Generator - An introspective fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Introspective fortune messages from a mystical fortune teller
FORTUNES = [
    "The answers you seek dwell within the quiet corners of your soul. Listen to what your heart whispers when the world grows still.",
    "A moment of doubt you're experiencing is not weakness—it's the fertile soil where wisdom takes root.",
    "The path ahead is not about finding yourself, but about creating yourself with each deliberate choice.",
    "What feels like an ending is merely the universe making space for something more aligned with your truth.",
    "The courage you need is not the absence of fear, but the willingness to move forward while trembling.",
    "Your greatest strength lies not in what you've conquered, but in what you've learned to release.",
    "The reflection you see in still waters reveals more than any mirror ever could. Trust what you see.",
    "A question you've been avoiding holds the key to a freedom you've been craving.",
    "The journey inward is the only journey that truly matters. All outward paths are mere footnotes.",
    "You are not broken—you are becoming. The cracks are where your light learns to shine.",
]

# Sassy Goose ASCII Art - looking judgmental but wise
GOOSE_ART = """
      __      __
     /  \\____/  \\
    |  o      o  |
    |     <      |    *squints judgmentally*
    |   \\____/   |
     \\  \\    /  /
      \\  \\/\\/  /
       \\______/
      _/      \\_
     |  SASSY   |
     |   GOOSE  |
     \\__________/
       |      |
       |      |    \"HONK if you get it\"
       |      |
"""

# Border characters for the frame
TOP_BOTTOM = "╔" + "═" * 58 + "╗"
MIDDLE = "╠" + "═" * 58 + "╣"
BOTTOM = "╚" + "═" * 58 + "╝"
SIDE = "║"


def generate_fortune():
    """Generate an introspective fortune from the mystical oracle."""
    return random.choice(FORTUNES)


def create_fortune_display(fortune):
    """Create a visually appealing fortune display with ASCII art and border."""
    width = 60
    
    # Format the fortune text to fit within the border
    fortune_lines = []
    words = fortune.split()
    current_line = ""
    
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        if len(test_line) <= 54:
            current_line = test_line
        else:
            if current_line:
                fortune_lines.append(current_line)
            current_line = word
    
    if current_line:
        fortune_lines.append(current_line)
    
    # Build the complete display
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    display_lines = [
        TOP_BOTTOM,
        f"{SIDE}{'🔮 THE INTROSPECTIVE ORACLE 🔮':^56}{SIDE}",
        f"{SIDE}{'~' * 56}{SIDE}",
        f"{SIDE}{'Generated: ' + timestamp:^56}{SIDE}",
        f"{SIDE}{'~' * 56}{SIDE}",
        f"{SIDE}{'':^56}{SIDE}",
        f"{SIDE}{'YOUR FORTUNE:':^56}{SIDE}",
        f"{SIDE}{'':^56}{SIDE}",
    ]
    
    # Add fortune lines centered
    for line in fortune_lines:
        display_lines.append(f"{SIDE} {line:^54} {SIDE}")
    
    display_lines.extend([
        f"{SIDE}{'':^56}{SIDE}",
        MIDDLE,
        f"{SIDE}{'':^56}{SIDE}",
        f"{SIDE}{'THE SASSY GOOSE GUIDANCE:':^56}{SIDE}",
        f"{SIDE}{'':^56}{SIDE}",
    ])
    
    # Add the goose ASCII art (centered within the border)
    goose_lines = GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        # Center each line of the goose art
        line_len = len(line)
        padding = (54 - line_len) // 2
        if padding >= 0:
            display_lines.append(f"{SIDE} {' ' * padding}{line}{' ' * (54 - line_len - padding)} {SIDE}")
        else:
            display_lines.append(f"{SIDE} {line[:54]} {SIDE}")
    
    display_lines.extend([
        f"{SIDE}{'':^56}{SIDE}",
        f"{SIDE}{'~' * 56}{SIDE}",
        f"{SIDE}{'May wisdom find you where you stand 🌙':^56}{SIDE}",
        BOTTOM,
    ])
    
    return '\n'.join(display_lines)


def main():
    """Main function to generate and save the fortune."""
    # Define paths
    current_dir = os.getcwd()
    fortune_file = os.path.join(current_dir, 'fortune.md')
    old_folder = os.path.join(current_dir, 'old')
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        old_filename = f'fortune_{datetime.now().strftime("%Y%m%d_%H%M%S")}.md'
        old_file = os.path.join(old_folder, old_filename)
        os.rename(fortune_file, old_file)
        print(f"✓ Previous fortune archived to: {old_file}")
    
    # Generate the fortune
    fortune = generate_fortune()
    
    # Create the display with border, fortune above goose, and divider
    display = create_fortune_display(fortune)
    
    # Write to fortune.md as markdown code block
    with open(fortune_file, 'w') as f:
        f.write("# 📜 Your Introspective Fortune\n\n")
        f.write("```text\n")
        f.write(display)
        f.write("\n```\n")
    
    print("✨ Fortune generated successfully!")
    print(f"📁 Output saved to: {fortune_file}")
    print("\n" + display)


if __name__ == "__main__":
    main()
