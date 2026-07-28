#!/usr/bin/env python3
"""
Fortune Generator - A poetic fortune teller with a sassy goose
"""

import os
import random
from datetime import datetime

# Sassy Goose ASCII Art
GOOSE_ART = """
     __
    /  \\
   |    |
   |    |
   \\    /
    \\  /
     \\/
   _/\\_
  (o.o)
   >^<
  /| |\\
 (_| |_)
"""

# Poetic fortunes
FORTUNES = [
    "The winds of change whisper your name,\n    A new adventure calls, not in vain.",
    "Like clouds that drift across the sky,\n    Your dreams shall soar, reach ever high.",
    "A secret path awaits your feet,\n    Where fortune and joy and love will meet.",
    "The stars align in patterns bright,\n    Guiding you through darkest night.",
    "Like morning dew on petals new,\n    Fresh opportunities await for you.",
    "The river flows, the willow sways,\n    Your path unfolds in mysterious ways.",
    "A treasure hidden, not of gold,\n    But stories waiting to be told.",
    "The moon reflects what hearts desire,\n    Your wishes burn like sacred fire.",
    "As autumn leaves dance in the breeze,\n    You'll find what sets your spirit free.",
    "The ocean deep holds secrets vast,\n    Your future bright, both near and vast.",
]

# Divider between goose and fortune
DIVIDER = "=" * 40

# Border character
BORDER_CHAR = "#"

def generate_fortune():
    """Generate a random fortune with the sassy goose."""
    fortune = random.choice(FORTUNES)
    return fortune

def create_formatted_output():
    """Create the visually appealing fortune output with ASCII art."""
    fortune = generate_fortune()
    
    # Build the content
    lines = []
    
    # Top border
    border_line = BORDER_CHAR * 44
    lines.append(border_line)
    
    # Header
    header = "# 🦢 MYSTIC FORTUNE TELLER 🦢 #"
    lines.append(f"{BORDER_CHAR}{header:^42}{BORDER_CHAR}")
    
    # Date line
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"{BORDER_CHAR}{date_str:^42}{BORDER_CHAR}")
    
    lines.append(border_line)
    
    # Goose art section
    goose_lines = GOOSE_ART.strip().split('\n')
    for goose_line in goose_lines:
        # Center the goose art within the border
        padded_line = goose_line.center(42)
        lines.append(f"{BORDER_CHAR} {padded_line} {BORDER_CHAR}")
    
    lines.append(border_line)
    
    # Divider section
    lines.append(f"{BORDER_CHAR}{DIVIDER:^42}{BORDER_CHAR}")
    
    # Fortune section
    lines.append(f"{BORDER_CHAR}{'✨ YOUR FORTUNE ✨':^42}{BORDER_CHAR}")
    lines.append(f"{BORDER_CHAR}{DIVIDER:^42}{BORDER_CHAR}")
    
    # Add fortune lines
    fortune_lines = fortune.split('\n')
    for f_line in fortune_lines:
        lines.append(f"{BORDER_CHAR} {f_line:^40} {BORDER_CHAR}")
    
    lines.append(f"{BORDER_CHAR}{DIVIDER:^42}{BORDER_CHAR}")
    
    # Footer
    lines.append(f"{BORDER_CHAR}{'May the cosmos guide you 🌟':^42}{BORDER_CHAR}")
    lines.append(border_line)
    
    return '\n'.join(lines)

def main():
    """Main function to generate and save the fortune."""
    # Generate the formatted fortune
    fortune_output = create_formatted_output()
    
    # Output file path (current directory)
    output_file = "fortune.md"
    
    # Check if file exists and move to old folder
    if os.path.exists(output_file):
        old_folder = "old"
        if not os.path.exists(old_folder):
            os.makedirs(old_folder)
        
        # Generate a unique name for the old file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_filename = f"fortune_{timestamp}.md"
        old_path = os.path.join(old_folder, old_filename)
        
        # Move the existing file
        os.rename(output_file, old_path)
        print(f"Existing fortune moved to: {old_path}")
    
    # Write the new fortune to markdown file
    with open(output_file, 'w') as f:
        f.write(f"# 🦢 Daily Fortune 🦢\n\n")
        f.write("```\n")
        f.write(fortune_output)
        f.write("\n```\n")
    
    print(f"Fortune generated and saved to: {output_file}")
    print("\n" + fortune_output)

if __name__ == "__main__":
    main()
