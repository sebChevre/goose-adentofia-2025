#!/usr/bin/env python3
"""
Grumpy Fortune Teller - Generates fortunes with a sassy goose
"""

import os
import random
import shutil
from pathlib import Path

# Sassy goose ASCII art
SASSY_GOOSE = """
     __      __
    /  \\    /  \\
   |    \\__/    |
   |  o      o  |
   |     <      |  Hmph!
   |   \\____/   |
    \\  \\    /  /
     \\  \\__/  /
      \\______/
"""

# Grumpy fortune messages
FORTUNES = [
    "Your path is clear, but don't expect me to celebrate with you.",
    "Success is coming... eventually. Try not to get too excited.",
    "A surprise awaits, but I'm not telling you what it is. Figure it out yourself.",
    "Your hard work will pay off. Don't get cocky about it.",
    "Someone is talking about you. Probably complaining, but who cares?",
    "The stars say you'll succeed. The stars are wrong, but whatever.",
    "A new opportunity is coming. Don't mess it up like last time.",
    "Your luck is improving. Barely.",
    "Challenges await, but you'll probably figure it out somehow.",
    "A friend needs you. Try not to be too difficult about it.",
    "Your persistence will be rewarded. Finally.",
    "Watch out for obstacles. Or don't, see if I care.",
    "Good things are coming. Don't get your hopes up too high.",
    "You'll overcome your problems. It'll be messy, but you'll manage.",
    "The universe has plans for you. They're probably complicated.",
]

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
