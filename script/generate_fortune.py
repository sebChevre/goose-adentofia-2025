#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

def get_poetic_fortune():
    """Generate a poetic fortune from the mystical fortune teller."""
    fortunes = [
        "The stars whisper of journeys yet untraveled, where courage blooms like dawn's first light.",
        "A crossroads awaits your step; choose wisely, for destiny dances with the bold.",
        "Hidden treasures lie not in gold, but in the connections you nurture today.",
        "The winds of change carry whispers of renewal—embrace the transformation.",
        "An unexpected encounter shall illuminate a path you thought forgotten.",
        "Patience is the key that unlocks doors you've been pounding upon in vain.",
        "The moon's gentle glow reveals what the sun's harsh light could not show.",
        "Your creative spark shall ignite a flame that warms more than just yourself.",
        "A word spoken in kindness shall echo through corridors you've yet to enter.",
        "The river of time bends toward those who flow with its current, not against.",
        "In the quiet moments between heartbeats, your true answer awaits discovery.",
        "The seeds you plant today in secret shall bear fruit in seasons yet unnamed.",
    ]
    return random.choice(fortunes)

def get_sassy_goose():
    """Return the ASCII art of a sassy goose."""
    return """
    _
   (v\\
   //\\
  (  /
   \\ \\
    \\ \\
    _\\_
   (___)
    | |
   _/_\\_
  |     |
  |     |
  |_____|
    """

def create_ascii_border(content, width=70):
    """Create an ASCII border around the content."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + content.center(width - 2) + "║"
    bottom = "╚" + "═" * (width - 2) + "╝"
    return f"{top_bottom}\n{middle}\n{bottom}"

def generate_fortune_display():
    """Generate the complete fortune display with border, goose, and fortune."""
    fortune = get_poetic_fortune()
    goose_art = get_sassy_goose()
    
    # Create the display
    title = "🔮 Mystic Fortune Teller 🔮"
    date_line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    divider = "─" * 40
    
    # Build the content
    lines = []
    lines.append(title)
    lines.append(date_line)
    lines.append("")
    lines.append("The mystical oracle speaks...")
    lines.append("")
    lines.append(fortune)
    lines.append("")
    lines.append(divider)
    lines.append("")
    lines.append("Your guide to destiny:")
    lines.append(goose_art)
    
    content = "\n".join(lines)
    
    # Add ASCII border
    bordered_content = create_ascii_border(content, width=70)
    
    return bordered_content

def main():
    """Main function to generate and save the fortune."""
    # Define paths
    current_dir = os.getcwd()
    fortune_file = os.path.join(current_dir, "fortune.md")
    old_folder = os.path.join(current_dir, "old")
    
    # If fortune.md exists, move it to /old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        old_file = os.path.join(old_folder, f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
        os.rename(fortune_file, old_file)
        print(f"Previous fortune moved to: {old_file}")
    
    # Generate the fortune display
    fortune_display = generate_fortune_display()
    
    # Write to fortune.md
    with open(fortune_file, "w") as f:
        f.write(f"# 🎭 Daily Fortune 🎭\n\n")
        f.write("```\n")
        f.write(fortune_display)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
