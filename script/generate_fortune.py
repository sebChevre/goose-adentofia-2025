#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective musings.
Generates fortunes with ASCII art and saves to fortune.md.
"""

import os
import random
from datetime import datetime

# Fortune messages with introspective, slightly sassy mood
FORTUNES = [
    "The path you seek is not ahead, but within. Stop looking outward and start looking inward.",
    "Your doubts are merely echoes of your own potential. Listen closer.",
    "A decision you've been avoiding will reveal itself when you stop running from yourself.",
    "The answers you crave are already whispering in your mind. You're just too noisy to hear them.",
    "Patience is not waiting—it's the quiet courage to trust your own timing.",
    "What you fear most is the shadow of what you're capable of becoming.",
    "The universe is not conspiring against you; you're just overthinking everything.",
    "Your greatest strength is also your greatest vulnerability. Embrace the paradox.",
    "The change you desire begins the moment you stop waiting for permission.",
    "Silence is where wisdom lives. Your inner goose knows more than you think.",
    "You are not lost—you are exactly where you need to be to find yourself.",
    "The mirror reflects not who you are, but who you're afraid to become.",
    "Your intuition is louder than your excuses. Which will you listen to?",
    "The journey of a thousand miles begins with a single step... or a very dramatic honk.",
    "What you seek is seeking you. The question is: are you ready to answer?",
]

# Sassy Goose ASCII Art
GOOSE_ART = """
         __
        /  \\
       |    |
       |    |
       \\____/
       /    \\
      /      \\
     /        \\
    |  O    O  |
    |     <    |    *hONK*
    \\   __    /    I'm judging you.
     \\  ||   /
      \\ ||  /
       \\|| /
        \\/
     __/  \\__
    /        \\
   |  ~~~~    |
   |  ~~~~    |
   |  ~~~~    |
    \\        /
     \\______/
"""

def get_fortune():
    """Return a random introspective fortune."""
    return random.choice(FORTUNES)

def create_formatted_fortune(fortune_text):
    """Create the full fortune with border, art, and divider."""
    # Get terminal width or use default
    width = 60
    
    # Create top border
    top_border = "╔" + "═" * (width - 2) + "╗"
    bottom_border = "╚" + "═" * (width - 2) + "╝"
    side_border = "║"
    
    # Build the content
    lines = []
    lines.append(top_border)
    lines.append(side_border + " " * (width - 2) + side_border)
    
    # Add title
    title = "🔮 THE SASSY GOOSE FORTUNE TELLER 🔮"
    padding = (width - 2 - len(title)) // 2
    lines.append(side_border + " " * padding + title + " " * (width - 2 - padding - len(title)) + side_border)
    lines.append(side_border + " " * (width - 2) + side_border)
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ts_padding = (width - 2 - len(timestamp)) // 2
    lines.append(side_border + " " * ts_padding + timestamp + " " * (width - 2 - ts_padding - len(timestamp)) + side_border)
    lines.append(side_border + " " * (width - 2) + side_border)
    
    # Add fortune text with proper wrapping
    fortune_lines = []
    words = fortune_text.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += (" " if current_line else "") + word
        else:
            fortune_lines.append(current_line)
            current_line = word
    if current_line:
        fortune_lines.append(current_line)
    
    # Add fortune with padding
    lines.append(side_border + " " * (width - 2) + side_border)
    lines.append(side_border + " " * 2 + "Your Fortune:" + " " * (width - 17) + side_border)
    lines.append(side_border + " " * 2 + "-" * 30 + " " * (width - 35) + side_border)
    for fl in fortune_lines:
        padded = fl.ljust(width - 4)
        lines.append(side_border + " " * 2 + padded + side_border)
    lines.append(side_border + " " * (width - 2) + side_border)
    
    # Add divider
    divider = side_border + " " * 2 + "═══" + "─" * (width - 8) + "═══" + " " * 2 + side_border
    lines.append(divider)
    lines.append(side_border + " " * (width - 2) + side_border)
    
    # Add goose art (center it within the border)
    art_lines = GOOSE_ART.strip().split('\n')
    for art_line in art_lines:
        # Center the art within the available space
        art_width = len(art_line)
        total_padding = width - 2 - art_width
        left_pad = total_padding // 2
        if left_pad < 0:
            left_pad = 0
        padded_art = " " * left_pad + art_line
        lines.append(side_border + padded_art.ljust(width - 2) + side_border)
    
    lines.append(side_border + " " * (width - 2) + side_border)
    
    # Add footer
    footer = "  ~ Trust the honk, dear seeker ~  "
    footer_padding = (width - 2 - len(footer)) // 2
    lines.append(side_border + " " * footer_padding + footer + " " * (width - 2 - footer_padding - len(footer)) + side_border)
    lines.append(side_border + " " * (width - 2) + side_border)
    lines.append(bottom_border)
    
    return '\n'.join(lines)

def move_existing_fortune():
    """Move existing fortune.md to /old folder if it exists."""
    fortune_path = os.path.join(os.getcwd(), 'fortune.md')
    old_dir = os.path.join(os.getcwd(), 'old')
    
    if os.path.exists(fortune_path):
        # Create old directory if it doesn't exist
        os.makedirs(old_dir, exist_ok=True)
        
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_filename = f'fortune_{timestamp}.md'
        old_path = os.path.join(old_dir, old_filename)
        
        # Move the file
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to: {old_path}")

def main():
    """Main function to generate and save fortune."""
    # Get a fortune
    fortune_text = get_fortune()
    
    # Format with ASCII art and border
    formatted_fortune = create_formatted_fortune(fortune_text)
    
    # Handle existing file
    move_existing_fortune()
    
    # Write to fortune.md
    output_path = os.path.join(os.getcwd(), 'fortune.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted_fortune)
    
    print(f"Fortune generated and saved to: {output_path}")
    print("\n" + formatted_fortune)

if __name__ == "__main__":
    main()
