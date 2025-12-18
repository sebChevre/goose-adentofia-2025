# Festival Staff Scheduling System - Product Requirements Document

**Version**: 1.0  
**Date**: 2025-12-18  
**Author**: AI Engineer + Marcus Thompson  
**Project**: Day 13 - Advent of AI 2025

---

## Executive Summary

**Product**: Festival Staff Scheduling System  
**Goal**: Transform scattered staff availability notes into a professional, usable scheduling website  
**Primary User**: Marcus (Festival Coordinator) and Festival Staff  
**Timeline**: Staged implementation (Beginner → Intermediate → Advanced → Ultimate)

---

## Problem Statement

Marcus has critical staff scheduling information scattered across:
- Handwritten notes on napkins
- Receipts
- Back of his hand
- Mental notes

This creates:
- ❌ No centralized source of truth
- ❌ High risk of scheduling conflicts
- ❌ Unprofessional communication with staff
- ❌ Time-consuming manual coordination
- ❌ Potential festival operational failures

---

## Stage 1: Beginner ⭐ - Foundation & Core Functionality

### Goals
- Set up development environment with @goose
- Organize scattered data into structured format
- Create basic but functional scheduling system
- Deliver minimal viable product (MVP)

### Requirements

#### 1.1 Environment Setup
- [ ] Install/verify goose CLI (v1.16.1+)
- [ ] Set up terminal integration
- [ ] Create project directory structure
- [ ] Initialize `staff_notes.txt` with Marcus's data

#### 1.2 Data Organization
**Input**: Unstructured text notes  
**Output**: Structured data format (JSON/CSV)

**Data Fields to Extract**:
- Staff name
- Role/specialty
- Available days
- Available hours (start/end times)
- Preferences (morning/evening)
- Constraints (required breaks, specific stations only)
- Special notes

#### 1.3 Basic Website (HTML/CSS)
**Features**:
- Display 3-day festival schedule grid
- Show staff assignments by day and time slot
- List all staff with their availability
- Simple, clean layout (table-based)
- Printable format

**Pages**:
1. **Master Schedule** - Full 3-day view
2. **Staff List** - All staff with contact info
3. **Daily View** - Individual day schedules

#### 1.4 Conflict Detection
**Basic Validation**:
- Identify overlapping assignments
- Flag understaffed time slots
- Highlight critical role coverage (First Aid, Tech)
- Generate warnings report

### Deliverables
- ✅ Structured data file (JSON/YAML)
- ✅ Static HTML website with CSS
- ✅ Printable master schedule
- ✅ Individual staff schedules
- ✅ Basic conflict report

### Success Criteria
- All 8 staff members' data properly structured
- Visual schedule showing Mon-Wed coverage
- Zero scheduling conflicts
- Marcus can print and distribute schedules

---

## Stage 2: Intermediate ⭐⭐ - Enhanced UX & Functionality

### Goals
- Add interactivity
- Improve usability for staff
- Enable dynamic updates
- Mobile optimization

### Requirements

#### 2.1 Interactive Schedule
**Features**:
- Click shift cells for detailed information
- Modal/popup showing:
  - Staff member bio
  - Shift duration
  - Station/role details
  - Contact information
- Color coding by role type
- Tooltips on hover

#### 2.2 Shift Change Management
**Workflow**:
1. Staff requests shift change
2. System shows eligible replacements
3. Marcus approves/denies
4. Schedule updates automatically

**UI Components**:
- Request form
- Pending requests queue
- Approval interface
- Change history log

#### 2.3 Mobile Responsiveness
**Design Considerations**:
- Responsive grid layout
- Touch-friendly buttons (44px min)
- Swipe navigation between days
- Optimized for screens 320px+
- Progressive Web App (PWA) capabilities

#### 2.4 Automated Reminders
**Notification System**:
- Email/SMS reminders 24h before shift
- Day-of morning reminder
- Configurable reminder settings
- Reminder preview/testing

### Deliverables
- ✅ JavaScript-enhanced interactive website
- ✅ Shift change request system
- ✅ Mobile-optimized responsive design
- ✅ Automated reminder system (email integration)

### Success Criteria
- Works seamlessly on phones/tablets
- Staff can view their schedule on mobile
- Shift changes processed in < 2 minutes
- 90%+ reminder delivery rate

---

## Stage 3: Advanced ⭐⭐⭐ - Deployment & Real-time Features

### Goals
- Make system accessible to entire team
- Enable real-time collaboration
- Add operational features
- Provide analytics

