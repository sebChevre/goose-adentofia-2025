#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose delivers introspective wisdom
"""

import os
import random
from datetime import datetime

# Fortune messages with introspective themes
FORTUNES = [
    "The path you seek is not ahead, but within. Listen to the quiet voice that whispers when the world falls silent.",
    "What you fear losing is already gone. What you fear gaining is already yours. Embrace the paradox.",
    "The mirror shows not your face, but your potential. Are you brave enough to look deeper?",
    "Yesterday's wounds have become today's wisdom. Tomorrow's challenges will forge tomorrow's strength.",
    "You are the author of your story. Today, choose a chapter that makes you proud.",
    "The seeds you plant in darkness will bloom in light. Trust the process, even when you cannot see the sprout.",
    "Your greatest obstacle is also your greatest teacher. What lesson is hiding in plain sight?",
    "The river does not rush to reach the sea. Neither should you. Flow with purpose, not haste.",
    "In the space between thoughts, your true self awaits. Find that space, and you find freedom.",
    "The bird that fears the wind will never know the sky. Spread your wings, even when you tremble."
]

def get_sassy_goose():
    """Return ASCII art of a sassy goose"""
    return r"""
     __      __
    /  \    /  \
   |    \__/    |
   |  o      o  |
   |     <      |  *sassy honk*
   |   \____/   |
    \  \    /  /
     \  \__/  /
      \______/
    """

def create_ascii_border(content, width=60):
    """Create an ASCII border around content"""
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    
    lines = content.split('\n')
    bordered = [top]
    
    for line in lines:
        # Pad or truncate line to fit width
        padded = line[:width-2].ljust(width-2)
        bordered.append("║" + padded + "║")
    
    bordered.append(bottom)
    return '\n'.join(bordered)

def generate_fortune():
    """Generate a fortune with sassy goose and formatting"""
    fortune = random.choice(FORTUNES)
    goose = get_sassy_goose()
    divider = "─" * 58
    
    # Create the fortune content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""
  🌟 YOUR INTROSPECTIVE FORTUNE 🌟
  {timestamp}

  {fortune}

  {divider}
  
{goose}
  *The goose honks knowingly*
"""
    
    # Add ASCII border
    bordered_content = create_ascii_border(content.strip(), width=62)
    
    return bordered_content

def main():
    output_path = "fortune.md"
    old_dir = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(output_path):
        os.makedirs(old_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_dir, f"fortune_{timestamp}.md")
        os.rename(output_path, old_path)
        print(f"Previous fortune moved to: {old_path}")
    
    # Generate the fortune
    fortune_content = generate_fortune()
    
    # Write to fortune.md
    with open(output_path, 'w') as f:
        f.write(f"# 🦢 Sassy Goose Fortune 🦢\n\n")
        f.write("```text\n")
        f.write(fortune_content)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to: {output_path}")
    print("\n" + fortune_content)

if __name__ == "__main__":
    main()
