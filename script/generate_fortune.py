#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with poetic fortunes
"""

import os
import random
from datetime import datetime

# Sassy goose ASCII art
GOOSE_ART = """
   __
  /  \\
 |    |
 |    |
  \\__/
  (oo)_______
  (__)\\       )\\/\\
      ||----w |
      ||     ||
"""

# Poetic fortune messages
FORTUNES = [
    "The stars whisper of adventures waiting beyond your horizon.\nA path you've never trodden shall reveal its hidden treasures.",
    "Like a river finding its course, your destiny flows with grace.\nPatience now, for the bloom comes in its own sweet time.",
    "The moon casts shadows that dance with possibility.\nWhat seems lost shall return, transformed and brighter than before.",
    "A whisper on the wind carries news from distant shores.\nYour courage shall open doors you never knew existed.",
    "The stars align in patterns of ancient wisdom.\nTrust the journey, for even the winding road leads home.",
    "Like autumn leaves, old ways fall away to make room for new.\nEmbrace the change, for it carries gifts beyond measure.",
    "The ocean's depths hold secrets waiting to be discovered.\nYour intuition speaks truths that logic cannot comprehend.",
    "A spark ignites in the darkness, promising dawn's arrival.\nYour dreams are not mere fantasies, but maps to your future.",
    "The mountain stands tall against the storm's fierce fury.\nYour spirit, too, possesses such unyielding strength.",
    "Like threads in a tapestry, seemingly random events weave meaning.\nWhat appears chaotic now shall reveal its perfect design."
]

def generate_fortune():
    """Generate a random poetic fortune."""
    return random.choice(FORTUNES)

def create_ascii_border(content, width=60):
    """Create an ASCII border around the content."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    divider = "╟" + "─" * (width - 2) + "╢"
    
    lines = []
    lines.append(top_bottom)
    
    # Add header
    header = "  🌙 SASSY GOOSE FORTUNE TELLER 🌙"
    lines.append(f"║{header.center(width - 2)}║")
    
    # Add timestamp
    timestamp = f"  {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
    lines.append(f"║{timestamp.center(width - 2)}║")
    
    lines.append(top_bottom.replace("╔", "╟").replace("╗", "╢"))
    lines.append(middle)
    
    # Add goose art with padding
    goose_lines = GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        padded_line = line.center(width - 2)
        lines.append(f"║{padded_line}║")
    
    lines.append(middle)
    lines.append(divider)
    lines.append(middle)
    
    # Add fortune with proper padding
    fortune_lines = content.split('\n')
    for line in fortune_lines:
        # Center the fortune text within the border
        padded_fortune = line.center(width - 4)
        lines.append(f"║  {padded_fortune}  ║")
    
    lines.append(middle)
    lines.append(top_bottom.replace("╔", "╚").replace("╗", "╝"))
    
    return '\n'.join(lines)

def main():
    """Main function to generate fortune and save to file."""
    # Output file path
    output_file = "fortune.md"
    old_folder = "old"
    
    # Handle existing fortune.md file
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Existing fortune.md moved to {old_path}")
    
    # Generate the fortune
    fortune = generate_fortune()
    
    # Create the bordered output
    output = create_ascii_border(fortune)
    
    # Add markdown code block formatting
    markdown_output = f"```text\n{output}\n```"
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(markdown_output)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + output)

if __name__ == "__main__":
    main()
