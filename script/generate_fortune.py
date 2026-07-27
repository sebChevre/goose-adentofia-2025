#!/usr/bin/env python3
"""
Fortune Generator - A wise sassy goose fortune teller
"""
import os
import shutil
from datetime import datetime

# Sassy goose ASCII art
GOOSE_ART = """
   __
  /  \\
 |    |
 |    |
  \\__/
  (oo)\\____
  (__)\\    )\\/\\
      ||----w |
      ||     ||
   __/
  /  \\
 | 👁️ |
 | 👁️ |
  \\__/
"""

# Wise fortune messages
FORTUNES = [
    "The path you seek is not straight, but winding. Trust your instincts.",
    "Wisdom comes not from knowing all answers, but asking better questions.",
    "A sassy goose knows when to quack and when to be silent. Choose wisely.",
    "The stars align in your favor, but only if you dare to take flight.",
    "True strength lies in knowing when to waddle and when to soar.",
    "Your journey will be guided by those who seem most unlikely.",
    "Patience is the key that unlocks doors you didn't know existed.",
    "The wisdom you seek is already within you; listen to your inner goose.",
    "Challenges ahead will shape you into something greater than you imagine.",
    "A friend's advice will prove more valuable than gold this week."
]

def get_fortune():
    """Generate a wise fortune."""
    import random
    return random.choice(FORTUNES)

def create_fortune_display():
    """Create the full fortune display with border, goose, and fortune."""
    fortune = get_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Calculate max width for the border
    border_width = 50
    
    # Create the display
    lines = []
    
    # Top border
    lines.append("╔" + "═" * (border_width - 2) + "╗")
    
    # Title
    title = "🔮 WISE SASSY GOOSE FORTUNE TELLER 🔮"
    padding = (border_width - 2 - len(title)) // 2
    lines.append("║" + " " * padding + title + " " * (border_width - 2 - len(title) - padding) + "║")
    
    # Goose section
    goose_lines = GOOSE_ART.strip().split('\n')
    for line in goose_lines:
        # Center the goose art
        padding = (border_width - 2 - len(line)) // 2
        lines.append("║" + " " * padding + line + " " * (border_width - 2 - len(line) - padding) + "║")
    
    # Divider
    lines.append("║" + "─" * (border_width - 2) + "║")
    
    # Fortune section
    fortune_line = f"✨ {fortune} ✨"
    padding = (border_width - 2 - len(fortune_line)) // 2
    lines.append("║" + " " * padding + fortune_line + " " * (border_width - 2 - len(fortune_line) - padding) + "║")
    
    # Timestamp
    time_line = f"Generated: {timestamp}"
    padding = (border_width - 2 - len(time_line)) // 2
    lines.append("║" + " " * padding + time_line + " " * (border_width - 2 - len(time_line) - padding) + "║")
    
    # Bottom border
    lines.append("╚" + "═" * (border_width - 2) + "╝")
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md exists and move it to old folder
    if os.path.exists(output_file):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_folder, f"fortune_{timestamp}.md")
        shutil.move(output_file, old_file)
        print(f"Moved existing fortune.md to {old_file}")
    
    # Create the fortune display
    fortune_display = create_fortune_display()
    
    # Write to fortune.md
    with open(output_file, 'w') as f:
        f.write("```text\n")
        f.write(fortune_display)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + fortune_display)

if __name__ == "__main__":
    main()
