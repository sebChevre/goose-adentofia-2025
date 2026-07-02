#!/usr/bin/env python3
"""
Grumpy Fortune Teller Script
Generates fortunes from a sassy goose fortune teller with attitude.
"""

import os
import random
from datetime import datetime

# Grumpy fortune messages - because the goose is sassy
FORTUNES = [
    "Your path is unclear, much like my patience. Try again later.",
    "The stars say you'll succeed... eventually. Maybe.",
    "A surprise awaits you. Probably something annoying, like me.",
    "Your future looks bright. Too bad you're not as bright.",
    "The universe has a plan for you. I don't, but I'm judging you anyway.",
    "Success is near. Like that one step you keep forgetting to take.",
    "Your luck is improving. Not by much, but it's something.",
    "The answer is yes. Don't make me repeat myself.",
    "Challenges await. Just like my judgmental honking awaits you.",
    "Opportunities abound. Most of them you'll probably miss.",
    "Your dreams will come true. If you actually work for them.",
    "The cosmos approves. Barely.",
    "A friend will help you. Probably out of pity.",
    "Your wisdom grows. Slowly, like my tolerance for your questions.",
    "The future is uncertain. Unlike my irritation, which is certain.",
    "Good things are coming. I'm not holding my breath.",
    "Your potential is vast. Too vast, apparently, since you asked me this.",
    "The cards say... honestly, who cares? Do it anyway.",
    "Destiny calls. I'm just here to honk at you while it happens.",
    "Your time will come. Eventually. Stop asking when.",
]

# Sassy goose ASCII art
SASSY_GOOSE = r"""
      __
     /  \
    |    |
    |    |
   /|    |\
  / |    | \
 |  |    |  |
 |  |    |  |
 |  |    |  |
 |  |    |  |
 |  |    |  |
 |  |    |  |
  \ |    | /
   \|    |/
    |    |
    |    |
   /      \
  /        \
 |  O    O  |
 |    __    |
 |  (____)  |
 |  \____/  |
  \  \__/  /
   \______/
    |    |
   _/    \_
  /        \
 |  HONK!   |
 |          |
  \________/
"""

# Simpler sassy goose for variety
SASSY_GOOSE_V2 = r"""
      __
     /  \
    |    |
   /|    |\
  / |    | \
 |  |    |  |
 |  |    |  |
 |  |    |  |
 |  |    |  |
  \ |    | /
   \|    |/
    |    |
    |    |
   /      \
  |  O  O  |
  |   __   |
  |  (__)  |
  |  \__/  |
   \______/
    |  |
   _/  \_
  /      \
 | HONK!  |
  \______/
"""

# ASCII border characters
TOP_BORDER = "╔" + "═" * 60 + "╗"
BOTTOM_BORDER = "╚" + "═" * 60 + "╝"
MIDDLE_BORDER = "╟" + "─" * 60 + "╢"
SIDE_BORDER_LEFT = "║"
SIDE_BORDER_RIGHT = "║"


def format_line(text: str, width: int = 60) -> str:
    """Format a line of text within the border."""
    padding = width - len(text) - 2
    left_pad = padding // 2
    right_pad = padding - left_pad
    return f"{SIDE_BORDER_LEFT} {' ' * left_pad}{text}{' ' * right_pad} {SIDE_BORDER_RIGHT}"


def generate_fortune_output() -> str:
    """Generate the complete fortune output with ASCII art and formatting."""
    width = 60
    
    # Pick a random fortune
    fortune = random.choice(FORTUNES)
    
    # Pick a random goose art
    goose_art = random.choice([SASSY_GOOSE, SASSY_GOOSE_V2])
    
    # Build the output
    lines = []
    
    # Top border
    lines.append(TOP_BORDER)
    
    # Title
    lines.append(format_line("🔮 GRUMPY FORTUNE TELLER 🔮", width))
    lines.append(format_line(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", width))
    lines.append(TOP_BORDER)  # Double top for emphasis
    
    # Goose art section - center the goose
    goose_lines = goose_art.strip().split('\n')
    goose_width = max(len(line) for line in goose_lines)
    goose_padding = (width - goose_width) // 2
    
    for line in goose_lines:
        if line.strip():
            padding = goose_padding if goose_padding > 0 else 0
            lines.append(f"{SIDE_BORDER_LEFT} {' ' * padding}{line}{' ' * (width - len(line) - padding - 2)} {SIDE_BORDER_RIGHT}")
        else:
            lines.append(f"{SIDE_BORDER_LEFT}{' ' * (width - 2)}{SIDE_BORDER_RIGHT}")
    
    # Divider
    lines.append(MIDDLE_BORDER)
    lines.append(format_line("✨ YOUR FORTUNE ✨", width))
    lines.append(MIDDLE_BORDER)
    
    # Fortune text - wrap if needed
    fortune_words = fortune.split()
    current_line = []
    current_length = 0
    
    for word in fortune_words:
        if current_length + len(word) + 1 <= 56:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            if current_line:
                lines.append(format_line(' '.join(current_line), width))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(format_line(' '.join(current_line), width))
    
    # Add some grumpy goose commentary
    grumpy_comments = [
        "Now stop bothering me and go do something!",
        "That's all I'm telling you. Honk!",
        "Don't come back asking for another fortune!",
        "I have better things to do than this.",
        "Go away now. My patience is wearing thin.",
    ]
    lines.append("")
    lines.append(format_line(f"~ {random.choice(grumpy_comments)} ~", width))
    lines.append("")
    
    # Bottom border
    lines.append(BOTTOM_BORDER)
    
    return '\n'.join(lines)


def main():
    """Main function to generate and save the fortune."""
    output_dir = os.getcwd()
    fortune_file = os.path.join(output_dir, "fortune.md")
    old_dir = os.path.join(output_dir, "old")
    
    # Check if fortune.md already exists
    if os.path.exists(fortune_file):
        # Create old directory if it doesn't exist
        os.makedirs(old_dir, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_filepath = os.path.join(old_dir, old_filename)
        
        os.rename(fortune_file, old_filepath)
        print(f"Moved existing fortune.md to {old_filepath}")
    
    # Generate the fortune
    fortune_output = generate_fortune_output()
    
    # Write to fortune.md
    with open(fortune_file, 'w', encoding='utf-8') as f:
        f.write(fortune_output)
    
    print(f"Fortune generated and saved to {fortune_file}")
    print("\n" + "=" * 60)
    print(fortune_output)
    print("=" * 60)


if __name__ == "__main__":
    main()
