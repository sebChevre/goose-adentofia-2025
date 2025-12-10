# 🔍 Lost & Found Data Detective Recipe

> **Transform messy lost & found data into organized, actionable web applications**

A specialized goose recipe that brings expert lost & found management to any event, festival, conference, or venue. Built for the Advent of AI 2025 - Day 7 challenge.

## 🎯 What This Recipe Does

The Lost & Found Data Detective is an AI agent that:

- ✅ **Cleans messy data** - Handles inconsistent formats, typos, and variations
- ✅ **Merges duplicates** - Intelligently identifies and combines duplicate reports
- ✅ **Categorizes items** - Automatically organizes into logical categories
- ✅ **Flags urgent items** - Highlights electronics, IDs, jewelry that need immediate attention
- ✅ **Detects matches** - Finds potential connections between lost and found items
- ✅ **Generates web apps** - Creates beautiful, mobile-responsive HTML applications
- ✅ **Works for anyone** - No customization needed, reusable across events

## 📁 Files in This Recipe Package

```
├── lost-found-detective.yaml           # Recipe configuration file
├── lost-found-detective-prompt.md      # Complete agent prompt (expertise definition)
├── HOW-TO-USE-RECIPE.md               # Detailed usage guide
├── RECIPE-README.md                    # This file
└── example-data/
    ├── day1-opening-chaos.txt         # 20 items, simple test case
    ├── day2-peak-crowd.txt            # 35 items, complex with urgency
    └── day3-family-frenzy.txt         # 45 items, maximum complexity
```

## 🚀 Quick Start

### 1. Install the Recipe

**Option A: Using goose Desktop**
1. Open goose Desktop
2. Go to Settings → Recipes
3. Click "Import Recipe"
4. Select `lost-found-detective.yaml`

**Option B: Manual Installation**
```bash
# Copy recipe to your goose recipes directory
cp lost-found-detective.yaml ~/.config/goose/recipes/

# Copy the prompt file
cp lost-found-detective-prompt.md ~/.config/goose/recipes/
```

### 2. Run the Recipe

**Using goose Desktop:**
1. Select "lost-found-detective" from your recipes
2. Paste your data when prompted
3. Watch the magic happen!

**Using Command Line:**
```bash
goose session --recipe lost-found-detective
```

### 3. Test with Example Data

Try it with the included test datasets:

```bash
# Test with Day 1 data (20 items)
goose run lost-found-detective --data example-data/day1-opening-chaos.txt

# Test with Day 2 data (35 items, more complex)
goose run lost-found-detective --data example-data/day2-peak-crowd.txt

# Test with Day 3 data (45 items, maximum complexity)
goose run lost-found-detective --data example-data/day3-family-frenzy.txt
```

## 💡 Example Usage

### Input (Messy Data):
```
blue scarf, found near ice rink, 2pm
BLUE SCARF - ice skating area - 2:15pm
iPhone 13 pro, black case, storytelling tent, 3pm - URGENT
red mitten for kid, cocoa booth, around 2:30
Red mitten (child size), hot cocoa stand, 2:35pm
```

### Output:
1. **Console Summary:**
```
🔍 LOST & FOUND DATA DETECTIVE - ANALYSIS COMPLETE
════════════════════════════════════════════════════
📥 INPUT PROCESSING
   • Entries processed: 5
   • Duplicates identified: 2 sets (4 entries)
   • Unique items: 3

🎯 KEY FINDINGS
   • Urgent items: 1 (iPhone)
   • Potential matches: 2 pairs

📊 CATEGORY BREAKDOWN
   • Electronics: 1 item (urgent)
   • Clothing & Accessories: 2 items
```

2. **Generated Web App:** `lost-found-inventory.html`
   - Beautiful, mobile-responsive design
   - Winter festival theme
   - Search and filter functionality
   - Organized by category
   - Urgent items highlighted

## 🎨 What the Web App Looks Like

The generated web application includes:

### Summary Dashboard
```
📊 SUMMARY OF FINDINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Total Entries: 5
• Unique Items: 3 (2 duplicates merged)
• Potential Matches: 2 pairs
• Urgent Items: 1
```

### Urgent Items Section
```
🚨 URGENT ITEMS - IMMEDIATE ATTENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 iPhone 13 Pro (Black Case)
   📍 Storytelling Tent | 🕐 3:00 PM
   ⚠️ High priority - electronics
```

### Organized Inventory
- **📱 Electronics** (red highlight for urgent items)
- **👔 Clothing & Accessories** (scarves, mittens, etc.)
- **🔑 Keys & Wallets**
- **💍 Jewelry & Valuables**
- And more...

### Interactive Features
- 🔍 **Real-time search** - Filter as you type
- 🏷️ **Category filters** - Show only specific types
- ⚠️ **Urgency filters** - Focus on urgent items
- 📱 **Mobile responsive** - Works on phones and tablets
- 🖨️ **Print-friendly** - Clean layout for reports

## 🧠 How It Works

### The Recipe's Expertise

The Lost & Found Data Detective has built-in knowledge about:

1. **Duplicate Detection**
   - Recognizes that "blue scarf" = "BLUE SCARF" = "Blue Scarf"
   - Matches locations: "ice rink" = "ice skating area"
   - Groups items reported within reasonable time windows

