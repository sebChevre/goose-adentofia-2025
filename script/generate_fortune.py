#!/usr/bin/env python3
"""
Fortune Generator - Grumpy Fortune Teller Edition
Generates fortunes from a sassy, grumpy goose fortune teller.
"""

import os
import random
from datetime import datetime

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.dirname(SCRIPT_DIR)  # Current directory (parent of script/)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "fortune.md")
OLD_DIR = os.path.join(OUTPUT_DIR, "old")

# Grumpy fortune messages
FORTUNES = [
    "Ugh, you want another fortune? Fine. The stars say you're wasting my time.",
    "Hmmph! Your future looks... *sigh*... the same as your past. Boring.",
    "Oh great, another human. The universe whispers: 'Stop asking for advice.'",
    "I hate doing this. Your luck is... adequate. There, happy now?",
    "*rolls eyes* The cosmos tells me you'll find what you're looking for... eventually.",
    "Fine, fine! Your destiny involves more coffee and less complaining.",
    "Ugh, whatever. The omens say you should just go outside. Touch grass.",
    "This better be quick. Your future involves... *checks notes*... more of today.",
    "Hmph! The spirits say you're overthinking everything. Shocking.",
    "*grumbles* Your fortune: Stop looking for magic answers. They don't exist.",
    "Oh joy, another reading. The universe says: 'Try harder, I guess.'",
    "*sighs dramatically* Your future is bright. Too bad you're too grumpy to see it.",
    "Look, I'm not paid enough for this. Your luck will improve... maybe.",
    "Ugh, the fates say you need to listen more and talk less. There. You're welcome.",
    "Fine! Your destiny involves less screen time and more actual friends.",
]

# Sassy Goose ASCII Art
SASSY_GOOSE = r"""
     __      __
    /  \    /  \
   |    \__/    |
   |  o      o  |
   |     <      |  UGH. ANOTHER HUMAN?
   |   \____/   |  Can't you see I'm busy
   |  /______\  |  being magnificent?
   |  \      /  |
    \  \____/  /
     \        /
      \______/
       |    |
       |    |
      /      \
     |        |
     |  /  \  |
     |  \__/  |
     |        |
     |        |
     \        /
      \______/
"""

# Border characters
TOP_BORDER = "╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
BOTTOM_BORDER = "╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝"
SIDEBAR = "║"
DIVIDER = "╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╢"


def generate_fortune():
    """Generate a random fortune from the grumpy fortune teller."""
    return random.choice(FORTUNES)


def create_fortune_display():
    """Create the full fortune display with borders, goose, and fortune."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build the display
    lines = []
    lines.append(TOP_BORDER)
    lines.append(f"{SIDEBAR}{'🔮 GRUMPY FORTUNE TELLER 🔮'.center(116)}{SIDEBAR}")
    lines.append(f"{SIDEBAR}{'(A Sassy Goose Who Definitely Doesnt Want to Be Here)'.center(116)}{SIDEBAR}")
    lines.append(TOP_BORDER)
    lines.append(SIDEBAR)
    lines.append(SIDEBAR)

    # Add the sassy goose
    for goose_line in SASSY_GOOSE.strip().split('\n'):
        lines.append(f"{SIDEBAR} {goose_line.ljust(114)}{SIDEBAR}")

    lines.append(SIDEBAR)
    lines.append(DIVIDER)
    lines.append(f"{SIDEBAR}{'📜 YOUR FORTUNE 📜'.center(116)}{SIDEBAR}")
    lines.append(f"{SIDEBAR}{''.center(116)}{SIDEBAR}")

    # Wrap the fortune text
    fortune_words = fortune.split()
    current_line = ""
    for word in fortune_words:
        if len(current_line) + len(word) + 1 <= 114:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(f"{SIDEBAR} {current_line.ljust(114)}{SIDEBAR}")
            current_line = word
    if current_line:
        lines.append(f"{SIDEBAR} {current_line.ljust(114)}{SIDEBAR}")

    lines.append(f"{SIDEBAR}{''.center(116)}{SIDEBAR}")
    lines.append(f"{SIDEBAR}{'Generated on: ' + timestamp.center(104)}{SIDEBAR}")
    lines.append(BOTTOM_BORDER)

    return '\n'.join(lines)


def move_existing_fortune():
    """Move existing fortune.md to the old folder if it exists."""
    if os.path.exists(OUTPUT_FILE):
        os.makedirs(OLD_DIR, exist_ok=True)
        old_filename = f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        old_path = os.path.join(OLD_DIR, old_filename)
        os.rename(OUTPUT_FILE, old_path)
        print(f"Moved existing fortune to: {old_path}")


def save_fortune(content):
    """Save the fortune content to fortune.md."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fortune saved to: {OUTPUT_FILE}")


def main():
    """Main function to generate and save the fortune."""
    print("🔮 Consulting the grumpy fortune teller...")
    print("🦢 (She's already annoyed, but here we go anyway)")

    # Move existing fortune if present
    move_existing_fortune()

    # Generate the fortune display
    fortune_display = create_fortune_display()

    # Save to file
    save_fortune(fortune_display)

    # Also print to console
    print("\n")
    print(fortune_display)
    print("\n✨ Your fortune has been generated! ✨")


if __name__ == "__main__":
    main()