### Requirements

#### 3.1 Deployment
**Hosting Options**:
- **Option A**: Static hosting (Netlify, Vercel, GitHub Pages)
- **Option B**: Simple backend (Node.js + Express)
- **Option C**: Cloud platform (AWS, Google Cloud)

**Requirements**:
- HTTPS enabled
- Custom domain (festivalstaff.com)
- Authentication (basic auth initially)
- Environment variables for config

#### 3.2 Real-time Updates
**Technology**: WebSockets or Server-Sent Events

**Features**:
- Live schedule updates without refresh
- Broadcast changes to all connected users
- "Someone is viewing this" indicators
- Optimistic UI updates

#### 3.3 Staff Check-in System
**Functionality**:
- QR code per staff member
- Mobile check-in interface
- GPS verification (optional)
- Check-in status dashboard
- Late/absent notifications

#### 3.4 Reporting & Analytics
**Reports**:
1. **Coverage Analysis**
   - Hours per time slot
   - Understaffed periods
   - Overstaffed periods
   
2. **Staff Metrics**
   - Total hours per person
   - On-time percentage
   - Shift completion rate
   
3. **Role Distribution**
   - Skills coverage
   - Backup availability
   - Training needs

**Visualizations**:
- Bar charts (hours worked)
- Heatmaps (coverage density)
- Timeline view
- Export to PDF/Excel

### Deliverables
- ✅ Deployed website with public URL
- ✅ Real-time update system
- ✅ Staff check-in functionality
- ✅ Comprehensive reporting dashboard

### Success Criteria
- 99.9% uptime during festival
- < 2 second update propagation
- 80%+ staff using check-in system
- Reports generated on-demand

---

## Stage 4: Ultimate Challenge ⭐⭐⭐⭐ - Enterprise Features

### Goals
- Scale to multiple events
- Intelligent automation
- Integration ecosystem
- Advanced optimization

### Requirements

#### 4.1 Multi-Event Management
**Architecture**:
- Event templates library
- Clone/duplicate events
- Multi-tenant data model
- Event series support

**Features**:
- Calendar view of all events
- Staff allocation across events
- Resource pooling
- Cross-event reporting

#### 4.2 AI-Powered Recommendations
**Machine Learning Features**:

**Staff Matching Algorithm**:
```
Input: Event requirements, staff availability, historical performance
Output: Optimal staff assignments with confidence scores
```

**Factors**:
- Skills matching
- Availability overlap
- Performance history
- Preference alignment
- Fairness (equal hours distribution)
- Travel distance (if venues vary)

#### 4.3 Calendar Integration
**Supported Platforms**:
- Google Calendar
- Apple Calendar (iCal)
- Outlook
- CalDAV standard

**Features**:
- Two-way sync
- Automatic updates
- Timezone handling
- Conflict detection with personal calendars

#### 4.4 Automated Conflict Resolution
**Smart Suggestions**:
- Identify conflicts automatically
- Generate 3-5 resolution options
- Show impact analysis
- One-click resolution application

**Conflict Types**:
- Double-booking
- Understaffing
- Skill gaps
- Break time violations
- Overtime concerns

### Deliverables
- ✅ Multi-event platform
- ✅ AI recommendation engine
- ✅ Calendar app integrations
- ✅ Automated conflict resolver

### Success Criteria
- Manage 10+ simultaneous events
- 85%+ recommendation acceptance rate
- < 5 minute conflict resolution
- Seamless calendar sync

---

## Technical Architecture

### Beginner Stack
```
Frontend: HTML + CSS + minimal JavaScript
Data: JSON/YAML files
Hosting: Local development only
```

### Intermediate Stack
```
Frontend: HTML + CSS + JavaScript (Vanilla or lightweight framework)
Data: JSON files or LocalStorage
Backend: Optional simple Node.js server
Hosting: Still local or simple static hosting
```

### Advanced Stack
```
Frontend: React/Vue/Svelte
Backend: Node.js + Express + Socket.io
Database: PostgreSQL/MongoDB
Hosting: Cloud platform (Vercel, Railway, Render)
```

### Ultimate Stack
```
Frontend: React/Next.js or Vue/Nuxt
Backend: Node.js/Python microservices
Database: PostgreSQL + Redis
ML: Python (scikit-learn/TensorFlow)
Hosting: AWS/GCP with auto-scaling
APIs: RESTful + GraphQL
```

---

## Implementation Roadmap

