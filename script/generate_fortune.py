#!/usr/bin/env python3
"""
Generate a grumpy fortune teller's prediction with ASCII art.
"""

import os
import random
from datetime import datetime

# Grumpy fortunes
FORTUNES = [
    "Ugh, fine. You'll find what you're looking for... if you stop bothering me.",
    "Honestly? Your future is as predictable as a goose honking at 6 AM.",
    "Oh wonderful, another human seeking wisdom. You'll succeed... eventually.",
    "Hmph. The stars say you'll do something sensible for once. Don't let it happen again.",
    "Fine, fine. Luck is coming your way, but I'm not holding my breath.",
    "Ugh, the universe is loud today. You'll avoid disaster... barely.",
    "Wonderful, you want a fortune? You'll learn something useful. Shocking, I know.",
    "Hah! As if I care. But fine, good things are coming. Don't tell anyone I said that.",
    "Oh joy, another reading. You'll overcome obstacles... mostly because I'm tired of yours.",
    "The cosmos whisper... you'll be just fine. Now leave me alone."
]

# Sassy goose ASCII art
GOOSE_ART = """
   __
  /  \\
 |    |
 |    |
  \\  /
   \\/
   ||
   ||
  /  \\
 |    |
 |    |
  \\__/
"""

# Alternative sassy goose variations
GOOSE_ARTS = [
    GOOSE_ART,
    """
   __
  /  \\
 | o o|
 |  ^ |
  \\__/
   ||
   ||
  /  \\
 |    |
 |    |
  \\__/
""",
    """
   __
  /  \\
 |    |
 | >_<|
  \\  /
   \\/
   ||
   ||
  /  \\
 |    |
 |    |
  \\__/
"""
]

def generate_fortune():
    """Generate a random grumpy fortune."""
    return random.choice(FORTUNES)

def get_sassy_goose():
    """Get a random sassy goose ASCII art."""
    return random.choice(GOOSE_ARTS)

def create_fortune_display():
    """Create the full fortune display with border, goose, and fortune."""
    fortune = generate_fortune()
    goose = get_sassy_goose()
    
    # Get timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Calculate border width based on content
    lines = goose.split('\n') + [''] + fortune.split('\n')
    max_width = max(len(line) for line in lines) + 4
    
    # Create the display
    border = '+' + '-' * max_width + '+'
    empty_border = '|' + ' ' * max_width + '|'
    
    display = []
    display.append(border)
    display.append(f'| Fortune Teller - {timestamp} ' + ' ' * (max_width - 28 - len(timestamp)) + '|')
    display.append(border)
    display.append(empty_border)
    
    # Add goose art centered
    for line in goose.split('\n'):
        padding = (max_width - len(line) - 2) // 2
        display.append(f'| {" " * padding}{line}{" " * (max_width - len(line) - 2 - padding)} |')
    
    display.append(empty_border)
    display.append('|' + '-' * (max_width - 2) + '|')  # Divider
    display.append(empty_border)
    
    # Add fortune text centered
    for line in fortune.split('\n'):
        padding = (max_width - len(line) - 2) // 2
        display.append(f'| {" " * padding}{line}{" " * (max_width - len(line) - 2 - padding)} |')
    
    display.append(empty_border)
    display.append('|' + ' ' * (max_width - 2) + '|')
    display.append('|  "A grumpy fortune teller knows best..." ' + ' ' * (max_width - 38) + '|')
    display.append(empty_border)
    display.append(border)
    
    return '\n'.join(display)

def main():
    """Main function to generate and save fortune."""
    fortune_content = create_fortune_display()
    
    # Check if fortune.md exists
    fortune_path = 'fortune.md'
    old_dir = 'old'
    
    if os.path.exists(fortune_path):
        # Create old directory if it doesn't exist
        os.makedirs(old_dir, exist_ok=True)
        
        # Move existing file to old directory with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_path = os.path.join(old_dir, f'fortune_{timestamp}.md')
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write new fortune to file
    with open(fortune_path, 'w') as f:
        f.write(fortune_content)
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + fortune_content)

if __name__ == "__main__":
    main()
