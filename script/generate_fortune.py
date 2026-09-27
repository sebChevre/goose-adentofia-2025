#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with introspective moods.
"""

import os
import random
from datetime import datetime

# Introspective fortune messages
FORTUNES = [
    "The path you seek is not ahead, but within. Listen to the quiet voice that whispers when the world falls silent.",
    "Today, ask yourself: What am I running from? The answer holds the key to your next chapter.",
    "A decision you've been avoiding will reveal its truth when you stop looking for perfection.",
    "The reflection you see in still water shows more than your face—it shows your potential.",
    "Sometimes the bravest thing is to sit with uncertainty and let clarity emerge on its own terms.",
    "Your greatest strength has been hiding in plain sight, disguised as something you take for granted.",
    "The question you're afraid to ask is the one that will set you free.",
    "There is wisdom in your discomfort. What is it trying to teach you?",
    "The version of yourself you're becoming is already proud of the work you're doing now.",
    "Not every door needs to open. Some are meant to show you what you're willing to leave behind.",
    "The answer lies not in changing who you are, but in remembering who you've always been.",
    "Your intuition has been speaking. The question is: have you been listening?",
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
    {<}>
    /  \\
   |    |
   |    |
   |    |
   |    |
  /|    |\\
 / |    | \\
   |    |
   |    |
   |    |
   |    |
  /      \\
 /        \\
|          |
|          |
|  __      |
| (  )     |
|  ^^      |
|          |
|          |
\\__________/
"""

def generate_fortune():
    """Generate a random introspective fortune."""
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the full fortune display with ASCII art and border."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the display
    border_char = "═"
    side_char = "║"
    corner_tl = "╔"
    corner_tr = "╗"
    corner_bl = "╚"
    corner_br = "╝"
    divider_char = "─"
    
    # Width calculation
    inner_width = 60
    
    # Create top border
    top_border = corner_tl + border_char * inner_width + corner_tr
    
    # Create bottom border
    bottom_border = corner_bl + border_char * inner_width + corner_br
    
    # Create fortune text lines (wrapped to fit)
    fortune_lines = []
    words = fortune.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= inner_width - 4:  # Account for side chars and padding
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            fortune_lines.append(current_line)
            current_line = word
    if current_line:
        fortune_lines.append(current_line)
    
    # Build the complete display
    lines = []
    lines.append(top_border)
    lines.append(f"{side_char}{'FORTUNE TELLER'.center(inner_width)}{side_char}")
    lines.append(f"{side_char}{'🔮 Introspective Reading 🔮'.center(inner_width)}{side_char}")
    lines.append(f"{side_char}{side_char}")
    lines.append(f"{side_char}{side_char}")
    
    # Add fortune with padding
    for line in fortune_lines:
        lines.append(f"{side_char}  {line.ljust(inner_width - 4)}  {side_char}")
    
    lines.append(f"{side_char}{side_char}")
    
    # Add divider between fortune and goose
    divider = f"{side_char}{divider_char * (inner_width - 2)}{side_char}"
    lines.append(divider)
    lines.append(f"{side_char}{side_char}")
    
    # Add goose ASCII art
    goose_lines = GOOSE_ART.strip().split('\n')
    for goose_line in goose_lines:
        # Center the goose art within the border
        centered_goose = goose_line.center(inner_width)
        lines.append(f"{side_char}{centered_goose}{side_char}")
    
    lines.append(f"{side_char}{side_char}")
    lines.append(f"{side_char}{'🌙 ' + timestamp.center(inner_width - 4) + ' 🌙'.center(inner_width)}{side_char}")
    lines.append(bottom_border)
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save fortune."""
    output_dir = os.getcwd()
    fortune_file = os.path.join(output_dir, "fortune.md")
    old_folder = os.path.join(output_dir, "old")
    
    # Check if fortune.md already exists
    if os.path.exists(fortune_file):
        # Create old folder if it doesn't exist
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Move existing file to old folder with timestamp
        import shutil
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_folder, f"fortune_{timestamp}.md")
        shutil.move(fortune_file, old_file)
        print(f"Moved existing fortune.md to: {old_file}")
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Create markdown content
    markdown_content = f"""# 🌙 Fortune Teller Reading 🌙

## Your Introspective Fortune

```
{fortune_display}
```

---

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

> "The journey of self-discovery begins with a single question."
"""
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
