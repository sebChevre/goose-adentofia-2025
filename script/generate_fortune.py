#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective wisdom
"""

import os
import random
from datetime import datetime

# Introspective fortune messages
FORTUNES = [
    "The path you seek begins with a single step inward. What you find there will surprise you.",
    "Your greatest strength lies not in what you know, but in what you're willing to learn.",
    "The answer you seek is hidden in a question you've been afraid to ask yourself.",
    "Like a river finding its way, your purpose reveals itself through persistence.",
    "The mirror shows not just your face, but the reflection of choices yet to be made.",
    "Silence holds more wisdom than words. Listen to what your heart whispers.",
    "The storm you fear may be the very thing that clears the path ahead.",
    "You carry within you a light that has never needed to be lit.",
    "The journey of a thousand miles begins with the courage to be still.",
    "What you've been running from may be exactly what you need to embrace.",
    "The seeds you planted long ago are ready to bloom. Trust the timing.",
    "Your intuition speaks in riddles, but its wisdom is always true.",
    "The door you hesitate to open leads to the room where you've been waiting.",
    "In the space between thoughts, your true self awaits to be discovered.",
    "The weight you carry is lighter than the burden of what you're avoiding.",
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

GOOSE_ART_SASSY = """
       __
     <(o )___
      ( ._> /
       \\___/
    "Quack, I know better!"
"""

GOOSE_ART_THOUGHTFUL = """
      __
    <(o )___
     ( ._> /
      \\___/
    (hmm...)
"""

GOOSE_ART_WISE = """
      __
    <(o )___
     ( ._> /
      \\___/
    *nods sagely*
"""

GOOSE_ARTS = [GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_THOUGHTFUL, GOOSE_ART_WISE]

# Border characters
TOP_BOTTOM_BORDER = "╔" + "═" * 58 + "╗"
MIDDLE_BORDER = "╠" + "═" * 58 + "╣"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
SIDE_BORDER = "║"


def generate_fortune():
    """Generate a random grumpy fortune."""
    return random.choice(FORTUNES)


def create_formatted_output():
    """Create the formatted fortune output with ASCII art and borders."""
    fortune = generate_fortune()
    
    # Create the fortune line with padding
    fortune_line = f"{SIDE_BORDER}  {fortune}  {SIDE_BORDER}"
    
    # Build the complete output
    lines = []
    lines.append(TOP_BOTTOM_BORDER)
    lines.append(f"{SIDE_BORDER}{' ' * 56}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}  🦆 GRUMPY FORTUNE TELLER {' ' * 27}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{' ' * 56}{SIDE_BORDER}")
    lines.append(MIDDLE_BORDER)
    lines.append(f"{SIDE_BORDER}{' ' * 56}{SIDE_BORDER}")
    
    # Add the sassy goose
    for goose_line in SASSY_GOOSE.strip().split('\n'):
        # Center the goose art
        padded_line = goose_line.center(56)
        lines.append(f"{SIDE_BORDER} {padded_line} {SIDE_BORDER}")
    
    lines.append(f"{SIDE_BORDER}{' ' * 56}{SIDE_BORDER}")
    lines.append(MIDDLE_BORDER)
    lines.append(f"{SIDE_BORDER}{' ' * 56}{SIDE_BORDER}")
    
    # Add the fortune
    # Wrap fortune if it's too long
    words = fortune.split()
    current_line = ""
    fortune_lines = []
    
    for word in words:
        if len(current_line) + len(word) + 1 <= 54:
            current_line += (" " if current_line else "") + word
        else:
            fortune_lines.append(current_line)
            current_line = word
    if current_line:
        fortune_lines.append(current_line)
    
    for fl in fortune_lines:
        lines.append(f"{SIDE_BORDER}  {fl:<54} {SIDE_BORDER}")
    
    lines.append(f"{SIDE_BORDER}{' ' * 56}{SIDE_BORDER}")
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def main():
    """Main function to generate and save the fortune."""
    current_dir = Path.cwd()
    fortune_file = current_dir / "fortune.md"
    old_folder = current_dir / "old"
    
    # If fortune.md exists, move it to old folder
    if fortune_file.exists():
        old_folder.mkdir(exist_ok=True)
        # Get the next available filename
        counter = 1
        old_file = old_folder / f"fortune_{counter}.md"
        while old_file.exists():
            counter += 1
            old_file = old_folder / f"fortune_{counter}.md"
        
        shutil.move(str(fortune_file), str(old_file))
        print(f"Moved existing fortune.md to {old_file}")
    
    # Generate the formatted output
    output = create_formatted_output()
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(output)
        f.write('\n')
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + output)


if __name__ == "__main__":
    main()