2. **Smart Categorization**
   - Electronics (phones, tablets, cameras)
   - Clothing (scarves, coats, gloves)
   - Keys & Wallets
   - Jewelry & Valuables
   - Children's Items
   - And more...

3. **Urgency Assessment**
   - 🚨 **URGENT**: Electronics, IDs, medications, jewelry, keys
   - ⚠️ **IMPORTANT**: Bags with contents, glasses, favorite toys
   - 📋 **STANDARD**: General clothing and accessories

4. **Data Standardization**
   - Normalizes capitalization
   - Standardizes location names
   - Converts time formats
   - Cleans descriptions

## 📊 Test Data Overview

### Day 1: Opening Day Chaos (20 items)
- **Best for:** Learning the basics
- **Complexity:** Low
- **Duplicates:** 4 sets (~8 items total)
- **Urgent items:** 3
- **Use case:** First-time testing, demos

### Day 2: Peak Crowd Day (35 items)
- **Best for:** Real-world simulation
- **Complexity:** Medium-High
- **Duplicates:** 8 sets (~16 items total)
- **Urgent items:** 8
- **Use case:** Testing scalability, urgency handling

### Day 3: Family Day Frenzy (45 items)
- **Best for:** Stress testing
- **Complexity:** High
- **Duplicates:** 10 sets (~20 items total)
- **Urgent items:** 6
- **Use case:** Maximum complexity, performance testing

## 🎓 Educational Value

This recipe demonstrates key concepts:

1. **Domain Expertise in Prompts**
   - How to encode specialized knowledge
   - Creating consistent behavior
   - Making reusable agents

2. **Data Processing Pipelines**
   - Input → Clean → Categorize → Match → Output
   - Handling messy real-world data
   - Duplicate detection algorithms

3. **Full-Stack Generation**
   - HTML/CSS/JavaScript generation
   - Responsive design principles
   - User experience considerations

4. **Reusability**
   - Building once, using everywhere
   - Sharing expertise through recipes
   - Scaling solutions

## 🔧 Customization Options

### Change Output Filename
Edit the prompt to specify:
```yaml
Always save the web application as 'my-custom-name.html'
```

### Add Venue-Specific Locations
Add to the prompt:
```yaml
For this venue, the canonical location names are:
- Main Ice Rink
- Storytelling Tent
- Hot Cocoa Booth
- Children's Play Area
```

### Adjust Categories
Modify the categorization section in `lost-found-detective-prompt.md` to add/remove categories.

### Change Urgency Criteria
Edit the urgency assessment rules to match your specific needs.

## 📤 Sharing This Recipe

### Make It Your Own
1. Fork this repository
2. Customize the prompt for your use case
3. Add your own test data
4. Share with your community!

### Share on Social
Built something cool with this recipe? Share it:
- Tag: `#AdventOfAI2025 #goose #LostAndFound`
- Twitter/X: [@blocksquare](https://twitter.com/blocksquare)
- Discord: [goose Community](https://discord.gg/goose)

## 🏆 Success Stories

Use cases where this recipe shines:

- ✅ **Winter festivals** - Exactly what it was built for!
- ✅ **Summer fairs** - Works year-round
- ✅ **School events** - Track student belongings
- ✅ **Conferences** - Professional event management
- ✅ **Theme parks** - High-volume lost & found
- ✅ **Hotels** - Guest services
- ✅ **Concert venues** - Quick reunions during events

## 🐛 Troubleshooting

### Recipe doesn't merge duplicates
- Check that your data includes enough detail (item, location, time)
- Verify location names are reasonably similar
- Try increasing the duplicate detection threshold

### Web app doesn't display correctly
- Ensure the HTML file was generated completely
- Check browser console for JavaScript errors
- Try a different browser

### Search/filter not working
- Verify JavaScript was embedded in the HTML
- Check that data structure is correct
- Test in a modern browser

## 📚 Additional Resources

- [goose Documentation](https://block.github.io/goose/)
- [Recipe Guide](https://block.github.io/goose/recipes)
- [HOW-TO-USE-RECIPE.md](./HOW-TO-USE-RECIPE.md) - Detailed usage guide
- [Advent of AI 2025](https://adventofai.com) - More challenges!

## 🎁 Bonus Features to Add

Consider enhancing your recipe with:

- [ ] Multi-day comparison view
- [ ] PDF export functionality
- [ ] Email templates for reunions
- [ ] QR code generation for items
- [ ] Photo attachment support
- [ ] Multi-language support
- [ ] Statistics dashboard with charts
- [ ] Integration with notification systems

## 🤝 Contributing

Found a bug? Have an improvement? Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

MIT License - Feel free to use, modify, and share!

## 🙏 Acknowledgments

Created for **Advent of AI 2025 - Day 7 Challenge**

Built with:
- [goose](https://block.github.io/goose/) by Block
- Claude Sonnet 4 (or your preferred LLM)
- Love for solving real-world problems ❤️

---

**Remember:** This recipe is designed to work for anyone, anytime, anywhere. Build once, share with everyone! 🎉

Happy organizing! 🔍🧤
