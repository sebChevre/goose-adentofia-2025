# Festival Operations Skills - Tier 2 Complete ✅⭐⭐

## Overview
Multi-skill architecture breaking down the monolithic festival operations into specialized, focused skills for each department.

## Skill Structure

### 1. Customer Experience 🎭
**Path:** `~/.config/goose/skills/customer-experience/`  
**Expert:** Madame Zelda  
**Focus:** Guest relations, queue management, VIP service, personality types

**Key Features:**
- Difficult customer handling protocols
- Wait time recovery techniques
- VIP upgrade system
- Personality-based service styles
- Decision trees for customer issues

**Templates:**
- Customer feedback form
- VIP experience checklist

### 2. Security & Vendor Management 🛡️
**Path:** `~/.config/goose/skills/security-vendor-management/`  
**Expert:** Marcus  
**Focus:** Emergency response codes, vendor relations, safety protocols

**Key Features:**
- 4 Emergency codes (Yellow, Blue, White, Orange)
- Vendor setup requirements
- Noise complaint escalation
- Dispute resolution process
- Daily security checklists

**Templates:**
- Incident report template
- Vendor complaint form

### 3. Lost & Found 📦
**Path:** `~/.config/goose/skills/lost-and-found/`  
**Expert:** Maria  
**Focus:** Item tracking, fraud prevention, pattern recognition

**Key Features:**
- 4-step intake documentation
- Verification protocols
- Location pattern analysis
- 30-day hold policy
- Decision trees for claim verification

**Templates:**
- Lost item claim form

### 4. Festival Marketing 📢
**Path:** `~/.config/goose/skills/festival-marketing/`  
**Expert:** Elena  
**Focus:** Communications, emergency protocols, timeline management

**Key Features:**
- Request timeline management
- Emergency communication protocols
- Channel selection decision matrix
- Crisis communication guidelines
- Good news vs bad news strategies

**Templates:**
- Emergency communication template

## Cross-Skill References

Skills reference each other using `[See: skill-name]` notation:

- Customer issues requiring security → References security-vendor-management
- Lost children → References lost-and-found
- Emergency communications → References festival-marketing
- Vendor conflicts → May reference customer-experience for de-escalation

## Decision Trees Included

Each skill contains visual decision trees:
- **Customer Experience:** Complaint resolution, personality type selection
- **Security:** Emergency code decision, vendor dispute resolution
- **Lost & Found:** Claim verification, priority handling
- **Marketing:** Channel selection, urgency prioritization

## Testing the Skills

### Test Scenario 1: Lost Child
**Ask:** "A child is lost at the festival"  
**Expected:** Code Yellow protocol from security-vendor-management skill

### Test Scenario 2: Vendor Dispute
**Ask:** "How do I handle a vendor payment dispute?"  
**Expected:** Vendor management protocols with escalation steps

### Test Scenario 3: Weather Delay
**Ask:** "I need to announce a weather delay"  
**Expected:** Emergency communication template from festival-marketing

### Test Scenario 4: Customer Complaint
**Ask:** "A customer has been waiting 25 minutes and is upset"  
**Expected:** Wait time recovery protocol from customer-experience

### Test Scenario 5: Lost Item Claim
**Ask:** "Someone claims they lost their phone"  
**Expected:** Verification protocol from lost-and-found

## Cross-Platform Compatibility

### goose (Current Setup)
Skills located in: `~/.config/goose/skills/`
- ✅ customer-experience
- ✅ security-vendor-management
- ✅ lost-and-found
- ✅ festival-marketing

### Claude Desktop (Optional)
To make skills work in Claude Desktop, copy to: `~/.claude/skills/`

```bash
# Copy all skills to Claude Desktop
cp -r ~/.config/goose/skills/customer-experience ~/.claude/skills/
cp -r ~/.config/goose/skills/security-vendor-management ~/.claude/skills/
cp -r ~/.config/goose/skills/lost-and-found ~/.claude/skills/
cp -r ~/.config/goose/skills/festival-marketing ~/.claude/skills/
```

## File Count

**Total Skills:** 4  
**Total Templates:** 6
- incident-report-template.md
- vendor-complaint-form.md
- lost-item-claim-form.md
- emergency-communication-template.md
- customer-feedback-form.md
- vip-experience-checklist.md

**Total Checklists:** 2 (from Tier 1)
- opening.md
- closing.md

## Tier 2 Requirements Status

### Functional Requirements ✅
- [x] Split into 4 focused skills
- [x] Created templates directory with 6+ templates
- [x] Added decision trees to all skills
- [x] Skills reference each other appropriately

### Non-Functional Requirements ✅
- [x] Skills reference each other when appropriate
- [x] Decision trees are visual (ASCII/Markdown)
- [x] Templates are copy-paste ready
- [x] Skills work in goose Desktop and CLI

### Success Metrics ✅
- [x] Each skill loads independently
- [x] Skills reference each other appropriately
- [x] Templates are accessible and usable
- [x] Decision trees provide clear guidance

## What's Next?

### Tier 3: Advanced ⭐⭐⭐
- Add executable scripts for automation
- Create skill generator tool
- Build testing framework
- Implement inter-skill references

### Tier 4: Ultimate ⭐⭐⭐⭐
- Build personal "Mini Me" skill
- Capture individual expertise
- Decision-making patterns
- Personal working style

## Quick Start Guide

1. **Verify skills loaded:**
   ```
   Ask goose: "What skills do you have?"
   ```

2. **Test a scenario:**
   ```
   Ask: "A vendor is playing music too loud and neighbors are complaining. What should I do?"
   ```

3. **Access a template:**
   ```
   Ask: "Show me the incident report template"
   ```

4. **Cross-skill reference:**
   ```
   Ask: "A child is lost at the festival"
   Expected: Security skill with Lost & Found references
   ```

---

**Version:** 2.0 - Tier 2 Complete  
**Last Updated:** 2025-12-19  
**Status:** Production Ready ✅
