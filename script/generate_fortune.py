#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective wisdom.
"""

import os
import random
from datetime import datetime

# Introspective fortunes
FORTUNES = [
    "The path you seek is not ahead, but within. Listen to the quiet voice you've been ignoring.",
    "Your greatest strength is also your greatest vulnerability. Embrace the paradox.",
    "The answer you seek has been whispering to you through your dreams. Wake up and listen.",
    "Sometimes the detour is the destination. Trust the winding road.",
    "You are closer to understanding than you realize. The pieces are falling into place.",
    "The mirror shows not who you are, but who you're becoming. What do you see?",
    "Your fears are not walls, but doors. What lies beyond them?",
    "The question you're afraid to ask is the one that will set you free.",
    "You carry wisdom in your silence. Speak it when the time is right.",
    "The past is a teacher, not a prison. What lesson are you ready to learn?",
    "Your intuition knows the way. Follow it, even when logic protests.",
    "The weight you carry is not meant to break you, but to strengthen you.",
    "In letting go, you gain everything. What are you holding onto?",
    "The stars align not to dictate your fate, but to illuminate your choices.",
    "Your reflection shows more than your face—it reveals your soul's journey.",
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
     /  \\
    |    |
    |    |
    |    |
    |    |
     \\  /
      \\/
     /|\\
    / | \\
   /  |  \\
  |   |   |
  |   |   |
 /    |    \\
|     |     |
|     |     |
 \\   / \\   /
  \\_/   \\_/
"""

# Alternative goose art for variety
GOOSE_ART_VARIATIONS = [
    GOOSE_ART,
    """
      __
     /  \\
    | o o|
    |  ^ |
    | \\_/|
     \\  /
      \\/
    __|__
   /  |  \\
  |   |   |
  |   |   |
 /    |    \\
|     |     |
 \\   / \\   /
  \\_/   \\_/
""",
    """
      __
     /  \\
    |    |
    |    |
    |    |
     \\  /
      \\/
     /|\\
    / | \\
   /  |  \\
  |   |   |
  |   |   |
 /    |    \\
|     |     |
|     |     |
 \\   |   /
  \\  |  /
   \\_|_/
""",
]

def generate_fortune():
    """Generate a random introspective fortune."""
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the full fortune display with border, goose, and fortune."""
    fortune = generate_fortune()
    goose = random.choice(GOOSE_ART_VARIATIONS)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Calculate width for border (based on longest line in goose art + fortune)
    lines = fortune.split('\n') + goose.split('\n')
    max_width = max(len(line) for line in lines) + 4
    
    # Create the border
    top_border = "╔" + "═" * max_width + "╗"
    bottom_border = "╚" + "═" * max_width + "╝"
    side_border = "║"
    
    # Build the display
    display_lines = []
    display_lines.append(top_border)
    
    # Fortune section
    display_lines.append(f"{side_border}  🌟 YOUR FORTUNE 🌟{' ' * (max_width - 20)}{side_border}")
    display_lines.append(f"{side_border}{' ' * max_width}{side_border}")
    
    for line in fortune.split('\n'):
        padded_line = line.ljust(max_width - 2)
        display_lines.append(f"{side_border} {padded_line}{side_border}")
    
    display_lines.append(f"{side_border}{' ' * max_width}{side_border}")
    
    # Divider
    divider = f"{side_border}{'─' * max_width}{side_border}"
    display_lines.append(divider)
    
    # Goose section
    display_lines.append(f"{side_border}{' ' * max_width}{side_border}")
    display_lines.append(f"{side_border}  🪿 THE SASSY GOOSE SAYS... 🪿{' ' * (max_width - 32)}{side_border}")
    display_lines.append(f"{side_border}{' ' * max_width}{side_border}")
    
    for line in goose.split('\n'):
        padded_line = line.ljust(max_width - 2)
        display_lines.append(f"{side_border} {padded_line}{side_border}")
    
    display_lines.append(f"{side_border}{' ' * max_width}{side_border}")
    display_lines.append(f"{side_border}  Generated: {timestamp}{' ' * (max_width - 26)}{side_border}")
    display_lines.append(bottom_border)
    
    return '\n'.join(display_lines)

def main():
    """Main function to generate fortune and save to file."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md already exists
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Write to markdown file
    with open(output_file, 'w') as f:
        f.write("# 🌟 Your Introspective Fortune 🌟\n\n")
        f.write("```text\n")
        f.write(fortune_display)
        f.write("\n```\n")
        f.write("\n*May the wisdom of the sassy goose guide your journey.*\n")
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
