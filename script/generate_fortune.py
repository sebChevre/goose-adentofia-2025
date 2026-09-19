#!/usr/bin/env python3
"""
Fortune Generator - A sassy goose fortune teller
Generates poetic fortunes with ASCII art
"""

import os
import random
from datetime import datetime

# Sassy Goose ASCII Art
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

GOOSE_ART_SASSY = """
        __
      <(o )___
       ( ._> /  *snort*
        \\___/
"""

GOOSE_ART_WISE = """
       __
     <(o )___
      ( ._> /  *hmm*
       \\___/
"""

GOOSE_ART_MISCHIEVOUS = """
        __
      <(o )___
       ( ._> /  *wink*
        \\___/
"""

# Poetic Fortune Messages
FORTUNES = [
    "The stars whisper that your courage will bloom like midnight roses, \n   revealing paths unseen to those who dare to dream.",
    "A river of opportunity flows toward you, but only if you \n   remember to build bridges, not walls.",
    "The moon knows your secret wish. Three cycles from now, \n   it shall manifest in ways most unexpected.",
    "Beware the golden hour—it brings both treasure and trials. \n   Choose wisely which you shall embrace.",
    "The wind carries news from distant shores. Listen closely, \n   for the answer you seek rides on its breath.",
    "An old friend returns bearing gifts you thought lost forever. \n   Their timing, as always, is impeccable.",
    "The universe conspires in your favor, but only after you \n   take the first step into the unknown.",
    "A door you've been avoiding holds the key to your greatest \n   adventure. Turn the handle.",
    "The seeds you planted in darkness now seek the light. \n   Tend them well, for they will bear fruit.",
    "Your intuition speaks in riddles because the truth is \n   too beautiful for plain words. Trust its voice.",
    "A chance encounter will rewrite a chapter you thought \n   was finished. Keep your quill ready.",
    "The mirror shows not who you are, but who you're becoming. \n   The reflection is more magnificent than you know.",
]

# Border and Divider Characters
BORDER_CHAR = "═"
CORNER_CHAR = "╔"
CORNER_CHAR_END = "╗"
CORNER_CHAR_BOTTOM_START = "╚"
CORNER_CHAR_BOTTOM_END = "╝"
SIDE_CHAR = "║"
DIVIDER = "────────────────────────────────────────"


def generate_fortune():
    """Generate a random poetic fortune."""
    return random.choice(FORTUNES)


def get_random_goose():
    """Return a random sassy goose ASCII art."""
    gooses = [GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_WISE, GOOSE_ART_MISCHIEVOUS]
    return random.choice(gooses)


def create_border(content, width=50):
    """Create an ASCII border around content."""
    border_top = CORNER_CHAR + BORDER_CHAR * (width - 2) + CORNER_CHAR_END
    border_bottom = CORNER_CHAR_BOTTOM_START + BORDER_CHAR * (width - 2) + CORNER_CHAR_BOTTOM_END

    lines = content.split('\n')
    bordered_lines = []

    for line in lines:
        # Pad line to fit within border
        padded_line = line.ljust(width - 2)
        bordered_lines.append(SIDE_CHAR + padded_line + SIDE_CHAR)

    return f"{border_top}\n" + "\n".join(bordered_lines) + f"\n{border_bottom}"


def generate_fortune_output():
    """Generate the complete fortune output with all decorations."""
    fortune = generate_fortune()
    goose = get_random_goose()

    # Create the header
    header = """
    ╔════════════════════════════════════════════╗
    ║         🌙 THE SASSY GOOSE FORTUNE 🌙       ║
    ║          Your Cosmic Guidance Awaits       ║
    ╚════════════════════════════════════════════╝
    """

    # Create the fortune section
    fortune_section = f"""
    ║                                          ║
    ║   YOUR FORTUNE:                          ║
    ║                                          ║
    """

    # Add fortune lines with border
    fortune_lines = fortune.split('\n')
    for line in fortune_lines:
        fortune_section += f"║   {line.ljust(44)}║\n"

    fortune_section += """
    ║                                          ║
    ║   ════════════════════════════════════════   ║
    ║                                          ║
    """

    # Add goose art
    goose_lines = goose.strip().split('\n')
    for line in goose_lines:
        fortune_section += f"║     {line.center(40)}║\n"

    fortune_section += """
    ║                                          ║
    ║   May the cosmos be ever in your favor   ║
    ║                                          ║
    """

    # Create footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    footer = f"""
    ║   Generated: {timestamp.ljust(28)}║
    ╚════════════════════════════════════════════╝
    """

    return header + fortune_section + footer


def main():
    """Main function to generate and save fortune."""
    # Current working directory
    cwd = os.getcwd()
    fortune_path = os.path.join(cwd, "fortune.md")
    old_folder = os.path.join(cwd, "old")

    # Check if fortune.md exists and move it to old folder
    if os.path.exists(fortune_path):
        os.makedirs(old_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_path = os.path.join(old_folder, f"fortune_{timestamp}.md")
        os.rename(fortune_path, old_path)
        print(f"Existing fortune.md moved to: {old_path}")

    # Generate the fortune
    fortune_content = generate_fortune_output()

    # Write to fortune.md
    with open(fortune_path, 'w') as f:
        f.write(fortune_content)

    print(f"Fortune generated successfully! Saved to: {fortune_path}")
    print("\n" + "=" * 50)
    print(fortune_content)


if __name__ == "__main__":
    main()
