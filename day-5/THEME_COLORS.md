# Theme Color Reference

## Color Palette Comparison

### 🌞 Light Mode - Winter Day
```css
/* Backgrounds - Whitish with blue tints */
--background: oklch(0.98 0.01 240)      /* Very light blue-white */
--card: oklch(1 0.005 240)               /* Pure white with hint of blue */
--secondary: oklch(0.94 0.01 240)        /* Light gray-blue */

/* Text Colors */
--foreground: oklch(0.15 0.02 240)       /* Very dark blue-black */
--muted-foreground: oklch(0.48 0.01 240) /* Medium gray-blue */

/* Primary & Accent */
--primary: oklch(0.52 0.14 240)          /* Ice Blue ❄️ */
--accent: oklch(0.55 0.14 300)           /* Soft Purple 💜 */

/* Borders */
--border: oklch(0.88 0.02 240)           /* Light blue-gray border */
```

**Visual Feel**: Clean, bright, crisp winter day with blue sky

---

### 🌙 Dark Mode - Winter Night
```css
/* Backgrounds - Deep blue/purple night */
--background: oklch(0.12 0.02 260)       /* Deep midnight blue */
--card: oklch(0.18 0.02 260)             /* Slightly lighter blue */
--secondary: oklch(0.24 0.02 260)        /* Medium dark blue */

/* Text Colors */
--foreground: oklch(0.95 0.01 240)       /* Bright white */
--muted-foreground: oklch(0.65 0.01 240) /* Light gray */

/* Primary & Accent */
--primary: oklch(0.72 0.14 240)          /* Bright Ice Blue ✨ */
--accent: oklch(0.68 0.16 300)           /* Bright Purple 🌟 */

/* Borders */
--border: oklch(0.72 0.14 240 / 20%)     /* Subtle glowing blue */
```

**Visual Feel**: Enchanted winter night with glowing lights

---

## Color Psychology & Theme

### Inspiration from Day 4
The color scheme is inspired by the Winter Festival website which featured:
- ❄️ **Ice Blue**: Main winter theme color
- 💜 **Purple**: Magical, mystical accent
- 🌨️ **White/Blue backgrounds**: Clean snow and ice
- 🌌 **Deep Blues**: Winter night sky

### Applied to Homecoming Board
We adapted these colors for a flight tracking interface:
- Ice blue works perfectly for flight-related UI
- Purple adds a premium, tech-forward feel
- High contrast ensures readability of flight data
- Subtle blue tints create cohesive winter aesthetic

---

## Chart Colors (Both Themes)

### Light Mode Charts
```css
--chart-1: oklch(0.52 0.14 240)  /* Ice Blue */
--chart-2: oklch(0.55 0.14 300)  /* Soft Purple */
--chart-3: oklch(0.6 0.12 200)   /* Cyan */
--chart-4: oklch(0.7 0.15 330)   /* Pink-Purple */
--chart-5: oklch(0.48 0.13 260)  /* Deep Blue */
```

### Dark Mode Charts
```css
--chart-1: oklch(0.72 0.14 240)  /* Bright Ice Blue */
--chart-2: oklch(0.68 0.16 300)  /* Bright Purple */
--chart-3: oklch(0.7 0.15 200)   /* Bright Cyan */
--chart-4: oklch(0.75 0.16 330)  /* Bright Pink */
--chart-5: oklch(0.65 0.15 260)  /* Medium Blue */
```

---

## OKLCH Color Space Benefits

We use OKLCH instead of RGB/HSL because:
- **Perceptually uniform**: Equal changes look equal to human eye
- **Better interpolation**: Smooth gradients and transitions
- **Consistent lightness**: Light/dark modes stay readable
- **Wide gamut**: More vibrant colors possible
- **Modern**: Better than older color spaces

Example: `oklch(L C H / A)`
- **L** = Lightness (0-1)
- **C** = Chroma/saturation
- **H** = Hue angle (degrees)
- **A** = Alpha/transparency (optional)

---

## Semantic Color Usage

| Use Case | Light Mode | Dark Mode |
|----------|------------|-----------|
| Page background | Whitish blue | Deep blue |
| Text | Dark blue-gray | White |
| Links/Primary actions | Ice blue | Bright ice blue |
| Accent/Secondary | Soft purple | Bright purple |
| Success indicators | Green | Green |
| Error indicators | Red | Red |
| Warning indicators | Yellow | Yellow |
| Card backgrounds | White | Dark blue |
| Borders | Light gray-blue | Translucent blue |

---

## Accessibility Notes

✅ **WCAG AA Compliant**: All text meets minimum contrast ratios
✅ **Color Independence**: Information not conveyed by color alone
✅ **High Contrast**: Dark mode has excellent contrast
✅ **Readable**: Blue tints enhance rather than hinder readability
