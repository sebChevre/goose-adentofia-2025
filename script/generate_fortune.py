#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose companion
"""

import os
import random
from datetime import datetime

# Wise fortunes from the mystical fortune teller
WISE_FORTUNES = [
    "The path you seek is not ahead, but within. Trust your intuition.",
    "Wisdom comes not from knowing all answers, but from asking better questions.",
    "A challenge awaits, but you possess the strength to transform it into opportunity.",
    "The seeds you plant today will bear fruit in seasons yet to come.",
    "Patience is the companion of wisdom. Your time will come.",
    "The universe whispers secrets to those who listen with their hearts.",
    "Your greatest strength lies in your ability to adapt and grow.",
    "The journey of a thousand miles begins with a single step forward.",
    "What you seek is also seeking you. Stay open to unexpected paths.",
    "The wisdom you need is already written in the stars of your own experience.",
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
     (  )
     /\\
    /  \\
   /    \\
  /      \\
 /   __   \\
(   /  \\   )
 \\ /    \\ /
  (      )
   \\    /
    \\  /
     \\/
    _||_
   (____)
   /|  |\\
  / |  | \\
 /  |  |  \\
    |__|
   (____)
  _/    \\_
 (  o  o  )
 (    <   )
  \\  ____/
   \\____/
"""

def get_fortune():
    """Select a random wise fortune."""
    return random.choice(WISE_FORTUNES)

def create_border(width):
    """Create an ASCII border of specified width."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    return top_bottom, middle

def format_fortune_output(fortune):
    """Format the fortune with ASCII art, borders, and dividers."""
    # Get the goose art and fortune
    goose = GOOSE_ART.strip()
    wise_fortune = fortune.strip()
    
    # Calculate dimensions
    lines = goose.split('\n') + [''] + ['『 WISE FORTUNE 『'] + [''] + wise_fortune.split('\n')
    max_width = max(len(line) for line in lines) + 4  # Add padding
    
    # Create border components
    top, middle = create_border(max_width)
    bottom = "╚" + "═" * (max_width - 2) + "╝"
    
    # Build the output
    output_lines = []
    output_lines.append(top)
    
    # Add goose art with left padding
    for line in goose.split('\n'):
        output_lines.append("║  " + line + " " * (max_width - 6 - len(line)) + "║")
    
    # Add divider
    output_lines.append("║" + "─" * (max_width - 2) + "║")
    
    # Add fortune title
    title = "『 WISE FORTUNE 『"
    output_lines.append("║  " + title.center(max_width - 6) + "║")
    
    # Add another divider
    output_lines.append("║" + "─" * (max_width - 2) + "║")
    
    # Add fortune text
    for line in wise_fortune.split('\n'):
        output_lines.append("║  " + line.center(max_width - 6) + "║")
    
    # Add timestamp
    timestamp = f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    output_lines.append("║  " + timestamp.center(max_width - 6) + "║")
    
    output_lines.append(bottom)
    
    return '\n'.join(output_lines)

def main():
    """Main function to generate and save the fortune."""
    # Define paths
    current_dir = os.getcwd()
    fortune_file = os.path.join(current_dir, 'fortune.md')
    old_folder = os.path.join(current_dir, 'old')
    
    # Ensure old folder exists
    os.makedirs(old_folder, exist_ok=True)
    
    # Move existing fortune.md to old folder if it exists
    if os.path.exists(fortune_file):
        import shutil
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_file = os.path.join(old_folder, f'fortune_{timestamp}.md')
        shutil.move(fortune_file, old_file)
        print(f"Moved existing fortune.md to: {old_file}")
    
    # Generate the fortune
    fortune = get_fortune()
    output = format_fortune_output(fortune)
    
    # Write to fortune.md
    with open(fortune_file, 'w', encoding='utf-8') as f:
        f.write(output)
        f.write('\n')
    
    print("Fortune generated successfully!")
    print(f"Output saved to: {fortune_file}")
    print("\n" + output)

if __name__ == "__main__":
    main()
