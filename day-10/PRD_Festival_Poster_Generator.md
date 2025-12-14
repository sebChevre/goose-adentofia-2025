# Product Requirements Document (PRD)
## Festival Poster Generator

---

## 1. Overview

### 1.1 Product Name
Festival Poster Generator

### 1.2 Product Description
An automated, parameterized recipe system that generates customized HTML festival event posters based on user input. The solution eliminates manual poster creation by accepting event parameters and applying conditional styling logic to produce production-ready, themed HTML posters suitable for both digital display and print.

### 1.3 Problem Statement
Marketing coordinators spend excessive time (8+ hours) manually creating similar posters for multiple festival events using design tools like Photoshop. Each poster follows the same layout but requires manual updates for event-specific details (name, time, location, theme), resulting in inefficient, repetitive work.

### 1.4 Solution
A single, reusable recipe that accepts event parameters and uses conditional logic to automatically generate styled, themed HTML posters. Same recipe, different inputs, different results.

---

## 2. Target Users

### 2.1 Primary User
- **Role**: Festival Marketing Coordinator (e.g., Elena)
- **Pain Points**: 
  - Time-consuming manual poster creation
  - Repetitive design tasks
  - Need for consistent branding across multiple events
  - Requirement for multiple format outputs (digital/print)

### 2.2 Secondary Users
- Event organizers
- Community managers
- Small business owners running events
- Festival operations teams

---

## 3. Goals & Success Criteria

### 3.1 Business Goals
- Reduce poster creation time from 8 hours to minutes
- Enable scalable poster generation for 15+ events
- Maintain consistent branding across all festival materials
- Support reusability and flexibility

### 3.2 User Goals
- Generate professional posters quickly
- Customize posters for different event types
- Produce ready-to-share outputs
- Run generation from both CLI and Desktop environments

### 3.3 Success Metrics
- Recipe successfully uses parameters
- Conditional logic appropriately changes output based on event type
- Posters generate correctly for all event types
- Recipe runs successfully in both CLI and Desktop modes
- HTML output is production-ready (print and digital compatible)

---

## 4. Functional Requirements

### 4.1 Core Features

#### 4.1.1 Parameter System
**Required Parameters:**
- `event_name` (string): Name of the festival event
- `event_datetime` (string): Date and time of event (e.g., "December 15, 2pm–4pm")
- `location` (string): Event location or venue
- `event_type` (select): Type of event determining theme and styling
  - Options: `food`, `kids`, `performance`, `competition`, `workshop`

**Optional Parameters:**
- `tagline` (string): Optional subtitle or tagline
- `description` (string): Detailed event description
- `organizer` (string): Event organizer name
- `ticket_info` (string): Admission or ticket information
- Additional custom parameters as needed

#### 4.1.2 Conditional Styling Logic
The system must apply theme-specific styling based on `event_type`:

**Food Events:**
- Colors: Warm, inviting (burgundy, warm orange, cream, brown tones)
- Emojis: 🍴, 🍷, 🥘, ☕, 🍰
- Typography: Friendly, rounded fonts
- Background: Warm gradients or textures
- Mood: Cozy, appetizing, welcoming

**Kids Events:**
- Colors: Bright, playful (rainbow palette, pastels, vibrant primary colors)
- Emojis: 🎈, 🎨, 🎪, ⭐, 🌈, 🎉, 🧸
- Typography: Playful, bold, easy-to-read fonts
- Background: Colorful patterns or illustrations
- Mood: Fun, energetic, joyful, safe

**Performance Events:**
- Colors: Elegant, refined (deep purple, gold, black, navy, silver)
- Emojis: 🎭, 🎵, 🎼, 🎤, 🎸
- Typography: Sophisticated serif or elegant script fonts
- Background: Dramatic gradients, subtle patterns
- Mood: Classy, artistic, refined, captivating

**Competition Events:**
- Colors: Bold, energetic (red, electric blue, bright yellow, neon accents)
- Emojis: 🏆, 🥇, ⚡, 🔥, 💪, 🎯
- Typography: Strong, bold, impactful fonts
- Background: Dynamic patterns, sharp angles
- Mood: Intense, motivating, exciting, powerful

