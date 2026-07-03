#!/usr/bin/env python3
"""
Sarcastic Fortune Teller - A sassy goose delivers your "fate"
"""

import os
import random
from datetime import datetime

# Sarcastic fortune messages
FORTUNES = [
    "Your future looks bright... too bright. You'll need sunglasses.",
    "I see great things in your future. Oh wait, that's just the sun in my eyes.",
    "A surprise awaits you! Try not to faint from the shock.",
    "Your luck is about to change. Unfortunately, it's going downhill.",
    "You will encounter a challenge. No, the other kind of challenge.",
    "Money is coming your way! Well, it's coming, but not to you.",
    "Love is in the air. Unfortunately, it's not for you.",
    "Your dreams will come true. In someone else's life.",
    "A journey awaits! From your bed to the fridge.",
    "Success is just around the corner. Too bad you're facing the wrong way.",
    "You'll meet someone special. They'll be special at ignoring you.",
    "Your hard work will pay off. Eventually. Like, never.",
    "A mysterious stranger will change your life. They'll change your mind about staying away.",
    "Your potential is limitless. Your opportunities, however, are not.",
    "Good things come to those who wait. You've been waiting. Nothing happened.",
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
    <(o )___   *snorts*
     ( ._> /   "Oh, YOU again?"
      \\___/
"""

GOOSE_ART_UNIMPRESSED = """
      __
    <(o )___   *side-eye*
     ( ._> /   "Really?"
      \\___/
"""

GOOSE_ART_EXASPERATED = """
      __
    <(o )___   *deep sigh*
     ( ._> /   "Fine, let me help you."
      \\___/
"""

def get_sassy_goose():
    """Return a random sassy goose ASCII art."""
    gooses = [GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_UNIMPRESSED, GOOSE_ART_EXASPERATED]
    return random.choice(gooses)

def generate_fortune():
    """Generate a sarcastic fortune."""
    return random.choice(FORTUNES)

def create_border(content, width=60):
    """Create an ASCII border around content."""
    border_top = "╔" + "═" * (width - 2) + "╗"
    border_bottom = "╚" + "═" * (width - 2) + "╝"
    
    lines = []
    for line in content.split('\n'):
        padded_line = line.ljust(width - 2)
        lines.append("║" + padded_line + "║")
    
    return border_top + "\n" + "\n".join(lines) + "\n" + border_bottom

def generate_output():
    """Generate the complete fortune output."""
    goose = get_sassy_goose()
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the content
    lines = [
        "",
        "    🦆 SARCASTIC FORTUNE TELLER 🦆",
        "",
        f"    {timestamp}",
        "",
        "    " + "-" * 40,
        "",
        "    Your Fortune:",
        "",
        f"    {fortune}",
        "",
        "    " + "-" * 40,
        "",
        "    Here's your wise prediction, delivered by",
        "    a goose who clearly doesn't care:",
        "",
    ]
    
    # Add goose art with proper indentation
    for line in goose.split('\n'):
        if line.strip():
            lines.append(f"    {line}")
        else:
            lines.append("")
    
    lines.append("")
    lines.append("    Remember: I'm only as accurate as you are patient.")
    lines.append("")
    
    content = '\n'.join(lines)
    return create_border(content, 60)

def main():
    """Main function to generate and save fortune."""
    # Generate the fortune output
    output = generate_output()
    
    # Check if fortune.md exists
    fortune_path = "fortune.md"
    old_dir = "old"
    
    if os.path.exists(fortune_path):
        # Create old directory if it doesn't exist
        if not os.path.exists(old_dir):
            os.makedirs(old_dir)
        
        # Move existing file to old directory with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_dir, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Write the new fortune file
    with open(fortune_path, 'w') as f:
        f.write(output)
    
    print(f"Fortune generated and saved to {fortune_path}")
    print("\n" + output)

if __name__ == "__main__":
    main()
