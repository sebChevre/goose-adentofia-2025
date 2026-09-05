#!/usr/bin/env python3
"""
Fortune Generator - A Grumpy Fortune Teller
Generates a fortune from a grumpy, sassy goose and writes it to fortune.md
"""

import os
import shutil
from datetime import datetime

# Grumpy/sassy fortunes from the fortune teller
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
    "The mystical forces say... 'meh'. Even they're not impressed.",
    "I consulted the ancient scrolls. They said 'go touch grass'.",
    "Your aura is... beige. How utterly predictable.",
    "The spirits are too bored to give you a real fortune today.",
    "I see... more coffee. Lots more coffee. That's it. That's the fortune.",
]

# Sassy goose ASCII art - grumpy expression
GOOSE_ART = """
      __
     /  \\
    | o o |
    |  >  |   Hmph!
    \\  _  /
     |   |
     |   |
    /|   |\\
   / |   | \\
  /  |   |  \\
 |   |   |   |
 |   |   |   |
 \\___|___|___/
    /     \\
   |       |
   |       |
   |       |
   |_______|
  _/       \\_
 (           )
  \\_________/
"""

def get_fortune():
    """Return a random grumpy fortune."""
    import random
    return random.choice(FORTUNES)

def generate_fortune_output():
    """Generate the complete fortune output with all decorations."""
    fortune = get_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Define the border width
    border_width = 50
    
    # Create top border
    top_border = "╔" + "═" * (border_width - 2) + "╗"
    bottom_border = "╚" + "═" * (border_width - 2) + "╝"
    side_border = "║"
    
    # Build the output line by line
    output_lines = []
    output_lines.append(top_border)
    
    # Title line
    title = "🔮 GRUMPY FORTUNE TELLER 🔮"
    output_lines.append(f"{side_border} {title.center(border_width - 2)} {side_border}")
    output_lines.append(f"{side_border} {'─' * (border_width - 2)} {side_border}")
    
    # Add goose art with proper padding
    goose_lines = GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        # Center the goose art within the border
        padded_line = line.center(border_width - 2)
        output_lines.append(f"{side_border} {padded_line} {side_border}")
    
    # Add divider between goose and fortune
    output_lines.append(f"{side_border} {'─' * (border_width - 2)} {side_border}")
    
    # Add fortune header
    output_lines.append(f"{side_border} {'YOUR FORTUNE:'.center(border_width - 2)} {side_border}")
    output_lines.append(f"{side_border} {'─' * (border_width - 2)} {side_border}")
    
    # Add fortune text (wrapped if needed)
    # Simple word wrapping for the fortune
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= border_width - 4:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            output_lines.append(f"{side_border} {current_line.center(border_width - 2)} {side_border}")
            current_line = word
    if current_line:
        output_lines.append(f"{side_border} {current_line.center(border_width - 2)} {side_border}")
    
    # Add spacing and timestamp
    output_lines.append(f"{side_border} {' ' * (border_width - 2)} {side_border}")
    output_lines.append(f"{side_border} {'─' * (border_width - 2)} {side_border}")
    output_lines.append(f"{side_border} {f'Generated: {timestamp}'.center(border_width - 2)} {side_border}")
    
    output_lines.append(bottom_border)
    
    # Join all lines
    output = '\n'.join(output_lines)
    
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
        f.write("# 🦢 Grumpy Goose Fortune 🦢\n\n")
        f.write("```\n")
        f.write(fortune_output)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + fortune_output)

if __name__ == "__main__":
    main()
