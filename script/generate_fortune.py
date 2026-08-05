#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Wise fortunes from the mystical goose oracle
FORTUNES = [
    "The path ahead is clear, but only for those who dare to flap their wings with confidence.",
    "A challenge approaches, but like a sassy goose, you shall waddle through it with style.",
    "Wisdom comes not from knowing all the answers, but from asking the right honks.",
    "The universe conspires to help you, much like how geese help each other during migration.",
    "Patience is your greatest ally today. Even the sages take time to preen their feathers.",
    "An unexpected opportunity will appear - keep your eyes on the horizon, not your feet.",
    "The answers you seek are closer than you think, like a goose to its pond.",
    "Trust your instincts today. Your inner goose knows the way.",
    "A friend will offer unexpected wisdom. Listen as carefully as a goose listening for danger.",
    "The stars align in your favor, but remember: even geese must learn to fly.",
]

# ASCII art of a sassy goose
GOOSE_ART = """
  __      __
 /'\\    /'\\
( o)  (o )
 \\__/  \\__/
  ||    ||
  ||    ||
 _||____||_
(__________)
"""

# Alternative sassy goose poses
GOOSE_ARTS = [
    GOOSE_ART,
    """
   __      __
  /  \\  /  \\
 ( o )  (o )
  \\__/  \\__/
   ||    ||
   ||    ||
 _ ||____|| _
( __________)
""",
    """
  __      __
 /  \\  /  \\
( o)  (o )
  \\__/  \\__/
   ||    ||
   ||    ||
 _ ||____||_
( __________)
"""
]

def generate_fortune():
    """Generate a random wise fortune."""
    return random.choice(FORTUNES)

def get_goose_art():
    """Get a random sassy goose ASCII art."""
    return random.choice(GOOSE_ARTS)

def create_fortune_display():
    """Create the full fortune display with border, goose, and fortune."""
    fortune = generate_fortune()
    goose = get_goose_art()
    
    # Calculate the width needed for the border
    lines = goose.split('\n') + [''] + fortune.split('\n')
    max_width = max(len(line) for line in lines) + 4  # Add padding
    
    # Create the border
    border_top = '╔' + '═' * max_width + '╗'
    border_bottom = '╚' + '═' * max_width + '╝'
    border_side = '║'
    
    # Build the display
    display_lines = []
    display_lines.append(border_top)
    
    # Add goose art with side borders
    for line in goose.split('\n'):
        if line:
            padded_line = line.ljust(max_width - 2)
            display_lines.append(f"{border_side} {padded_line} {border_side}")
        else:
            display_lines.append(f"{border_side} {' ' * max_width} {border_side}")
    
    # Add divider
    divider = '║' + '─' * max_width + '║'
    display_lines.append(divider)
    
    # Add fortune with side borders
    for line in fortune.split('\n'):
        padded_line = line.ljust(max_width - 2)
        display_lines.append(f"{border_side} {padded_line} {border_side}")
    
    display_lines.append(border_bottom)
    
    return '\n'.join(display_lines)

def main():
    """Main function to generate and save the fortune."""
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Add timestamp header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = f"# 🦢 Daily Fortune from the Sassy Goose Oracle 🦢\n\n"
    output += f"*Generated on: {timestamp}*\n\n"
    output += f"```\n{fortune_display}\n```\n"
    
    # Handle existing fortune.md file
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp_suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp_suffix}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write the new fortune file
    with open(fortune_path, 'w') as f:
        f.write(output)
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
