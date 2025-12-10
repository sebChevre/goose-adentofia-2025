# How to Use the Lost & Found Data Detective Recipe

## Quick Start Guide

### Step 1: Create the Recipe File

In goose Desktop, you'll create a recipe file that uses the prompt. Here's how:

1. **Create a new file called `lost-found-detective.yaml`** in your goose recipes directory

2. **Structure your recipe file:**

```yaml
name: lost-found-detective
description: Transform messy lost & found data into organized, actionable web applications

prompt: |
  [PASTE THE ENTIRE CONTENT FROM lost-found-detective-prompt.md HERE]

kickoff_message: |
  🔍 Lost & Found Data Detective activated!
  
  I'm ready to transform your messy lost & found data into a beautiful, organized web application.
  
  Please provide your lost & found data in any format:
  - Paste messy notes directly
  - Upload a CSV file
  - Share a text file path
  - Provide structured data
  
  I'll handle:
  ✅ Cleaning and standardizing entries
  ✅ Identifying and merging duplicates
  ✅ Categorizing items
  ✅ Flagging urgent items
  ✅ Detecting potential matches
  ✅ Generating a complete web application
  
  What data should I process?

# Optional: Specify which extensions this recipe can use
extensions:
  - developer  # For file operations and shell commands
  - autovisualiser  # Could be used for data visualization if needed

# Optional: Customize settings
settings:
  model: claude-sonnet-4  # Or your preferred model
  temperature: 0.7
```

### Step 2: Use the Recipe

#### Option A: Through goose Desktop UI
1. Open goose Desktop
2. Go to Recipes section
3. Select "lost-found-detective"
4. Paste your data when prompted
5. Let the recipe work its magic!

#### Option B: Through Command Line
```bash
goose run lost-found-detective --data "path/to/your/data.txt"
```

#### Option C: Interactive Mode
```bash
goose session --recipe lost-found-detective
```
Then paste your data when prompted.

### Step 3: Provide Your Data

The recipe accepts data in multiple formats:

**Format 1: Simple Text (Messy Notes)**
```
blue scarf, ice rink, 2pm
iPhone 13, black case, storytelling tent, 3pm - URGENT!
red mitten (child size), cocoa booth, 2:30pm
BLUE SCARF - ice skating area - 2:15
```

**Format 2: CSV**
```csv
item,location,time,notes
Blue scarf,Ice rink,2:00 PM,
iPhone 13 Pro,Storytelling tent,3:00 PM,URGENT - black case
Red mitten,Cocoa booth,2:30 PM,Child size
```

**Format 3: JSON**
```json
[
  {
    "item": "Blue scarf",
    "location": "Ice rink",
    "time": "2:00 PM"
  },
  {
    "item": "iPhone 13 Pro",
    "location": "Storytelling tent",
    "time": "3:00 PM",
    "urgent": true
  }
]
```

**Format 4: Point to a File**
```
Process the data in ./festival-day1-lost-items.txt
```

### Step 4: Review the Output

The recipe will:

1. **Show you a summary in the console:**
   - How many entries were processed
   - How many duplicates were found
   - How many urgent items detected
   - How many categories created

2. **Generate a web application file:**
   - Usually named `lost-found-inventory.html`
   - Complete, standalone file
   - Ready to open in any browser

3. **Provide next steps:**
   - How to open the app
   - What to do with urgent items
   - How to use the search/filter features

### Step 5: Use the Web App

1. **Open the generated HTML file** in any web browser
2. **Review the summary dashboard** at the top
3. **Check urgent items** immediately
4. **Explore matched pairs** for quick reunions
5. **Use search/filter** to find specific items
6. **Share with your team** - just send them the HTML file!

## Example Usage Scenarios

### Scenario 1: Single Event, Single Day
```
User: "Process the lost items from today's festival"
[Paste data]
Recipe: Generates lost-found-inventory.html with clean, organized data
```

### Scenario 2: Multiple Days Combined
```
User: "Process data from all three festival days"
[Provide three separate datasets]
Recipe: Creates comprehensive inventory with trends across days
```

### Scenario 3: Quick Update During Event
```
User: "We just found 5 more items, update the inventory"
[Provide new items]
Recipe: Regenerates the web app with all items included
```

## Testing Your Recipe

### Test Data Sets

**Test Set 1: Basic (10 items, 2 duplicates)**
```
blue scarf, ice rink, 2pm
Blue Scarf, ice skating area, 2:15pm
iPhone 12, food court, 3pm
red mittens, kids area, 1:30pm
car keys (Toyota), parking lot, 4pm
black wallet, main entrance, 2:45pm
eyeglasses (reading), storytelling tent, 3:30pm
green winter coat, coat check, 5pm
stuffed bear, kids zone, 1pm
water bottle (blue), vendor area, 2:20pm
```

