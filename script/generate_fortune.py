#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with poetic moods
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic flair
FORTUNES = [
    "The stars whisper of adventures awaiting beyond your horizon.\nA journey of the heart shall bring unexpected joy.",
    "Like a river finding its course, your path shall reveal itself.\nTrust in the wisdom of your own gentle strength.",
    "The moon watches over you with benevolent eyes.\nCreativity flows through you like a silver stream.",
    "An old friend brings news that will spark your imagination.\nListen closely to the whispers of the wind.",
    "The universe conspires to bring you a moment of pure magic.\nKeep your eyes open for signs in the morning dew.",
    "Your courage shall be rewarded with a treasure beyond gold.\nIt lives in the laughter you share with others.",
    "A unexpected turn shall lead you to a door you never knew existed.\nStep through with confidence and an open heart.",
    "The cosmos aligns to remind you of your innate brilliance.\nShine forth, dear soul, for the world needs your light.",
]

# Sassy Goose ASCII Art
GOOSE_ART = """
   __
  /  \\
 |    |
 |    |
  \\  /
   \\/
  /  \\
 |    |
 | o  |
  \\__/
   ||
   ||
  _||_
 |    |
 |    |
 |____|
"""

# Fortune with border and formatting
def generate_fortune_output():
    """Generate the complete fortune output with ASCII art and border."""
    fortune = random.choice(FORTUNES)
    
    # Create the fortune box with border
    border_top = "+------------------------------------------+"
    border_bottom = "+------------------------------------------+"
    border_middle = "|                                          |"
    
    # Split fortune into lines and format
    fortune_lines = fortune.split('\n')
    formatted_fortune = []
    for line in fortune_lines:
        # Pad each line to fit within the border
        padded_line = line.ljust(40)
        formatted_fortune.append(f"| {padded_line[:40]} |")
    
    # Build the complete output
    output_lines = []
    output_lines.append(border_top)
    output_lines.append(border_middle)
    output_lines.append("|          Your Fortune Awaits...          |")
    output_lines.append(border_middle)
    output_lines.append(border_top)
    output_lines.append("")
    
    # Add fortune text
    for line in formatted_fortune:
        output_lines.append(line)
    
    output_lines.append(border_middle)
    output_lines.append(border_top)
    output_lines.append("")
    
    # Add divider
    divider = "+------------------------------------------+"
    output_lines.append(divider)
    output_lines.append("|          ~ The Sassy Goose Says ~        |")
    output_lines.append(divider)
    output_lines.append("")
    
    # Add goose ASCII art with border
    for line in GOOSE_ART.split('\n'):
        if line.strip():
            output_lines.append(f"| {line.center(40)} |")
        else:
            output_lines.append("|                                          |")
    
    output_lines.append(border_bottom)
    output_lines.append("")
    output_lines.append(f"Fortune generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output_lines.append("Remember: The future is yours to create! 🪿✨")
    
    return '\n'.join(output_lines)

def main():
    """Main function to generate fortune and save to file."""
    output_content = generate_fortune_output()
    
    # Define file paths
    fortune_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write new fortune to file
    with open(fortune_file, 'w') as f:
        f.write(output_content)
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + output_content)

if __name__ == "__main__":
    main()
