#!/usr/bin/env python3
"""
Grumpy Fortune Teller - Generates fortunes from a sassy goose fortune teller.
"""

import os
import random
from datetime import datetime

# Sassy goose ASCII art
GOOSE_ART = """
  __      _
 o'__)_   (
 (      _ \\
  `----'  )
     /   /
    (   (
     `--'
"""

# Grumpy fortune messages
FORTUNES = [
    "Your luck is as unreliable as my patience.",
    "A surprise awaits you, but don't expect me to care.",
    "The stars say... honestly, who cares what they say?",
    "You'll find what you're looking for, eventually.",
    "Beware of people who ask too many questions. Like you.",
    "Good things come to those who wait. I'm still waiting.",
    "Your future looks bright. Try not to squander it.",
    "A friend in need is a friend indeed. Are you either?",
    "The universe has a plan. It probably involves more paperwork.",
    "Today is your lucky day. Don't get used to it.",
    "Success is around the corner. So is disappointment.",
    "You have the wisdom of a sage and the energy of a sloth.",
    "Something wonderful is coming. I'm not telling you what.",
    "Your path is clear. Stop asking for directions.",
    "Money may come your way. Don't spend it all on nonsense.",
]

def generate_fortune():
    """Generate a random grumpy fortune."""
    return random.choice(FORTUNES)

def create_fortune_display(fortune):
    """Create the full ASCII art fortune display."""
    border_width = 50
    border = "+" + "-" * (border_width - 2) + "+"
    
    # Date line
    date_line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Title
    title = "GRUMPY FORTUNE TELLER"
    
    # Create the display
    lines = []
    lines.append(border)
    lines.append(f"| {title:^{border_width-4}} |")
    lines.append(f"| {date_line:^{border_width-4}} |")
    lines.append(border)
    lines.append("|")
    
    # Goose art with border
    for line in GOOSE_ART.strip().split('\n'):
        padded = line.center(border_width - 4)
        lines.append(f"| {padded} |")
    
    lines.append("|")
    
    # Divider
    divider = "|" + "-" * (border_width - 2) + "|"
    lines.append(divider)
    lines.append("|")
    
    # Fortune message
    fortune_lines = fortune.split('\n')
    for fl in fortune_lines:
        padded = fl.center(border_width - 4)
        lines.append(f"| {padded} |")
    
    lines.append("|")
    lines.append(border)
    lines.append("")
    lines.append("  *Hmph. There. Are you happy now?*")
    lines.append("")
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save the fortune."""
    # Current working directory
    cwd = os.getcwd()
    fortune_file = os.path.join(cwd, "fortune.md")
    old_folder = os.path.join(cwd, "old")
    
    # Check if fortune.md exists and move it
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_name = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_name)
        os.rename(fortune_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune
    fortune = generate_fortune()
    display = create_fortune_display(fortune)
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(display)
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + display)

if __name__ == "__main__":
    main()
