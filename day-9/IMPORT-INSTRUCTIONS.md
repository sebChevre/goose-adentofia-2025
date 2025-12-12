# 🎁 Import Instructions for Goose UI

## Quick Start: Import Your Recipe in 3 Steps

### Step 1: Locate the Recipe File
You need this file:
```
📄 gift-tag-generator.yaml (15 KB)
```

**Full Path:**
```
/Users/nicktaylor/dev/advent-of-ai-2025/day-9/gift-tag-generator.yaml
```

---

### Step 2: Import into Goose Desktop

#### Option A: Via Goose UI (Recommended)
1. **Open Goose Desktop Application**
2. **Click the Menu** (top-right, three horizontal lines or dots)
3. **Navigate to:** Settings → Recipes
4. **Click "Import Recipe"** or "Add Recipe"
5. **Browse to:** `/Users/nicktaylor/dev/advent-of-ai-2025/day-9/`
6. **Select:** `gift-tag-generator.yaml`
7. **Click "Import"** or "Open"

#### Option B: Via File System (Alternative)
1. **Copy the recipe file** to Goose's recipe directory
2. **Goose Recipe Directory** is typically at:
   - macOS: `~/Library/Application Support/Goose/recipes/`
   - Or check Goose settings for the exact path
3. **Restart Goose** if needed to detect the new recipe

---

### Step 3: Verify Import

After importing, you should see:
- ✅ Recipe appears in your recipe list
- ✅ Recipe name: "Gift Tag Generator"
- ✅ Version: 1.0.0
- ✅ 9 parameters visible when you view the recipe details

---

## Test Your Recipe

### Test 1: Simple Generation
In Goose chat, try:
```
Create an elegant gift tag for Sarah Chen with a handmade scarf, 
medium size, heartfelt tone
```

### Test 2: Full Parameters
```
Generate a gift tag with these details:
- Recipient: Marcus Rodriguez
- Gift: Professional microphone
- From: Winter Festival Team
- Style: playful
- Size: large
- Include poem: yes
- QR URL: https://festival.example.com/thank-you-marcus
- Language: Spanish
- Tone: casual
- Favorite color: purple
```

### Test 3: Minimalist Small Tag
```
Make a minimalist gift tag:
- For: Emma Thompson
- Gift: Artisan chocolate collection
- From: Mayor's Office
- Size: small
- Style: minimalist
- No poem
- Language: French
- Tone: formal
- Favorite color: gold
```

---

## Expected Output

After running the recipe, Goose will:
1. ✅ Generate a complete HTML file
2. ✅ Save it to your current directory
3. ✅ Provide the filename and path
4. ✅ Offer a description of the design

**Example Output Filename:**
```
tag_sarah_chen_20251211_230342.html
```

---

## Opening and Printing Your Tag

### View in Browser
```bash
# macOS - open in default browser
open tag_sarah_chen_20251211_230342.html

# Or double-click the file in Finder
```

### Print
1. **Open the HTML file** in any web browser
2. **Press Cmd+P** (Mac) or **Ctrl+P** (Windows/Linux)
3. **Print Settings:**
   - Paper Size: Custom or closest match
   - Margins: None
   - Scale: 100%
   - Background Graphics: ON ✓
4. **Print** or **Save as PDF**

---

## Troubleshooting Import

### Recipe Doesn't Appear
- ✅ Check file extension is `.yaml` (not `.txt` or `.yml`)
- ✅ Verify file isn't corrupted (should be 15 KB)
- ✅ Restart Goose application
- ✅ Check Goose logs for import errors

### Import Fails with Error
- ✅ Ensure YAML syntax is valid
- ✅ Check for special characters in file path
- ✅ Try copying recipe to Desktop and import from there
- ✅ Verify Goose version is up to date

### Recipe Parameters Don't Show
- ✅ View the recipe details/edit screen
- ✅ Parameters may be collapsible - expand the section
- ✅ Check recipe format matches Goose's expected schema

---

## Recipe Parameters Quick Reference

