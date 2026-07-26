#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with poetic wisdom
"""

import os
import random
from datetime import datetime

# Fortune teller's poetic fortunes
FORTUNES = [
    "The stars whisper that your path leads to unexpected joy. \nA small act of kindness today will bloom into tomorrow's blessing.",
    "Beware the shadow of doubt, for it clouds the mirror of truth. \nTrust your inner voice—it sings a song only you can hear.",
    "Three winds blow your way: one of change, one of love, one of growth. \nEmbrace them all, for they carry gifts from the universe.",
    "The moon reveals what the sun hides. \nYour hidden talents shall surface when the time is ripe.",
    "A door you thought closed forever creaks open again. \nStep through with courage, for destiny awaits within.",
    "The river of time flows both ways. \nWhat you seek has been seeking you all along.",
    "Beware the fox in sheep's clothing, but trust the wolf who shows his teeth. \nHonesty, even when sharp, is kinder than false sweetness.",
    "Your name shall be spoken in whispers of admiration. \nNot for what you have, but for who you have become.",
    "The coin flips twice before landing. \nPatience is the key that unlocks the treasure chest.",
    "A feather from a distant bird lands at your feet. \nTake it as a sign that adventure calls your name."
]

# Sassy Goose ASCII Art
GOOSE_ART = """
     __
    (  >  SASSY!
     \\
      \\    _
       \\  (o\\_
       _//, \\ \\
      (_/  \\  \\
         /   \\ \\
        /     \\ \\
       /       \\ \\
      /         \\ \\
     /           \\ \\
    /             \\ \\
   /               \\ \\
  /                 \\ \\
 /                   \\ \\
/                     \\ \\
\\                     / /
 \\                   / /
  \\                 / /
   \\               / /
    \\             / /
     \\           / /
      \\         / /
       \\       / /
        \\     / /
         \\   / /
          \\ / /
           V V
"""

# ASCII Border
BORDER_TOP = "╔" + "═" * 58 + "╗"
BORDER_BOTTOM = "╚" + "═" * 58 + "╝"
BORDER_MIDDLE = "║" + " " * 58 + "║"
BORDER_DIVIDER = "╟" + "─" * 58 + "╢"


def create_fortune_display(fortune: str) -> str:
    """Create a visually appealing fortune display with border and goose."""
    lines = []
    
    # Top border
    lines.append(BORDER_TOP)
    
    # Title
    title = "🔮 THE SASSY GOOSE FORTUNE TELLER 🔮"
    padding = (58 - len(title)) // 2
    lines.append("║" + " " * padding + title + " " * (57 - padding - len(title)) + "║")
    lines.append("║" + " " * 58 + "║")
    
    # Fortune section
    fortune_title = "Your Poetic Fortune:"
    lines.append("║" + " " * 2 + fortune_title + " " * (55 - len(fortune_title)) + "║")
    lines.append(BORDER_DIVIDER)
    
    # Fortune text (wrapped to fit)
    fortune_lines = fortune.split("\n")
    for line in fortune_lines:
        # Wrap long lines
        words = line.split()
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= 56:
                current_line += (" " if current_line else "") + word
            else:
                if current_line:
                    lines.append("║" + " " * 2 + current_line + " " * (56 - len(current_line)) + "║")
                current_line = word
        if current_line:
            lines.append("║" + " " * 2 + current_line + " " * (56 - len(current_line)) + "║")
    
    lines.append("║" + " " * 58 + "║")
    lines.append(BORDER_DIVIDER)
    
    # Goose section
    goose_title = "🪿 Your Sassy Guide 🪿"
    padding = (58 - len(goose_title)) // 2
    lines.append("║" + " " * padding + goose_title + " " * (57 - padding - len(goose_title)) + "║")
    lines.append("║" + " " * 58 + "║")
    
    # Add goose art (centered)
    for goose_line in GOOSE_ART.strip().split("\n"):
        # Center the goose art
        centered = goose_line.center(58)
        lines.append("║" + centered + "║")
    
    lines.append("║" + " " * 58 + "║")
    
    # Footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    footer = f"Fortune told on: {timestamp}"
    padding = (58 - len(footer)) // 2
    lines.append("║" + " " * padding + footer + " " * (57 - padding - len(footer)) + "║")
    lines.append(BORDER_BOTTOM)
    
    return "\n".join(lines)


def main():
    """Main function to generate and save fortune."""
    # Output file paths
    output_file = "fortune.md"
    old_folder = "old"
    
    # Handle existing fortune.md
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate fortune
    fortune = random.choice(FORTUNES)
    display = create_fortune_display(fortune)
    
    # Create markdown content
    markdown_content = f"""# 🪿 Sassy Goose Fortune 🪿

```
{display}
```

*May the winds of fortune blow in your direction!*
"""
    
    # Write to file
    with open(output_file, "w") as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + "=" * 50)
    print(display)


if __name__ == "__main__":
    main()
