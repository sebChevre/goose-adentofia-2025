#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller with poetic moods.
Generates a fortune and saves it to fortune.md in the current directory.
"""

import os
import random
from datetime import datetime

# ASCII art of a sassy goose
SASSY_GOOSE = """
      __
     /  \\
    |    |
    |    |
    |    |
   /|    |\\
  / |    | \\
 |  |    |  |
 |  |    |  |
  \\ |    | /
   \\|    |/
    |    |
    |    |
   _/    \\_
  /        \\
 |  o    o  |
 |    <     |
 |   __     |
  \\  ||    /
   \\ ||   /
    \\||  /
     |||
    _|||_
   |     |
   |     |
   |_____|
"""

# Poetic fortunes
FORTUNES = [
    "The stars whisper secrets of courage,\n  for within you lies a fire untamed.\n  Today, the universe aligns to bring\n  unexpected joy to your path.",
    "Like a river finding its way to the sea,\n  your destiny calls with gentle persistence.\n  Trust in the journey, for wisdom\n  blooms in the soil of patience.",
    "The moon casts silver on your dreams,\n  revealing treasures hidden in shadow.\n  A surprise awaits that will illuminate\n  the darkest corners of doubt.",
    "As the goose takes flight at dawn,\n  so shall you rise above yesterday's worries.\n  New horizons beckon with promises\n  of adventure and sweet discovery.",
    "The winds of change blow softly now,\n  carrying whispers of opportunities.\n  Listen closely, for fortune favors\n  those who dare to seize the moment.",
    "In the garden of fate, a seed has been planted.\n  With care and time, it shall bloom into\n  something magnificent beyond imagination.\n  Tend to your dreams with loving hands.",
    "The oracle sees a bridge of starlight,\n  connecting your heart to distant hopes.\n  Cross it with confidence, for the way\n  is clear and the journey is yours.",
    "Like autumn leaves dancing in the breeze,\n  your path twists with graceful unpredictability.\n  Embrace the unexpected turns, for they\n  lead to wonders you have yet to name.",
]

# Border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
MIDDLE_BORDER = "╠" + "═" * 58 + "╣"
SIDE_BORDER = "║"

def generate_fortune():
    """Generate a random poetic fortune."""
    return random.choice(FORTUNES)

def create_formatted_output():
    """Create the formatted fortune output with ASCII art and border."""
    fortune = generate_fortune()
    
    # Build the output
    lines = []
    lines.append(TOP_BORDER)
    
    # Title line
    title = "✨ THE SASSY GOOSE FORTUNE TELLER ✨"
    padding = (58 - len(title)) // 2
    lines.append(f"║{' ' * padding}{title}{' ' * (58 - len(title) - padding)}║")
    lines.append(f"║{' ' * 58}║")
    
    # Date line
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    padding = (58 - len(date_str)) // 2
    lines.append(f"║{' ' * padding}{date_str}{' ' * (58 - len(date_str) - padding)}║")
    lines.append(f"║{' ' * 58}║")
    
    # Divider
    lines.append(f"║{'─' * 58}║")
    lines.append(f"║{' ' * 58}║")
    
    # Goose ASCII art (centered)
    goose_lines = SASSY_GOOSE.strip().split('\n')
    for goose_line in goose_lines:
        # Center the goose art
        padding = (58 - len(goose_line)) // 2
        lines.append(f"║{' ' * padding}{goose_line}{' ' * (58 - len(goose_line) - padding)}║")
    
    lines.append(f"║{' ' * 58}║")
    
    # Divider between goose and fortune
    lines.append(f"║{'─' * 58}║")
    lines.append(f"║{' ' * 58}║")
    
    # Fortune header
    fortune_header = "🔮 YOUR FORTUNE 🔮"
    padding = (58 - len(fortune_header)) // 2
    lines.append(f"║{' ' * padding}{fortune_header}{' ' * (58 - len(fortune_header) - padding)}║")
    lines.append(f"║{' ' * 58}║")
    
    # Fortune text (formatted to fit within border)
    fortune_lines = fortune.split('\n')
    for fortune_line in fortune_lines:
        # Center the fortune text
        padding = (58 - len(fortune_line)) // 2
        lines.append(f"║{' ' * padding}{fortune_line}{' ' * (58 - len(fortune_line) - padding)}║")
    
    lines.append(f"║{' ' * 58}║")
    lines.append(f"║{'─' * 58}║")
    
    # Closing message
    closing = "May the feathers be ever in your favor! 🪶"
    padding = (58 - len(closing)) // 2
    lines.append(f"║{' ' * padding}{closing}{' ' * (58 - len(closing) - padding)}║")
    
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
        print(f"Existing fortune.md moved to: {old_filepath}")
    
    # Generate the formatted output
    output = create_formatted_output()
    
    # Create markdown content with code block for ASCII art preservation
    markdown_content = f"""# 🎭 Daily Fortune from the Sassy Goose

```
{output}
```

*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*
"""
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + output)

if __name__ == "__main__":
    main()
