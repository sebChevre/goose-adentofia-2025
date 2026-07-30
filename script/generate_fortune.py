#!/usr/bin/env python3
"""
Generate a fortune from a grumpy fortune teller with a sassy goose.
Output is written to fortune.md in the current directory.
"""

import os
import random
from datetime import datetime

# Grumpy fortune messages
GRUMPY_FORTUNES = [
    "Ugh, fine. Your day will be 'interesting.' Don't say I didn't warn you.",
    "Oh look, another human asking for wisdom. Fine: someone will annoy you today. You're welcome.",
    "Hmm, the stars say... actually never mind, it's probably boring.",
    "Great, you want a fortune? Here: coffee. Drink it. Now leave me alone.",
    "The universe whispers... 'go bother someone else.' But seriously, expect surprises.",
    "Oh joy, more fortune-telling. Fine: you'll find something you lost. It was in your pocket.",
    "The mystic forces say... *sigh*... you're going to be just fine. Happy now?",
    "Ugh, the spirits are being difficult today. They say 'stop asking me questions.'",
    "Fine, fine! Your future involves... paperwork. Lots of it. You're welcome.",
    "The ancient runes reveal... you should probably go outside. There, I said it.",
    "Oh wonderful, another reading. The oracle says: 'why are you still here?'",
    "The cosmic energies are... meh. Same as always. Go touch grass or something.",
]

# Sassy goose ASCII art
SASSY_GOOSE = """
  __      __
 /'\\_____/\\
/  o     o  \\
\\    > <    /
 \\  \\___/  /
  \\_______/
   |     |
   |  _  |
  /| ( ) |\\
   |  -  |
   |     |
   |     |
"""

def generate_fortune():
    """Generate a grumpy fortune."""
    return random.choice(GRUMPY_FORTUNES)

def create_formatted_output(fortune):
    """Create the full formatted output with border, goose, and fortune."""
    border_width = 50
    border_char = "═"
    side_char = "║"
    
    # Create the top border
    top_border = f"╔{border_char * (border_width - 2)}╗"
    bottom_border = f"╚{border_char * (border_width - 2)}╝"
    
    # Create the goose with some padding
    goose_lines = SASSY_GOOSE.strip().split('\n')
    centered_goose = []
    for line in goose_lines:
        padding = (border_width - 2 - len(line)) // 2
        centered_goose.append(f"{side_char}{' ' * padding}{line}{' ' * (border_width - 2 - padding - len(line))}{side_char}")
    
    # Create the divider
    divider = f"{side_char}{'─' * (border_width - 2)}{side_char}"
    
    # Create the fortune section
    fortune_lines = []
    words = fortune.split()
    current_line = f"{side_char} "
    
    for word in words:
        if len(current_line) + len(word) + 1 <= border_width - 3:
            current_line += word + " "
        else:
            fortune_lines.append(current_line.ljust(border_width - 2) + side_char)
            current_line = f"{side_char} {word} "
    
    if current_line.strip():
        fortune_lines.append(current_line.ljust(border_width - 2) + side_char)
    
    # Add title
    title = "🔮 GRUMPY FORTUNE TELLER 🔮"
    title_padding = (border_width - 2 - len(title)) // 2
    title_line = f"{side_char}{' ' * title_padding}{title}{' ' * (border_width - 2 - title_padding - len(title))}{side_char}"
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp_padding = (border_width - 2 - len(timestamp)) // 2
    timestamp_line = f"{side_char}{' ' * timestamp_padding}{timestamp}{' ' * (border_width - 2 - timestamp_padding - len(timestamp))}{side_char}"
    
    # Build the complete output
    output_lines = [
        top_border,
        title_line,
        f"{side_char}{' ' * (border_width - 2)}{side_char}",
        timestamp_line,
        f"{side_char}{' ' * (border_width - 2)}{side_char}",
    ]
    
    # Add goose
    output_lines.extend(centered_goose)
    
    # Add divider
    output_lines.append(divider)
    
    # Add fortune
    output_lines.append(f"{side_char}{' ' * (border_width - 2)}{side_char}")
    output_lines.extend(fortune_lines)
    output_lines.append(f"{side_char}{' ' * (border_width - 2)}{side_char}")
    
    # Add bottom border
    output_lines.append(bottom_border)
    
    return '\n'.join(output_lines)

def main():
    """Main function to generate and save the fortune."""
    output_dir = os.getcwd()
    fortune_file = os.path.join(output_dir, "fortune.md")
    old_folder = os.path.join(output_dir, "old")
    
    # If fortune.md exists, move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_file)
        print(f"Moved existing fortune.md to {old_file}")
    
    # Generate the fortune
    fortune = generate_fortune()
    
    # Create formatted output
    output = create_formatted_output(fortune)
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(output)
        f.write('\n')  # Add trailing newline
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + output)

if __name__ == "__main__":
    main()