When running the recipe, you can specify:

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| recipient_name | text | ✅ Yes | "Sarah Chen" |
| gift_description | text | ✅ Yes | "Handmade scarf" |
| sender_name | text | ✅ Yes | "Festival Committee" |
| tag_style | choice | ✅ Yes | elegant / playful / minimalist / festive |
| gift_size | choice | ✅ Yes | small / medium / large |
| include_poem | yes/no | No (default: yes) | true / false |
| qr_message_url | text | No | "https://example.com/message" |
| favorite_color | text | No (default: blue) | "navy", "red", "gold" |
| language | choice | No (default: english) | english / spanish / french |
| tone | choice | No (default: heartfelt) | formal / casual / humorous / heartfelt |

---

## Natural Language Examples

Goose understands natural language! Try these:

### Minimal Input
```
Make a gift tag for John
```
*(Goose will ask for missing required details)*

### Casual Description
```
I need a playful gift tag for my niece Emma, 
it's a stuffed unicorn from Aunt Sarah
```

### Detailed Specification
```
Create a festive large gift tag for the Johnson family,
gift is a holiday cookie baking kit,
from the neighbors at #42,
make it humorous and fun,
their favorite color is green
```

### With QR Code
```
Generate an elegant tag for Dr. Sarah Chen,
professional stethoscope from the medical board,
include a QR code linking to https://medboard.org/tribute/sarah,
formal tone, navy blue color
```

---

## Getting Help

### Documentation
- **README.md** - Complete user guide (14 KB)
- **PRD.md** - Full technical specifications (16 KB)
- **SUMMARY.md** - Project overview (15 KB)

### Support Channels
- **Goose Documentation:** https://block.github.io/goose/
- **Advent of AI Discord:** #adventofai channel
- **GitHub Discussions:** Advent of AI Day 9 thread

### Common Questions

**Q: Can I edit the generated HTML?**  
A: Yes! The HTML files are yours to customize.

**Q: How do I create multiple tags at once?**  
A: Run the recipe multiple times, or use batch processing (see README.md Advanced Usage).

**Q: Do I need internet to use the recipe?**  
A: Yes, for AI generation and QR code APIs. Once generated, tags work offline.

**Q: Can I add my own styles?**  
A: The four styles are built-in. For custom styles, edit the YAML or modify generated HTML.

**Q: What if the tag doesn't fit my printer?**  
A: Choose the closest paper size or print at 100% and trim to size.

---

## Next Steps After Import

1. ✅ **Test with one tag** - Verify everything works
2. 📸 **Print a test** - Check colors and sizing
3. 🎨 **Try all 4 styles** - See what you like best
4. 🌍 **Test languages** - Generate multilingual samples
5. 📱 **Test QR codes** - Ensure they scan properly
6. 🎁 **Generate real tags** - For your actual event/gifts
7. 📤 **Share results** - Post in Advent of AI community!

---

## Success Checklist

After importing and testing, you should have:

- ✅ Recipe imported into Goose
- ✅ Generated at least one test tag
- ✅ HTML file opens in browser
- ✅ Tag prints correctly (or saved as PDF)
- ✅ Design looks professional
- ✅ (If used) QR code scans successfully

---

## Share Your Work! 📤

When you've created amazing tags, share them:

### Required for Challenge
- Post in **Advent of AI Discussions** under Day 9
- Include:
  - Your `gift-tag-generator.yaml` file
  - Screenshots of at least 3 tag styles
  - Example showing QR code integration

### Optional but Awesome
- Side-by-side comparison of all 4 styles
- Batch of printed tags
- Video showing the recipe in action
- Multi-language examples
- Your most creative poem
- Print "sheet" with multiple tags

### Social Media
- **Discord:** #adventofai
- **Twitter/X:** #AdventOfAI
- **LinkedIn:** Share your AI development skills
- **Bluesky:** Tag @adventofai

---

**You're Ready to Create Beautiful Gift Tags! 🎁✨**

Happy tagging!
