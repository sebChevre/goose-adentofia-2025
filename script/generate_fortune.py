#!/usr/bin/env python3
"""
Sassy Goose Fortune Teller
Generates poetic fortunes with ASCII art flair.
"""

import os
import random
from datetime import datetime

# Sassy goose ASCII art - positioned at the bottom
GOOSE_ART = [
    "           __           ",
    "        .-(  `.         ",
    "       /   _    \\       ",
    "      |   (o)   |       ",
    "       \\   _.  /        ",
    "        `.__.'         ",
    "         \\  /          ",
    "      _   \\/   _       ",
    "     ( \\_     _/ )     ",
    "      \\  `---'  /      ",
    "       `-------`       ",
]

# Poetic fortune messages (single line with \\n for line break)
FORTUNES = [
    "Like autumn leaves that dance upon the breeze,  Your path unfolds through whispered mysteries.",
    "A star will rise when twilight paints the sky,  And guide your heart where dreams dare touch the high.",
    "The river flows with secrets yet untold,  Of silver threads and stories waiting to unfold.",
    "Like moonlight on a mirror's gentle face,  You'll find the grace to run your own sweet race.",
    "The winds of change will carry you afar,  To distant shores where bright new stars are.",
    "As morning breaks upon a dew-kissed rose,  A gentle truth the universe will show.",
    "Like echoes in a canyon deep and wide,  Your courage will become your inner guide.",
    "The garden of tomorrow waits to bloom,  With flowers that dispel all shadowed gloom.",
    "A melody will drift upon the air,  To lift your spirit from its quiet lair.",
    "Like tides that pull the moon across the sea,  You're drawn to where your soul is meant to be.",
    "The pages turn of life's great open book,  And in your hands, a fresh and hopeful look.",
    "As fireflies ignite the summer night,  Your path will shimmer with reflected light.",
    "The mountain stands, both ancient and so still,  Yet you possess the will to climb the hill.",
    "Like petals falling from a cherry tree,  New chances bloom for you to truly see.",
    "The compass points where courage leads the way,  To brighter days that beckon and will stay.",
]


def wrap_text(text, width):
    """Wrap text to fit within specified width."""
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines


def create_fortune_output():
    """Create the complete fortune output with ASCII art and border."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Width constants
    OUTER_WIDTH = 60
    INNER_WIDTH = 56
    
    # Build fortune lines (wrapped to fit)
    fortune_lines = wrap_text(fortune, 52)
    
    # Build goose lines (already formatted)
    goose_lines = GOOSE_ART
    
    # Calculate heights
    fortune_height = len(fortune_lines)
    goose_height = len(goose_lines)
    
    # Build the output
    lines = []
    
    # Outer top border
    lines.append("╔" + "═" * OUTER_WIDTH + "╗")
    
    # Header
    header = "🔮 THE MYSTIC FORTUNE TELLER 🔮"
    lines.append("║" + header.center(OUTER_WIDTH) + "║")
    lines.append("║" + " " * OUTER_WIDTH + "║")
    
    # Timestamp
    lines.append("║" + f"  {timestamp}  ".center(OUTER_WIDTH) + "║")
    lines.append("║" + " " * OUTER_WIDTH + "║")
    
    # Inner border top
    lines.append("╠" + "═" * INNER_WIDTH + "╣")
    
    # Fortune section
    lines.append("║" + " YOUR FORTUNE: ".ljust(INNER_WIDTH) + "║")
    lines.append("║" + " " * INNER_WIDTH + "║")
    
    for fl in fortune_lines:
        lines.append("║  " + fl.ljust(50) + "  ║")
    
    lines.append("║" + " " * INNER_WIDTH + "║")
    
    # Inner border bottom
    lines.append("╚" + "═" * INNER_WIDTH + "╝")
    
    # Divider
    lines.append("├" + "─" * INNER_WIDTH + "┤")
    
    # Goose section header
    lines.append("║" + " 🦢 THE SASSY GOOSE 🦢 ".ljust(INNER_WIDTH) + "║")
    lines.append("║" + " " * INNER_WIDTH + "║")
    
    # Goose art
    for gl in goose_lines:
        lines.append("║  " + gl.center(50) + "  ║")
    
    lines.append("║" + " " * INNER_WIDTH + "║")
    
    # Goose quote
    lines.append("║" + " \"The goose foresees... you'll need more coffee.\" ".ljust(INNER_WIDTH) + "║")
    lines.append("║" + " " * INNER_WIDTH + "║")
    
    # Closing message
    lines.append("║" + " May your day be as bright as a goose's opinion of itself. ".ljust(INNER_WIDTH) + "║")
    lines.append("║" + " " * INNER_WIDTH + "║")
    
    # Outer bottom border
    lines.append("╚" + "═" * OUTER_WIDTH + "╝")
    
    return "\n".join(lines)


def generate_fortune():
    """Generate a random poetic fortune."""
    return random.choice(FORTUNES)


def main():
    """Main function to generate and save the fortune."""
    # Current working directory
    cwd = os.getcwd()

    # Check if fortune.md already exists
    fortune_path = os.path.join(cwd, "fortune.md")
    old_folder = os.path.join(cwd, "old")

    if os.path.exists(fortune_path):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)

        # Move existing file to old folder with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_name = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_name)
        os.rename(fortune_path, old_path)
        print(f"Moved existing fortune.md to: {old_path}")

    # Generate the fortune
    fortune_output = create_fortune_output()

    # Write to fortune.md
    with open(fortune_path, "w", encoding="utf-8") as f:
        f.write(fortune_output)

    print(f"Fortune generated and saved to: {fortune_path}")
    print("\n" + fortune_output)


if __name__ == "__main__":
    main()
