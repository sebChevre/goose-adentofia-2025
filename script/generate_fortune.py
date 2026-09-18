#!/usr/bin/env python3
"""
Fortune Generator - A Sarcastic Fortune Teller
Generates witty, sassy fortunes with ASCII art flair.
"""

import os
import random
from datetime import datetime

# Sarcastic fortune messages
FORTUNES = [
    "Ah yes, your future looks... predictable. Shocking, I know.",
    "The stars align to tell you one thing: try harder next time.",
    "A great opportunity awaits! (Just kidding, it's probably not for you.)",
    "Your destiny? To be mildly disappointed by this fortune.",
    "The universe whispers: 'Did you really expect anything better?'",
    "Congratulations! Your future is exactly as exciting as you imagined.",
    "The cosmic energies suggest... well, they suggest nothing. Just like your life.",
    "A mysterious stranger will enter your life. Probably just the mailman.",
    "Your lucky numbers are 404 - Not Found. Fitting, right?",
    "The oracle sees... a lot of scrolling through your phone.",
    "Fortune favors the bold, but you? You favor comfort.",
    "Today is a good day to do nothing. The stars approve.",
    "Your future holds... more of the same. But with better lighting!",
    "The universe has a sense of humor. Your future is its punchline.",
    "A grand adventure awaits! (It involves laundry, but still.)",
]

# ASCII art sassy goose
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

GOOSE_ART_SASSY = """
       __
     <(o )___
      ( ._> /
       \\___/
     *sassiest goose*
"""

GOOSE_ART_ROLLING_EYES = """
      __
    <(@ )___
     ( ._> /
      \\___/
     (eye roll)
"""

GOOSE_ART_UNIMPRESSED = """
      __
    <(o )___
     ( ._> /
      \\___/
     (not impressed)
"""

GOOSE_ARTS = [GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_ROLLING_EYES, GOOSE_ART_UNIMPRESSED]

# ASCII border characters
TOP_BORDER = "╔" + "═" * 58 + "╗"
BOTTOM_BORDER = "╚" + "═" * 58 + "╝"
MIDDLE_BORDER = "║" + " " * 58 + "║"
DIVIDER = "║" + "─" * 58 + "║"


def generate_fortune():
    """Generate a random sarcastic fortune."""
    return random.choice(FORTUNES)


def get_goose_art():
    """Get a random sassy goose ASCII art."""
    return random.choice(GOOSE_ARTS)


def format_fortune_with_art(fortune, goose_art):
    """Format the fortune with ASCII art, border, and divider."""
    lines = []
    lines.append(TOP_BORDER)
    lines.append("║" + " " * 20 + "🔮 FORTUNE TELLER 🔮" + " " * 16 + "║")
    lines.append("║" + " " * 18 + "(sarcasm level: expert)" + " " * 12 + "║")
    lines.append(MIDDLE_BORDER)

    # Add goose art with padding
    for art_line in goose_art.strip().split('\n'):
        lines.append("║  " + art_line.center(54) + "  ║")

    lines.append(DIVIDER)
    lines.append("║" + " " * 24 + "YOUR FORTUNE" + " " * 21 + "║")
    lines.append(MIDDLE_BORDER)

    # Add fortune text with proper wrapping
    fortune_lines = []
    words = fortune.split()
    current_line = "║  "
    for word in words:
        if len(current_line) + len(word) + 1 <= 58:
            current_line += word + " "
        else:
            fortune_lines.append(current_line + "║")
            current_line = "║  " + word + " "
    fortune_lines.append(current_line + "║")

    for fl in fortune_lines:
        lines.append(fl)

    lines.append(MIDDLE_BORDER)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append("║" + f" Generated: {timestamp}".ljust(56) + "║")
    lines.append(BOTTOM_BORDER)

    return '\n'.join(lines)


def handle_existing_fortune():
    """Move existing fortune.md to /old folder if it exists."""
    fortune_path = "fortune.md"
    old_folder = "old"

    if os.path.exists(fortune_path):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to {old_path}")


def main():
    """Main function to generate and save the fortune."""
    # Handle existing fortune file
    handle_existing_fortune()

    # Generate fortune and art
    fortune = generate_fortune()
    goose_art = get_goose_art()

    # Format output
    output = format_fortune_with_art(fortune, goose_art)

    # Write to fortune.md
    with open("fortune.md", "w") as f:
        f.write(output)
        f.write("\n")

    print("Fortune generated successfully!")
    print("\n" + output)


if __name__ == "__main__":
    main()
