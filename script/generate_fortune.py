#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective wisdom
"""

import os
import shutil
from datetime import datetime
import random

# Sassy goose ASCII art
GOOSE_ART = """
      __
    /'  \\
   |  o o|
   |  >  |  *Honk honk!*
    \\ ~ /
     | |
    _\\|/_
   (_____)
   /     \\
  |  |  |
  |  |  |
  (___|___)
"""

# Introspective fortunes
FORTUNES = [
    "The path you seek is not ahead, but within. Listen to the quiet voice that whispers when the world sleeps.",
    "What you fear most is the very thing that will set you free. Embrace the unknown.",
    "Your greatest strength lies not in what you've achieved, but in what you've overcome.",
    "The answers you seek are already written in the stars of your own heart.",
    "Sometimes the shortest journey is the one inward. Look within.",
    "The mirror shows your face, but only silence reveals your soul.",
    "You are not broken; you are becoming. The cracks are where the light enters.",
    "The question you ask is less important than why you ask it.",
    "True wisdom comes not from knowing all the answers, but from loving all the questions.",
    "The goose who looks inward finds the worm of truth."
]

def generate_fortune():
    """Generate a fortune with ASCII art and border"""
    fortune = random.choice(FORTUNES)
    
    # Create the fortune display
    border = "╔" + "═" * 58 + "╗"
    bottom = "╚" + "═" * 58 + "╝"
    side = "║"
    
    # Build the content
    lines = []
    lines.append(border)
    lines.append(side + " " * 58 + side)
    lines.append(side + "           🦢  SASSY GOOSE FORTUNE TELLER  🦢           " + side)
    lines.append(side + " " * 58 + side)
    lines.append(side + " " * 58 + side)
    
    # Fortune text (wrapped to fit)
    fortune_lines = []
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 56:
            current_line += (" " if current_line else "") + word
        else:
            fortune_lines.append(current_line)
            current_line = word
    if current_line:
        fortune_lines.append(current_line)
    
    # Add fortune with padding
    for fl in fortune_lines:
        lines.append(side + "  " + fl.ljust(54) + "  " + side)
    
    lines.append(side + " " * 58 + side)
    
    # Divider
    lines.append(side + " " * 58 + side)
    lines.append(side + "  ──────────────────────────────────────────────  " + side)
    lines.append(side + " " * 58 + side)
    
    # Add goose art with proper spacing
    goose_lines = GOOSE_ART.strip().split('\n')
    for gl in goose_lines:
        lines.append(side + "  " + gl.ljust(54) + "  " + side)
    
    lines.append(side + " " * 58 + side)
    lines.append(side + f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  " + side)
    lines.append(side + " " * 58 + side)
    lines.append(bottom)
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save fortune"""
    # Output path
    output_path = "fortune.md"
    old_dir = "old"
    
    # If fortune.md exists, move it to old folder
    if os.path.exists(output_path):
        os.makedirs(old_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_path = os.path.join(old_dir, f"fortune_{timestamp}.md")
        shutil.move(output_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune
    fortune_content = generate_fortune()
    
    # Write to fortune.md
    with open(output_path, 'w') as f:
        f.write("# 🦢 Today's Fortune 🦢\n\n")
        f.write("```\n")
        f.write(fortune_content)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {output_path}")
    print("\n" + fortune_content)

if __name__ == "__main__":
    main()
