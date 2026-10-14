#!/usr/bin/env python3
"""
Grumpy Fortune Teller - Generates fortunes from a sassy goose fortune teller
"""

import os
import random
from datetime import datetime

# Grumpy fortune messages
FORTUNES = [
    "Ugh, fine. Your future looks... tolerable. I guess.",
    "Hmph. I see you'll make it through today. Don't expect me to cheer.",
    "Your destiny? Meh. It's adequate. Like everything else.",
    "Oh joy, another fortune reading. You'll encounter someone annoying.",
    "Great. Your luck is... fine. Stop looking at me like that.",
    "I'm too old for this. Your future involves coffee and patience.",
    "Ugh. You'll find what you're looking for. Eventually. Maybe.",
    "Fine. Success is coming. But you'll have to work for it.",
    "Whatever. You're going to be just... okay. Don't get excited.",
    "Sigh. Your day will be predictable. Like my mood.",
    "Hmph. A surprise awaits you. Try not to be disappointed.",
    "Look, you'll be fine. Can I go back to sleep now?",
    "Your future holds... more of the same. Thrilling, I know.",
    "Ugh. You'll make a mistake. But you'll recover. Barely.",
    "Fine. Someone will appreciate you today. Don't get used to it.",
]

# Sassy goose ASCII art
SASSY_GOOSE = r"""
      __
    <(o )___
     ( ._> /
      \___/
"""

SASSY_GOOSE_2 = r"""
     __
    ( )
   (   )
  (     )
   \___/
"""

SASSY_GOOSE_3 = r"""
      _
    <(o )
     (  >
      \_/
"""

# Border character
BORDER_CHAR = "═"
DIVIDER_CHAR = "─"


def generate_fortune():
    """Generate a grumpy fortune with ASCII art"""
    fortune = random.choice(FORTUNES)
    goose_art = random.choice([SASSY_GOOSE, SASSY_GOOSE_2, SASSY_GOOSE_3])
    
    # Create the formatted output
    border = BORDER_CHAR * 50
    divider = DIVIDER_CHAR * 50
    
    output = f"""{border}
    🦢 GRUMPY FORTUNE TELLER 🦢
    {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{border}

{goose_art}

{divider}

    {fortune}

{divider}

    *Hmph.* Come back when you're interesting.
{border}
"""
    return output


def main():
    """Main function to generate and save fortune"""
    output_dir = os.getcwd()
    fortune_file = os.path.join(output_dir, "fortune.md")
    old_dir = os.path.join(output_dir, "old")
    
    # Create old directory if it doesn't exist
    if not os.path.exists(old_dir):
        os.makedirs(old_dir)
    
    # If fortune.md exists, move it to old folder
    if os.path.exists(fortune_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_file = os.path.join(old_dir, f"fortune_{timestamp}.md")
        os.rename(fortune_file, old_file)
        print(f"Moved existing fortune.md to: {old_file}")
    
    # Generate the fortune
    fortune_content = generate_fortune()
    
    # Write to fortune.md
    with open(fortune_file, 'w', encoding='utf-8') as f:
        f.write(fortune_content)
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + fortune_content)


if __name__ == "__main__":
    main()
