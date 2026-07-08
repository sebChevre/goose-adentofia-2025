#!/usr/bin/env python3
"""
Fortune Generator Script
Generates a wise fortune with ASCII art of a sassy goose.
"""

import os
import random
from pathlib import Path

# Wise fortune messages
WISE_FORTUNES = [
    "The path you seek is not ahead, but within. Listen to the quiet voice that speaks when the world is still.",
    "Wisdom comes not from knowing all the answers, but from asking the right questions.",
    "Like the river that shapes the stone through persistence, your gentle efforts will transform mountains.",
    "The seeds you plant today may not bloom tomorrow, but they will grow into something magnificent.",
    "True strength lies not in avoiding storms, but in learning to dance in the rain.",
    "The wisdom you seek has been with you all along. Look to the lessons of your past.",
    "Patience is the companion of wisdom. What seems delayed is often perfectly timed.",
    "The greatest discoveries come from those willing to wander off the beaten path.",
    "Your intuition is a compass that never lies. Trust it, even when reason doubts.",
    "The answers you seek are hidden in the questions you have yet to ask yourself."
]

# Sassy goose ASCII art
SASSY_GOOSE_ART = """
   __
  /  \\
 |    |
 |    |
 |    |
  \\__/
   ||
   ||
   ||
   ||
  _||_
 (____)
"""

def generate_fortune():
    """Generate a random wise fortune."""
    return random.choice(WISE_FORTUNES)

def create_formatted_output(fortune):
    """Create the formatted output with border, fortune, divider, and goose."""
    # ASCII border
    border_top = "╔" + "═" * 50 + "╗"
    border_bottom = "╚" + "═" * 50 + "╝"
    border_side = "║"
    
    # Create the fortune text with proper spacing
    fortune_lines = fortune.split('\n')
    centered_fortune = []
    for line in fortune_lines:
        # Center the text within the border (48 chars available for text)
        padding = (48 - len(line)) // 2
        centered_fortune.append(" " * padding + line)
    
    # Build the complete output
    output_lines = []
    output_lines.append(border_top)
    output_lines.append(border_side + "           ✨ WISE FORTUNE ✨            " + border_side)
    output_lines.append(border_side + "                                       " + border_side)
    
    for line in centered_fortune:
        output_lines.append(border_side + line.ljust(48) + border_side)
    
    output_lines.append(border_side + "                                       " + border_side)
    
    # Divider between fortune and goose
    output_lines.append(border_side + "           ─────────────────            " + border_side)
    output_lines.append(border_side + "           🪿 SASSY GOOSE 🪿             " + border_side)
    output_lines.append(border_side + "                                       " + border_side)
    
    # Add goose art (centered)
    goose_lines = SASSY_GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        # Center the goose art
        padding = (48 - len(line)) // 2
        output_lines.append(border_side + " " * padding + line + " " * padding + border_side)
    
    output_lines.append(border_side + "                                       " + border_side)
    output_lines.append(border_bottom)
    
    return '\n'.join(output_lines)

def main():
    """Main function to generate and save the fortune."""
    # Get current working directory
    cwd = Path.cwd()
    
    # Check if fortune.md exists and move to /old folder
    fortune_file = cwd / "fortune.md"
    if fortune_file.exists():
        old_folder = cwd / "old"
        old_folder.mkdir(exist_ok=True)
        old_file = old_folder / f"fortune_{fortune_file.stat().st_mtime}.md"
        fortune_file.rename(old_file)
        print(f"Moved existing fortune.md to {old_file}")
    
    # Generate the fortune
    fortune = generate_fortune()
    print(f"Generated fortune: {fortune}")
    
    # Create formatted output
    output = create_formatted_output(fortune)
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(output)
    
    print(f"\nFortune saved to {fortune_file}")
    print("\n" + output)

if __name__ == "__main__":
    main()
