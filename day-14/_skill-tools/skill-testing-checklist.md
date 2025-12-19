# Skill Quality Testing Checklist

Use this checklist to validate skill quality before deploying or sharing.

---

## 1. Completeness Criteria

### Content Coverage
- [ ] Skill covers stated domain comprehensively
- [ ] All major scenarios addressed
- [ ] Common edge cases included
- [ ] No obvious gaps in expertise
- [ ] Related skills referenced where appropriate

### Documentation
- [ ] YAML frontmatter present and valid
- [ ] Skill name follows naming conventions
- [ ] Description is clear and accurate
- [ ] All sections have clear headers
- [ ] Examples provided where helpful

### Supporting Materials
- [ ] Templates are included (if applicable)
- [ ] Scripts/tools are functional (if applicable)
- [ ] Checklists are complete (if applicable)
- [ ] Decision trees are clear (if applicable)

**Completeness Score:** ___/12

---

## 2. Actionability Validation

### Guidance Quality
- [ ] Instructions tell users WHAT to do (not just information)
- [ ] Steps are specific and concrete
- [ ] Decision points have clear criteria
- [ ] Timelines/deadlines specified where relevant
- [ ] Success criteria defined

### Usability
- [ ] Language is direct and imperative ("Do X", not "X should be done")
- [ ] No ambiguous terms without definition
- [ ] Priority/urgency clearly indicated
- [ ] Dependencies explicitly stated
- [ ] Assumes appropriate user knowledge level

### Real-World Applicability
- [ ] Protocols can be executed as written
- [ ] Resources referenced are accessible
- [ ] Timelines are realistic
- [ ] Examples reflect actual scenarios
- [ ] Edge cases have practical solutions

**Actionability Score:** ___/15

---

## 3. Format Consistency

### Structure
- [ ] Follows skill template structure
- [ ] Consistent heading hierarchy (H2, H3, H4)
- [ ] Logical section ordering
- [ ] Related content grouped together
- [ ] Navigation is intuitive

### Visual Elements
- [ ] Emoji used consistently for visual scanning
- [ ] Code blocks properly formatted
- [ ] Tables used where appropriate
- [ ] Lists formatted consistently (bullets vs numbered)
- [ ] Decision trees/flowcharts are clear

### Writing Style
- [ ] Professional but accessible tone
- [ ] Consistent voice throughout
- [ ] Active voice preferred
- [ ] Concise (no unnecessary verbosity)
- [ ] Free of typos and grammatical errors

**Format Score:** ___/15

---

## 4. Cross-Skill Integration

### References
- [ ] Related skills properly referenced
- [ ] Reference format consistent: `[See: skill-name]`
- [ ] No broken references
- [ ] Bidirectional references where appropriate
- [ ] No circular reference loops

### Overlap Management
- [ ] No significant duplication with other skills
- [ ] Handoffs between skills are clear
- [ ] Domain boundaries well-defined
- [ ] Complementary skills identified
- [ ] Conflicts with other skills resolved

**Integration Score:** ___/10

---

## 5. Scenario Coverage Matrix

Test the skill against real scenarios. Each should have a clear answer.

### Test Scenarios (Customize to Domain)

| # | Scenario | Covered? | Clear Guidance? | Notes |
|---|----------|----------|-----------------|-------|
| 1 | [Common scenario 1] | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| 2 | [Common scenario 2] | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| 3 | [Edge case 1] | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| 4 | [Emergency situation] | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| 5 | [Complex decision] | ☐ Yes ☐ No | ☐ Yes ☐ No | |

**Scenario Coverage Score:** ___/10 (2 points per scenario)

---

## 6. Technical Validation

### File Structure
- [ ] Files in correct directory
- [ ] Permissions set correctly (scripts executable)
- [ ] File naming follows conventions
- [ ] No broken file paths
- [ ] Cross-platform compatible paths

### Script Testing (if applicable)
- [ ] Scripts execute without errors
- [ ] Input validation works
- [ ] Output format is correct
- [ ] Error handling is robust
- [ ] Dependencies documented

### Platform Compatibility
- [ ] Works in goose Desktop
- [ ] Works in goose CLI
- [ ] Compatible with Claude Desktop (if intended)
- [ ] No platform-specific issues
- [ ] Tested on target systems

**Technical Score:** ___/15

---

## 7. User Experience

### Findability
- [ ] Skill appears in skill list
- [ ] Description helps users find it
- [ ] Search terms likely to be used are present
- [ ] Related skills are discoverable
- [ ] Skill name is intuitive

### Learnability
- [ ] New users can understand without training
- [ ] Examples clarify complex concepts
- [ ] Progressive disclosure (simple → complex)
- [ ] Quick reference section present
- [ ] Common mistakes anticipated and addressed

### Efficiency
- [ ] Expert users can find info quickly
- [ ] Decision trees speed up decisions
- [ ] Templates save time
- [ ] No unnecessary reading required
- [ ] Quick reference formats available

**UX Score:** ___/15

---

## 8. Maintenance & Updates

### Sustainability
- [ ] Owner/maintainer identified
- [ ] Update frequency defined
- [ ] Version number present
- [ ] Change log or update notes
- [ ] Feedback mechanism exists

### Evolution Path
- [ ] Areas for future expansion noted
- [ ] Known limitations documented
- [ ] Integration with future skills considered
- [ ] Deprecated content removed
- [ ] Review date scheduled

**Maintenance Score:** ___/10

---

## Overall Assessment

### Total Scores
- Completeness: ___/12
- Actionability: ___/15
- Format: ___/15
- Integration: ___/10
- Scenarios: ___/10
- Technical: ___/15
- UX: ___/15
- Maintenance: ___/10

**TOTAL: ___/102**

### Rating Scale
- **90-102:** Excellent - Production ready
- **75-89:** Good - Minor improvements recommended
- **60-74:** Acceptable - Moderate revisions needed
- **Below 60:** Needs significant work before deployment

---

## Critical Issues Found

List any critical issues that must be fixed:

1. 
2. 
3. 

---

## Improvement Recommendations

### High Priority
1. 
2. 
3. 

### Medium Priority
1. 
2. 
3. 

### Low Priority (Nice to Have)
1. 
2. 
3. 

---

## Approval

**Tested By:** _______________________________________________  
**Date:** _______________  
**Status:** ☐ Approved ☐ Needs Revision ☐ Rejected

**Reviewer Notes:**
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

---

## Next Steps

- [ ] Address critical issues
- [ ] Implement high-priority improvements
- [ ] Retest after changes
- [ ] Deploy to production
- [ ] Schedule next review

**Follow-up Date:** _______________
