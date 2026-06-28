#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with poetic moods
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic flair
FORTUNES = [
    "The stars whisper of adventures yet unwritten, and your name appears in their celestial script.",
    "A door you thought closed forever shall creak open, revealing treasures you forgot you sought.",
    "The wind carries news from distant shores—listen closely, for opportunity knocks in disguise.",
    "Your courage shall bloom like midnight flowers, surprising even those who thought you timid.",
    "An old friend's shadow will cross your path again, bringing gifts wrapped in familiar laughter.",
    "The universe conspires in your favor, though it wears a mask of challenges first.",
    "Creativity flows through you like a river finding its way to the sea—trust its course.",
    "What you seek is already seeking you, drawn by the magnet of your authentic self.",
    "A small act of kindness shall return multiplied, like seeds that grow into forests.",
    "The moon's phases mirror your journey—sometimes full, sometimes hidden, always beautiful.",
]

# Sassy goose ASCII art variations
GOOSE_ARTS = [
    """
     _   _
    (q\\_/p)
     /. .\\
    =\\_t_/=   A wise and sassy goose
     /   \\
    ((   ))
    """,
    """
      _   _
     (q\\_/p)
      /. .\\
    =\\_C_/=   The oracle speaks
     /   \\
    ((   ))
    """,
    """
     _   _
    (q\\_/p)
     /. .\\
    =\\_t_/=   *honks mysteriously*
     /   \\
    ((   ))
    """,
]

def generate_fortune():
    """Generate a random fortune with poetic mood."""
    return random.choice(FORTUNES)

def get_goose_art():
    """Get a random sassy goose ASCII art."""
    return random.choice(GOOSE_ARTS)

def create_bordered_content(fortune, goose_art):
    """Create the fortune with ASCII border and formatting."""
    border_char = "═"
    side_char = "║"
    
    # Create fortune box with border
    lines = []
    
    # Top border
    lines.append("╔" + border_char * 60 + "╗")
    
    # Fortune section
    lines.append("║" + "  🌙 POETIC FORTUNE OF THE DAY  " + " " * 27 + "║")
    lines.append("║" + "  " + datetime.now().strftime("%B %d, %Y") + " " * (32 - len(datetime.now().strftime("%B %d, %Y"))) + "║")
    lines.append("╟" + border_char * 60 + "╢")
    lines.append("║")
    
    # Fortune text (wrapped to fit)
    fortune_lines = []
    words = fortune.split()
    current_line = "║   "
    for word in words:
        if len(current_line) + len(word) + 1 <= 58:
            current_line += word + " "
        else:
            fortune_lines.append(current_line)
            current_line = "║   " + word + " "
    fortune_lines.append(current_line)
    
    for fl in fortune_lines:
        lines.append(fl + " " * (58 - len(fl)) + "║")
    
    lines.append("║")
    
    # Divider
    lines.append("╟" + "─" * 60 + "╢")
    lines.append("║" + "  " + "✨" * 29 + " ✨" + "  ║")
    lines.append("╟" + "─" * 60 + "╢")
    
    # Goose section
    goose_lines = goose_art.strip().split('\n')
    for gline in goose_lines:
        # Center the goose art
        padding = (58 - len(gline)) // 2
        lines.append("║" + " " * padding + gline + " " * (padding + len(gline) - 58) + "║")
    
    lines.append("║")
    lines.append("╟" + border_char * 60 + "╢")
    lines.append("║" + "  Fortune told by a sassy goose 🪿✨  " + " " * 19 + "║")
    lines.append("╚" + border_char * 60 + "╝")
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save fortune."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(os.getcwd(), "fortune.md")
    old_folder = os.path.join(os.getcwd(), "old")
    
    # Generate fortune content
    fortune = generate_fortune()
    goose_art = get_goose_art()
    content = create_bordered_content(fortune, goose_art)
    
    # Handle existing fortune.md
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to: {old_path}")
    
    # Write new fortune to markdown file
    with open(output_file, 'w') as f:
        f.write("# 🌙 Daily Fortune 🌙\n\n")
        f.write("```text\n")
        f.write(content)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to: {output_file}")
    print("\n" + "=" * 60)
    print(content)
    print("=" * 60)

if __name__ == "__main__":
    main()
