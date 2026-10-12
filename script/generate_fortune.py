#!/usr/bin/env python3
"""
Fortune Generator - A Sarcastic Fortune Teller
Generates fortunes with a sassy goose ASCII art
"""

import os
import random
from datetime import datetime

# Sarcastic fortune messages
FORTUNES = [
    "Your potential is as limitless as your ability to procrastinate.",
    "A wise person once said you're doing great... and that person was you, in a dream.",
    "The stars align to tell you: yes, you really do need more coffee.",
    "Your future looks bright... mostly because you're squinting at your bank account.",
    "Today is a perfect day to pretend you have your life together.",
    "The universe whispers: 'Have you tried actually trying?'",
    "Your charisma is unmatched, especially when you're avoiding responsibilities.",
    "A journey of a thousand miles begins with a single step... or just scrolling more.",
    "Your destiny awaits, right after you finish this episode.",
    "The cosmos say: you're special, like a limited edition mistake.",
    "Your luck is about to change... to slightly different bad luck.",
    "Today's horoscope: You will make decisions you'll question tomorrow.",
    "The universe believes in you, mostly because it has no choice.",
    "Your ambition is inspiring, if only it matched your energy levels.",
    "A great opportunity approaches... it's called 'figuring things out'.",
]

# Sassy goose ASCII art
SASSY_GOOSE = r"""
  __      __
 (o \____/)
 / /      \
( (  @  @  )
 \ \  ^  /
  \ \____/
   /    \
  (      )
  |      |
  |      |
  \      /
   \____/
   /    \
  /      \
 |        |
 |  \__/  |
 |        |
  \______/
"""

# Fortune text with border
def generate_fortune_output():
    fortune = random.choice(FORTUNES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the output with ASCII border
    border_top = "╔" + "═" * 58 + "╗"
    border_mid = "║" + " " * 58 + "║"
    border_bottom = "╚" + "═" * 58 + "╝"
    divider = "╟" + "─" * 58 + "╢"
    
    output = []
    output.append(border_top)
    output.append("║" + " " * 20 + "🔮 FORTUNE TELLER 🔮" + " " * 15 + "║")
    output.append("║" + " " * 22 + f"Generated: {timestamp}" + " " * 11 + "║")
    output.append(border_mid)
    output.append("║" + " " * 58 + "║")
    output.append("║" + " " * 10 + "Your fortune for today:" + " " * 24 + "║")
    output.append("║" + " " * 58 + "║")
    
    # Word wrap the fortune
    words = fortune.split()
    line = "║    "
    for word in words:
        if len(line) + len(word) + 1 <= 58:
            line += word + " "
        else:
            output.append(line.rstrip() + "    ║")
            line = "║    " + word + " "
    output.append(line.rstrip() + "    ║")
    
    output.append("║" + " " * 58 + "║")
    output.append(divider)
    output.append("║" + " " * 58 + "║")
    output.append("║" + SASSY_GOOSE.rstrip() + " " * (58 - len(SASSY_GOOSE.rstrip().split('\n')[0])) + "║")
    
    # Add goose lines with border
    goose_lines = SASSY_GOOSE.strip().split('\n')
    for line in goose_lines[1:]:  # Skip first line, already added
        padded_line = line.ljust(58)
        output.append("║" + padded_line + "║")
    
    output.append("║" + " " * 58 + "║")
    output.append("║" + " " * 15 + "🦢 *sassy goose noises* 🦢" + " " * 15 + "║")
    output.append("║" + " " * 58 + "║")
    output.append(border_bottom)
    
    return '\n'.join(output)

def main():
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    working_dir = os.getcwd()
    fortune_file = os.path.join(working_dir, "fortune.md")
    old_dir = os.path.join(working_dir, "old")
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_dir, exist_ok=True)
        # Move to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_dir, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_file)
        print(f"Moved existing fortune.md to: {old_file}")
    
    # Generate fortune
    fortune_content = generate_fortune_output()
    
    # Write to fortune.md
    with open(fortune_file, 'w', encoding='utf-8') as f:
        f.write(f"# 🦢 Sarcastic Fortune 🦢\n\n")
        f.write("```text\n")
        f.write(fortune_content)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + fortune_content)

if __name__ == "__main__":
    main()
