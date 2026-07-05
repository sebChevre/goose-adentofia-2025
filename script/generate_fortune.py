#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import shutil
import random

# Poetic fortunes
FORTUNES = [
    "The stars whisper of adventures yet untold,\n  Where courage blooms and hearts grow bold.",
    "A path of gold awaits your careful feet,\n  Where wisdom and delight shall meet.",
    "Beware the shadow, trust the light,\n  For dawn will bring what suits you right.",
    "In quiet moments, truth is found,\n  Where silence speaks without a sound.",
    "The winds of change are gently blowing,\n  New horizons wait, your spirit growing.",
    "A friend's true word shall guide your way,\n  And turn the darkest night to day.",
    "Like rivers flow to meet the sea,\n  Your destiny calls out to thee.",
    "The moon reveals what sun conceals,\n  In twilight's grace, what fortune feels."
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
    <(o______/>
     /       \\
    /    _    \\
   |    ( )    |
   |     |     |
   |    / \\    |
   |   |   |   |
   |   |   |   |
   \\  |   |  /
    \\ |   | /
     \\|   |/
      |   |
      |   |
      |   |
"""

def generate_fortune():
    """Generate a random poetic fortune."""
    return random.choice(FORTUNES)

def create_border(content, width=60):
    """Create an ASCII border around content."""
    top_bottom = "+" + "-" * (width - 2) + "+"
    lines = content.split('\n')
    
    result = [top_bottom]
    for line in lines:
        # Pad line to fit within border
        padded = line.ljust(width - 2)
        result.append("|" + padded[:width-2] + "|")
    result.append(top_bottom)
    
    return '\n'.join(result)

def create_fortune_display():
    """Create the complete fortune display with goose and border."""
    fortune = generate_fortune()
    
    # Create divider
    divider = "=" * 58
    
    # Combine elements
    display_parts = [
        "   ~*~ Your Poetic Fortune ~*~",
        "",
        fortune,
        "",
        divider,
        "",
        GOOSE_ART.strip()
    ]
    
    full_content = '\n'.join(display_parts)
    
    # Add border
    bordered = create_border(full_content, 60)
    
    return bordered

def main():
    """Main function to generate and save fortune."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.getcwd()
    fortune_file = os.path.join(current_dir, "fortune.md")
    old_folder = os.path.join(current_dir, "old")
    
    # Generate fortune
    fortune_display = create_fortune_display()
    
    # Add markdown header
    md_content = f"# 🦢 Your Fortune 🦢\n\n```\n{fortune_display}\n```\n"
    
    # Handle existing file
    if os.path.exists(fortune_file):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        timestamp = len(os.listdir(old_folder)) + 1
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        shutil.move(fortune_file, old_path)
        print(f"Moved existing fortune to: {old_path}")
    
    # Write new fortune file
    with open(fortune_file, 'w') as f:
        f.write(md_content)
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
