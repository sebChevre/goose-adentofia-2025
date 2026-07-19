#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Wise fortunes from the fortune teller
FORTUNES = [
    "The winds of change are blowing in your favor. Embrace the unknown with courage.",
    "A wise decision you made long ago will soon bear unexpected fruit.",
    "Patience is your greatest ally today. The stars align in your favor.",
    "An old friend will bring news that changes everything.",
    "The path ahead is clear, but only if you trust your intuition.",
    "What you seek is already seeking you. Stay open to opportunities.",
    "A small act of kindness today will ripple into something magnificent.",
    "The answers you seek lie within. Listen to your inner voice.",
    "Unexpected joy awaits you around the next corner. Keep walking forward.",
    "Your persistence will be rewarded beyond your wildest dreams."
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
     /  \\
    |    |
    |    |
   /|    |\\
  (_|    |_)
    \\    /
     \\  /
      \\/
    __|__
   /     \\
  |  o o  |
  |   ^   |
  |  \\_/  |
   \\_____/
    |   |
    |   |
   /|   |\\
  (_|___|_)
"""

# Border character
BORDER_CHAR = "█"
DIVIDER = "─" * 60

def generate_fortune():
    """Generate a random wise fortune."""
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the full fortune display with ASCII art and border."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the bordered display
    border = BORDER_CHAR * 62
    
    display = f"""{border}
{BORDER_CHAR}  ✨ WISE FORTUNE TELLER ✨{DIVIDER[19:]}{BORDER_CHAR}
{BORDER_CHAR}  {DIVIDER}{BORDER_CHAR}
{BORDER_CHAR}  {GOOSE_ART.strip()}  {BORDER_CHAR}
{BORDER_CHAR}  {DIVIDER}{BORDER_CHAR}
{BORDER_CHAR}  📜 YOUR FORTUNE 📜{DIVIDER[20:]}{BORDER_CHAR}
{BORDER_CHAR}  {DIVIDER}{BORDER_CHAR}
{BORDER_CHAR}  {fortune.center(58)}  {BORDER_CHAR}
{BORDER_CHAR}  {DIVIDER}{BORDER_CHAR}
{BORDER_CHAR}  Generated: {timestamp}{DIVIDER[35:]}{BORDER_CHAR}
{border}"""
    
    return display

def main():
    """Main function to generate and save the fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(output_file):
        os.makedirs(old_folder, exist_ok=True)
        old_path = os.path.join(old_folder, f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
        os.rename(output_file, old_path)
        print(f"Moved existing fortune to: {old_path}")
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Write to fortune.md
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fortune_display)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
