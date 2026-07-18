#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose delivers introspective fortunes
"""

import os
import random
from datetime import datetime

# Introspective fortunes
FORTUNES = [
    "The path you seek is not ahead, but within the quiet moments you've been avoiding.",
    "Your greatest strength lies in the vulnerability you've been too proud to show.",
    "The question you're afraid to ask is the one that will set you free.",
    "What you call a wound is actually a door you haven't learned to open yet.",
    "The silence you fear is not empty—it's waiting for your voice.",
    "You've been looking for answers in places that only hold echoes of who you were.",
    "The weight you carry is not yours to bear forever. Put it down.",
    "Your intuition knows the way, even when your mind refuses to follow.",
    "The person you're running from is the one who holds your next breakthrough.",
    "What feels like an ending is actually the universe making space for something true.",
]

# Sassy goose ASCII art
GOOSE_ART = """
   __      __
  /  \\    /  \\
 |    \\/\\    |
 |   O    O   |
 |     <      |
  \\    __    /
   \\__/  \\__/
   /        \\
  |  ~~~~~   |
  |  \\____/  |
  |          |
  \\__________/
"""

def generate_fortune():
    """Generate a random introspective fortune."""
    return random.choice(FORTUNES)

def create_bordered_output(fortune, goose_art):
    """Create visually appealing output with border, fortune, divider, and goose."""
    # Create the fortune section with some styling
    fortune_lines = fortune.split('\n')
    
    # Build the content with proper spacing
    content_lines = []
    
    # Add fortune with some visual treatment
    content_lines.append("  ✦  YOUR FORTUNE  ✦")
    content_lines.append("")
    for line in fortune_lines:
        content_lines.append(f"  {line}")
    content_lines.append("")
    
    # Create divider
    divider = "  " + "─" * 38
    
    # Combine all parts
    all_lines = content_lines + [divider, goose_art]
    
    # Calculate max width for border
    max_width = max(len(line) for line in all_lines)
    border_width = max_width + 4
    
    # Create top border
    border_top = "╔" + "═" * (border_width - 2) + "╗"
    border_bottom = "╚" + "═" * (border_width - 2) + "╝"
    border_side = "║" + " " * (border_width - 2) + "║"
    
    # Build final output
    output = []
    output.append(border_top)
    output.append(f"║{'  ✧ ✦ ✧  Introspective Fortune ✧ ✦ ✧  ':^{border_width-2}}║")
    output.append(f"║{' '* (border_width-2)}║")
    
    for line in all_lines:
        # Pad each line to fit within border
        padded_line = line.ljust(border_width - 2)
        output.append(f"║{padded_line}║")
    
    output.append(f"║{' '* (border_width-2)}║")
    output.append(f"║{'  Generated on ' + datetime.now().strftime('%Y-%m-%d %H:%M'):^{border_width-2}}║")
    output.append(border_bottom)
    
    return '\n'.join(output)

def main():
    """Main function to generate fortune and save to file."""
    output_dir = os.getcwd()
    fortune_file = os.path.join(output_dir, 'fortune.md')
    old_dir = os.path.join(output_dir, 'old')
    
    # If fortune.md exists, move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_name = f'fortune_{timestamp}.md'
        old_path = os.path.join(old_dir, old_name)
        os.rename(fortune_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate fortune
    fortune = generate_fortune()
    
    # Create formatted output
    output = create_bordered_output(fortune, GOOSE_ART)
    
    # Write to markdown file
    with open(fortune_file, 'w') as f:
        f.write("# 🌟 Your Introspective Fortune 🌟\n\n")
        f.write("```text\n")
        f.write(output)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + output)

if __name__ == "__main__":
    main()