**Test Set 2: Complex (20+ items, multiple duplicates, urgency)**
```
iPhone 13 Pro, black case, storytelling tent, 3pm - URGENT!!!
blue scarf, found near ice rink, 2pm
BLUE SCARF - ice skating area - 2:15pm
red mitten for kid, cocoa booth, around 2:30
Red mitten (child size), hot cocoa stand, 2:35pm
gold wedding ring, storytelling tent, 3:15pm - URGENT
car keys - Toyota, parking area, 4pm
Toyota car keys, lot B, 4:10pm
black leather wallet, entrance, 2:45pm
prescription glasses, food court, 3:30pm
green puffy jacket, coat check, 5pm
teddy bear (brown), children's area, 1pm
BROWN TEDDY BEAR, kids zone, 1:15pm
blue water bottle, vendor booth 3, 2:20pm
airpods (white case), main stage, 4:30pm - urgent
silver watch, bathroom area, 3:45pm
red and white striped scarf, ice rink, 2:05pm
house keys (3 keys on ring), parking lot, 4:15pm
purple backpack, storytelling tent, 3:00pm
pink hat (knitted), kids area, 1:45pm
```

### Expected Outcomes

After processing Test Set 2, you should see:
- **Total entries**: 20
- **Unique items**: ~15 (after deduplication)
- **Duplicates merged**: ~5 sets
- **Urgent items**: 4-5 (iPhone, ring, AirPods, wallet)
- **Potential matches**: Multiple (blue scarves, red mittens, keys, teddy bears)
- **Categories**: Electronics, Clothing, Keys & Wallets, Jewelry, etc.

## Customizing the Recipe

### Change the Output Filename
Add to the prompt:
```yaml
prompt: |
  [existing prompt]
  
  Always save the web application as 'festival-inventory-[DATE].html'
```

### Add Specific Location Names
Add to the prompt:
```yaml
prompt: |
  [existing prompt]
  
  For this venue, the canonical location names are:
  - Main Ice Rink
  - Storytelling Tent
  - Hot Cocoa Booth
  - Children's Play Area
  - Parking Lot B
  - Main Entrance
```

### Adjust Urgency Criteria
Modify the urgency section in the prompt to match your needs.

## Sharing Your Recipe

### Make It Public
1. Save your recipe to a GitHub repository
2. Add documentation (README.md)
3. Include example data sets
4. Share the repository link

### Share Locally
1. Export the recipe file
2. Send to colleagues
3. They import into their goose Desktop
4. Ready to use immediately!

### Create a Recipe Package
```
lost-found-detective/
  ├── recipe.yaml              # The recipe file
  ├── README.md                # Documentation
  ├── examples/
  │   ├── day1-data.txt       # Example dataset 1
  │   ├── day2-data.txt       # Example dataset 2
  │   └── day3-data.txt       # Example dataset 3
  └── screenshots/
      ├── summary.png          # Screenshot of generated app
      └── filters.png          # Screenshot of filters in action
```

## Troubleshooting

### Recipe doesn't detect duplicates properly
- Check that location names are standardized
- Verify time formats are consistent
- Review the duplicate detection threshold in the prompt

### Web app doesn't render correctly
- Check that HTML was generated completely
- Verify no special characters broke the HTML
- Try opening in a different browser

### Search/filter not working
- Ensure JavaScript was embedded properly
- Check browser console for errors
- Verify data structure in the HTML

### Too many/too few categories
- Adjust the categorization rules in the prompt
- Add or remove category definitions
- Modify the "Other" category threshold

## Tips for Success

1. **Start Simple**: Test with small datasets first
2. **Iterate**: Refine the prompt based on results
3. **Document**: Add examples of what works well
4. **Share**: Let others benefit from your recipe
5. **Maintain**: Update the recipe as you learn what works best

## Advanced Features to Add

Consider enhancing your recipe with:
- **Multi-language support**: Handle items in different languages
- **Photo attachments**: Include image URLs in the inventory
- **Export functionality**: Add PDF or CSV export buttons
- **Email templates**: Generate ready-to-send reunion emails
- **Statistics dashboard**: Add charts showing trends over time
- **QR codes**: Generate QR codes for quick item lookup
- **Print-optimized view**: Special CSS for printing end-of-day reports

## Resources

- [goose Recipe Documentation](https://block.github.io/goose/recipes)
- [Recipe Examples](https://github.com/block/goose/tree/main/recipes)
- [goose Desktop Guide](https://block.github.io/goose/desktop)
- [Community Recipes](https://block.github.io/goose/v1/extensions/)

---

**Remember**: The power of recipes is reusability. Build once, use forever, share with everyone! 🎉
