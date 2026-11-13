#!/usr/bin/env python3
"""
Fortune Generator - Wise Fortune Teller with a Sassy Goose
Generates a visually appealing fortune with ASCII art and saves to fortune.md
"""

import os
import shutil
from datetime import datetime

# Wise fortune messages from the mystical fortune teller
WISE_FORTUNES = [
    "The path you seek is not straight, but winding like a river. Trust your intuition.",
    "Wisdom comes not from knowing all answers, but from asking better questions.",
    "The stars whisper that your patience will bloom into unexpected opportunity.",
    "A challenge you fear is actually a gift in disguise. Embrace it with courage.",
    "The goose knows: sometimes you must waddle before you can fly.",
    "Your past has prepared you. The future awaits your wisdom.",
    "In the quiet moments between thoughts, your true purpose reveals itself.",
    "The universe conspires to help those who trust the journey.",
    "What seems like an ending is merely the universe turning the page.",
    "The sassy goose teaches us: confidence comes before competence. Strut anyway.",
]

# Sassy Goose ASCII Art
SASSY_GOOSE = """
      __
    <(o______)>
        ( )
      (__|__)
     /       \\
    |  \\\\///  |
    |   \\\\    |
     \\  ___  /
      \\/   \\/
    """

# Alternative sassier goose
SASSY_GOOSE_ALT = """
         __
       <(o)>
      /|   |\\
     / |   | \\
    |  |___|  |
    |  |   |  |
    |  |   |  |
    |  |___|  |
     \\       /
      \\_____/
    """

def get_wise_fortune():
    """Select a random wise fortune."""
    import random
    return random.choice(WISE_FORTUNES)

def create_ascii_border(content, width=60):
    """Create an ASCII border around the content."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + content + "║"
    return f"{top_bottom}\n{middle}\n{'═' * width}\n╚" + "═" * (width - 2) + "╝"

def generate_fortune_display():
    """Generate the complete fortune display with all ASCII elements."""
    fortune = get_wise_fortune()
    
    # Build the display
    lines = []
    
    # Title
    lines.append("  ✦ ✦ ✦  MYSTIC FORTUNE TELLER  ✦ ✦ ✦")
    lines.append("  ─────────────────────────────────────")
    lines.append("")
    lines.append("  🌙 WISE FORTUNE 🌙")
    lines.append("")
    lines.append(f"  \"{fortune}\"")
    lines.append("")
    lines.append("  ─────────────────────────────────────")
    lines.append("")
    lines.append("  ┌─────────────────────────────────────┐")
    lines.append("  │         THE SASSY GOOSE SAYS:       │")
    lines.append("  └─────────────────────────────────────┘")
    lines.append("")
    
    # Add the goose ASCII art with proper indentation
    for line in SASSY_GOOSE.split('\n'):
        if line.strip():
            lines.append(f"  {line}")
    
    lines.append("")
    lines.append("  ─────────────────────────────────────")
    lines.append(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("  ✦ Trust the journey ✦")
    
    # Join all lines
    content = '\n'.join(lines)
    
    # Create the bordered version
    # Calculate the actual width needed
    max_line_len = max(len(line) for line in lines)
    border_width = max(max_line_len + 4, 60)
    
    # Build the final bordered output
    result_lines = []
    result_lines.append("╔" + "═" * (border_width - 2) + "╗")
    
    for line in lines:
        # Pad each line to fit the border
        padded_line = line.ljust(border_width - 2)
        result_lines.append("║" + padded_line + "║")
    
    result_lines.append("╚" + "═" * (border_width - 2) + "╝")
    
    return '\n'.join(result_lines)

def main():
    """Main function to generate and save the fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md already exists
    if os.path.exists(output_file):
        print(f"Found existing {output_file}. Moving to {old_folder}/...")
        
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move the existing file to old folder with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        shutil.move(output_file, old_path)
        print(f"Moved to {old_path}")
    
    # Generate the fortune display
    fortune_display = generate_fortune_display()
    
    # Create markdown content with code block for proper formatting
    markdown_content = f"""# 🦢 Mystic Fortune Teller

> *A wise fortune from the mystical fortune teller*

```
{fortune_display}
```

---

*May the stars guide your path today.*
"""
    
    # Write to fortune.md
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + "="*50)
    print(fortune_display)
    print("="*50)

if __name__ == "__main__":
    main()
