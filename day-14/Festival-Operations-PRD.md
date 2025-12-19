# Product Requirements Document: Festival Operations Manual Skill System

**Project:** Day 14 - The Festival Operations Manual  
**Version:** 1.0  
**Date:** 2025-12-19  
**Status:** Draft

---

## Executive Summary

The Winter Festival's success has attracted interest from three neighboring towns. To scale this success, we need to capture operational expertise in a portable, actionable format using goose Skills - a system that makes domain knowledge accessible to any festival coordinator through AI assistance.

## Problem Statement

Currently, critical operational knowledge is trapped in team members' heads:
- Madame Zelda's customer experience expertise
- Marcus's security protocols and vendor management
- Maria's lost & found system
- Elena's marketing and communications workflows

This knowledge must be:
1. **Portable** - Transferable to other festival coordinators
2. **Actionable** - Provides clear guidance, not just information
3. **Accessible** - Available in-the-moment when decisions are needed
4. **Shareable** - Works across teams, projects, and tools

## Solution Overview

Create a Festival Operations Skill that:
- Lives as a markdown file with YAML frontmatter
- Gets automatically discovered and loaded by goose
- Provides expert guidance for common festival scenarios
- Includes supporting files (checklists, templates)
- Is compatible with both goose and Claude Desktop

---

## Implementation Plan: Progressive Difficulty Levels

We'll tackle this in sequential order, with each level building on the previous:

---

## Level 1: Beginner ⭐ - Core Skill Creation

### Objectives
- Create basic skill structure
- Capture foundational expertise from all 4 team members
- Ensure skill is discoverable and usable
- Add enhanced formatting and quick-reference materials

### User Stories
**As a** festival coordinator  
**I want** goose to know how to handle common operational scenarios  
**So that** I can get expert guidance without consulting multiple team members

**As a** goose user  
**I want** the skill to be easy to read and navigate  
**So that** I can quickly find relevant information

### Requirements

#### Functional Requirements
- [ ] Create skill directory at `~/.config/goose/skills/festival-operations/`
- [ ] Create `SKILL.md` with proper YAML frontmatter:
  - name: festival-operations
  - description: Expert knowledge for running winter festival operations
