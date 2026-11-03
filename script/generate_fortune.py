#!/usr/bin/env python3
"""
Fortune Generator Script
Generates a wise fortune with a sassy goose ASCII art.
"""

import os
import random
from datetime import datetime

# Wise fortune messages
FORTUNES = [
    "The winds of change are at your back. Embrace the journey ahead with courage.",
    "A secret you've been keeping will soon reveal itself in unexpected ways.",
    "Patience is your greatest ally today. The stars favor those who wait wisely.",
    "An old friend will bring news that changes everything you thought you knew.",
    "The path you seek is not straight, but the destination will be worth the journey.",
    "Wisdom comes to those who listen. The answer you seek is in a conversation today.",
    "A small act of kindness will return to you tenfold in the coming days.",
    "The goose knows when to fly and when to rest. Trust your instincts.",
    "What seems like an ending is merely the beginning of something greater.",
    "Your curiosity will lead you to a treasure more valuable than gold.",
]

# ASCII art of a sassy goose
GOOSE_ART_SASSY = """
       __
     <(o )___   *HONK!*
      ( ._> /   "I'm watching you..."
       \\___/   
"""

# ASCII border characters
BORDER_CHAR = "═"
SIDEBAR_CHAR = "║"
TOP_CORNER = "╔"
BOTTOM_CORNER = "╚"
TOP_RIGHT = "╗"
BOTTOM_RIGHT = "╝"

def generate_fortune():
    """Generate a random fortune from the wise fortune teller."""
    return random.choice(FORTUNES)

def create_formatted_fortune():
    """Create the formatted fortune output with ASCII art and borders."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Choose the sassy goose art
    goose = GOOSE_ART_SASSY
    
    # Create the content
    lines = []
    lines.append(fortune)
    lines.append("")
    lines.append("— A message from the Wise Fortune Teller —")
    
    # Calculate the maximum width needed
    max_width = max(len(line) for line in lines)
    max_width = max(max_width, len(goose.strip()))
    
    # Add padding
    padding = 4
    total_width = max_width + padding * 2
    
    # Build the bordered output
    output = []
    
    # Top border
    output.append(TOP_CORNER + BORDER_CHAR * total_width + TOP_RIGHT)
    
    # Title
    title = "🔮 WISDOM OF THE DAY 🔮"
    title_padding = (total_width - len(title)) // 2
    output.append(SIDEBAR_CHAR + " " * title_padding + title + " " * (total_width - title_padding - len(title)) + SIDEBAR_CHAR)
    output.append(SIDEBAR_CHAR + " " * total_width + SIDEBAR_CHAR)
    
    # Fortune text
    for line in lines:
        output.append(SIDEBAR_CHAR + " " * padding + line + " " * (total_width - padding - len(line)) + SIDEBAR_CHAR)
    
    output.append(SIDEBAR_CHAR + " " * total_width + SIDEBAR_CHAR)
    
    # Divider
    divider = SIDEBAR_CHAR + " " * padding + "─" * (total_width - padding * 2) + " " * padding + SIDEBAR_CHAR
    output.append(divider)
    output.append(SIDEBAR_CHAR + " " * total_width + SIDEBAR_CHAR)
    
    # Goose ASCII art (centered)
    for goose_line in goose.split('\n'):
        if goose_line.strip():
            centered = goose_line.center(total_width - padding * 2)
            output.append(SIDEBAR_CHAR + " " * padding + centered + " " * padding + SIDEBAR_CHAR)
        else:
            output.append(SIDEBAR_CHAR + " " * total_width + SIDEBAR_CHAR)
    
    output.append(SIDEBAR_CHAR + " " * total_width + SIDEBAR_CHAR)
    
    # Timestamp
    time_msg = f"Generated: {timestamp}"
    time_padding = (total_width - len(time_msg)) // 2
    output.append(SIDEBAR_CHAR + " " * time_padding + time_msg + " " * (total_width - time_padding - len(time_msg)) + SIDEBAR_CHAR)
    
    # Bottom border
    output.append(BOTTOM_CORNER + BORDER_CHAR * total_width + BOTTOM_RIGHT)
    
    return '\n'.join(output)

def main():
    """Main function to generate and save the fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md already exists
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the formatted fortune
    fortune_content = create_formatted_fortune()
    
    # Add markdown header
    markdown_output = f"""# 🦢 Daily Fortune 🦢

{fortune_content}

---

*May the wisdom of the sassy goose guide you today!*
"""
    
    # Write to fortune.md
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + "=" * 50)
    print(fortune_content)
    print("=" * 50)

if __name__ == "__main__":
    main()
