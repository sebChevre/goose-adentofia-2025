#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""
import os
import random
from datetime import datetime

# Sassy Goose ASCII Art
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

# More elaborate sassy goose variations
GOOSE_VARIATIONS = [
    """
      __
    <(o )___
     ( ._> /
      \\___/
    *sassy*
""",
    """
      __
    <(o )___
     ( ._> /
      \\___/
    honk!
""",
    """
      __
    <(o )___
     ( ._> /
      \\___/
    feathered
""",
]

# Poetic fortunes from the mystical fortune teller
FORTUNES = [
    "The stars whisper that your path shall bloom with unexpected joy.",
    "A river of opportunity flows toward you; dip your cup and drink deep.",
    "The winds of change carry whispers of triumph on the horizon.",
    "Like a garden after rain, your efforts shall blossom beautifully.",
    "The moon smiles upon your endeavors; success is woven in your fate.",
    "A surprise awaits you, as sweet as morning dew on fresh petals.",
    "The cosmic dance aligns in your favor; step forward with confidence.",
    "Like a phoenix from the ashes, your brilliance shall shine anew.",
    "The universe conspires to bring you a treasure beyond measure.",
    "Your journey winds through golden fields; peace and prosperity await.",
]

# ASCII Border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
SIDE_BORDER = "║"
DIVIDER = "╟" + "─" * 58 + "╢"


def generate_fortune():
    """Generate a poetic fortune with sassy goose ASCII art."""
    fortune = random.choice(FORTUNES)
    goose = random.choice(GOOSE_VARIATIONS)
    
    # Build the fortune message
    lines = []
    
    # Top border
    lines.append(TOP_BORDER)
    
    # Header
    lines.append(f"{SIDE_BORDER}{'🔮 MYSTIC FORTUNE TELLER 🔮':^56}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{'Generated on: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'):^56}{SIDE_BORDER}")
    lines.append(f"{SIDE_BORDER}{'':^56}{SIDE_BORDER}")
    
    # Fortune text with proper formatting
    fortune_lines = fortune.split()
    wrapped_lines = []
    current_line = ""
    
    for word in fortune_lines:
        if len(current_line) + len(word) + 1 <= 54:
            current_line += " " + word if current_line else word
        else:
            wrapped_lines.append(current_line)
            current_line = word
    if current_line:
        wrapped_lines.append(current_line)
    
    lines.append(f"{SIDE_BORDER}{'':^56}{SIDE_BORDER}")
    for line in wrapped_lines:
        lines.append(f"{SIDE_BORDER} {line:^54} {SIDE_BORDER}")
    
    lines.append(f"{SIDE_BORDER}{'':^56}{SIDE_BORDER}")
    
    # Divider
    lines.append(DIVIDER)
    lines.append(f"{SIDE_BORDER}{'':^56}{SIDE_BORDER}")
    
    # Sassy Goose ASCII Art (centered)
    goose_lines = goose.strip().split('\n')
    for goose_line in goose_lines:
        # Center the goose art
        padded_line = goose_line.center(56)
        lines.append(f"{SIDE_BORDER}{padded_line}{SIDE_BORDER}")
    
    lines.append(f"{SIDE_BORDER}{'':^56}{SIDE_BORDER}")
    
    # Bottom border
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def main():
    """Main function to generate and save fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md already exists
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune
    fortune_output = generate_fortune()
    
    # Write to fortune.md
    with open(output_file, 'w') as f:
        f.write(fortune_output)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + fortune_output)


if __name__ == "__main__":
    main()
