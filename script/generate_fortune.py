#!/usr/bin/env python3
"""
Fortune Generator - A Sarcastic Fortune Teller
Generates a fortune from a sassy goose and writes it to fortune.md
"""

import os
import shutil
from datetime import datetime

# Sarcastic fortunes from the sassy goose
FORTUNES = [
    "Ah, I see your future... it involves more scrolling and less doing. Shocking.",
    "The stars align to tell me one thing: you should probably drink more water.",
    "I sense a great opportunity coming your way. Too bad you'll probably ignore it.",
    "Your future self is judging your current decisions. Hard.",
    "The universe has a plan for you. It's mostly just awkward silences.",
    "I see... oh wait, that's just your reflection in my crystal ball. You're the problem.",
    "Great news! Your luck is about to change. Bad news: it's getting worse.",
    "The cosmos whisper: 'Have you tried turning yourself off and on again?'",
    "I predict with 100% certainty that you'll read another fortune tomorrow.",
    "Your destiny? Honestly, I'm not sure you have one. But here's hoping!",
]

# Sassy goose ASCII art
GOOSE_ART = """
  __      __
 /'\\_____/\\
/  o     o  \\
\\    > <    /
 \\  \\___/  /
  \\_______/
   /     \\
  /       \\
 /         \\
/___________\\
   \\_____/
    |   |
    |   |
   /|   |\\
  / |   | \\
 /  |   |  \\
|   |   |   |
|   |   |   |
\\___|___|___/
"""

def get_fortune():
    """Return a random sarcastic fortune."""
    import random
    return random.choice(FORTUNES)

def create_ascii_border(content, width=60):
    """Create an ASCII border around the content."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + content.center(width - 2) + "║"
    return f"{top_bottom}\n{middle}\n{'╚' + '═' * (width - 2) + '╝'}"

def generate_fortune_output():
    """Generate the complete fortune output with all decorations."""
    fortune = get_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the fortune section
    fortune_lines = fortune.split('\n')
    fortune_box = []
    for line in fortune_lines:
        fortune_box.append(f"  {line}")
    
    # Create the divider
    divider = "  " + "─" * 56
    
    # Combine goose, divider, and fortune
    inner_content = f"{GOOSE_ART}\n\n{divider}\n\n" + '\n'.join(fortune_box) + "\n"
    
    # Add timestamp
    inner_content += f"\n  Generated: {timestamp}"
    
    # Create the bordered output
    output = create_ascii_border(inner_content, 60)
    
    return output

def main():
    """Main function to generate and save the fortune."""
    # Current working directory
    cwd = os.getcwd()
    fortune_file = os.path.join(cwd, "fortune.md")
    old_folder = os.path.join(cwd, "old")
    
    # If fortune.md exists, move it to /old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_name = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_name)
        shutil.move(fortune_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune
    fortune_output = generate_fortune_output()
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(f"# 🦢 Sassy Goose Fortune 🦢\n\n")
        f.write(fortune_output)
        f.write("\n")
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + fortune_output)

if __name__ == "__main__":
    main()
