#!/usr/bin/env python3
"""
Fortune Generator Script
Generates a wise fortune from a sassy goose fortune teller.
"""

import os
import shutil
from datetime import datetime

# Wise fortune messages
FORTUNES = [
    "The path you seek is not straight, but winds like wisdom through the ages.",
    "Patience is your greatest ally today. Like the goose that waits for the perfect moment, so shall you succeed.",
    "A challenge ahead will reveal a strength you never knew you possessed.",
    "The answers you seek lie not in looking forward, but in reflecting upon what has passed.",
    "Trust your instincts today. They are as reliable as the seasons.",
    "A small act of kindness will return to you multiplied many times over.",
    "The stars align to favor your creative endeavors. Let your spirit soar.",
    "Wisdom comes not from knowing all the answers, but from asking the right questions.",
    "Today brings an unexpected opportunity. Be ready to embrace it.",
    "The journey of a thousand miles begins with a single, confident step."
]

# Sassy goose ASCII art
GOOSE_ART = """
      _
     (\\_)
      \\_
     /   \\
    |  o  |
    |  _  |
   /|  |  |\\
  / |  |  | \\
 /  |  |  |  \\
/   |  |  |   \\
    |  |  |
    |  |  |
   /   \\   \\
  /     \\   \\
 /       \\   \\
/         \\   \\
"""

# Alternative sassy goose with attitude
GOOSE_ART_SASSY = """
      _
     (\\_)
      \\_
     /   \\
    | (_) |  *sassy squint*
    |  _  |
   /|  |  |\\
  / |  |  | \\
 /  |  |  |  \\
/   |  |  |   \\
    |  |  |
    |  |  |
   /   \\   \\
  /     \\   \\
 /       \\   \\
/         \\   \\
   \\_____/
  *oh honey*
"""

def get_wise_fortune():
    """Return a random wise fortune."""
    import random
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the full fortune display with border, goose, and fortune."""
    fortune = get_wise_fortune()
    
    # Get the widest line for border calculation
    lines = GOOSE_ART_SASSY.strip().split('\n')
    max_width = max(len(line) for line in lines)
    # Add space for fortune text
    fortune_lines = fortune.split('\n')
    for fl in fortune_lines:
        if len(fl) > max_width:
            max_width = len(fl)
    
    # Add padding
    border_width = max_width + 4
    
    # Create top border
    top_border = '╔' + '═' * (border_width - 2) + '╗'
    
    # Create bottom border
    bottom_border = '╚' + '═' * (border_width - 2) + '╝'
    
    # Build the display
    display_lines = []
    display_lines.append(top_border)
    
    # Add title
    title = "🔮 WISE FORTUNE 🔮"
    padding = (border_width - 2 - len(title)) // 2
    title_line = '║' + ' ' * padding + title + ' ' * (border_width - 2 - padding - len(title)) + '║'
    display_lines.append(title_line)
    display_lines.append('╠' + '═' * (border_width - 2) + '╣')
    
    # Add goose art with padding
    for line in GOOSE_ART_SASSY.strip().split('\n'):
        padding_left = (border_width - 2 - len(line)) // 2
        display_lines.append('║' + ' ' * padding_left + line + ' ' * (border_width - 2 - padding_left - len(line)) + '║')
    
    # Add divider
    divider = '╠' + '─' * (border_width - 2) + '╣'
    display_lines.append(divider)
    
    # Add fortune with padding
    fortune_line = '║' + ' ' * 2 + fortune + ' ' * (border_width - 4 - len(fortune)) + '║'
    display_lines.append(fortune_line)
    
    # Add footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    footer_text = f"Fortune told on: {timestamp}"
    padding_left = (border_width - 2 - len(footer_text)) // 2
    footer_line = '╚' + ' ' * padding_left + footer_text + ' ' * (border_width - 2 - padding_left - len(footer_text)) + '╝'
    # Actually use bottom border for footer
    display_lines.pop()  # Remove the last border we added
    display_lines.append('╠' + '═' * (border_width - 2) + '╣')
    display_lines.append(footer_line)
    
    return '\n'.join(display_lines)

def main():
    """Main function to generate and save the fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(output_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        shutil.move(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Create markdown content with code block for ASCII art
    markdown_content = f"""# 🦢 Sassy Goose Fortune Teller 🔮

```
{fortune_display}
```

*May wisdom guide your path today!*
"""
    
    # Write to fortune.md
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + "=" * 50)
    print(fortune_display)

if __name__ == "__main__":
    main()
