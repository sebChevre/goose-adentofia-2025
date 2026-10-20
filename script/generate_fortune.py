#!/usr/bin/env python3
"""
Grumpy Fortune Teller Script
Generates a fortune from a sassy goose fortune teller with ASCII art.
"""

import os
import random
from datetime import datetime

# Fortune messages from a grumpy fortune teller
FORTUNES = [
    "Your path is clear, but I'd watch your step anyway.",
    "Luck is coming... if you're lucky.",
    "Someone is thinking of you. Probably wondering why you're so difficult.",
    "A surprise awaits. Try not to be disappointed.",
    "Your future looks bright. Unlike my mood.",
    "Patience is a virtue. Something you clearly lack.",
    "Success is near. Don't mess it up.",
    "A friend will help you. They'll probably regret it.",
    "Your dreams will come true. Eventually.",
    "Money is coming. Don't spend it all on nonsense.",
    "Love is in the air. Don't choke on it.",
    "A challenge awaits. Try not to cry about it.",
    "Your wisdom will shine. If you can find it.",
    "Good news is coming. Brace yourself for mediocrity.",
    "Your talent will be recognized. By the right people, maybe.",
]

# ASCII art of a sassy goose
SASSY_GOOSE = r"""
      __
     /  \
    |    |
    |    |
   /|    |\
  / |    | \
   \|    |/
    |    |
    |    |
   /      \
  |  o  o  |
  |   __   |
  |  (__)  |
   \      /
    |    |
   /|    |\
  /_|____|_\
    |    |
    |    |
    |    |
   /|    |\
  /_|____|_\
"""

# ASCII border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
SIDE_BORDER = "║"
DIVIDER = "╟" + "─" * 58 + "╢"


def generate_fortune():
    """Generate a random fortune from the grumpy fortune teller."""
    return random.choice(FORTUNES)


def create_fortune_display():
    """Create the full fortune display with ASCII art and formatting."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the display
    lines = []
    
    # Top border
    lines.append(TOP_BORDER)
    
    # Header
    header = " 🦆 GRUMPY FORTUNE TELLER "
    lines.append(f"{SIDE_BORDER}{header.center(56)}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{timestamp.center(56)}{SIDE_BORDER}")
    lines.append(TOP_BORDER.replace("╔", "╠").replace("╗", "╣"))
    
    # Sassy goose
    goose_lines = SASSY_GOOSE.strip().split('\n')
    for goose_line in goose_lines:
        lines.append(f"{SIDE_BORDER} {goose_line.center(56)} {SIDE_BORDER}")
    
    # Divider
    lines.append(DIVIDER)
    
    # Fortune section
    lines.append(f"{SIDE_BORDER}{SIDE_BORDER}")
    
    # Add fortune with wrapping
    fortune_words = fortune.split()
    current_line = "Your fortune:"
    lines.append(f"{SIDE_BORDER} {current_line.center(56)} {SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{SIDE_BORDER}")
    
    # Wrap fortune text
    line_length = 0
    wrapped_fortune = []
    current_line = ""
    
    for word in fortune_words:
        if len(current_line) + len(word) + 1 <= 54:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            wrapped_fortune.append(current_line)
            current_line = word
    
    if current_line:
        wrapped_fortune.append(current_line)
    
    for line in wrapped_fortune:
        lines.append(f"{SIDE_BORDER} {line.center(56)} {SIDE_BORDER}")
    
    lines.append(f"{SIDE_BORDER}{SIDE_BORDER}")
    
    # Closing message
    closing = "Now get out of here!"
    lines.append(f"{SIDE_BORDER} {closing.center(56)} {SIDE_BORDER}")
    
    # Bottom border
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def save_to_markdown(content, output_path):
    """Save the fortune display to a markdown file."""
    # Check if file exists, if so move to /old folder
    if os.path.exists(output_path):
        old_folder = os.path.join(os.path.dirname(output_path), 'old')
        os.makedirs(old_folder, exist_ok=True)
        
        # Get current timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.basename(output_path)
        base_name, ext = os.path.splitext(filename)
        old_filename = f"{base_name}_{timestamp}{ext}"
        old_path = os.path.join(old_folder, old_filename)
        
        os.rename(output_path, old_path)
        print(f"Previous fortune moved to: {old_path}")
    
    # Write the new fortune
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 🦆 Grumpy Fortune Teller\n\n")
        f.write("```\n")
        f.write(content)
        f.write("\n```\n")
    
    print(f"Fortune saved to: {output_path}")


def main():
    """Main function to generate and save the fortune."""
    # Get the current directory for output
    output_dir = os.getcwd()
    output_path = os.path.join(output_dir, 'fortune.md')
    
    # Create the fortune display
    display = create_fortune_display()
    
    # Display in console
    print("\n")
    print(display)
    print("\n")
    
    # Save to markdown
    save_to_markdown(display, output_path)


if __name__ == "__main__":
    main()
