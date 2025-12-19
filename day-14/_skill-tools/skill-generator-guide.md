---
name: skill-generator
description: Interactive tool to help capture expert knowledge and generate well-structured goose skills through guided interviews
---

# Skill Generator

This is a meta-skill that helps you create new skills by interviewing subject matter experts and systematically extracting their knowledge.

## How to Use This Skill

Ask goose to help you create a new skill:
- "Help me create a skill for [domain expertise]"
- "I want to capture expertise in [topic]"
- "Guide me through creating a skill about [subject]"

goose will use this skill to interview you and generate the skill structure.

---

## Skill Generation Process

### Phase 1: Discovery (10-15 minutes)

**Ask the Expert:**

1. **Domain Definition**
   - "What is your area of expertise?"
   - "What problems do you solve regularly?"
   - "Who would use this knowledge?"

2. **Common Scenarios**
   - "What are the 5 most common situations you handle?"
   - "What questions do people ask you most often?"
   - "What mistakes do beginners make?"

3. **Decision Points**
   - "What decisions do you make frequently?"
   - "What criteria do you use to decide?"
   - "Are there any 'rules of thumb' you follow?"

4. **Edge Cases**
   - "What unusual situations come up?"
   - "What emergencies or urgent cases exist?"
   - "What happens when things go wrong?"

**Output:** List of scenarios, decisions, and edge cases

---

### Phase 2: Knowledge Extraction (15-20 minutes)

**For Each Common Scenario:**

1. **Step-by-Step Process**
   - "Walk me through exactly what you do"
   - "What's your first step? Then what?"
   - "How do you know when you're done?"

2. **Decision Trees**
   - "What determines which path you take?"
   - "If X happens, then what?"
   - "What are the options at this point?"

3. **Success Criteria**
   - "How do you know it worked?"
   - "What does good look like?"
   - "What are the warning signs?"

4. **Timing & Resources**
   - "How long does this typically take?"
   - "What do you need to complete this?"
   - "What could slow this down?"

**Output:** Detailed protocols for each scenario

---

### Phase 3: Structure Generation (10 minutes)

**Organize the Knowledge:**

1. **Group Related Content**
   - Cluster similar scenarios
   - Identify natural categories
   - Create logical flow

2. **Identify Supporting Materials**
   - What templates would help?
   - What checklists are needed?
   - What scripts could automate tasks?

3. **Cross-References**
   - What other expertise areas connect?
   - Where do handoffs happen?
   - What dependencies exist?

**Output:** Skill outline with sections

---

### Phase 4: Skill Creation (20-30 minutes)

**Generate the SKILL.md file:**

```markdown
---
name: [domain-name]
description: [One-line description of expertise]
---

# [Skill Title]

**Expert:** [Name]  
**Specialty:** [Focus areas]

[Brief introduction to what this skill provides]

## [Section 1: Common Scenarios]

### [Scenario 1 Name]

**When to Use:**
- [Trigger condition 1]
- [Trigger condition 2]

**Step-by-Step:**
1. [First action]
2. [Second action]
3. [Third action]

**Decision Point:**
\`\`\`
[Decision tree or flowchart]
\`\`\`

**Success Criteria:**
- [How you know it worked]

### [Scenario 2 Name]
[Repeat structure]

## [Section 2: Edge Cases & Emergencies]

### [Emergency Type 1]
[Protocol]

## Quick Reference

[Summary table or checklist]

## Templates & Tools

See \`templates/\` directory for:
- [Template 1]
- [Template 2]

## Related Skills

- [See: related-skill-1]
- [See: related-skill-2]
```

---

### Phase 5: Template Creation (15-20 minutes)

**For Each Template Identified:**

1. **Define Purpose**
   - What is this template for?
   - Who fills it out?
   - When is it used?

2. **Identify Required Fields**
   - What information is needed?
   - What's mandatory vs optional?
   - What validation is needed?

3. **Create Structure**
   - Headers and sections
   - Field placeholders
   - Instructions or examples

**Output:** Template files in `templates/` directory

---

### Phase 6: Script Automation (Optional, 20-30 minutes)

**For Repetitive Tasks:**

