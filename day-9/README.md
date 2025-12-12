# Gift Tag Generator 🎁✨

**Advent of AI - Day 9 Challenge**

Generate beautiful, personalized, print-ready gift tags with AI assistance. This Goose recipe creates professional-quality gift tags with multiple styles, languages, QR codes, and dynamic layouts.

## Features

✨ **4 Unique Styles**
- **Elegant**: Sophisticated serif typography with metallic accents
- **Playful**: Fun, colorful designs with whimsical elements
- **Minimalist**: Clean, modern layouts with purposeful negative space
- **Festive**: Holiday-themed with traditional seasonal colors

🌍 **Multilingual Support**
- English
- Spanish (Español)
- French (Français)

🎨 **Smart Design System**
- Adapts to recipient's favorite color
- Responsive layouts for 3 gift sizes (small, medium, large)
- AI-generated contextual poems
- Print-ready HTML with inline CSS

📱 **QR Code Integration**
- Embeds working QR codes for digital experiences
- Automatic sizing and positioning based on tag size

🎭 **Tone Variations**
- Formal
- Casual
- Humorous
- Heartfelt

## Design Inspiration

This project draws inspiration from:
- **[Jhey Tompkins](https://codepen.io/jh3y)** - Playful CSS animations and creative design
- **[Adam Argyle](https://codepen.io/argyleink)** - Modern CSS techniques and minimalist layouts

## Quick Start

### 1. Import the Recipe into Goose

1. Open the Goose Desktop application
2. Navigate to Settings → Recipes
3. Click "Import Recipe"
4. Select `gift-tag-generator.yaml`

### 2. Run the Recipe

From within Goose, use natural language to trigger the recipe:

```
Generate a gift tag for Sarah Chen, elegant style, medium size
```

Or use the recipe directly with parameters:

```
Run gift-tag-generator with:
- recipient_name: Sarah Chen
- gift_description: Handmade winter scarf
- sender_name: Festival Committee
- tag_style: elegant
- include_poem: true
- gift_size: medium
- favorite_color: navy
- language: english
- tone: heartfelt
```

### 3. Print Your Tag

1. Open the generated HTML file in your browser
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Adjust printer settings:
   - **Paper Size**: Custom or closest match to tag dimensions
   - **Margins**: None
   - **Scale**: 100%
   - **Background Graphics**: Enabled
4. Print or save as PDF

## Tag Sizes

| Size | Dimensions | Best For |
|------|------------|----------|
| **Small** | 3" × 2" (7.6cm × 5.1cm) | Small gifts, gift bags, minimal info |
| **Medium** | 4" × 3" (10.2cm × 7.6cm) | Standard gifts, balanced design |
| **Large** | 5" × 4" (12.7cm × 10.2cm) | Large gifts, elaborate designs |

## Parameter Reference

### Required Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `recipient_name` | string | Full name of gift recipient | "Sarah Chen" |
| `gift_description` | string | What the gift is | "Handmade winter scarf" |
| `sender_name` | string | Who the gift is from | "Festival Committee" |
| `tag_style` | enum | Visual style | `elegant`, `playful`, `minimalist`, `festive` |
| `gift_size` | enum | Physical tag size | `small`, `medium`, `large` |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `include_poem` | boolean | `true` | Generate contextual poem |
| `qr_message_url` | string | `null` | URL for QR code |
| `favorite_color` | string | `"blue"` | Accent color for tag |
| `language` | enum | `"english"` | Content language |
| `tone` | enum | `"heartfelt"` | Message tone |
| `output_filename` | string | Auto-generated | Custom filename |

## Example Scenarios

### Example 1: Elegant Volunteer Appreciation

```yaml
recipient_name: "Sarah Chen"
gift_description: "Handmade winter scarf with festival colors"
sender_name: "The Festival Committee"
tag_style: elegant
include_poem: true
gift_size: medium
favorite_color: "red"
language: english
tone: heartfelt
```

**Perfect for**: Thanking volunteers with a warm, professional touch

---

### Example 2: Playful Performer Gift

```yaml
recipient_name: "Marcus Rodriguez"
gift_description: "Professional wireless microphone"
sender_name: "Winter Festival Team"
tag_style: playful
include_poem: true
qr_message_url: "https://festival.example.com/thank-you-marcus"
gift_size: large
favorite_color: "purple"
language: spanish
tone: casual
```

**Perfect for**: Energetic, fun gifts with digital enhancement

---

### Example 3: Minimalist VIP Gift

```yaml
recipient_name: "Emma Thompson"
gift_description: "Artisan chocolate collection from local makers"
sender_name: "Mayor's Office"
tag_style: minimalist
include_poem: true
qr_message_url: "https://city.gov/special-message"
gift_size: small
favorite_color: "gold"
language: french
tone: formal
```

**Perfect for**: High-profile gifts requiring sophistication

---

### Example 4: Festive Family Gift

```yaml
recipient_name: "The Johnson Family"
gift_description: "Holiday cookie baking kit with recipes"
sender_name: "Your Neighbors at #42"
tag_style: festive
include_poem: true
gift_size: medium
favorite_color: "green"
language: english
tone: humorous
```

**Perfect for**: Cheerful holiday gifts with personality

## Style Guide

### Elegant 🎩

**Visual Characteristics**:
- Serif fonts (Georgia, Garamond)
- Sophisticated color palette (navy, gold, cream)
- Subtle borders and dividers
- Generous whitespace
- Centered, balanced layouts

**Best For**: Professional gifts, formal occasions, VIP recipients

---

### Playful 🎈

**Visual Characteristics**:
- Rounded sans-serif fonts
- Bright, cheerful colors
- Fun emojis and shapes
- Dynamic, asymmetric layouts
- Whimsical decorative elements

**Best For**: Children, casual celebrations, creative personalities

---

### Minimalist ⬜

**Visual Characteristics**:
- Clean sans-serif fonts (Helvetica, Arial)
- Monochromatic + single accent color
- Geometric shapes
- Precise grid alignment
- Purposeful negative space

**Best For**: Modern aesthetics, design-conscious recipients, sleek gifts

---

### Festive 🎄

**Visual Characteristics**:
- Bold, celebratory fonts
- Traditional holiday colors (red, green, gold)
- Seasonal motifs (snowflakes, stars)
- Decorative borders and patterns
- Layered, abundant layouts

**Best For**: Holiday celebrations, seasonal events, tradition-focused gifts

## Multilingual Support

### Language Options

**English**
- Natural, conversational tone
- Clear, concise messaging
- Classic greeting phrases

**Spanish (Español)**
- Culturally appropriate greetings
- Formal and informal variants
- Maintains tone across translation

**French (Français)**
- Elegant, refined language
- Proper formal/informal address
- Cultural sensitivity

### Translation Quality

All translations are contextually appropriate and culturally sensitive. Poems maintain their intended tone and meaning across languages while adapting to cultural expectations for rhythm and style.

## QR Code Integration

### When to Use QR Codes

QR codes are perfect for:
- 📹 Video messages from the sender
- 🎵 Curated playlists or songs
- 📸 Photo galleries or memories
- 📝 Extended thank-you messages
- 🎁 Gift registries or wish lists
- 🗓️ Event invitations or RSVPs
- 🌐 Personal websites or portfolios

### QR Code Best Practices

1. **Test the URL first**: Make sure it loads correctly
2. **Keep URLs short**: Long URLs create complex QR codes
3. **Use HTTPS**: More secure and professional
4. **Test before printing**: Scan the digital version first
5. **Minimum size**: 0.75" × 0.75" (2cm × 2cm) for reliability
6. **High contrast**: Dark QR on light background works best

### QR Code Size by Tag Size

- **Small tags**: 0.75" QR code in corner
- **Medium tags**: 1" QR code integrated into design
- **Large tags**: 1.25" QR code with descriptive label

## Printing Tips

### Optimal Print Settings

**Printer Configuration**:
- Color Mode: Color (if available)
- Quality: Best or High
- Paper Type: Cardstock (recommended) or Premium
- Scale: 100% (no scaling)
- Margins: None

**Recommended Materials**:
- **Paper Weight**: 80-110 lb cardstock
- **Finish**: Matte (easier to write on) or glossy (more vibrant)
- **Color**: White or cream for best color accuracy

### Print Preparation

1. **Preview First**: Always check in browser before printing
2. **Test Print**: Print one tag on regular paper first
3. **Color Calibration**: Colors may vary between screen and print
4. **Cut Carefully**: Use a paper trimmer for clean edges
5. **Finishing Touches**: Consider hole punch for ribbon/string

### Batch Printing

For multiple tags:
1. Generate all tags as separate HTML files
2. Open each in a browser tab
3. Print each individually, or
4. Combine into a single page layout (advanced)

## Troubleshooting

### Tag Looks Different When Printed

**Problem**: Colors or layout don't match the screen preview

**Solutions**:
- Enable "Background Graphics" in print settings
- Check printer color management settings
- Use "Print to PDF" first to verify before physical printing
- Ensure `-webkit-print-color-adjust: exact` is in CSS

---

### QR Code Won't Scan

**Problem**: QR code doesn't scan with phone camera

**Solutions**:
- Ensure QR code is at least 0.75" × 0.75"
- Verify the URL is correct and accessible
- Check for sufficient white space around QR code
- Increase contrast between QR and background
- Try a dedicated QR scanner app if camera doesn't work

---

### Text Is Too Small/Large

**Problem**: Font sizes don't look right when printed

**Solutions**:
- Print a test at 100% scale (no fitting to page)
- Try a different gift_size parameter
- Remember: screen DPI ≠ print DPI
- Use a ruler to measure actual printed dimensions

---

### Poem Doesn't Make Sense

**Problem**: Generated poem is awkward or doesn't fit

**Solutions**:
- Try a different tone parameter
- Provide more specific gift_description
- Set `include_poem: false` for critical applications
- Re-generate for a different variation

---

### Colors Are Too Dark/Light

**Problem**: Color scheme doesn't work well

**Solutions**:
- Try a different favorite_color
- Switch to a different tag_style
- Check printer color settings
- Use matte paper for more muted colors

## Advanced Usage

### Batch Processing (Manual)

To create multiple tags:

1. Create a spreadsheet with recipient data
2. For each row, run the recipe with those parameters
3. Save each generated tag with a unique filename
4. Organize in a folder for batch printing

### Customization Ideas

**Adding Personal Touches**:
- Hand-write a short note on the back
- Add stickers or stamps
- Use metallic markers for accents
- Attach with ribbon matching favorite_color
- Spray with subtle fragrance (optional)

**Creative Variations**:
- Create matching envelope liners
- Design coordinating wrapping paper
- Make a gift tag "collection" for one person
- Use as place cards for dinner events

### Integration Ideas

**Event Management**:
- Generate tags from event registration data
- Create seating cards with QR codes to meal preferences
- Make name badges with similar styling

**E-commerce**:
- Auto-generate tags for online orders
- Include QR codes to order tracking
- Brand consistency across packaging

## Project Structure

```
day-9/
├── gift-tag-generator.yaml    # Main Goose recipe
├── PRD.md                      # Product Requirements Document
├── README.md                   # This file
├── examples/                   # Generated example tags
│   ├── elegant_sarah.html
│   ├── playful_marcus.html
│   ├── minimalist_emma.html
│   └── festive_johnson.html
└── screenshots/                # Visual examples
    ├── elegant_preview.png
    ├── playful_preview.png
    ├── minimalist_preview.png
    └── festive_preview.png
```

## Contributing

This is an Advent of AI challenge project. Feel free to:
- Share your generated tags in the community
- Suggest new styles or features
- Report issues or improvements
- Create derivative works

## Design Attribution

This project is inspired by the creative CSS work of:

- **Jhey Tompkins** - For playful animations and creative design patterns
  - Website: https://jhey.dev
  - CodePen: https://codepen.io/jh3y
  
- **Adam Argyle** - For modern CSS techniques and clean layouts
  - Website: https://nerdy.dev
  - CodePen: https://codepen.io/argyleink

Specific inspirations are credited in HTML comments within generated tags.

## License

Created for the Advent of AI 2025 challenge by Block/Goose.

Free to use, modify, and share for personal and educational purposes.

## Support & Community

- **Advent of AI Discussions**: Share your work under Day 9
- **Discord**: #adventofai channel
- **Twitter/X**: Share with #AdventOfAI
- **Goose Documentation**: https://block.github.io/goose/

## FAQ

**Q: Can I use custom fonts?**  
A: The recipe uses system fonts for reliability. For custom fonts, you'd need to embed them as base64 or use widely available web fonts (requires internet connection).

**Q: How do I create a batch of tags from a CSV?**  
A: Currently, you need to run the recipe multiple times. A future enhancement could add CSV import functionality.

**Q: Can I customize the styles further?**  
A: Yes! The generated HTML can be manually edited. Save as a template for repeated customization.

**Q: Do QR codes work offline?**  
A: The QR codes will be generated and printed, but the URLs they point to require internet access to visit.

**Q: What if my printer doesn't support custom sizes?**  
A: Print on standard paper and cut to size, or choose the closest standard size and adjust spacing.

**Q: Can I add photos or logos?**  
A: Not directly through the recipe, but you can edit the generated HTML to add base64-encoded images.

---

## Quick Reference Card

### Essential Commands

```bash
# Basic usage
"Create an elegant gift tag for [name]"

# With all options
"Generate a playful, large gift tag for [name] with a poem, 
QR code to [url], in Spanish, casual tone, favorite color blue"

# Multiple tags
"Create 3 gift tags: one elegant for Sarah, one playful for 
Carlos, and one minimalist for Emma"
```

### Style Selection Guide

| Recipient Type | Recommended Style |
|----------------|-------------------|
| Professional/VIP | Elegant or Minimalist |
| Children/Family | Playful or Festive |
| Design-conscious | Minimalist |
| Traditional/Seasonal | Festive or Elegant |
| Creative/Artist | Playful or Minimalist |

### Size Selection Guide

| Gift Package Size | Tag Size |
|-------------------|----------|
| Small item (jewelry, etc.) | Small |
| Standard box | Medium |
| Large package | Large |
| Gift basket | Large |
| Gift bag | Small or Medium |

---

**Happy Tag Creating! 🎁✨**

*May your gifts be beautifully tagged and your recipients delighted!*
