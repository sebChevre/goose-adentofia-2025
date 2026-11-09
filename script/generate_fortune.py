#!/usr/bin/env python3
"""
Fortune Generator - A Sarcastic Fortune Teller
Generates fortunes with attitude and delivers them with a sassy goose.
"""

import os
import random
from datetime import datetime

# Sassy fortune messages
FORTUNES = [
    "Your dreams are valid, but your execution is questionable.",
    "I see great things in your future... if you actually put in effort.",
    "The stars say you're capable, but are you willing to stop procrastinating?",
    "Success is within reach. So is your ex's new relationship. Pick one.",
    "A surprise awaits you! It's probably just another email.",
    "Your future looks bright... unlike your current search history.",
    "Opportunity knocks. Unfortunately, you're too busy scrolling.",
    "The universe has a plan for you. It involves more coffee.",
    "You will achieve your goals. Eventually. Maybe.",
    "Fortune favors the bold. You favor the comfortable.",
    "Your potential is limitless. Your motivation is not.",
    "Good things come to those who wait. You've been waiting.",
    "The road to success is under construction. Like your life.",
    "Your lucky numbers are 1, 2, 3... oh wait, you already knew that.",
    "A wise person learns from mistakes. A wiser person avoids them. You?",
    "The future holds promise. Your past holds receipts.",
    "You'll succeed when you stop asking AI for life advice.",
    "Fortune smiles upon you. It's a pity you can't smile back.",
    "Your destiny is written in the stars. Or maybe just in your notes app.",
    "Everything will work out. Eventually. Don't hold your breath.",
]

# Sassy Goose ASCII Art
SASSY_GOOSE = r"""
           __
          /  \
         |    |
         |    |
        /      \
       |        |
       |  o  o  |
       |   <    |  *Sigh* Here we go again...
       |  __    |
      /| /  \ |\
     / | \__/ | \
    |  |      |  |
    |  |      |  |
    |  |      |  |
    |  |      |  |
    |  |      |  |
    |  |      |  |
    \  \      /  /
     \  \____/  /
      \        /
       \______/
"""

# Border character
BORDER_CHAR = "="
DIVIDER = "-" * 60


def get_fortune():
    """Select a random sarcastic fortune."""
    return random.choice(FORTUNES)


def generate_fortune_output():
    """Generate the complete fortune output with ASCII art and formatting."""
    fortune = get_fortune()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the fortune output with ASCII border
    border = BORDER_CHAR * 62
    
    # Format fortune text with proper width
    fortune_lines = []
    words = fortune.split()
    current_line = "║ "
    for word in words:
        if len(current_line) + len(word) + 1 <= 60:
            current_line += word + " "
        else:
            fortune_lines.append(current_line.ljust(60) + " ║")
            current_line = "║ " + word + " "
    fortune_lines.append(current_line.ljust(60) + " ║")
    
    fortune_box = f"""
{border}
║                    ✨ YOUR FORTUNE ✨                    ║
{border}
║                                                          ║
{chr(10).join(fortune_lines)}
║                                                          ║
{border}"""

    # Combine goose and fortune with divider
    output = f"""{border}
║                                                          ║
║              🦢 THE SASSY GOOSE FORTUNE TELLER 🦢         ║
║                                                          ║
{border}

{SASSY_GOOSE}

{DIVIDER}

{fortune_box}

{border}
║           Generated: {timestamp:<38} ║
║                                                          ║
║        "The goose giveth, and the goose takeeth away."   ║
{border}
"""
    return output


def move_existing_file():
    """Move existing fortune.md to /old folder if it exists."""
    fortune_file = "fortune.md"
    old_folder = "old"
    
    if os.path.exists(fortune_file):
        # Create old folder if it doesn't exist
        os.makedirs(old_folder, exist_ok=True)
        
        # Move the existing file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        
        os.rename(fortune_file, old_path)
        print(f"Moved existing fortune.md to: {old_path}")


def main():
    """Main function to generate and save the fortune."""
    # Move existing file if present
    move_existing_file()
    
    # Generate fortune output
    output = generate_fortune_output()
    
    # Write to fortune.md
    with open("fortune.md", "w") as f:
        f.write(output)
    
    print("Fortune generated successfully!")
    print(f"Output saved to: fortune.md")
    print("\n" + output)


if __name__ == "__main__":
    main()
