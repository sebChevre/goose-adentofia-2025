#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective wisdom
"""

import os
import random
from datetime import datetime

# Introspective fortunes
FORTUNES = [
    "The path you seek is already beneath your feet. Walk mindfully.",
    "Your reflection reveals more truth than any mirror could show.",
    "The answers you pursue dwell within the quiet spaces of your heart.",
    "Like a river carving stone, your persistence shapes your destiny.",
    "What you seek is also seeking you. Be still and listen.",
    "The bird that flies alone finds the clearest skies. Trust your wings.",
    "Your shadow grows longer as the sun rises within you.",
    "The question you ask holds the key to the answer you fear.",
    "In the mirror of another's eyes, you see only what you bring.",
    "The weight you carry is lighter than the fear of letting go.",
    "Your footsteps echo in places you have yet to visit.",
    "The silence between thoughts holds the wisdom you seek.",
    "What seems like a beginning is often a return to yourself.",
    "The goose that quacks loudest is often the one most afraid.",
    "Your intuition whispers; only the quiet can hear it.",
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
     <(o )___  *snort*
      ( ._> /  "Oh, you want wisdom?"
       \\___/   *adjusts feathers*"
"""

GOOSE_ART_THOUGHTFUL = """
       __
     <(o )___
      ( ._> /   Hmm...
       \\___/   *ponders deeply*
"""

GOOSE_ART_WISE = """
       __
     <(o )___  *squints wisely*
      ( ._> /  "Ah, I see..."
       \\___/   *fluffs feathers*
"""

def get_random_fortune():
    """Return a random introspective fortune."""
    return random.choice(FORTUNES)

def get_random_goose_art():
    """Return a random sassy goose ASCII art."""
    art_options = [GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_THOUGHTFUL, GOOSE_ART_WISE]
    return random.choice(art_options)

def create_border(content, width):
    """Create an ASCII border around content."""
    border_top = "╔" + "═" * width + "╗"
    border_bottom = "╚" + "═" * width + "╝"
    border_side = "║"
    
    lines = content.split('\n')
    bordered_lines = []
    
    for line in lines:
        # Pad line to width
        padded = line + " " * (width - len(line))
        bordered_lines.append(f"{border_side} {padded} {border_side}")
    
    return f"{border_top}\n" + "\n".join(bordered_lines) + f"\n{border_bottom}"

def generate_fortune_output():
    """Generate the complete fortune output with ASCII art and formatting."""
    fortune = get_random_fortune()
    goose_art = get_random_goose_art()
    
    # Get current date/time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the content
    content_lines = [
        "✨ MYSTIC FORTUNE TELLER ✨",
        "",
        f"📜 {fortune}",
        "",
        "──────────────────────────────",
        "",
        "🪿",
        goose_art.strip(),
        "",
        f"🔮 Generated: {timestamp}",
    ]
    
    content = "\n".join(content_lines)
    
    # Calculate width (add padding for border)
    max_line_length = max(len(line) for line in content.split('\n'))
    width = max_line_length + 4  # padding on each side
    
    return create_border(content, width)

def main():
    """Main function to generate fortune and save to file."""
    output_file = "fortune.md"
    old_dir = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(output_file):
        os.makedirs(old_dir, exist_ok=True)
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_dir, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune
    fortune_output = generate_fortune_output()
    
    # Write to fortune.md
    with open(output_file, 'w') as f:
        f.write(fortune_output)
        f.write("\n")
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + fortune_output)

if __name__ == "__main__":
    main()
