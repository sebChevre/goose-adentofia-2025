#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Wise fortune messages
FORTUNES = [
    "The path you seek is hidden in plain sight. Trust your instincts, for they are your greatest guide.",
    "A challenge awaits, but within it lies the seed of your greatest triumph.",
    "The wisdom you seek comes from within. Listen to the quiet voice that speaks truth.",
    "Three doors stand before you. The one you hesitate at holds the key to your destiny.",
    "An old friend will bring news that changes everything. Keep your heart open.",
    "The stars align in your favor, but only if you dare to take the first step.",
    "Patience is not your virtue today, but courage is. Act when the moment is right.",
    "A treasure you've overlooked holds more value than gold. Look with fresh eyes.",
    "The journey of a thousand miles begins with a single, deliberate step.",
    "What you seek is also seeking you. Stay true to your purpose.",
]

# Sassy Goose ASCII Art
GOOSE_ART = """
     __      __
    /  \\    /  \\
   |    \\/\/    |
   |   O      O |
   |     <      |
   |   \\____/   |
    \\  \\    /  /
     \\  \\/\\/  /
      \\______/
     _/      \\_
    |          |
    |  SASSY   |
    \\__________/
"""

# Fortune border character
BORDER_CHAR = "═"
SIDE_CHAR = "║"


def generate_fortune():
    """Generate a wise fortune from the mystical goose oracle."""
    return random.choice(FORTUNES)


def create_fortune_display(fortune):
    """Create a visually appealing fortune display with ASCII art."""
    width = 60
    
    # Create the border
    top_border = BORDER_CHAR * width
    bottom_border = BORDER_CHAR * width
    
    # Format the fortune text to fit within the border
    lines = fortune.split('\n')
    formatted_lines = []
    for line in lines:
        # Split long lines
        while len(line) > width - 4:
            formatted_lines.append(f"{SIDE_CHAR}  {line[:width-6]}  {SIDE_CHAR}")
            line = line[width-6:]
        formatted_lines.append(f"{SIDE_CHAR}  {line.ljust(width-6)}  {SIDE_CHAR}")
    
    # Create the divider
    divider = f"{SIDE_CHAR}{BORDER_CHAR * (width - 2)}{SIDE_CHAR}"
    
    # Build the complete display
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    display_lines = [
        top_border,
        f"{SIDE_CHAR}{center_text('🔮 WISE FORTUNE ORACLE 🔮', width)}{SIDE_CHAR}",
        f"{SIDE_CHAR}{center_text(f'Generated: {timestamp}', width)}{SIDE_CHAR}",
        f"{SIDE_CHAR}{center_text('~' * 40, width)}{SIDE_CHAR}",
        f"{SIDE_CHAR}{center_text(GOOSE_ART, width)}{SIDE_CHAR}",
        divider,
        f"{SIDE_CHAR}{center_text('YOUR FORTUNE AWAITS...', width)}{SIDE_CHAR}",
        f"{SIDE_CHAR}{center_text('~' * 40, width)}{SIDE_CHAR}",
    ]
    
    # Add fortune lines
    for line in formatted_lines:
        display_lines.append(line)
    
    display_lines.extend([
        f"{SIDE_CHAR}{center_text('~' * 40, width)}{SIDE_CHAR}",
        f"{SIDE_CHAR}{center_text('May wisdom guide your path 🌟', width)}{SIDE_CHAR}",
        bottom_border,
    ])
    
    return '\n'.join(display_lines)


def center_text(text, width):
    """Center text within a given width."""
    lines = text.split('\n')
    centered_lines = []
    for line in lines:
        if len(line) < width:
            padding = (width - len(line)) // 2
            centered_lines.append(' ' * padding + line + ' ' * (width - len(line) - padding))
        else:
            centered_lines.append(line[:width])
    return '\n'.join(centered_lines)


def main():
    """Main function to generate and save the fortune."""
    # Define paths
    current_dir = os.getcwd()
    fortune_file = os.path.join(current_dir, 'fortune.md')
    old_folder = os.path.join(current_dir, 'old')
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        old_file = os.path.join(old_folder, f'fortune_{datetime.now().strftime("%Y%m%d_%H%M%S")}.md')
        os.rename(fortune_file, old_file)
        print(f"Previous fortune moved to: {old_file}")
    
    # Generate the fortune
    fortune = generate_fortune()
    
    # Create the display
    display = create_fortune_display(fortune)
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(display)
        f.write('\n')
    
    print("Fortune generated successfully!")
    print(f"Output saved to: {fortune_file}")
    print("\n" + display)


if __name__ == "__main__":
    main()
