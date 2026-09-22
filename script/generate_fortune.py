#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose delivers introspective wisdom
"""

import os
import random
from datetime import datetime

def get_fortune():
    """Return a random introspective fortune."""
    fortunes = [
        "The answers you seek are not found in the stars, but in the quiet moments between your thoughts.",
        "Today, ask yourself: What would I do if I weren't afraid of my own potential?",
        "A mirror reflects what is, but only you can decide what should be.",
        "The weight you carry is not a burden—it is the anchor that keeps you grounded while you learn to fly.",
        "In the silence of your own company, you will find the loudest truths.",
        "Your reflection shows not who you were, but who you are becoming.",
        "The path ahead is not written in stone, but in the footprints you choose to leave.",
        "Sometimes the deepest wisdom comes from asking the simplest question: 'What do I truly want?'",
        "The shadows you avoid are the same ones that give your light meaning.",
        "You are both the question and the answer, dancing together in the dark.",
    ]
    return random.choice(fortunes)

def get_sassy_goose():
    """Return ASCII art of a sassy goose."""
    goose_art = """
     __
    /  \\
   |    |
   |    |
   \\    /
    \\/\\/
    /  \\
   |  |
   |  |
   |  |
   |  |
  _/  \\_
 (      )
  \\    /
   \\__/
    ||
    ||
    ||
    ||
   _||_
  (____)
    """
    return goose_art

def create_border(text_lines, padding=2):
    """Create an ASCII border around the content."""
    max_length = max(len(line.rstrip()) for line in text_lines)
    border_width = max_length + (padding * 2) + 4
    
    top_border = "╔" + "═" * (border_width - 2) + "╗"
    bottom_border = "╚" + "═" * (border_width - 2) + "╝"
    
    bordered_lines = []
    for line in text_lines:
        padded = " " * padding + line.rstrip() + " " * (max_length - len(line.rstrip()) + padding)
        bordered_lines.append("║" + padded + "║")
    
    return [top_border] + bordered_lines + [bottom_border]

def generate_fortune_output():
    """Generate the complete fortune output with ASCII art and border."""
    fortune = get_fortune()
    goose = get_sassy_goose()
    
    # Build the content
    lines = []
    
    # Header
    lines.append("🔮  MYSTIC FORTUNE  🔮")
    lines.append("")
    lines.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    
    # Fortune text
    lines.append("─" * 40)
    lines.append("✨  YOUR FORTUNE  ✨")
    lines.append("─" * 40)
    lines.append("")
    lines.append(f"  {fortune}")
    lines.append("")
    lines.append("─" * 40)
    
    # Divider
    lines.append("═══  🪿  THE SASSY GOOSE SPEAKS  🪿  ═══")
    lines.append("")
    
    # Add goose art lines
    for line in goose.strip().split('\n'):
        lines.append(f"  {line}")
    
    # Footer
    lines.append("")
    lines.append("─" * 40)
    lines.append("Remember: The goose knows what you're thinking.")
    
    # Create bordered output
    bordered_content = create_border(lines)
    
    return '\n'.join(bordered_content)

def main():
    """Main function to generate and save the fortune."""
    output_dir = os.getcwd()
    fortune_file = os.path.join(output_dir, "fortune.md")
    old_folder = os.path.join(output_dir, "old")
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_file)
        print(f"Moved existing fortune.md to: {old_file}")
    
    # Generate the fortune
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
