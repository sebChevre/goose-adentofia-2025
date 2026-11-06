#!/usr/bin/env python3
"""
Sarcastic Fortune Generator by a Sassy Goose Fortune Teller
"""

import os
import random
from datetime import datetime

# Sarcastic fortunes
FORTUNES = [
    "Congratulations! Your future is as predictable as a weather forecast in spring... which is to say, not at all.",
    "The stars say you'll achieve great things. The stars also say they're tired of you asking them for advice.",
    "A mysterious stranger will enter your life. They're probably just there to return your lost dignity.",
    "You will soon face a challenge. Spoiler alert: it's the same one you faced last week.",
    "Love is in the air. Unfortunately, so is pollution and that weird smell from the neighbor's BBQ.",
    "Your lucky numbers are 4, 8, 15, 16, 23, and 42. Good luck finding a lottery that accepts those.",
    "Success is just around the corner. Too bad you keep walking in circles.",
    "The universe has a plan for you. Unfortunately, the universe is also terrible at communication.",
    "You'll receive unexpected news today. It's probably going to be about your student loans.",
    "A friend will need your help. Remember: friends are like stars, some shine brighter when they're far away.",
    "Your career will flourish! Flourish like a weed in an abandoned parking lot.",
    "Money will come your way. It's called 'paycheck' and it arrives every two weeks.",
    "You'll discover a hidden talent. It's probably the ability to procrastinate with style.",
    "The cosmos whispers your destiny. They're whispering because they know you won't listen anyway.",
    "Today is the perfect day to start that project you've been avoiding since 2019.",
]

# Sassy goose ASCII art
GOOSE_ART = """
      __
    <(o )___
     ( ._> /
      \\___/
"""

GOOSE_ART_SASSY = """
       __
     <(o )___  "Oh, you want YOUR fortune? How ORIGINAL."
      ( ._> /  "Let me consult my crystal ball... it's just a disco ball."
       \\___/   "Your future looks... *checks notes*... mildly concerning."
"""

GOOSE_ART_EXTRA_SASSY = """
        __
      <(o )___  "Look, I'm a goose, not a LIFE COACH."
       ( ._> /  "But fine, let me squawk something profound."
        \\___/   "Your future is as clear as my vision after eating too many breadcrumbs."
"""

# Divider
DIVIDER = "=" * 60


def get_random_fortune():
    """Select a random sarcastic fortune."""
    return random.choice(FORTUNES)


def get_random_goose():
    """Select a random sassy goose art."""
    return random.choice([GOOSE_ART, GOOSE_ART_SASSY, GOOSE_ART_EXTRA_SASSY])


def generate_fortune_output():
    """Generate the complete fortune output with all decorations."""
    fortune = get_random_fortune()
    goose = get_random_goose()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build the fortune content
    fortune_text = f"""
┌────────────────────────────────────────────────────────────┐
│                    ✨ YOUR FORTUNE ✨                      │
│                                                            │
│   {fortune[:50]}{"..." if len(fortune) > 50 else ""}
│   {fortune[50:100] if len(fortune) > 50 else ""}
│                                                            │
└────────────────────────────────────────────────────────────┘
"""
    
    # Combine goose and fortune with divider
    full_content = f"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           🦢 THE SASSY GOOSE FORTUNE TELLER 🦢           ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║{goose}║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║{fortune_text}║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║           Generated on: {timestamp:<36} ║
║                                                          ║
║   "The goose giveth, and the goose takeeth away."        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""
    
    return full_content


def main():
    """Main function to generate and save the fortune."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.getcwd()
    
    fortune_file = os.path.join(current_dir, "fortune.md")
    old_dir = os.path.join(current_dir, "old")
    
    # Check if fortune.md already exists
    if os.path.exists(fortune_file):
        # Create old directory if it doesn't exist
        os.makedirs(old_dir, exist_ok=True)
        
        # Move existing file to old folder
        import shutil
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_dir, old_filename)
        shutil.move(fortune_file, old_path)
        print(f"Moved existing fortune.md to: {old_path}")
    
    # Generate the fortune
    fortune_output = generate_fortune_output()
    
    # Write to fortune.md
    with open(fortune_file, "w") as f:
        f.write(fortune_output)
    
    print(f"Fortune generated and saved to: {fortune_file}")
    print("\n" + fortune_output)


if __name__ == "__main__":
    main()
