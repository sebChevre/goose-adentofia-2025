#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with sarcastic mood
"""

import os
import random
from datetime import datetime

# Sarcastic fortune messages
FORTUNES = [
    "Oh look, another day to pretend you have your life together.\nSpoiler alert: You don't. But hey, at least you're trying!",
    "The universe has a sense of humor, and apparently it finds you amusing.\nThat's either great news or deeply concerning.",
    "A mysterious stranger will enter your life... \nProbably just someone asking for directions. Deal with it.",
    "Your future looks bright! \nToo bad you're wearing sunglasses indoors again.",
    "Someone is talking about you behind your back.\nGasp! Oh wait, it's just your inner critic. Relax.",
    "You will face a challenge today. \nActually, it's just Monday. Same difference.",
    "Love is in the air! \nUnfortunately, so is pollen. Your allergies will ruin everything.",
    "A surprise awaits you around the corner! \nIt's probably just a pigeon. You've seen a pigeon before.",
    "The stars say you'll achieve great things... \nLike finally folding that laundry. Quantum levels of achievement.",
    "Your charisma will shine today! \nJust don't forget to put on pants first.",
    "Money may come your way... \nOr you'll find a $5 bill in an old jacket. Either way, jackpot!",
    "You possess untapped potential!\nLike that one drawer full of cables you swear you'll sort someday.",
]

# Sassy Goose ASCII Art - looking unimpressed
GOOSE_ART = """
        __
       /  \\
      |    |
      |  o |  *unimpressed side-eye*
      |  _ |
       \\__/
        ||
       _||_
      /|  |\\
     / |  | \\
    |  |  |  |
    |  |__|  |
    |________|
    /        \\
   |  SASSY   |
   |   MODE   |
   |   ON     |
   \\__________/
"""

# ASCII Border Configuration
BORDER_WIDTH = 50

def generate_fortune_output():
    """Generate the complete fortune output with ASCII art and border."""
    fortune = random.choice(FORTUNES)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create border characters
    top_corner = "+"
    bottom_corner = "+"
    side_border = "|"
    horizontal_line = "+" + "-" * (BORDER_WIDTH - 2) + "+"
    spaces = " " * (BORDER_WIDTH - 2)
    
    lines = []
    
    # Top border
    lines.append(horizontal_line)
    
    # Title section
    title = "🔮 SARCASTIC FORTUNE TELLER 🔮"
    lines.append(f"{side_border}{title:^{BORDER_WIDTH-2}}{side_border}")
    presenter = "Presented by your friend, The Sassy Goose:"
    padding = " " * (BORDER_WIDTH - 2 - len(presenter))
    lines.append(f"{side_border}{presenter}{padding}{side_border}")
    lines.append(horizontal_line)
    lines.append("")
    
    # Fortune section header
    fortune_header = "✨ YOUR SARCASTIC FORTUNE ✨"
    lines.append(f"{side_border}{fortune_header:^{BORDER_WIDTH-2}}{side_border}")
    tildes = "~" * (BORDER_WIDTH - 2)
    lines.append(f"{side_border}{tildes:^^{BORDER_WIDTH-2}}{side_border}")
    
    # Fortune text with proper padding
    fortune_lines = fortune.split('\n')
    for line in fortune_lines:
        padded_line = line.center(BORDER_WIDTH - 4)
        lines.append(f"{side_border} {padded_line} {side_border}")
    
    lines.append(f"{side_border}{tildes:^^{BORDER_WIDTH-2}}{side_border}")
    lines.append(horizontal_line)
    lines.append("")
    
    # Divider between fortune and goose
    divider = "╔" + "═" * (BORDER_WIDTH - 2) + "╗"
    divider_mid = "║" + " 🪿 THE SASSY GOOSE APPROVES (NOT) 🪿 " + " " * (BORDER_WIDTH - 45) + "║"
    divider_bottom = "╚" + "═" * (BORDER_WIDTH - 2) + "╝"
    lines.append(divider)
    lines.append(divider_mid)
    lines.append(divider_bottom)
    lines.append("")
    
    # Goose ASCII art section
    goose_header = "🦆 THE SASSY GOOSE 🦆"
    lines.append(f"{side_border}{goose_header:^{BORDER_WIDTH-2}}{side_border}")
    dashes = "-" * (BORDER_WIDTH - 2)
    lines.append(f"{side_border}{dashes:^^{BORDER_WIDTH-2}}{side_border}")
    
    for line in GOOSE_ART.split('\n'):
        if line.strip():
            # Center the goose art within the border
            centered = line.center(BORDER_WIDTH - 4)
            lines.append(f"{side_border} {centered} {side_border}")
        else:
            lines.append(f"{side_border}{spaces:^^{BORDER_WIDTH-2}}{side_border}")
    
    lines.append(f"{side_border}{dashes:^^{BORDER_WIDTH-2}}{side_border}")
    lines.append(horizontal_line)
    lines.append("")
    
    # Footer
    footer = f"Fortune generated: {timestamp} | Remember: I'm a goose, not a therapist 🪿"
    lines.append(f"{side_border}{footer:^{BORDER_WIDTH-2}}{side_border}")
    lines.append(f"{side_border}{spaces:^^{BORDER_WIDTH-2}}{side_border}")
    slogan = "💅 Go forth and be mildly annoyed! 💅"
    lines.append(f"{side_border} {slogan:^{BORDER_WIDTH-4}} {side_border}")
    lines.append(horizontal_line)
    
    return '\n'.join(lines)

def main():
    """Main function to generate fortune and save to file."""
    output_content = generate_fortune_output()
    
    # Define file paths
    fortune_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_path)
        print(f"✓ Moved existing fortune.md to {old_path}")
    
    # Write new fortune to file
    with open(fortune_file, 'w') as f:
        f.write(output_content)
    
    print(f"✓ Fortune generated and saved to {fortune_file}")
    print("\n" + output_content)

if __name__ == "__main__":
    main()
