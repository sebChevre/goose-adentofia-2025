#!/usr/bin/env python3
"""
Grumpy Fortune Teller - A sassy goose fortune generator
"""

import os
import random
from datetime import datetime

# Grumpy fortunes with a sassy attitude
FORTUNES = [
    "Your path forward is... meh. Try harder next time.",
    "I see... nothing spectacular. Get back to work.",
    "The stars say you'll be fine. Don't get cocky.",
    "Luck is coming. But probably not for you specifically.",
    "Your future holds... more of the same. Surprise!",
    "The universe is indifferent to your struggles. Join the club.",
    "Success awaits! If you can drag yourself off the couch.",
    "A surprise is coming. It's probably something annoying.",
    "Your dreams are valid. Too bad reality doesn't care.",
    "The cosmos whisper... 'figure it out yourself'.",
    "You'll find what you're looking for. Eventually. Maybe.",
    "Great news! You survived another day. Congratulations.",
    "The future looks... adequate. I guess.",
    "Your luck is about to change. Don't hold your breath.",
    "The universe has a plan. It's not a good one for you.",
]

# Sassy goose ASCII art
GOOSE_ART = """
  __      __
 /'\\_____/\\
/  o     o  \\
(    ==    )
 \\        /
  /|      |\\
 ( |      | )
/\\|______|/\\
   |    |
   |    |
   |    |
  _/      \\_
 (          )
  \\________/
"""

# Alternative grumpier goose
GOOSE_ART_GRUMPY = """
  __      __
 /'\\_____/\\
/  ^     ^  \\
(    --    )
 \\        /
  /|      |\\
 ( |      | )
/\\|______|/\\
   |    |
   |    |
   |    |
  _/      \\_
 (          )
  \\________/
"""

# Even sassier goose
GOOSE_ART_SASSY = """
  __      __
 /'\\_____/\\
/  ~     ~  \\
(    ><    )
 \\        /
  /|      |\\
 ( |      | )
/\\|______|/\\
   |    |
   |    |
   |    |
  _/      \\_
 (          )
  \\________/
"""

def generate_fortune():
    """Generate a random grumpy fortune."""
    return random.choice(FORTUNES)

def get_goose_art():
    """Get a random sassy goose art."""
    return random.choice([GOOSE_ART, GOOSE_ART_GRUMPY, GOOSE_ART_SASSY])

def create_fortune_display():
    """Create the complete fortune display with ASCII art and border."""
    fortune = generate_fortune()
    goose = get_goose_art()
    
    # Get the max width needed for the border
    lines = fortune.split('\n') + [''] + [goose]
    max_width = max(len(line) for line in lines) + 4
    
    # Create top border
    top_border = '╔' + '═' * (max_width - 2) + '╗'
    bottom_border = '╚' + '═' * (max_width - 2) + '╝'
    side_border = '║'
    
    # Build the display
    display_lines = []
    display_lines.append(top_border)
    
    # Title
    title = "🔮 GRUMPY FORTUNE TELLER 🔮"
    padding = (max_width - len(title) - 2) // 2
    display_lines.append(f"{side_border}{' ' * padding}{title}{' ' * (max_width - len(title) - padding - 2)}{side_border}")
    display_lines.append(f"{side_border}{' ' * (max_width - 2)}{side_border}")
    
    # Fortune section
    for line in fortune.split('\n'):
        display_lines.append(f"{side_border}  {line}{' ' * (max_width - len(line) - 4)}{side_border}")
    
    # Divider
    divider = f"{side_border}{'─' * (max_width - 2)}{side_border}"
    display_lines.append(divider)
    
    # Goose art
    for line in goose.split('\n'):
        display_lines.append(f"{side_border}  {line}{' ' * (max_width - len(line) - 4)}{side_border}")
    
    # Footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    footer_text = f"🌙 Fortune told on {timestamp} 🌙"
    padding = (max_width - len(footer_text) - 2) // 2
    display_lines.append(f"{side_border}{' ' * padding}{footer_text}{' ' * (max_width - len(footer_text) - padding - 2)}{side_border}")
    
    display_lines.append(bottom_border)
    
    return '\n'.join(display_lines)

def main():
    """Main function to generate and save fortune."""
    output_file = "fortune.md"
    old_folder = "old"
    
    # Check if fortune.md already exists
    if os.path.exists(output_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        os.rename(output_file, old_path)
        print(f"Moved existing fortune.md to {old_path}")
    
    # Generate the fortune display
    fortune_display = create_fortune_display()
    
    # Create markdown content with the ASCII art
    markdown_content = f"""# 🦆 Grumpy Fortune Teller 🦆

```
{fortune_display}
```

*May your day be slightly less annoying than usual.*
"""
    
    # Write to fortune.md
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    print(f"Fortune generated and saved to {output_file}")
    print("\n" + "=" * 50)
    print(fortune_display)
    print("=" * 50)

if __name__ == "__main__":
    main()
