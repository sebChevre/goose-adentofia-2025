#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Fortune messages with poetic moods
FORTUNES = [
    "The stars whisper of adventures waiting just beyond your horizon.",
    "A unexpected joy approaches on wings of golden opportunity.",
    "The universe conspires to bring you wisdom in unexpected places.",
    "Your path forward shines bright with possibilities yet unseen.",
    "Like morning dew on fresh petals, new beginnings await you.",
    "The winds of change carry whispers of your greatest triumph.",
    "A moment of clarity will illuminate your darkest doubts.",
    "The tapestry of fate weaves threads of fortune in your favor.",
    "Ancient wisdom guides you toward a destiny of wonder.",
    "The moon's gentle light reveals a secret waiting to be discovered.",
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
    <(o______)
    (         )
     (_______)
      /     \\
     /       \\
    /         \\
   /___________\\
"""

# Alternative sassy goose variations
GOOSE_VARIATIONS = [
    """
      __
    <(o______)
    (         )
     (_______)
      /     \\
     /       \\
    /         \\
   /___________\\
""",
    """
      __
    <(O___O)
    (   _   )
     (_____)
      /   \\
     /     \\
    /_______\\
""",
    """
      __
    <(@___@)
    (  ___  )
     (_____)
      /   \\
     /     \\
    /_______\\
""",
]

def generate_fortune():
    """Generate a random poetic fortune."""
    return random.choice(FORTUNES)

def get_sassy_goose():
    """Get a random sassy goose ASCII art."""
    return random.choice(GOOSE_VARIATIONS)

def create_bordered_content(fortune, goose):
    """Create the final bordered content with fortune and goose."""
    border_char = "═"
    side_char = "║"
    
    # Calculate the width needed
    max_width = max(len(line) for line in fortune.split('\n') + 
                    goose.split('\n') + 
                    ["Your Fortune", "═══════════════"])
    
    # Ensure minimum width
    max_width = max(max_width, 40)
    
    lines = []
    
    # Top border
    lines.append("╔" + border_char * max_width + "╗")
    
    # Fortune title
    title = "Your Fortune"
    padding = (max_width - len(title)) // 2
    lines.append(f"║{' ' * padding}{title}{' ' * (max_width - len(title) - padding)}║")
    
    # Fortune content
    for line in fortune.split('\n'):
        padding = (max_width - len(line)) // 2
        lines.append(f"║{' ' * padding}{line}{' ' * (max_width - len(line) - padding)}║")
    
    # Divider line
    lines.append(f"║{'─' * max_width}║")
    
    # Goose title
    goose_title = "Your Sassy Guide"
    padding = (max_width - len(goose_title)) // 2
    lines.append(f"║{' ' * padding}{goose_title}{' ' * (max_width - len(goose_title) - padding)}║")
    
    # Goose ASCII art (centered)
    for line in goose.split('\n'):
        if line.strip():
            padding = (max_width - len(line)) // 2
            lines.append(f"║{' ' * padding}{line}{' ' * (max_width - len(line) - padding)}║")
        else:
            lines.append(f"║{' ' * max_width}║")
    
    # Bottom border
    lines.append("╚" + border_char * max_width + "╝")
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"\nGenerated on: {timestamp}")
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save the fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md already exists
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Get current timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        
        # Move existing file to old folder
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate fortune and goose
    fortune = generate_fortune()
    goose = get_sassy_goose()
    
    # Create the final content
    content = create_bordered_content(fortune, goose)
    
    # Write to fortune.md
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + content)

if __name__ == "__main__":
    main()
