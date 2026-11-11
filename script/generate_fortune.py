#!/usr/bin/env python3
"""
Fortune Generator - A Poetic Fortune Teller with a Sassy Goose
Generates fortunes with ASCII art and writes to fortune.md
"""

import os
import random
from datetime import datetime

# Poetic fortune messages
FORTUNES = [
    "In twilight's gentle whisper, where dreams and reality dance,\nYou shall find courage in the most unexpected of places.",
    "The stars align with mischief in their eyes,\nA journey awaits that will surprise your weary eyes.",
    "Like dew upon the morning rose, new opportunities bloom,\nEmbrace the change that comes with life's sweet perfume.",
    "A secret path reveals itself to those who dare to look,\nYour destiny is written in the stars, not in any book.",
    "The winds of fortune blow in unexpected directions,\nYet your heart knows the way to your true attractions.",
    "What you seek has been seeking you all along,\nLike a melody that lingers in a forgotten song.",
    "The moon bears witness to your hidden desires,\nYour dreams shall rise like fire, like phoenix fires.",
    "In the quiet moments when the world falls still,\nYou will discover the strength of your own will.",
    "A friend you've yet to meet holds a treasure in their hand,\nTogether you shall build a bridge across the land.",
    "The river of time flows onward, never turning back,\nYet within its currents lies your lucky track."
]

# Sassy goose ASCII art
GOOSE_ARTS = [
    r"""
      __
     /  \
    |    |
    |    |     _
    |    |    / \
    |    |   |   |
    |    |   |   |
    |    |   |   |
    |    |   |   |
    |    |   |   |
    |    |   |   |
    \____/   \___/
    """,
    r"""
      __
     /  \
    |    |
    |    |     __
    |    |    /  \
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    \____/   \____/
    """,
    r"""
      __
     /  \
    |    |
    |    |     ~~
    |    |    /  \
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    \____/   \____/
    """,
    r"""
      __
     /  \
    |    |
    |    |     ><
    |    |    /  \
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    \____/   \____/
    """,
    r"""
      __
     /  \
    |    |
    |    |     oO
    |    |    /  \
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    |    |   |    |
    \____/   \____/
    """
]

# Border character
BORDER_CHAR = "═"
SIDE_BORDER = "║"

def generate_border(width):
    """Generate top and bottom border."""
    return BORDER_CHAR * width

def generate_sassy_goose():
    """Return a random sassy goose ASCII art."""
    return random.choice(GOOSE_ARTS)

def generate_fortune():
    """Return a random poetic fortune."""
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the complete fortune display with border, fortune, divider, and goose."""
    fortune = generate_fortune()
    goose = generate_sassy_goose()
    
    # Calculate width needed (fortune lines + border padding)
    lines = fortune.split('\n')
    max_fortune_width = max(len(line) for line in lines)
    goose_lines = goose.split('\n')
    max_goose_width = max(len(line) for line in goose_lines)
    
    content_width = max(max_fortune_width, max_goose_width) + 4  # Padding
    border_width = content_width + 2
    
    # Build the display
    display = []
    
    # Top border
    display.append("╔" + BORDER_CHAR * (border_width - 2) + "╗")
    
    # Fortune section
    display.append(f"{SIDE_BORDER}  🌙  THE SASSY GOOSE FORTUNE  🌙  {SIDE_BORDER}")
    display.append(f"{SIDE_BORDER}{' ' * (border_width - 4)}{SIDE_BORDER}")
    
    for line in lines:
        padded_line = line.ljust(max_fortune_width)
        display.append(f"{SIDE_BORDER}  {padded_line}  {SIDE_BORDER}")
    
    # Divider
    display.append(f"{SIDE_BORDER}{' ' * (border_width - 4)}{SIDE_BORDER}")
    display.append(f"{SIDE_BORDER}{'─' * (border_width - 4)}{SIDE_BORDER}")
    display.append(f"{SIDE_BORDER}{' ' * (border_width - 4)}{SIDE_BORDER}")
    
    # Goose section
    for line in goose_lines:
        padded_line = line.ljust(max_goose_width)
        display.append(f"{SIDE_BORDER}  {padded_line}  {SIDE_BORDER}")
    
    # Bottom border
    display.append(f"{SIDE_BORDER}{' ' * (border_width - 4)}{SIDE_BORDER}")
    display.append(f"{SIDE_BORDER}  Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}  {SIDE_BORDER}")
    display.append("╚" + BORDER_CHAR * (border_width - 2) + "╝")
    
    return '\n'.join(display)

def backup_existing_fortune():
    """Move existing fortune.md to /old folder if it exists."""
    current_dir = os.getcwd()
    fortune_path = os.path.join(current_dir, 'fortune.md')
    old_dir = os.path.join(current_dir, 'old')
    
    if os.path.exists(fortune_path):
        # Create old directory if it doesn't exist
        os.makedirs(old_dir, exist_ok=True)
        
        # Generate timestamp for backup filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f'fortune_{timestamp}.md'
        backup_path = os.path.join(old_dir, backup_name)
        
        # Move the file
        os.rename(fortune_path, backup_path)
        print(f"Backed up existing fortune.md to: {backup_path}")

def save_fortune(content, filename='fortune.md'):
    """Save the fortune display to a markdown file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fortune saved to: {filename}")

def main():
    """Main function to generate and save the fortune."""
    print("🔮 Consulting the Sassy Goose Fortune Teller... 🔮")
    print()
    
    # Backup existing fortune if present
    backup_existing_fortune()
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Save to fortune.md
    save_fortune(fortune_display)
    
    # Also print to console
    print()
    print(fortune_display)
    print()
    print("✨ May your fortune bring you joy! ✨")

if __name__ == "__main__":
    main()
