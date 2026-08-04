#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective wisdom.
Generates a fortune and saves it to fortune.md with ASCII art.
"""

import os
import random
from datetime import datetime

# Fortune messages with introspective themes
FORTUNES = [
    "The mirror of your soul reflects a path not yet walked. What you seek is already within you, waiting to be discovered.",
    "A question you've been avoiding holds the key to your next breakthrough. Face it with courage.",
    "The answers you seek lie not in the stars, but in the quiet moments between your thoughts.",
    "Your intuition speaks louder than you realize. Trust the whispers that guide your steps.",
    "The change you fear is actually the growth you need. Embrace the transformation.",
    "A memory from your past holds wisdom for your present. Look back to move forward.",
    "The weight you carry is lighter than you think. Set it down and breathe.",
    "Your greatest strength has been hiding in plain sight. It's the vulnerability you've been afraid to show.",
    "The universe is conspiring in your favor, but only if you take the first step.",
    "Silence is not empty; it's full of answers. Listen more deeply today.",
    "The person you're becoming is already proud of the person you are.",
    "Your doubts are not enemies; they're guardians protecting your potential.",
]

# Sassy Goose ASCII Art
GOOSE_ART = """
    __      __
   /  \\    /  \\
  |    \\/\\/    |
  |   O     O   |
  |      <      |
   \\  \\___/  /
    \\_______/
     /     \\
    /       \\
   |  SASSY  |
   |   GOOSE |
   \\_________/
"""

def generate_fortune():
    """Generate a random introspective fortune."""
    return random.choice(FORTUNES)

def create_formatted_output(fortune):
    """Create the formatted fortune output with ASCII art and border."""
    border = "╔" + "═" * 58 + "╗"
    middle = "║" + " " * 58 + "║"
    bottom = "╚" + "═" * 58 + "╝"
    
    # Split fortune into lines that fit within the border (56 chars for content)
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
    
    # Build the output
    output_lines = []
    output_lines.append(border)
    output_lines.append(middle)
    output_lines.append("║" + " " * 20 + "FORTUNE" + " " * 27 + "║")
    output_lines.append(middle)
    
    # Add fortune lines with border
    for line in fortune_lines:
        output_lines.append("║ " + line.ljust(54) + " ║")
    
    output_lines.append(middle)
    
    # Divider
    divider = "║" + "─" * 58 + "║"
    output_lines.append(divider)
    output_lines.append(middle)
    
    # Add goose art (centered)
    goose_lines = GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        # Center the goose art within the border
        centered_line = line.center(56)
        output_lines.append("║ " + centered_line + " ║")
    
    output_lines.append(middle)
    output_lines.append("║" + " " * 20 + "SASSY GOOSE" + " " * 25 + "║")
    output_lines.append(middle)
    output_lines.append(f"║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".ljust(57) + " ║")
    output_lines.append(bottom)
    
    return '\n'.join(output_lines)

def main():
    """Main function to generate fortune and save to file."""
    # Check if fortune.md exists and move to old folder
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate fortune
    fortune = generate_fortune()
    
    # Create formatted output
    output = create_formatted_output(fortune)
    
    # Write to fortune.md
    with open(fortune_path, 'w') as f:
        f.write(output)
    
    print("Fortune generated successfully!")
    print(f"Output saved to {fortune_path}")
    print("\n" + output)

if __name__ == "__main__":
    main()
