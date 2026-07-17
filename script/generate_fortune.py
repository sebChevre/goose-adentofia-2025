#!/usr/bin/env python3
"""
Fortune Generator - A wise fortune teller with a sassy goose
"""

import os
import shutil
from datetime import datetime

# Wise fortunes from the mystical goose oracle
FORTUNES = [
    "The path you seek is not straight, but winding like a river through time. Trust your instincts.",
    "Wisdom comes not from knowing all answers, but from asking better questions.",
    "A challenge awaits, but within you lies the strength to transform it into opportunity.",
    "The stars align in your favor, but only if you dare to take the first step.",
    "Patience is your greatest ally. What seems delayed is being perfected.",
    "The goose sees three paths: one of knowledge, one of love, one of courage. Choose wisely.",
    "Your past mistakes are not chains, but stepping stones to your destiny.",
    "The answer you seek comes from within, not from the voices around you.",
    "A unexpected encounter will bring clarity to your current dilemma.",
    "The universe whispers of abundance, but you must open your hands to receive.",
]

# Sassy goose ASCII art
GOOSE_ART = """
  __
 (o o)
  \\_/
 /| |\\
/_| |_\\
  | |
  | |
 /   \\
(     )
 \\___/
"""

# Alternative sassy goose variations
GOOSE_ARTS = [
    """
  __
 (o o)  *squint*
  \\_/
 /| |\\
/_| |_\\
  | |
  | |
 /   \\
(     )
 \\___/
""",
    """
  __
 (> <)  *unimpressed*
  \\_/
 /| |\\
/_| |_\\
  | |
  | |
 /   \\
(     )
 \\___/
""",
    """
  __
 (o o)  *knows better*
  \\_/
 /| |\\
/_| |_\\
  | |
  | |
 /   \\
(     )
 \\___/
""",
]

def get_random_fortune():
    """Get a random wise fortune."""
    import random
    return random.choice(FORTUNES)

def get_sassy_goose():
    """Get a random sassy goose ASCII art."""
    import random
    return random.choice(GOOSE_ARTS)

def create_bordered_content(fortune, goose_art, border_width=60):
    """Create visually appealing bordered content with divider."""
    border_char = "═"
    side_char = "║"
    
    lines = []
    
    # Top border
    lines.append("╔" + border_char * border_width + "╗")
    
    # Title
    title = "🔮 WISE FORTUNE ORACLE 🔮"
    padding = (border_width - len(title)) // 2
    lines.append("║" + " " * padding + title + " " * (border_width - padding - len(title)) + "║")
    lines.append("╠" + border_char * border_width + "╣")
    
    # Fortune section
    fortune_lines = fortune.split('\n')
    for fl in fortune_lines:
        padding = (border_width - len(fl)) // 2
        lines.append("║" + " " * padding + fl + " " * (border_width - padding - len(fl)) + "║")
    
    lines.append("╠" + border_char * border_width + "╣")
    
    # Divider
    lines.append("║" + " " * (border_width // 2 - 3) + "✦ ✦ ✦" + " " * (border_width // 2 - 3) + "║")
    lines.append("║" + " " * border_width + "║")
    
    # Goose section
    goose_lines = goose_art.strip().split('\n')
    for gl in goose_lines:
        padding = (border_width - len(gl)) // 2
        lines.append("║" + " " * padding + gl + " " * (border_width - padding - len(gl)) + "║")
    
    lines.append("╠" + border_char * border_width + "╣")
    
    # Footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    footer = f"Oracle consulted: {timestamp}"
    padding = (border_width - len(footer)) // 2
    lines.append("║" + " " * padding + footer + " " * (border_width - padding - len(footer)) + "║")
    
    # Bottom border
    lines.append("╚" + border_char * border_width + "╝")
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save fortune."""
    # Output file path
    output_file = "fortune.md"
    old_folder = "old"
    
    # Handle existing fortune.md
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        shutil.move(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate content
    fortune = get_random_fortune()
    goose_art = get_sassy_goose()
    content = create_bordered_content(fortune, goose_art)
    
    # Add markdown header for the file
    markdown_content = f"""# 🦢 Wise Fortune Oracle

{content}

---

*May the wisdom of the sassy goose guide your path.*
"""
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + "=" * 50)
    print("Your fortune:")
    print(fortune)
    print("=" * 50)

if __name__ == "__main__":
    main()
