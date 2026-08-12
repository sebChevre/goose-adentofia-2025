#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller
Generates poetic fortunes with ASCII art
"""

import os
import shutil
import random
from datetime import datetime

# Fortune messages from the mystical fortune teller
FORTUNES = [
    "The stars whisper that your courage shall bloom like midnight roses,\n    leading you to treasures hidden in plain sight.",
    "A sassy goose knows: the winds of change carry whispers of opportunity.\n    Listen closely, for fortune favors the bold.",
    "The cosmos dance in rhythm with your destiny.\n    What seems a detour is but a graceful pirouette toward your purpose.",
    "Like a goose who sees the storm before it breaks,\n    your intuition guides you to shores of abundant joy.",
    "The ancient stars align to tell a tale of your making:\n    patience now shall harvest a garden of wonders.",
    "A sassy goose preens her feathers and declares:\n    your path is illuminated by the moon's silver blessing.",
    "The river of time flows toward a waterfall of surprises.\n    Embrace the plunge, for it leads to a crystal pool of clarity.",
    "Like dawn breaking over a misty lake,\n    your dreams shall reveal themselves in colors more vibrant than imagined.",
    "The cosmic goose honks a prophecy: unexpected allies shall appear,\n    bearing gifts that unlock doors you thought forever sealed.",
    "Stars align in a celestial dance, whispering that your next step\n    shall echo through the halls of destiny with resounding triumph."
]

def get_sassy_goose():
    """Return ASCII art of a sassy goose"""
    return r"""
      __
     (o>
     // \
    // _ \
   =\___)=
    /   \
   /     \
  /       \
 /         \
/___________\
    """

def create_ascii_border(content, width=60):
    """Create an ASCII border around content"""
    top_bottom = "╔" + "═" * width + "╗"
    middle = "║" + " " * width + "║"
    
    lines = content.split('\n')
    bordered = [top_bottom]
    
    for line in lines:
        # Pad or truncate line to fit width
        padded = line.ljust(width)[:width]
        bordered.append("║" + padded + "║")
    
    bordered.append(top_bottom.replace("╔", "╚").replace("╗", "╝"))
    return '\n'.join(bordered)

def generate_fortune():
    """Generate a fortune with ASCII art"""
    fortune = random.choice(FORTUNES)
    goose = get_sassy_goose()
    
    # Create the divider
    divider = "─" * 58
    
    # Build the content
    fortune_lines = fortune.split('\n')
    
    content_parts = [
        "  🌙✨ THE MYSTIC GOOSE FORTUNE TELLER ✨🌙  ".center(58),
        f"  {datetime.now().strftime('%B %d, %Y - %I:%M %p')}  ".center(58),
        "",
        "  " + divider,
        "",
        "  YOUR FORTUNE:",
        ""
    ]
    
    for line in fortune_lines:
        content_parts.append("  " + line)
    
    content_parts.extend([
        "",
        "  " + divider,
        "",
        "  " + goose
    ])
    
    content = '\n'.join(content_parts)
    return create_ascii_border(content)

def main():
    """Main function to generate and save fortune"""
    fortune_output = generate_fortune()
    
    # Check if fortune.md exists
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        shutil.move(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write new fortune to fortune.md
    with open(fortune_path, 'w') as f:
        f.write("# 🌙 Mystic Goose Fortune 🌙\n\n")
        f.write("```text\n")
        f.write(fortune_output)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + fortune_output)

if __name__ == "__main__":
    main()
