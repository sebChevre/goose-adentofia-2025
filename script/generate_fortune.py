#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose companion
"""

import os
import random
from datetime import datetime

# Fortune messages with wise tone
FORTUNES = [
    "The path ahead is shrouded in mist, but your inner light will guide you. Trust in your wisdom.",
    "A challenge approaches, yet it carries within it the seeds of great opportunity. Embrace it with courage.",
    "The universe whispers of change. Those who flow with the river find peace; those who resist find struggle.",
    "An old friendship holds a lesson you have yet to learn. Listen with an open heart.",
    "The stars align to remind you: patience is not passive waiting, but active preparation.",
    "What you seek is also seeking you. Continue your journey with steadfast determination.",
    "The greatest wisdom comes from understanding that uncertainty is the only certainty.",
    "A decision you face will seem difficult, but your intuition knows the way. Trust yourself.",
    "The past has taught you well. Now is the time to apply those lessons with confidence.",
    "Like a river carving through stone, persistence will shape your destiny more than force ever could."
]

# ASCII art of a sassy goose
GOOSE_ART = """
  _._     _,-'""`-._
 (,-.`._,'(       |\\`-/|
     `-.-' \\ )-`( , o o)
           `-    \\_  `
                 '~~~
"""

# Alternative sassy goose variations
GOOSE_ARTS = [
    """
  _._     _,-'""`-._
 (,-.`._,'(       |\\`-/|
     `-.-' \\ )-`( , o o)
           `-    \\_  `
                 '~~~
""",
    """
      _._     _,-'""`-._
     (,-.`._,'(       |\\`-/|
         `-.-' \\ )-`( , o o)
               `-    \\_  `
                     '~~~
  *SASSY*
""",
    """
  _._     _,-'""`-._
 (,-.`._,'(       |\\`-/|
     `-.-' \\ )-`( , o o)
           `-    \\_  `
                 '~~~
   *HONK*
"""
]

def generate_fortune():
    """Generate a random wise fortune."""
    return random.choice(FORTUNES)

def create_ascii_border(content, width=60):
    """Create an ASCII border around the content."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    
    lines = content.split('\n')
    bordered = [top_bottom]
    
    for line in lines:
        # Pad or truncate line to fit within border
        padded = line.ljust(width - 2)[:width - 2]
        bordered.append("║" + padded + "║")
    
    bordered.append(top_bottom)
    return '\n'.join(bordered)

def generate_fortune_display():
    """Generate the complete fortune display with border, fortune, divider, and goose."""
    fortune = generate_fortune()
    goose = random.choice(GOOSE_ARTS)
    
    # Create the display content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""
  ✨ WISE FORTUNE ✨
  {timestamp}

  ──────────────────────────────────────────────────
  
  {fortune}

  ──────────────────────────────────────────────────
  
  Your wise guide awaits:

{goose.strip()}
"""
    
    # Add ASCII border
    bordered_content = create_ascii_border(content.strip())
    
    return bordered_content

def main():
    """Main function to generate fortune and save to file."""
    # Generate the fortune display
    fortune_display = generate_fortune_display()
    
    # Check if fortune.md exists and move to /old folder
    fortune_path = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_path):
        os.makedirs(old_folder, exist_ok=True)
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write the new fortune to fortune.md
    with open(fortune_path, 'w') as f:
        f.write(f"# 🌟 Your Fortune 🌟\n\n")
        f.write("```\n")
        f.write(fortune_display)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
