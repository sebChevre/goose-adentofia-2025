# Skill System Architecture Documentation

## Overview

The Festival Operations skill system demonstrates a modular, scalable approach to capturing and deploying domain expertise through AI-accessible skills.

---

## Design Principles

### 1. Modularity
Each skill focuses on a single domain of expertise:
- **Single Responsibility:** One skill = one domain expert
- **Clear Boundaries:** Well-defined handoffs between skills
- **Independent Loading:** Skills work standalone or together

### 2. Actionability
Skills provide executable guidance, not just information:
- **Imperative Language:** "Do X" not "X should be done"
- **Concrete Steps:** Specific actions with clear outcomes
- **Decision Support:** Criteria for choosing between options

### 3. Discoverability
Skills are easy to find and understand:
- **Clear Naming:** Descriptive, searchable names
- **Rich Metadata:** YAML frontmatter with descriptions
- **Cross-References:** Skills link to related expertise

### 4. Extensibility
System grows without breaking existing skills:
- **Standard Format:** Consistent structure across skills
- **Loose Coupling:** Skills don't depend on implementation details
- **Version Tolerance:** Changes don't break consumers

---

## Architecture Layers

```
┌─────────────────────────────────────────┐
│         User Interface Layer            │
│  (goose Desktop, CLI, Claude Desktop)   │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│         Skill Discovery Layer           │
│    (Skills Extension, File System)      │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│         Skill Processing Layer          │
│  (Markdown Parser, YAML Frontmatter)    │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│         Knowledge Layer                 │
│   (Individual SKILL.md files)           │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│         Supporting Resources            │
│  (Templates, Scripts, Checklists)       │
└─────────────────────────────────────────┘
```

---

## Directory Structure

```
~/.config/goose/skills/              # Primary skill location
├── _skill-tools/                    # Meta-tools for skill creation
│   ├── skill-generator-guide.md     # How to create skills
│   ├── skill-testing-checklist.md   # Quality validation
│   └── architecture.md              # This file
│
├── festival-operations/             # Tier 1: Monolithic skill
│   ├── SKILL.md                     # Combined expertise
│   ├── checklists/
│   │   ├── opening.md
│   │   └── closing.md
│   └── README.md
│
├── customer-experience/             # Tier 2: Specialized skill
│   ├── SKILL.md
│   └── templates/
│       ├── customer-feedback-form.md
│       └── vip-experience-checklist.md
│
├── security-vendor-management/      # Tier 2: Specialized skill
│   ├── SKILL.md
│   ├── templates/
│   │   ├── incident-report-template.md
│   │   └── vendor-complaint-form.md
│   └── scripts/                     # Tier 3: Automation
│       ├── incident-report-generator.js
│       └── vendor-checklist-validator.js
│
├── lost-and-found/                  # Tier 2: Specialized skill
│   ├── SKILL.md
│   ├── templates/
│   │   └── lost-item-claim-form.md
│   └── scripts/                     # Tier 3: Automation
│       └── lost-item-logger.js
│
└── festival-marketing/              # Tier 2: Specialized skill
    ├── SKILL.md
    ├── templates/
    │   └── emergency-communication-template.md
    └── scripts/                     # Tier 3: Automation
        └── emergency-notifier.js
```

---

## Skill File Format

### YAML Frontmatter (Required)

```yaml
---
name: skill-identifier       # Lowercase, hyphens, unique
description: One-line summary of expertise and use cases
---
```

### Markdown Structure (Recommended)

```markdown
# Skill Title

**Expert:** [Name]
**Specialty:** [Focus Areas]

[Introduction paragraph]

## Major Section 1

### Subsection A
[Content with actionable guidance]

### Subsection B
[Decision trees, protocols, etc.]

## Major Section 2

### Common Scenarios
[Quick reference for frequent cases]

## Templates & Forms

See `templates/` directory for:
- [List of templates]

## Related Skills

- [See: related-skill-1]
- [See: related-skill-2]
```

---

## Cross-Skill Referencing

### Reference Format

Use consistent notation for cross-skill references:

```markdown
[See: skill-name]
```

### Best Practices

**DO:**
- ✅ Reference skills for related domains
- ✅ Create bidirectional references when appropriate
- ✅ Use references to avoid duplication
- ✅ Explain the handoff context

**DON'T:**
- ❌ Create circular reference loops
- ❌ Reference skills that don't exist
- ❌ Over-reference (keep skills self-contained)
- ❌ Leave vague references ("see other skills")

### Example

From **customer-experience** skill:
```markdown
### Security Issues
For safety or security concerns:
[See: security-vendor-management skill]

For lost items:
[See: lost-and-found skill]
```

From **security-vendor-management** skill:
```markdown
### Customer Service Issues
For customer de-escalation:
[See: customer-experience skill]
```

---

## Script Integration

### Script Guidelines