### Week 1: Beginner Stage
- Days 1-2: Setup & data organization
- Days 3-4: Basic HTML/CSS website
- Days 5-6: Conflict detection & testing
- Day 7: Documentation & handoff

### Week 2: Intermediate Stage
- Days 1-3: Interactivity & UX improvements
- Days 4-5: Mobile optimization
- Days 6-7: Shift change system & reminders

### Week 3: Advanced Stage
- Days 1-2: Deployment setup
- Days 3-4: Real-time features
- Days 5-6: Check-in & reporting
- Day 7: Testing & optimization

### Month 2+: Ultimate Stage
- Weeks 1-2: Multi-event architecture
- Weeks 3-4: AI/ML implementation
- Weeks 5-6: Integrations & automation
- Weeks 7-8: Testing, optimization, launch

---

## Using @goose Throughout

### Beginner Phase
```bash
# Example @goose interactions
cat staff_notes.txt
@goose "parse this into structured JSON format"

@goose "create an HTML table showing the schedule"

@goose "identify any scheduling conflicts"
```

### Intermediate Phase
```bash
@goose "add click handlers to show staff details"

@goose "make this mobile responsive using CSS grid"

@goose "create a shift swap request form"
```

### Advanced Phase
```bash
@goose "help me deploy this to Vercel"

@goose "add WebSocket for real-time updates"

@goose "create a coverage heatmap visualization"
```

### Ultimate Phase
```bash
@goose "design a staff recommendation algorithm"

@goose "implement Google Calendar sync"

@goose "build conflict resolution AI"
```

---

## Success Metrics

### Beginner
- ✅ Data structured: Yes/No
- ✅ Website functional: Yes/No
- ✅ Conflicts identified: Count
- ✅ Marcus satisfaction: 1-10

### Intermediate
- ✅ Mobile traffic: %
- ✅ Shift changes processed: Count/week
- ✅ Reminder delivery rate: %
- ✅ Staff satisfaction: 1-10

### Advanced
- ✅ System uptime: %
- ✅ Check-in adoption: %
- ✅ Report generation time: Seconds
- ✅ Real-time sync latency: ms

### Ultimate
- ✅ Events managed: Count
- ✅ AI recommendation accuracy: %
- ✅ Calendar sync success: %
- ✅ Automated resolutions: %

---

## Staff Data Reference

### Marcus's Original Notes

```
Marcus Thompson - security guy - told me he's free Mon-Wed 6am-6pm, likes mornings better
Elena from marketing - she said Tue-Thu 9am-9pm works, but absolutely no weekends
Sarah Chen our coordinator - available every day 8am-8pm, just needs lunch break
David the tech guy - Mon-Wed 10am-10pm, he's the only one who knows the photo booth
Lisa new volunteer - Wed-Fri 12pm-8pm, she'll need someone to train her
Tom setup crew - Sun-Tue 5am-3pm, he's the strong guy for heavy stuff  
Emma first aid - available all week 9am-5pm, festival requires her at every event
Jake sound tech - Mon-Wed 7am-11pm, but he only does main stage work
```

---

## Appendix A: Challenge Details

**Source**: Advent of AI 2025 - Day 13  
**Challenge**: The Festival Staff Scheduling Crisis  
**Tool**: @goose terminal integration  
**Required Version**: goose CLI v1.16.1+  
**Documentation**: https://block.github.io/goose/llms.txt

### Submission Requirements
- Screenshot of final scheduling website
- Highlights from @goose conversations
- Before/after comparison
- Optional: Screen recording, learning highlights

### Discussion
Submit work to Advent of AI Discussion under Day 13

### Social
Tag on: Discord • Twitter/X • YouTube • LinkedIn • Bluesky

---

## Appendix B: Bonus Challenges Summary

**Beginner ⭐**:
- Add contact information for each staff member
- Create a printable schedule Marcus can post
- Add backup staff assignments
- Generate individual schedules for each person

**Intermediate ⭐⭐**:
- Build an interactive schedule (click for details)
- Add shift change request system
- Make it mobile-friendly for staff phones
- Create automated reminders

**Advanced ⭐⭐⭐**:
- Deploy the site so the whole team can access it
- Add real-time updates when changes happen
- Create staff check-in functionality
- Build reporting (coverage analysis, hours worked)

**Ultimate Challenge ⭐⭐⭐⭐**:
- Multi-event scheduling for future festivals
- Staff skill matching and recommendations
- Integration with calendar apps
- Automated conflict resolution suggestions

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-18 | AI Engineer | Initial PRD creation |

---

**END OF DOCUMENT**
