#!/usr/bin/env python3
"""
Generate a grumpy fortune teller output with ASCII art.
"""

import os
import random
from datetime import datetime

# Grumpy fortunes
FORTUNES = [
    "Ugh, fine. Your day will be 'adequate'. Don't expect miracles.",
    "Hmmph. Someone will annoy you today. Prepare your sigh.",
    "Tch. Your coffee will be lukewarm. Just like your prospects.",
    "Oh joy. You'll find something you lost. It was under your nose.",
    "Whatever. A stranger will smile at you. Don't get used to it.",
    "Hmph. Your plans will work out, but only because I said so.",
    "Sigh. You'll avoid a minor inconvenience. Try not to celebrate too hard.",
    "Ugh. Someone will ask for your opinion. Give the vague answer.",
    "Fine. You'll discover a new favorite snack. Don't share it.",
    "Tch. A small problem will solve itself. Don't get cocky.",
    "Whatever. You'll remember something embarrassing from 2012. You're welcome.",
    "Hmph. The universe has a sense of humor. Today, you'll see it.",
]

# Sassy goose ASCII art
GOOSE_ART = """
   __
  /  \\
 |    |
 |    |
 |    |
  \\  /
   \\/
   ||
   ||
  /  \\
 |    |
 |    |
 |    |
  \\__/
"""

# Alternative sassy goose variations
GOOSE_VARIATIONS = [
    """
   _
  ( )
   |
  / \\
 |   |
 |   |
  \\_/
   |
  / \\
""",
    """
   __
  /  \\
 | o |
 |   |
  \\_/
   |
  / \\
 |   |
  \\_/
""",
]

def get_grumpy_fortune():
    """Return a random grumpy fortune."""
    return random.choice(FORTUNES)

def create_ascii_border(content, width=60):
    """Create an ASCII border around content."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    
    lines = content.split('\n')
    bordered_lines = []
    
    for line in lines:
        # Pad or truncate line to fit within border
        padded = line.ljust(width - 2)[:width - 2]
        bordered_lines.append("║ " + padded + " ║")
    
    return top_bottom + "\n" + "\n".join(bordered_lines) + "\n" + top_bottom

def generate_fortune_output():
    """Generate the complete fortune output with ASCII art."""
    fortune = get_grumpy_fortune()
    
    # Choose a goose art (sometimes use variation for variety)
    if random.random() < 0.3:
        goose = random.choice(GOOSE_VARIATIONS)
    else:
        goose = GOOSE_ART
    
    # Create the fortune message box
    fortune_box = f"""
┌──────────────────────────────────────────────────────┐
│                                                      │
│  {fortune}  │
│                                                      │
└──────────────────────────────────────────────────────┘
"""
    
    # Combine elements
    output = f"""
{fortune_box}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
{goose}
    ~ A grumpy goose has spoken ~
"""
    
    # Add header with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"""
╔══════════════════════════════════════════════════════╗
║         GRUMPY FORTUNE TELLER - {timestamp}          ║
╚══════════════════════════════════════════════════════╝
"""
    
    return header + output

def main():
    """Main function to generate and save fortune."""
    output = generate_fortune_output()
    
    # Check if fortune.md exists, move to /old folder if so
    fortune_path = "fortune.md"
    if os.path.exists(fortune_path):
        old_dir = "old"
        os.makedirs(old_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_dir, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write new fortune
    with open(fortune_path, 'w') as f:
        f.write(output)
    
    print(f"Fortune generated and saved to {fortune_path}")

if __name__ == "__main__":
    main()