- [ ] Include 4+ sections covering:
  - Customer Experience (Zelda's expertise)
  - Security & Vendor Relations (Marcus's expertise)
  - Lost & Found Operations (Maria's expertise)
  - Marketing & Communications (Elena's expertise)
- [ ] Add 2+ supporting files:
  - Opening checklist
  - Closing checklist
  - OR incident report template
  - OR communication templates

#### Non-Functional Requirements
- Skill must be discoverable (appears in "what skills do you have?")
- Skill must be loadable (goose can access when needed)
- Content must be actionable (tells users what to DO)
- Formatting must be scannable (headers, bullets, emoji)

### Acceptance Criteria
**Test Question:** "A vendor is playing music too loud and neighboring vendors are complaining. What should I do?"

**Expected Response:** goose should cite the specific protocol:
1. First warning: Verbal
2. Second warning: Written
3. Third incident: Shutdown

### Deliverables
1. `~/.config/goose/skills/festival-operations/SKILL.md`
2. `~/.config/goose/skills/festival-operations/checklists/opening.md`
3. `~/.config/goose/skills/festival-operations/checklists/closing.md`
4. Verification that skill loads in goose Desktop

### Success Metrics
- ✅ Skill appears in skill list
- ✅ goose correctly answers vendor noise complaint scenario
- ✅ goose correctly answers at least 3 other scenario questions
- ✅ Supporting files are referenced appropriately

---

## Level 2: Intermediate ⭐⭐ - Multi-Skill Architecture

### Objectives
- Break monolithic skill into department-specific skills
- Add comprehensive templates
- Create decision trees for complex scenarios
- Ensure cross-platform compatibility (goose + Claude Desktop)

### User Stories
**As a** department coordinator  
**I want** specialized skills for my specific area  
**So that** I get focused expertise without information overload

**As a** festival director  
**I want** skills to work in both goose and Claude Desktop  
**So that** my team can use whichever tool they prefer

### Requirements

#### Functional Requirements
- [ ] Split festival-operations into 4 focused skills:
  - `customer-experience` (Zelda's domain)
  - `security-vendor-management` (Marcus's domain)
  - `lost-and-found` (Maria's domain)
  - `festival-marketing` (Elena's domain)
- [ ] Create `templates/` directory with:
  - Incident report template
  - Vendor complaint form
  - Lost item claim form
  - Emergency communication template
- [ ] Add decision trees for:
  - Security code scenarios
  - Vendor dispute escalation
  - Lost item priority handling
  - Communication channel selection
- [ ] Test skills in both:
  - goose Desktop
  - goose CLI
  - Claude Desktop (using `~/.claude/skills/`)

#### Non-Functional Requirements
- Skills must reference each other when appropriate
- Decision trees must be visual (ASCII art or Markdown tables)
- Templates must be copy-paste ready
- Skills must work identically across platforms

### Acceptance Criteria
**Test Scenarios:**
1. "A child is lost at the festival" → Should trigger Code Yellow protocol
2. "How do I handle a vendor payment dispute?" → Should load appropriate skill
3. "I need to announce a weather delay" → Should reference communication template

### Deliverables
1. Four separate skill directories with SKILL.md files
2. Templates directory with 4+ templates
3. Decision tree diagrams in skills
4. Cross-platform compatibility verification doc

### Success Metrics
- ✅ Each skill loads independently
- ✅ Skills reference each other appropriately
- ✅ Templates are accessible and usable
- ✅ Works in goose Desktop, CLI, and Claude Desktop
- ✅ Decision trees provide clear guidance

---

## Level 3: Advanced ⭐⭐⭐ - Intelligent Skill System

### Objectives
- Create inter-skill reference system
- Add executable scripts goose can run
- Build skill generator tool
- Develop skill quality validation framework

### User Stories
**As a** skill creator  
**I want** a tool that helps me capture expert knowledge systematically  
**So that** I can create high-quality skills efficiently

**As a** goose user  
**I want** skills to reference other skills intelligently  
**So that** I get comprehensive guidance without duplication

**As a** festival coordinator  
**I want** executable scripts for common tasks  
**So that** I can automate routine operations

### Requirements

#### Functional Requirements
- [ ] Implement cross-skill referencing:
  - Skills use `[See: skill-name]` notation
  - goose can load referenced skills automatically
  - Circular reference detection
- [ ] Add executable scripts in `scripts/` directory:
  - Incident report generator
  - Lost item logger
  - Vendor checklist validator
  - Emergency notification sender (mock)
- [ ] Create skill generator recipe:
  - Interviews subject matter expert
  - Extracts key scenarios and decisions
  - Generates skill structure
  - Creates supporting files
- [ ] Build skill testing checklist:
  - Completeness criteria
  - Actionability validation
  - Format consistency checks
  - Scenario coverage matrix

#### Non-Functional Requirements
- Scripts must be safe (no destructive operations)
- Skill generator must create Claude-compatible skills
- Testing checklist must be reusable
- Cross-references must be clear and useful

### Acceptance Criteria
**Test Scenarios:**
1. Load security skill → Should reference vendor management skill
2. Run incident report script → Should generate formatted report
3. Use skill generator → Should create valid skill from interview
4. Apply testing checklist → Should identify gaps in skills

### Deliverables
1. Updated skills with cross-references
2. `scripts/` directory with 4+ executable scripts
3. `skill-generator` recipe
4. `skill-testing-checklist.md`
5. Documentation on skill architecture

### Success Metrics
- ✅ Cross-references work bidirectionally
- ✅ Scripts execute successfully via goose
- ✅ Skill generator creates valid skills
- ✅ Testing checklist catches quality issues
- ✅ System handles 10+ interconnected skills

---

## Level 4: Ultimate ⭐⭐⭐⭐ - "Mini Me" Personal AI Clone

### Objectives
- Create skill that captures individual working style
- Document decision-making patterns
- Codify personal expertise and preferences
- Make personal knowledge portable and shareable

### User Stories
**As an** AI engineer  
**I want** to capture my personal expertise in a skill  
**So that** others can work with goose the way I would

**As a** team member  
**I want** to leverage senior engineers' expertise  
**So that** I can make decisions aligned with team standards

**As a** future self  
**I want** my current knowledge captured  
**So that** I can maintain consistency across projects

### Requirements

#### Functional Requirements
- [ ] Create `~/.config/goose/skills/mini-me/SKILL.md` containing:
  - **Problem-Solving Approach**
    - How you break down complex problems
    - Your debugging methodology
    - Your research process
  - **Coding Preferences**
    - Language-specific standards
    - Architectural patterns you favor
    - Code organization principles
    - Testing philosophy
  - **Communication Style**
    - How you explain technical concepts
    - Documentation preferences
    - Collaboration patterns
  - **Decision-Making Framework**
    - Technology selection criteria
    - Trade-off evaluation process
    - When to refactor vs. rewrite
    - Performance vs. readability balance
  - **Common Workflows**
    - Git workflow preferences
    - Code review checklist
    - Debugging process
    - Deployment practices

#### Supporting Files
- [ ] `templates/code-review-checklist.md`
- [ ] `templates/technical-design-template.md`
- [ ] `workflows/debugging-flowchart.md`
- [ ] `workflows/architecture-decision-process.md`
- [ ] `preferences/tech-stack-defaults.md`

#### Non-Functional Requirements
- Skill must capture nuanced decision-making
- Must include examples of your actual work
- Should reference real decisions you've made
- Must be updated regularly (living document)

### Acceptance Criteria
**Test: The "Would I Say That?" Test**

Give goose scenarios you've faced before. Compare goose's response (using your Mini Me skill) to what you actually did.

**Scenarios:**
1. "Should I optimize this function that runs once per day?"
2. "The client wants feature X but it conflicts with our architecture. What do I do?"
3. "I found a bug in production. What's my first step?"
4. "Should I write unit tests or integration tests for this?"
5. "A teammate's code works but violates our standards. How do I handle this?"

**Success:** goose's responses should align with your actual decision-making 80%+ of the time.

### Deliverables
1. `mini-me` skill with comprehensive personal expertise
2. 5+ supporting files (templates, workflows, preferences)
3. Test scenarios and response validation
4. "How to Build Your Mini Me" guide for others
5. Update process documentation

### Success Metrics
- ✅ Passes "Would I Say That?" test (80%+ accuracy)
- ✅ Captures at least 10 specific decision patterns
- ✅ Includes examples from real work
- ✅ Other team members find it useful
- ✅ Reduces decision-making time by 30%+
- ✅ Maintains consistency across projects

---

## Technical Specifications

### Skill File Format
```markdown
---
name: skill-name
description: Brief description of expertise
---

# Skill Title

## Section 1
Content...

## Section 2
Content...
```

### Directory Structure
```
~/.config/goose/skills/
├── festival-operations/          # Level 1
│   ├── SKILL.md
│   └── checklists/
│       ├── opening.md
│       └── closing.md
├── customer-experience/          # Level 2
│   ├── SKILL.md
│   └── templates/
│       └── customer-feedback.md
├── security-vendor-management/   # Level 2
│   ├── SKILL.md
│   ├── templates/
│   └── scripts/
│       └── incident-report.js
└── mini-me/                      # Level 4
    ├── SKILL.md
    ├── templates/
    ├── workflows/
    └── preferences/
```

### Skill Priority (Loading Order)
1. `~/.claude/skills/` (lowest priority, global, Claude compatible)
2. `~/.config/goose/skills/` (global, goose-specific)
3. `./.claude/skills/` (project-specific, Claude compatible)
4. `./.goose/skills/` (highest priority, project-specific)

---

## Dependencies

### System Requirements
- goose version 1.17.0 or higher
- Skills extension enabled
- Developer extension enabled (for file creation)

### Optional Dependencies
- Claude Desktop (for cross-platform testing)
- LLM credits (goose-credits.dev with code: ADVENTDAY14)

---

## Testing Strategy

### Level 1 Testing
- [ ] Skill discovery test
- [ ] Scenario response test (vendor noise complaint)
- [ ] Supporting file access test
- [ ] Cross-platform load test

### Level 2 Testing
- [ ] Multi-skill loading test
- [ ] Cross-skill reference test
- [ ] Template accessibility test
- [ ] Decision tree navigation test

### Level 3 Testing
- [ ] Script execution test
- [ ] Skill generator validation
- [ ] Quality checklist application
- [ ] Complex scenario handling

### Level 4 Testing
- [ ] "Would I Say That?" test
- [ ] Decision pattern validation
- [ ] Consistency across projects test
- [ ] Team member usability test

---

## Documentation Requirements

Each level must include:
- README.md explaining the skill system
- Usage examples
- Test scenarios and expected results
- Troubleshooting guide
- Update process

---

## Success Criteria (Overall Project)

### Quantitative Metrics
- ✅ All 4 levels completed sequentially
- ✅ 10+ skills created total
- ✅ 90%+ test scenario pass rate
- ✅ Works on 3+ platforms (goose Desktop, CLI, Claude Desktop)
- ✅ 20+ supporting files (templates, scripts, checklists)

### Qualitative Metrics
- ✅ Skills provide actionable guidance
- ✅ Knowledge is truly portable
- ✅ Team members can use skills effectively
- ✅ Skills reduce decision-making time
- ✅ System is extensible and maintainable

---

## Timeline (Suggested)

### Level 1: Beginner ⭐
**Time:** 2-3 hours  
**Focus:** Core skill creation, basic structure

### Level 2: Intermediate ⭐⭐
**Time:** 4-6 hours  
**Focus:** Multi-skill architecture, templates, cross-platform

### Level 3: Advanced ⭐⭐⭐
**Time:** 8-12 hours  
**Focus:** Skill generator, scripts, testing framework

### Level 4: Ultimate ⭐⭐⭐⭐
**Time:** 12-20 hours  
**Focus:** Personal expertise capture, validation, refinement

**Total Project Time:** 26-41 hours

---

## Risk Assessment

### Technical Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| Skill not discovered | High | Verify directory structure, check goose version |
| Cross-references break | Medium | Implement validation in testing checklist |
| Scripts fail silently | Medium | Add error handling and logging |
| Skills conflict across platforms | Low | Follow Claude Desktop compatibility guidelines |

### Usability Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| Skills too verbose | Medium | Use scannable formatting, clear headers |
| Decision trees confusing | Medium | Test with users, iterate on clarity |
| Templates not actionable | High | Include filled examples alongside blanks |
| Personal skill too specific | Low | Include "adapt to your context" guidance |

---

## Future Enhancements

### Post-Level 4 Ideas
1. **Skill Marketplace**: Share skills with community
2. **Skill Analytics**: Track which skills are most useful
3. **AI Skill Generator**: Use LLM to create skills from documentation
4. **Version Control**: Git integration for skill evolution
5. **Skill Composition**: Combine multiple skills dynamically
6. **Interactive Skill Builder**: GUI for creating skills
7. **Skill Validation Suite**: Automated testing framework
8. **Team Skill Libraries**: Organizational skill repositories

---

## Appendix A: Content from Team Members

### Madame Zelda - Customer Experience
```
HANDLING DIFFICULT CUSTOMERS:
- Always acknowledge their frustration first
- Offer alternatives, never just say "no"
- If someone's been waiting 20+ min, bump them up with a "VIP reading"
- Skeptics get the "mysterious stranger" fortune style - it wins them over
- Kids under 10 get the "adventure quest" style - parents love it

KEEPING THE LINE MOVING:
- Fortunes should be 2-3 minutes max
- If someone wants to chat, offer a "extended reading" slot for later
- Always have 5 pre-written fortunes ready for rush periods
```

### Marcus - Security & Vendor Relations
```
VENDOR ISSUES:
- Food vendors: Check health permits BEFORE they set up, not after
- Noise complaints: First warning is verbal, second is written, third is shutdown
- Vendor disputes: Never take sides publicly, mediate in the back office
- Payment issues: All vendors must pay 50% upfront, balance day-of

SECURITY PROTOCOLS:
- Lost child: Code Yellow - all exits notify, description broadcast
- Medical emergency: Code Blue - clear path to medical tent, call 911
- Weather emergency: Code White - announce shelter locations, secure loose items
- Suspicious activity: Code Orange - security team converges, don't confront alone
```

### Maria - Lost & Found
```
INTAKE PROCESS:
- Photo EVERYTHING before storing
- Tag with: item description, location found, time, finder's name
- High-value items (phones, wallets, jewelry) go in locked cabinet
- Perishables (food, drinks) disposed after 2 hours

MATCHING PROCESS:
- Ask claimants to describe item BEFORE showing it
- Check ID for high-value items
- Log all claims (successful and unsuccessful)
- Unclaimed items after 30 days go to charity

COMMON PATTERNS:
- Ice rink = mittens and scarves (check there first)
- Food court = phones and wallets (people put them down to eat)
- Kids areas = stuffed animals (URGENT - kids are devastated)
```

### Elena - Marketing & Communications
```
LAST-MINUTE REQUESTS:
- Poster changes: Need 2 hours minimum for print shop
- Social media posts: Can do in 15 minutes if content is provided
- Press inquiries: Route to Festival Director, never speak on record
- Sponsor logo additions: Check contract first, some have exclusivity

EMERGENCY COMMUNICATIONS:
- Weather delays: Post to all channels simultaneously
- Event cancellations: Email ticket holders FIRST, then public announcement
- Good news: Social media first, email newsletter follows
```

---

## Appendix B: Resources

### Documentation
- goose Skills documentation: (check goose docs)
- Claude Desktop skill compatibility guide
- Markdown formatting best practices

### Tools
- goose Desktop (primary interface)
- goose CLI (testing)
- Claude Desktop (cross-platform testing)
- Text editor with YAML support

### Community
- goose Discord/community channels
- Skill sharing repository (if exists)
- Festival operations best practices

---

**End of PRD**

*This document will be updated as we complete each level and learn from implementation.*
