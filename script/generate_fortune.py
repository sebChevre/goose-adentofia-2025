#!/usr/bin/env python3
"""
Fortune Generator - A fictional fortune teller with an introspective mood
Generates fortunes with ASCII art of a sassy goose
"""

import os
import random
from datetime import datetime

# Fortune messages with introspective themes
FORTUNES = [
    "The path you seek is not found in the distance, but in the quiet moments between your thoughts.",
    "What you fear losing is already within you; what you seek awaits in your own reflection.",
    "The answers you crave have been whispering in your heart all along—you simply need to listen.",
    "A choice approaches. Trust not the noise of others, but the stillness within.",
    "The journey ahead will teach you what you already know but have forgotten to believe.",
    "Your greatest strength lies in the vulnerability you've been hiding from yourself.",
    "The change you resist is the very transformation your soul has been preparing for.",
    "In the silence of self-discovery, you will find the voice you've been waiting to hear.",
    "The mirror shows not your face, but the story you tell yourself about who you are.",
    "What feels like an ending is merely the universe making room for your becoming."
]

# Sassy goose ASCII art (compact version)
SASSY_GOOSE = """
   .--.
  |o_o |
  |:_/ |  "Oh, another seeker of wisdom? How... predictable."
 /   \\ \\
|     | |
|     | |
|     | |
\\     / /
 `---'
"""

def generate_fortune():
    """Generate a random introspective fortune."""
    return random.choice(FORTUNES)

def create_fortune_display(fortune):
    """Create the full fortune display with ASCII art and border."""
    width = 70
    
    # Top border
    border_line = "+" + "-" * (width - 2) + "+"
    
    # Title line
    title = "✨ THE CRYSTAL BALL OF SELF-DISCOVERY ✨"
    title_line = f"| {title:^{width-2}} |"
    
    # Date line
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_line = f"| {date:^{width-2}} |"
    
    # Fortune section
    fortune_lines = []
    words = fortune.split()
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += " " + word if current_line else word
        else:
            fortune_lines.append(f"| {current_line:<{width-2}} |")
            current_line = word
    if current_line:
        fortune_lines.append(f"| {current_line:<{width-2}} |")
    
    # Divider
    divider = f"| {'=' * (width - 2)} |"
    
    # Goose section
    goose_lines = SASSY_GOOSE.split('\n')
    
    # Build the display
    display = []
    display.append(border_line)
    display.append(title_line)
    display.append(date_line)
    display.append(border_line)
    display.append("")
    display.append("🔮 YOUR INTROSPECTIVE FORTUNE 🔮")
    display.append("")
    
    for line in fortune_lines:
        display.append(line)
    
    display.append("")
    display.append(divider)
    display.append("")
    display.append("🪿 THE SASSY GOOSE SAYS:")
    display.append("")
    
    for line in goose_lines:
        if line.strip():
            display.append(f"| {line:<{width-2}} |")
        else:
            display.append(f"| {' ' * (width - 2)} |")
    
    display.append(border_line)
    display.append("")
    display.append("Remember: The only true wisdom is knowing you know nothing.")
    display.append("                              — Ancient Goose Philosophy")
    display.append(border_line)
    
    return '\n'.join(display)

def main():
    """Main function to generate and save the fortune."""
    # Current working directory
    cwd = os.getcwd()
    fortune_file = os.path.join(cwd, "fortune.md")
    old_folder = os.path.join(cwd, "old")
    
    # Check if fortune.md already exists
    if os.path.exists(fortune_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_file)
        print(f"Previous fortune.md moved to: {old_file}")
    
    # Generate the fortune
    fortune = generate_fortune()
    display = create_fortune_display(fortune)
    
    # Write to markdown file
    with open(fortune_file, 'w', encoding='utf-8') as f:
        f.write(display)
        f.write('\n')
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + "=" * 50)
    print(display)
    print("=" * 50)

if __name__ == "__main__":
    main()
