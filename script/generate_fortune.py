#!/usr/bin/env python3
"""
Grumpy Fortune Teller - A sassy goose delivers your fortune with attitude.
"""

import random
import os
from datetime import datetime

# Grumpy fortune messages
FORTUNES = [
    "Your path is clear, but don't expect me to walk it with you.",
    "Luck is coming... if you can handle it without complaining.",
    "The stars say success, but I say 'figure it out yourself'.",
    "A surprise awaits you. Try not to look so shocked.",
    "Your future is bright. Mine is dim, and I'm not happy about it.",
    "Someone is thinking of you. Probably wondering why you're so difficult.",
    "Good things are coming. Finally.",
    "The universe has a plan. I don't, and I'm annoyed.",
    "Your dreams will come true. Don't make me wait.",
    "Opportunity knocks. I told it to stop being so loud.",
    "You'll find what you're looking for. Eventually. Maybe.",
    "The omens are favorable. Don't push your luck.",
    "Success is near. I can smell it, and it's giving me a headache.",
    "A friend will help you. Don't make them regret it.",
    "Your persistence will pay off. Mine didn't, and I'm bitter.",
    "Change is coming. Deal with it.",
    "The answer you seek is obvious. Why are you still asking?",
    "Good fortune smiles upon you. I'm frowning.",
    "You'll overcome your obstacles. They're not that hard.",
    "The future holds promise. I hold a grudge.",
]

# Sassy goose ASCII art
SASSY_GOOSE = """
      __
    <(o )___
    ( ._> /
     `---'
   /       \\
  |  GRUMPY |
  |  GOOSE  |
   \\_______/
      | |
     /   \\
    |     |
    |     |
    |     |
   _|     |_
  (         )
   \\_______/
"""

# Alternative sassy goose variations
SASSY_GOOSE_VARIATIONS = [
    """
      _._
    <(o o)>
     /   \\
    |     |  UGH.
    |  _  |
    | (_) |
    |  -  |
     \\___/
      | |
     /   \\
    |     |
    |     |
   _|     |_
  (         )
   \\_______/
""",
    """
    __      __
   (o\\    /o)
    | \\  / |
    |  \\/  |  *sigh*
    |  ||  |
    |  ||  |
    |  ||  |
    |  ||  |
    |  ||  |
    |  ||  |
    |  ||  |
    |  ||  |
   _|  ||  |_
  (         )
   \\_______/
""",
]

def generate_fortune():
    """Generate a random grumpy fortune."""
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the full fortune display with ASCII art and border."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Choose a sassy goose variation
    goose_art = random.choice([SASSY_GOOSE] + SASSY_GOOSE_VARIATIONS)
    
    # Build the display
    border_width = 60
    border_char = "═"
    side_char = "║"
    
    lines = []
    
    # Top border
    lines.append("╔" + border_char * border_width + "╗")
    
    # Title
    title = "🔮 GRUMPY FORTUNE TELLER 🔮"
    padding = (border_width - len(title)) // 2
    lines.append(f"║{' ' * padding}{title}{' ' * (border_width - len(title) - padding)}║")
    lines.append(f"║{' ' * padding}~ ~ ~ ~ ~ ~ ~{' ' * (border_width - len(title) - padding)}║")
    
    # Empty line
    lines.append(f"║{' ' * border_width}║")
    
    # The fortune (centered)
    fortune_lines = fortune.split('\n')
    for fl in fortune_lines:
        padding = (border_width - len(fl)) // 2
        lines.append(f"║{' ' * padding}{fl}{' ' * (border_width - len(fl) - padding)}║")
    
    # Empty line
    lines.append(f"║{' ' * border_width}║")
    
    # Divider
    lines.append(f"║{'─' * border_width}║")
    
    # Empty line
    lines.append(f"║{' ' * border_width}║")
    
    # Add the sassy goose ASCII art (centered in the border)
    goose_lines = goose_art.strip().split('\n')
    for gl in goose_lines:
        # Center each line of the goose art
        padding = (border_width - len(gl)) // 2
        lines.append(f"║{' ' * padding}{gl}{' ' * max(0, border_width - len(gl) - padding)}║")
    
    # Empty line
    lines.append(f"║{' ' * border_width}║")
    
    # Footer with timestamp
    footer = f"Generated: {timestamp}"
    padding = (border_width - len(footer)) // 2
    lines.append(f"║{' ' * padding}{footer}{' ' * (border_width - len(footer) - padding)}║")
    
    # Bottom border
    lines.append("╚" + border_char * border_width + "╝")
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save the fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(output_file):
        os.makedirs(old_folder, exist_ok=True)
        old_file = os.path.join(old_folder, f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
        os.rename(output_file, old_file)
        print(f"Moved existing fortune.md to {old_file}")
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Write to markdown file
    with open(output_file, 'w') as f:
        f.write("# Grumpy Fortune Teller 🦆\n\n")
        f.write("```text\n")
        f.write(fortune_display)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + "=" * 50 + "\n")
    print(fortune_display)

if __name__ == "__main__":
    main()