1. **Identify Automation Opportunities**
   - What tasks are repetitive?
   - What requires consistency?
   - What could be error-prone if manual?

2. **Design Script Logic**
   - Input requirements
   - Processing steps
   - Output format

3. **Create Script**
   - Interactive prompts
   - Validation logic
   - Error handling
   - Output generation

**Output:** Executable scripts in `scripts/` directory

---

## Quality Checklist

Before finalizing the skill, verify:

### Completeness
- [ ] All common scenarios covered
- [ ] Edge cases addressed
- [ ] Decision points clearly explained
- [ ] Success criteria defined

### Actionability
- [ ] Instructions use imperative mood ("Do X")
- [ ] Steps are specific and concrete
- [ ] Timelines specified where relevant
- [ ] Resources identified

### Usability
- [ ] Sections logically organized
- [ ] Visual elements aid scanning (emoji, headers)
- [ ] Examples provided
- [ ] Quick reference available

### Integration
- [ ] Related skills referenced
- [ ] Handoffs clearly defined
- [ ] No duplication with existing skills
- [ ] Cross-references working

---

## Example Interview Flow

**goose:** "Let's create a skill together. What's your area of expertise?"

**Expert:** "I manage social media for events"

**goose:** "Great! What are the 5 most common tasks you do?"

**Expert:** 
1. Creating event announcements
2. Live posting during events
3. Responding to comments/DMs
4. Creating recap content
5. Handling crisis communications

**goose:** "Let's start with event announcements. Walk me through your process..."

[Interview continues, extracting details for each task]

---

## Skill Template Variations

### Process-Based Skill
Focus on: Workflows, checklists, timelines
Example: Event planning, manufacturing, onboarding

### Decision-Based Skill  
Focus on: Decision trees, criteria, trade-offs
Example: Diagnosis, troubleshooting, architecture

### Knowledge-Based Skill
Focus on: Facts, references, lookup tables
Example: Regulations, pricing, specifications

### Emergency Response Skill
Focus on: Rapid protocols, codes, escalation
Example: Security, medical, IT incidents

---

## Tips for Expert Interviews

### Getting Good Information

**DO:**
- ✅ Ask "walk me through exactly what you do"
- ✅ Probe on decision points: "how do you choose?"
- ✅ Ask for examples: "can you give me a case?"
- ✅ Explore edge cases: "what if X happens?"

**DON'T:**
- ❌ Accept vague answers ("it depends")
- ❌ Skip the "why" behind decisions
- ❌ Assume you understand jargon
- ❌ Rush through complex topics

### Handling "I just know" Responses

When expert says "I just know" or "it's intuition":
1. Ask for the last 3 times they made that decision
2. Look for patterns in their examples
3. Extract the implicit criteria they used
4. Make the unconscious conscious

### Validating Completeness

After interview, test with:
- "A new person uses only this skill. Can they succeed?"
- "What scenario would this skill NOT handle?"
- "What questions would users still have?"

---

## Post-Generation Tasks

After creating the skill:

1. **Test the Skill**
   - [ ] Load it in goose
   - [ ] Try example scenarios
   - [ ] Check cross-references
   - [ ] Verify templates work

2. **Get Expert Review**
   - [ ] Expert validates content
   - [ ] Expert tests with real scenarios
   - [ ] Expert suggests improvements

3. **Iterate**
   - [ ] Address gaps found in testing
   - [ ] Clarify ambiguous sections
   - [ ] Add missing examples

4. **Document**
   - [ ] Add to README
   - [ ] Update skill catalog
   - [ ] Note related skills

---

## Success Metrics

A well-generated skill should:
- ✅ Answer 90%+ of common questions in domain
- ✅ Enable beginners to operate at intermediate level
- ✅ Serve as quick reference for experts
- ✅ Integrate seamlessly with existing skills
- ✅ Require minimal updates (knowledge is stable)

---

## Version History

Track skill evolution:
- v1.0 - Initial creation from expert interview
- v1.1 - Added [section] after user feedback
- v1.2 - Updated [protocol] based on new requirements

---

**Remember:** The goal is to make tacit knowledge explicit. If an expert can do it, a skill should enable others to do it too.
