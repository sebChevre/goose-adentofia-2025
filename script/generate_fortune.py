#!/usr/bin/env python3
"""
Fortune Generator - An introspective fortune teller with a sassy goose
"""

import os
import shutil
import random
from datetime import datetime

# Introspective fortunes
FORTUNES = [
    "The path you seek is not ahead, but within. Look closer at what you've already built.",
    "Your greatest strength lies in your vulnerability. Embrace the cracks - they let the light in.",
    "The question you're afraid to ask holds the answer you desperately need.",
    "Sometimes the bravest thing is to pause and wonder 'what if I'm enough?'",
    "Your reflection shows more than you realize. The eyes you see are watching you grow.",
    "The silence between your thoughts speaks louder than your fears.",
    "You've been searching for a sign. This moment is it - breathe and begin.",
    "The weight you carry is not meant to anchor you, but to ground you as you rise.",
    "Your past is a compass, not a cage. Let it point you forward, not hold you back.",
    "The mirror shows not who you were, but who you're becoming. And that is beautiful."
]

def get_sassy_goose():
    """Return ASCII art of a sassy goose"""
    return r"""
      __
     /  \
    |    |
    |    |___
    |       /
    \      /
     \    /
      \__/
     /|  |\
    / |  | \
      |  |
      |  |
     _/  \_
    (      )
    |      |
    |      |
    |      |
    |      |
   _/      \_
  (__________)
"""

def create_border(content, width=60):
    """Create an ASCII border around content"""
    border_top_bottom = "╔" + "═" * (width - 2) + "╗"
    border_middle = "║" + " " * (width - 2) + "║"
    border_divider = "╟" + "─" * (width - 2) + "╢"
    
    lines = content.split('\n')
    bordered_lines = []
    
    for line in lines:
        # Pad line to fit within border
        padded = line.center(width - 2)
        bordered_lines.append("║" + padded + "║")
    
    return border_top_bottom + "\n" + "\n".join(bordered_lines) + "\n" + border_top_bottom

def generate_fortune_output():
    """Generate the complete fortune output with goose and border"""
    fortune = random.choice(FORTUNES)
    goose = get_sassy_goose()
    
    # Create the content with divider
    content = f"""
🔮 Your Introspective Fortune 🔮
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{fortune}
"""
    
    # Add divider and goose
    full_content = content + "\n" + "─" * 40 + "\n" + goose
    
    # Create bordered output
    output = create_border(full_content, width=65)
    
    # Add closing message
    output += "\n" + "Remember: The greatest mysteries are within you.\n"
    
    return output

def main():
    """Main function to generate fortune and save to file"""
    output_dir = os.getcwd()
    fortune_file = os.path.join(output_dir, "fortune.md")
    old_dir = os.path.join(output_dir, "old")
    
    # Check if fortune.md exists and move to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_dir, f"fortune_{timestamp}.md")
        shutil.move(fortune_file, old_file)
        print(f"Moved existing fortune.md to: {old_file}")
    
    # Generate fortune
    fortune_output = generate_fortune_output()
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(fortune_output)
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + "=" * 50)
    print(fortune_output)
    print("=" * 50)

if __name__ == "__main__":
    main()