**Workshop Events:**
- Colors: Creative, instructional (teal, coral, sage green, warm gray)
- Emojis: 📚, ✏️, 💡, 🎨, 🛠️, 👩‍🎨
- Typography: Clean, modern, readable fonts
- Background: Organized, inspiring layouts
- Mood: Educational, inspiring, hands-on, creative

#### 4.1.3 Output Generation
- **Format**: Self-contained HTML file with embedded CSS
- **Responsive Design**: Optimized for both screen display and printing
- **File Naming Convention**: Descriptive, automated naming
  - Pattern: `poster_{event_type}_{event_name_normalized}.html`
  - Example: `poster_food_hot_cocoa_tasting.html`
- **Content Requirements**:
  - All required information displayed prominently
  - Optional information included only when provided
  - Appropriate emojis for visual appeal
  - Production-ready quality

#### 4.1.4 Execution Environments
- **Goose CLI**: Command-line execution support
- **Goose Desktop**: GUI execution support

---

## 5. Technical Requirements

### 5.1 Recipe Specification
- **Version**: 1.0.0
- **Template Engine**: Jinja2
- **File Format**: YAML recipe configuration

### 5.2 Recipe Structure
```yaml
version: 1.0.0
title: Festival Poster Generator
description: Generate themed HTML posters for festival events
parameters:
  - Required parameter definitions
  - Optional parameter definitions
instructions: |
  Conditional logic using Jinja2 templating
  {% if event_type == "food" %}
  # Food-specific styling
  {% elif event_type == "kids" %}
  # Kids-specific styling
  {% endif %}
```

### 5.3 Tools & Technologies
- **Text Editor Tool**: Used with `write` command to save HTML files
- **Jinja2 Templating**: For conditional logic and parameter injection
- **HTML5/CSS3**: For poster markup and styling
- **Optional Extensions**: 
  - Screenshot generation tools (e.g., shot-scraper for PNG export)
  - Batch processing capabilities

---

## 6. Use Cases

### 6.1 Primary Use Case: Single Event Poster
**Actor**: Marketing Coordinator  
**Preconditions**: Recipe is installed and accessible  
**Flow**:
1. User runs recipe with event parameters
2. System validates required parameters
3. System applies conditional styling based on event_type
4. System generates HTML poster
5. System saves file with descriptive name
6. User receives production-ready poster

**Postconditions**: HTML poster file created and ready for use

### 6.2 Batch Use Case: Multiple Events
**Actor**: Marketing Coordinator  
**Preconditions**: Recipe is installed, multiple event data available  
**Flow**:
1. User runs recipe multiple times with different parameters OR
2. User uses batch processing mode (if implemented)
3. System generates poster for each event
4. System saves all files with unique names

**Postconditions**: Multiple HTML posters created

### 6.3 Test Cases
**Test Events Provided**:

1. **Hot Cocoa Tasting**
   - Type: food
   - Date: December 15, 2pm–4pm
   - Location: Main Plaza
   - Theme: Warm and cozy

2. **Kids' Storytelling Hour**
   - Type: kids
   - Date: December 17, 3pm–4pm
   - Location: Storytelling Tent
   - Theme: Playful and fun

3. **Live Music Performance**
   - Type: performance
   - Date: December 18, 7pm–9pm
   - Location: Main Stage
   - Theme: Sophisticated

---

## 7. Design Requirements

### 7.1 Visual Design Principles
- Theme-appropriate color schemes
- Clear information hierarchy
- Emoji integration for visual interest
- Professional, polished appearance
- Print-friendly layouts
- Responsive design patterns

### 7.2 Typography
- Event type-specific font choices
- Clear readability for all audience types
- Appropriate sizing for key information
- Hierarchical text styling

### 7.3 Layout
- Prominent event name display
- Clear date/time presentation
- Visible location information
- Optional information sections (conditional)
- Consistent spacing and alignment

---

