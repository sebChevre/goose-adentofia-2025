#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Wise fortunes from the fortune teller
FORTUNES = [
    "The path you seek is not straight, but winding like a river. Trust your instincts.",
    "Wisdom comes not from knowing all answers, but from asking the right questions.",
    "A challenge awaits, but you possess the strength to overcome it.",
    "The stars align in your favor, yet patience remains your greatest ally.",
    "What you seek is already within you. Look inward for the truth.",
    "Change is coming like the seasons. Embrace it with an open heart.",
    "Your past mistakes are but stepping stones to your future greatness.",
    "The answer lies not in what you see, but in what you feel.",
    "A unexpected connection will bring clarity to your current dilemma.",
    "Trust in the journey, even when the destination remains unclear."
]

# ASCII art of a sassy goose
SASSY_GOOSE = """
  __      __
 / \\_____/ \\
|  o     o  |
|     <     |  *HONK!*
|   \\___/   |
 \\  -----  /
  \\_______/
    |   |
    |   |
   /|   |\\
  / |   | \\
"""

def generate_fortune():
    """Generate a random wise fortune."""
    return random.choice(FORTUNES)

def create_border(text, width=60):
    """Create an ASCII border around text."""
    border_top = "╔" + "═" * (width - 2) + "╗"
    border_bottom = "╚" + "═" * (width - 2) + "╝"
    
    lines = text.split('\n')
    bordered_lines = []
    
    for line in lines:
        # Pad line to fit within border
        padded = line.ljust(width - 2)[:width - 2]
        bordered_lines.append("║" + padded + "║")
    
    return border_top + "\n" + "\n".join(bordered_lines) + "\n" + border_bottom

def format_fortune_output(fortune):
    """Format the complete fortune output with goose, divider, and border."""
    width = 60
    
    # Create the divider
    divider = "║" + "─" * (width - 2) + "║"
    
    # Format the goose art
    goose_lines = SASSY_GOOSE.strip().split('\n')
    formatted_goose = []
    for line in goose_lines:
        formatted_goose.append("║  " + line.ljust(width - 6) + "  ║")
    
    # Format the fortune text
    fortune_lines = fortune.split('\n')
    formatted_fortune = []
    for line in fortune_lines:
        formatted_fortune.append("║  " + line.ljust(width - 6) + "  ║")
    
    # Build the complete output
    output_parts = []
    
    # Header
    output_parts.append("║" + " " * (width - 2) + "║")
    output_parts.append("║   🔮 WISE FORTUNE TELLER 🔮".ljust(width - 2) + "║")
    output_parts.append("║" + " " * (width - 2) + "║")
    
    # Goose section
    output_parts.extend(formatted_goose)
    
    # Divider
    output_parts.append(divider)
    
    # Fortune section
    output_parts.append("║" + " " * (width - 2) + "║")
    output_parts.append("║   ✨ YOUR FORTUNE ✨".ljust(width - 2) + "║")
    output_parts.append("║" + " " * (width - 2) + "║")
    output_parts.extend(formatted_fortune)
    output_parts.append("║" + " " * (width - 2) + "║")
    
    # Footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_parts.append("║" + " " * (width - 2) + "║")
    output_parts.append(f"║   Generated: {timestamp}".ljust(width - 2) + "║")
    output_parts.append("║" + " " * (width - 2) + "║")
    
    # Add top and bottom borders
    full_text = "\n".join(output_parts)
    return create_border_content(full_text, width)

def create_border_content(content, width):
    """Add outer border to content."""
    border_top = "┌" + "─" * (width - 2) + "┐"
    border_bottom = "└" + "─" * (width - 2) + "┘"
    return border_top + "\n" + content + "\n" + border_bottom

def handle_existing_file():
    """Move existing fortune.md to old folder if it exists."""
    fortune_file = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        old_path = os.path.join(old_folder, f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
        os.rename(fortune_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")

def main():
    """Main function to generate and save fortune."""
    # Generate the fortune
    fortune = generate_fortune()
    
    # Format the output
    output = format_fortune_output(fortune)
    
    # Handle existing file
    handle_existing_file()
    
    # Write to fortune.md
    with open("fortune.md", "w") as f:
        f.write(output)
    
    print("Fortune generated successfully! Check fortune.md")
    print("\n" + output)

if __name__ == "__main__":
    main()
