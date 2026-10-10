#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
Generates mystical fortunes and writes them to fortune.md
"""

import os
import random
from datetime import datetime

# Poetic fortune teller messages
FORTUNES = [
    "The stars whisper of adventures yet untold, where courage meets opportunity.",
    "A door you thought closed shall swing wide, revealing paths of golden light.",
    "The winds of change carry whispers of joy on their gentle breath.",
    "Three moons shall align before your heart's deepest desire finds its way to you.",
    "An unexpected encounter shall bloom into something beautiful beyond measure.",
    "The river of time flows toward a treasure hidden in plain sight.",
    "Your laughter shall echo through halls yet unvisited, bringing warmth to strangers.",
    "A secret long kept shall reveal itself as the key to a new beginning.",
    "The stars dance in patterns meant only for your eyes to interpret.",
    "What seems like an ending is but a prelude to a magnificent new chapter.",
    "The goose knows what you seek, and the answer flaps its wings toward you.",
    "Wisdom comes not from the questions asked, but from the silence between them.",
    "A journey of a thousand miles begins with a single, sassy step.",
    "The universe conspires to bring you exactly what you need, not what you want.",
    "Like a goose gliding on water, your calm demeanor hides great strength.",
]

# Sassy goose ASCII art
SASSY_GOOSE = r"""
              __
            <(o )___
             ( ._> /
              \___/
                 _
                (o)
               /   \
              |     |
              |     |
             /|     |\
            / |     | \
           |  |     |  |
           |  |     |  |
          /|  |     |  |\
         / |  |     |  | \
        |  |  |     |  |  |
        |  |  |     |  |  |
       /|  |  |     |  |  |\
      / |  |  |     |  |  | \
     |  |  |  |     |  |  |  |
     |  |  |  |     |  |  |  |
    /|  |  |  |     |  |  |  |\
   / |  |  |  |     |  |  |  | \
  |  |  |  |  |     |  |  |  |  |
  |  |  |  |  |     |  |  |  |  |
 /|  |  |  |  |     |  |  |  |  |\
/ |  |  |  |  |     |  |  |  |  | \
   \  \  \  \  \     /  /  /  /  /
    \  \  \  \  \   /  /  /  /  /
     \  \  \  \  \ /  /  /  /  /
      \  \  \  \  V  /  /  /  /
       \  \  \  \   /  /  /  /
        \  \  \  \ /  /  /  /
         \  \  \  V  /  /  /
          \  \  \   /  /  /
           \  \  \ /  /  /
            \  \  V  /  /
             \  \   /  /
              \  \ /  /
               \  V  /
                \   /
                 \ /
                  V
    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    THE SASSY GOOSE SAYS:
    "Honk if you believe!"
    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"""

# Alternative smaller goose art
SASSY_GOOSE_SMALL = r"""
      __
    <(o )___
     ( ._> /
      \___/
   ~ ~ ~ ~ ~
   Honk! 🪿
   ~ ~ ~ ~ ~
"""

def generate_border(width=60):
    """Generate an ASCII border."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    bottom = "╚" + "═" * (width - 2) + "╝"
    return top_bottom, middle, bottom

def generate_divider(width=60):
    """Generate a divider line."""
    return "╟" + "─" * (width - 2) + "╢"

def center_text(text, width):
    """Center text within a given width."""
    padding = max(0, (width - len(text) - 4) // 2)
    return "║  " + " " * padding + text + " " * padding + "  ║"

def generate_fortune_output():
    """Generate the complete fortune output with borders and ASCII art."""
    width = 60
    top, middle, bottom = generate_border(width)
    divider = generate_divider(width)

    # Get current date/time
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y at %I:%M %p")

    # Select a random fortune
    fortune = random.choice(FORTUNES)

    # Build the output
    lines = []
    lines.append(top)
    lines.append(center_text("🔮 MYSTIC FORTUNE TELLER 🔮", width))
    lines.append(middle)
    lines.append(center_text(f"Date: {date_str}", width))
    lines.append(middle)
    lines.append(divider)
    lines.append(middle)
    lines.append(center_text("Your Poetic Fortune:", width))
    lines.append(middle)
    lines.append("║" + " " * 2)

    # Word wrap the fortune
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 50:
            current_line += (word + " ")
        else:
            if current_line:
                lines.append("║  " + current_line.strip().ljust(54) + "  ║")
            current_line = word + " "
    if current_line:
        lines.append("║  " + current_line.strip().ljust(54) + "  ║")

    lines.append(middle)
    lines.append(divider)
    lines.append(middle)
    lines.append(center_text("✨ The Sassy Goose Knows ✨", width))
    lines.append(middle)

    # Add the ASCII goose art (indented to fit within border)
    goose_lines = SASSY_GOOSE.split('\n')
    for goose_line in goose_lines:
        if goose_line.strip():
            # Center the goose art within the border
            centered_goose = goose_line.center(56)
            lines.append("║  " + centered_goose + "  ║")
        else:
            lines.append("║" + " " * 58 + "║")

    lines.append(middle)
    lines.append(divider)
    lines.append(middle)
    lines.append(center_text("May the stars guide your path 🌟", width))
    lines.append(middle)
    lines.append(bottom)

    return '\n'.join(lines)

def main():
    """Main function to generate and save the fortune."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(os.getcwd(), "fortune.md")
    old_dir = os.path.join(os.getcwd(), "old")

    # Check if fortune.md already exists and move it to old folder
    if os.path.exists(output_file):
        # Create old directory if it doesn't exist
        os.makedirs(old_dir, exist_ok=True)

        # Generate a timestamped filename for the old fortune
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_file_path = os.path.join(old_dir, old_filename)

        # Move the existing file
        os.rename(output_file, old_file_path)
        print(f"Moved existing fortune.md to: {old_file_path}")

    # Generate the fortune output
    fortune_output = generate_fortune_output()

    # Write to fortune.md
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fortune_output)

    print(f"Fortune generated and saved to: {output_file}")
    print("\n" + "=" * 50)
    print(fortune_output)
    print("=" * 50)

if __name__ == "__main__":
    main()