## 8. Non-Functional Requirements

### 8.1 Performance
- Instant poster generation (< 5 seconds)
- Efficient file size for HTML output
- Fast loading in browsers

### 8.2 Usability
- Simple parameter input process
- Clear error messages for missing required parameters
- Intuitive parameter naming
- Helpful parameter descriptions

### 8.3 Reliability
- Consistent output quality
- Proper handling of special characters
- Graceful handling of missing optional parameters
- Validation of required parameters

### 8.4 Maintainability
- Well-documented recipe code
- Clear conditional logic structure
- Modular styling approach
- Easy to add new event types

---

## 9. Level Up Features (Optional)

### 9.1 Enhanced Parameters
- Additional customization options
- Brand color overrides
- Custom logo support
- Font selection options

### 9.2 Batch Processing
- Multi-event input via CSV/JSON
- Bulk generation mode
- Progress tracking for large batches

### 9.3 Multi-Format Output
- PNG export support (via screenshot tools)
- PDF generation
- SVG vector output
- Social media format variants

### 9.4 Style Variants
- Multiple theme variations per event type
- Seasonal styling options
- Custom branding templates
- A/B testing variants

---

## 10. Constraints & Assumptions

### 10.1 Constraints
- Output limited to HTML format (core requirement)
- Requires Goose runtime environment
- Jinja2 templating syntax requirements
- File system access for saving outputs

### 10.2 Assumptions
- Users have basic understanding of recipe parameters
- Users can access generated HTML files
- Users have modern browsers for preview
- Users understand event type categorization

---

## 11. Acceptance Criteria

### 11.1 Must Have (MVP)
- ✅ Recipe accepts all required parameters
- ✅ Conditional logic changes output based on event_type
- ✅ All 5 event types supported with distinct styling
- ✅ HTML posters generate correctly
- ✅ Files save with descriptive names
- ✅ Works in both CLI and Desktop modes
- ✅ Production-ready output quality

### 11.2 Should Have
- Optional parameters properly handled
- Responsive design implementation
- Emoji integration
- Print optimization

### 11.3 Could Have (Future)
- Batch processing mode
- Multi-format exports
- Custom branding support
- Template variations

---

## 12. Release Plan

### 12.1 Version 1.0.0 (Initial Release)
- Core parameter system
- All 5 event type themes
- Basic HTML output
- CLI and Desktop support

### 12.2 Future Versions
- v1.1.0: Batch processing
- v1.2.0: Multi-format export
- v1.3.0: Custom branding
- v2.0.0: Template marketplace

---

## 13. Documentation Requirements

- Recipe usage guide
- Parameter reference documentation
- Example outputs for each event type
- Troubleshooting guide
- Best practices for customization

---

## 14. Support & Resources

### 14.1 Required Resources
- [Recipe Guide](https://block.github.io/goose/docs/recipes/)
- [Recipe Reference](https://block.github.io/goose/docs/recipes/reference)
- [Recipe Parameters](https://block.github.io/goose/docs/recipes/parameters)
- [Jinja2 Templating](https://jinja.palletsprojects.com/)

### 14.2 Community Resources
- Goose Community Recipes
- Discord support channel
- Video tutorials
- Example submissions

---

## 15. Submission & Validation

### 15.1 Submission Requirements
**Format Options**:
- Screenshot of structured output
- Blog post walkthrough
- Video demonstration
- Repository link

**Submission Location**: Advent of AI Discussion - Day 10

**Tagging**:
- Discord
- Twitter/X
- YouTube
- LinkedIn
- Bluesky

### 15.2 Validation Checklist
- [ ] Recipe uses parameters correctly
- [ ] Conditional logic changes output
- [ ] Posters generate for all event types
- [ ] Output is production-ready
- [ ] Works in CLI mode
- [ ] Works in Desktop mode
- [ ] Files save with correct naming
- [ ] Documentation is clear

---

**Document Version**: 1.0  
**Last Updated**: December 14, 2025  
**Author**: AI Engineering Team  
**Status**: Approved for Implementation
