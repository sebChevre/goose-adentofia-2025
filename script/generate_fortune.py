#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose companion
"""

import os
import random
from datetime import datetime

# Fortune messages from the wise fortune teller
FORTUNES = [
    "The stars whisper that wisdom comes not from knowing all, but from asking the right questions.",
    "A path you've walked before will reveal new treasures if you look with fresh eyes.",
    "Patience is your ally today. The best opportunities reveal themselves to those who wait.",
    "An unexpected conversation will illuminate a truth you've been seeking.",
    "The answer you seek is closer than you think—sometimes the simplest solutions are the profound ones.",
    "Trust your intuition when the world tries to convince you otherwise.",
    "A challenge you face today is actually a blessing in disguise, preparing you for greater things.",
    "The energy you put into the world returns to you multiplied. Choose wisely.",
    "Someone's opinion of you does not have to become your reality. Stay true to yourself.",
    "The universe is aligning in your favor. Be ready to seize the opportunity.",
]

# ASCII art of a sassy goose
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
    ╭───────────────────────────────────╮
    │   🪿 SASSY GOOSE FORTUNE TELLER   │
    ╰───────────────────────────────────╯
"""

# ASCII border template
def create_border(width=50):
    """Create an ASCII border."""
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = "║" + " " * (width - 2) + "║"
    return top_bottom, middle

def generate_fortune_output():
    """Generate the complete fortune output with ASCII art and formatting."""
    width = 50
    
    top_border, middle = create_border(width)
    
    # Get a random fortune
    fortune = random.choice(FORTUNES)
    
    # Format the fortune to fit within the border
    lines = []
    words = fortune.split()
    current_line = "║ "
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 1:
            current_line += word + " "
        else:
            lines.append(current_line.ljust(width - 1) + "║")
            current_line = "║ " + word + " "
    
    if current_line.strip():
        lines.append(current_line.ljust(width - 1) + "║")
    
    # Build the complete output
    output_lines = []
    output_lines.append(top_border)
    
    # Add the sassy goose
    goose_lines = GOOSE_ART.split('\n')
    for goose_line in goose_lines:
        if goose_line.strip():
            output_lines.append(f"║ {goose_line.center(width - 3)} ║")
        else:
            output_lines.append(f"║{' ' * (width - 2)}║")
    
    # Add divider
    output_lines.append(f"║{'─' * (width - 2)}║")
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_lines.append(f"║ {timestamp.center(width - 3)} ║")
    output_lines.append(f"║{'─' * (width - 2)}║")
    
    # Add the fortune
    for line in lines:
        output_lines.append(line)
    
    # Add closing
    output_lines.append(f"║{'─' * (width - 2)}║")
    output_lines.append(f"║ {'🔮 Your fortune has been revealed!' :^39} ║")
    output_lines.append(top_border)
    
    return '\n'.join(output_lines)

def main():
    """Main function to generate and save the fortune."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    
    fortune_file = os.path.join(base_dir, "fortune.md")
    old_dir = os.path.join(base_dir, "old")
    
    # If fortune.md exists, move it to old folder
    if os.path.exists(fortune_file):
        os.makedirs(old_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_dir, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_file)
        print(f"Moved existing fortune to: {old_file}")
    
    # Generate the fortune
    fortune_content = generate_fortune_output()
    
    # Convert to markdown format with code block for ASCII art
    markdown_output = f"""# 🪿 Sassy Goose Fortune

\`\`\`
{fortune_content}
\`\`\`

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    # Write to fortune.md
    with open(fortune_file, 'w') as f:
        f.write(markdown_output)
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + "=" * 50)
    print("ASCII Output Preview:")
    print("=" * 50)
    print(fortune_content)

if __name__ == "__main__":
    main()
