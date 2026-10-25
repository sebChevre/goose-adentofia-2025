#!/usr/bin/env python3
"""
Sassy Goose Fortune Teller
Generates sarcastic fortunes with ASCII art flair.
"""

import os
import random
from datetime import datetime

# Sassy goose ASCII art
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

GOOSE_ART_SASSY = """
       _
      ( \\
      / \\
     |   |
     |   |    __
     |   |   <(o )___
     |   |    ( ._> /
     |   |     \\___/
     |   |
     |   |
    /|   |\\
   / |   | \\
  /  |   |  \\
 /   |   |   \\
/____|___|____\\
"""

# Sarcastic fortune messages
FORTUNES = [
    "Your future is as bright as a fluorescent light in a dark room... if you enjoy that sort of thing.",
    "You will soon encounter a challenge. Or maybe just Monday. Either way, good luck with that.",
    "The stars say you'll make a decision today. Whether it's a good one remains to be seen.",
    "Someone is thinking about you. Probably wondering why you haven't replied to their message.",
    "Your luck is about to change. Unfortunately, so is the weather. It's going to rain.",
    "A surprise awaits you! It's called 'responsibility' and it's been waiting for you since 2019.",
    "You will find something you've been looking for. It was in your pocket the whole time.",
    "The universe has a message for you: 'Have you tried turning it off and on again?'",
    "Your talents will be recognized. By someone who doesn't understand them, but that's progress!",
    "A relationship will blossom. Like that plant you keep forgetting to water.",
    "Financial gain is on the horizon. It's called 'finding $5 in an old jacket.'",
    "You will face a difficult choice. Choose wisely, or don't. The goose doesn't care.",
    "Your dreams will come true. The ones you had while awake, during that meeting you weren't paying attention to.",
    "A journey awaits! It's from your couch to the kitchen. The snacks are calling.",
    "Your wisdom will be sought. By people who didn't read the instructions, naturally.",
    "You will overcome an obstacle. It's called 'hitting snooze one more time.'",
    "Love is in the air. Or maybe it's pollen. Either way, you might need tissues.",
    "Your creativity will flourish. Like that one idea you had in the shower three years ago.",
    "A secret will be revealed. It's that your coffee order is predictable.",
    "The future holds adventure! Like trying a new brand of cereal. Thrilling, I know.",
]

# Divider between goose and fortune
DIVIDER = "═══════════════════════════════════════════════════════════"


def generate_fortune():
    """Generate a random sarcastic fortune."""
    return random.choice(FORTUNES)


def create_fortune_output():
    """Create the complete fortune output with ASCII art and border."""
    fortune = generate_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build the output
    border = "═" * 67

    output = f"""{border}
║  {timestamp:^61}  ║
{border}
║                                                                      ║
║  ╔═══════════════════════════════════════════════════════════════╗  ║
║  ║                                                               ║  ║
║  ║           🦢 THE SASSY GOOSE FORTUNE TELLER 🦢                ║  ║
║  ║                                                               ║  ║
║  ║  {GOOSE_ART_SASSY:^61}  ║  ║
║  ║                                                               ║  ║
║  ║  {DIVIDER:^61}  ║  ║
║  ║                                                               ║  ║
║  ║  YOUR FORTUNE:                                                ║  ║
║  ║                                                               ║  ║
║  ║  "{fortune}"  ║  ║
║  ║                                                               ║  ║
║  ╚═══════════════════════════════════════════════════════════════╝  ║
║                                                                      ║
║  Remember: The goose knows all, judges nothing, and still thinks   ║
║  you could do better.                                               ║
║                                                                      ║
{border}"""

    return output


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
