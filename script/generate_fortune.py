#!/usr/bin/env python3
"""
Grumpy Fortune Teller - Generates fortunes with a sassy goose attitude
"""

import os
import random
from datetime import datetime

# Grumpy fortune messages
FORTUNES = [
    "Ugh, fine. Your day will be... tolerable. I suppose.",
    "Oh joy, another human asking for wisdom. Your path is... predictable.",
    "Hmph. The stars say you'll find what you're looking for. Eventually.",
    "Whatever. You're about to make a decision you'll regret. Just kidding... or am I?",
    "Sigh. Good news: nothing terrible will happen today. Boring, I know.",
    "Look, your future involves coffee. Lots of coffee. And patience.",
    "Fine, fine! Someone will surprise you today. Try not to faint.",
    "Ugh, the universe whispers that you need to stop asking me these questions.",
    "Oh, wonderful. Your luck is... adequate. Thrilling, I know.",
    "Whatever you're worried about, it'll be fine. Now leave me alone.",
    "Hmph. A unexpected opportunity awaits. Try not to mess it up.",
    "Sigh. Today you'll learn something. Whether you like it or not.",
]

# Sassy goose ASCII art
SASSY_GOOSE = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

SASSY_GOOSE_2 = """
   __
  ( oo)
  |  |
  |  |
  \\__/
"""

SASSY_GOOSE_3 = """
      _
    _( >
   ( ._)
    \\__
"""

SASSY_GOOSE_4 = """
   _  _
  (o)(o)--.
   \\../   )
   /\\*    /
  oo^--'o
"""

def get_border(width):
    """Create an ASCII border"""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    return top_bottom, middle, "╚" + "═" * (width - 2) + "╝"

def format_fortune(fortune, goose_art):
    """Format the fortune with border, goose art, and divider"""
    # Determine the maximum width needed
    lines = [goose_art, fortune]
    max_width = max(len(line) for line in lines) + 4  # Add padding
    
    # Ensure minimum width
    max_width = max(max_width, 40)
    
    top_border, middle_border, bottom_border = get_border(max_width)
    
    # Build the output
    output_lines = []
    output_lines.append(top_border)
    
    # Add goose art centered
    goose_lines = goose_art.strip().split('\n')
    for line in goose_lines:
        padding = (max_width - 2 - len(line)) // 2
        output_lines.append("║" + " " * padding + line + " " * (max_width - 2 - padding - len(line)) + "║")
    
    # Add divider
    divider = "║" + "─" * (max_width - 2) + "║"
    output_lines.append(divider)
    
    # Add fortune title
    title = "🔮 GRUMPY FORTUNE 🔮"
    padding = (max_width - 2 - len(title)) // 2
    output_lines.append("║" + " " * padding + title + " " * (max_width - 2 - padding - len(title)) + "║")
    
    # Add fortune text (wrap if needed)
    fortune_lines = fortune.split('\n')
    for line in fortune_lines:
        # Simple word wrapping
        words = line.split()
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= max_width - 4:
                current_line += " " + word if current_line else word
            else:
                if current_line:
                    padding = (max_width - 2 - len(current_line)) // 2
                    output_lines.append("║" + " " * padding + current_line + " " * (max_width - 2 - padding - len(current_line)) + "║")
                current_line = word
        if current_line:
            padding = (max_width - 2 - len(current_line)) // 2
            output_lines.append("║" + " " * padding + current_line + " " * (max_width - 2 - padding - len(current_line)) + "║")
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ts_padding = (max_width - 2 - len(timestamp)) // 2
    output_lines.append("║" + " " * ts_padding + timestamp + " " * (max_width - 2 - ts_padding - len(timestamp)) + "║")
    
    output_lines.append(bottom_border)
    
    return '\n'.join(output_lines)

def main():
    # Get a random fortune
    fortune = random.choice(FORTUNES)
    
    # Get a random sassy goose
    goose_artifacts = [SASSY_GOOSE, SASSY_GOOSE_2, SASSY_GOOSE_3, SASSY_GOOSE_4]
    goose_art = random.choice(goose_artifacts)
    
    # Format the fortune
    output = format_fortune(fortune, goose_art)
    
    # Handle existing fortune.md file
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write the new fortune
    with open(fortune_path, 'w') as f:
        f.write("# 🦢 Grumpy Fortune Teller 🔮\n\n")
        f.write("```text\n")
        f.write(output)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + output)

if __name__ == "__main__":
    main()