Scripts enhance skills with automation:

**Criteria for Creating Scripts:**
- Task is repetitive
- Consistency is critical
- Human error is likely
- Time savings are significant

**Script Requirements:**
- Executable (`chmod +x`)
- Safe (no destructive operations)
- Interactive (prompt for inputs)
- Documented (comments and help text)
- Error-handled (graceful failures)

### Example Script Structure

```javascript
#!/usr/bin/env node
// Script Purpose
// Usage: node script-name.js

const readline = require('readline');
const fs = require('fs');

// Input collection
async function collectInput() {
  // Interactive prompts
}

// Processing logic
function processData(input) {
  // Safe operations only
}

// Output generation
function generateOutput(data) {
  // Create files/reports
}

// Main execution
async function main() {
  try {
    const input = await collectInput();
    const processed = processData(input);
    generateOutput(processed);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
}

main();
```

---

## Testing Strategy

### Unit Testing (Per Skill)

Test individual skills in isolation:

1. **Discovery Test:** Skill appears in skill list
2. **Load Test:** Skill content accessible
3. **Scenario Test:** Key scenarios have clear answers
4. **Reference Test:** Cross-references resolve
5. **Format Test:** Structure is valid

### Integration Testing (Multi-Skill)

Test skills working together:

1. **Handoff Test:** References lead to correct skills
2. **Coverage Test:** No gaps between skills
3. **Conflict Test:** No contradictions between skills
4. **Performance Test:** Loading multiple skills works

### User Acceptance Testing

Real users test with real scenarios:

1. **Beginner Test:** New users can follow guidance
2. **Expert Test:** Experts validate accuracy
3. **Edge Case Test:** Unusual scenarios covered
4. **Efficiency Test:** Users save time vs. asking experts

---

## Deployment Strategy

### Skill Priority Order

Skills load in priority order:

1. `./.goose/skills/` (Highest - project-specific)
2. `./.claude/skills/` (Project, Claude compatible)
3. `~/.config/goose/skills/` (Global, goose-specific)
4. `~/.claude/skills/` (Lowest - global, Claude compatible)

### Cross-Platform Deployment

**For goose-only:**
```bash
~/.config/goose/skills/skill-name/
```

**For cross-platform (goose + Claude):**
```bash
# Primary
~/.config/goose/skills/skill-name/

# Copy to Claude
cp -r ~/.config/goose/skills/skill-name ~/.claude/skills/
```

---

## Versioning & Updates

### Skill Versioning

Track skill evolution in README or frontmatter:

```markdown
**Version:** 2.1.0
**Last Updated:** 2025-12-19
**Changelog:**
- 2.1.0 - Added emergency protocols
- 2.0.0 - Split into specialized skills
- 1.0.0 - Initial monolithic skill
```

### Update Process

1. **Identify Need:** User feedback, expert review, new requirements
2. **Plan Changes:** What sections need updates
3. **Test Updates:** Validate with scenarios
4. **Deploy:** Update files, notify users
5. **Monitor:** Watch for issues

---

## Performance Considerations

### Skill Size

**Optimal Skill Size:**
- 200-500 lines of markdown
- 5-10 major sections
- 10-20 scenarios covered

**Too Large (>1000 lines):**
- Consider splitting into multiple skills
- Create focused sub-skills
- Use more cross-references

**Too Small (<100 lines):**
- Might be too narrow
- Consider merging with related skill
- Ensure sufficient value

### Loading Performance

- Skills load on-demand
- First reference triggers load
- Cached after initial load
- Minimize heavy processing in skills

---

## Security Considerations

### Script Safety

**Scripts MUST:**
- ✅ Validate all inputs
- ✅ Use safe file operations
- ✅ Avoid destructive commands
- ✅ Handle errors gracefully
- ✅ Document all actions

**Scripts MUST NOT:**
- ❌ Execute arbitrary code
- ❌ Modify system files
- ❌ Access sensitive data
- ❌ Make network calls (except mocks)
- ❌ Run as privileged user

---

## Future Enhancements

### Planned Features

1. **Skill Analytics:** Track which skills are most used
2. **A/B Testing:** Compare skill variations
3. **Auto-Updates:** Pull latest versions from repository
4. **Skill Marketplace:** Share with community
5. **Visual Editor:** GUI for skill creation

---

## Best Practices Summary

### Creating Skills
- Start with expert interview
- Focus on common scenarios
- Make guidance actionable
- Include decision trees
- Provide templates

### Organizing Skills
- One expert = one skill
- Clear domain boundaries
- Logical section structure
- Cross-reference related skills
- Version your skills

### Maintaining Skills
- Regular expert review
- User feedback integration
- Test with real scenarios
- Update documentation
- Archive deprecated content

---

**Version:** 1.0  
**Last Updated:** 2025-12-19  
**Status:** Living Document
