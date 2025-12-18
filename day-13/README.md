# Winter Festival 2025 - Staff Scheduling System

## 🎉 Project Overview

A professional staff scheduling website for the Winter Festival 2025, transforming Marcus's scattered notes (napkins, receipts, back of hand) into a centralized, conflict-free scheduling system.

**Status:** ✅ **Beginner Phase Complete** (Stage 1 of 4)

---

## 📁 Project Structure

```
day-13/
├── index.html              # Master 3-day schedule view
├── staff-list.html         # Complete staff directory
├── monday.html             # Detailed Monday schedule
├── tuesday.html            # Detailed Tuesday schedule
├── wednesday.html          # Detailed Wednesday schedule
├── conflicts.html          # Conflict detection & analysis report
├── styles.css              # Professional styling with color-coding
├── staff_data.json         # Structured staff data (from scattered notes)
├── staff_notes.txt         # Original unstructured notes
├── PRD-Festival-Staff-Scheduling.md  # Complete product requirements
└── README.md               # This file
```

---

## ✅ Completed Features (Beginner Phase)

### 1.1 Environment Setup
- ✅ Project directory structure created
- ✅ Data organization complete
- ✅ All files initialized

### 1.2 Data Organization
- ✅ **Input:** Unstructured text notes from `staff_notes.txt`
- ✅ **Output:** Structured JSON format (`staff_data.json`)
- ✅ **Data Fields Extracted:**
  - Staff names, roles, availability (days & hours)
  - Preferences (morning shifts, lunch breaks)
  - Constraints (training needs, specialized roles)
  - Skills and special notes

### 1.3 Basic Website (HTML/CSS)
- ✅ **Master Schedule** - Full 3-day festival view with color-coded assignments
- ✅ **Staff List** - Complete directory with contact info and skills
- ✅ **Daily Views** - Individual schedules for Monday, Tuesday, Wednesday
- ✅ **Professional Design** - Purple gradient theme, clean tables, responsive layout
- ✅ **Printable Format** - Print-optimized styles with preserved colors

### 1.4 Conflict Detection
- ✅ **Conflict Analysis Report** - Comprehensive validation
- ✅ **Zero Conflicts Detected:**
  - No double-bookings
  - No availability violations
  - All constraints honored
- ✅ **Coverage Gaps Identified:**
  - First Aid gap 5:00-8:00 PM (all 3 days) ⚠️
  - Recommendations provided

---

## 🎯 Key Metrics

| Metric | Value |
|--------|-------|
| **Total Staff** | 8 team members |
| **Festival Days** | 3 (Monday - Wednesday) |
| **Festival Hours** | 10:00 AM - 8:00 PM |
| **Scheduling Conflicts** | 0 ✅ |
| **Coverage Gaps** | 1 (First Aid evening hours) ⚠️ |
| **Pages Created** | 6 HTML pages |
| **Mobile Responsive** | Yes ✅ |

---

## 👥 Staff Coverage

### Monday (6 staff)
- Marcus (Security) - 6am-6pm
- Emma (First Aid) - 9am-5pm ⚠️
- Sarah (Coordinator) - 8am-8pm
- David (Photo Booth) - 10am-10pm
- Jake (Sound) - 7am-11pm
- Tom (Setup) - 5am-3pm

### Tuesday (6 staff)
- Marcus (Security) - 6am-6pm
- Emma (First Aid) - 9am-5pm ⚠️
- Sarah (Coordinator) - 8am-8pm
- David (Photo Booth) - 10am-10pm
- Jake (Sound) - 7am-11pm
- Elena (Marketing) - 9am-9pm

### Wednesday (7 staff)
- Marcus (Security) - 6am-6pm
- Emma (First Aid) - 9am-5pm ⚠️
- Sarah (Coordinator) - 8am-8pm
- David (Photo Booth) - 10am-10pm
- Jake (Sound) - 7am-11pm
- Elena (Marketing) - 9am-9pm
- Lisa (Volunteer - Training) - 12pm-8pm

---

## ⚠️ Critical Issues & Recommendations

### 1. First Aid Coverage Gap (HIGH PRIORITY)
**Issue:** Emma available 9am-5pm, festival runs until 8pm  
**Impact:** Potential safety/regulatory violation  
**Solutions:**
1. Request Emma extend hours to 8pm (+3 hours/day)
2. Hire second certified first aid staff (5-8pm shifts)
3. Reduce festival hours to end at 5pm
4. Verify local regulations for first aid requirements

### 2. Single Points of Failure
- **David** - Only photo booth operator
- **Jake** - Only sound technician
- **Recommendation:** Cross-train Sarah or Elena on basics

### 3. High Staff Utilization
- **Jake:** 48 hours over 3 days (very high)
- **Sarah:** 36 hours with minimal breaks (high)
- **Recommendation:** Monitor for fatigue, ensure adequate breaks

---

## 🎨 Design Features

### Color Coding
- **Purple Gradient Header** - Professional festival branding
- **Green (Assigned)** - Regular shift assignments
- **Yellow (Critical)** - Essential roles (First Aid, required positions)
- **Red (Unavailable)** - Staff not available
- **Blue (Lunch)** - Break periods
- **Light Purple (Early Setup)** - Pre-festival setup crew
- **Light Yellow (Training)** - Training periods

### Responsive Design
- Mobile-friendly navigation
- Tablet-optimized tables
- Print-ready layouts
- Accessible color contrasts

---

## 🚀 How to Use

### Viewing the Schedule
1. Open `index.html` in any web browser
2. Navigate between pages using the top navigation menu
3. Review individual days for detailed schedules
4. Check `conflicts.html` for coverage analysis

### Printing Schedules
1. Open desired page in browser
2. Use browser print function (Ctrl+P / Cmd+P)
3. Colors will be preserved for clarity
4. Each day prints on separate pages

### Updating Staff Data
1. Edit `staff_data.json` with new information
2. Manually update HTML files to reflect changes
3. (Future: Intermediate phase will auto-generate from JSON)

---

## 📊 Success Criteria ✅

- [x] All 8 staff members' data properly structured
- [x] Visual schedule showing Mon-Wed coverage
- [x] Zero scheduling conflicts detected
- [x] Marcus can print and distribute schedules
- [x] Professional, usable website delivered
- [x] Individual staff schedules created
- [x] Basic conflict report generated

---

## 🔮 Future Enhancements (Next Phases)

### Stage 2: Intermediate ⭐⭐
- Interactive schedule with click handlers
- Shift change request system
- Mobile-responsive optimization
- Automated email/SMS reminders

### Stage 3: Advanced ⭐⭐⭐
- Cloud deployment (public URL)
- Real-time updates with WebSockets
- QR code staff check-in
- Analytics dashboard

### Stage 4: Ultimate ⭐⭐⭐⭐
- Multi-event management
- AI-powered staff recommendations
- Calendar app integration
- Automated conflict resolution

---

## 🛠️ Technology Stack

**Current (Beginner Phase):**
- HTML5 - Semantic markup
- CSS3 - Gradients, flexbox, grid, print styles
- JavaScript - Minimal (print date only)
- JSON - Data storage

**Planned (Future Phases):**
- React/Vue - Interactive UI
- Node.js - Backend server
- PostgreSQL - Database
- WebSockets - Real-time updates
- Python - AI/ML features

---

## 📝 Original Data Source

Marcus's scattered notes transformed into structured data:
- Security guy notes on napkin
- Marketing availability on receipt
- Coordinator schedule (mental note)
- Tech specialist constraints (verbal)
- Volunteer training needs (scribbled)
- Setup crew times (back of hand)
- First aid requirements (festival regulation)
- Sound tech preferences (text message)

---

## 👨‍💼 Project Information

**Project:** Advent of AI 2025 - Day 13  
**Challenge:** The Festival Staff Scheduling Crisis  
**Version:** 1.0 (Beginner Phase Complete)  
**Date:** December 18, 2025  
**Created with:** @goose AI Assistant  

---

## 📄 License

Created for Winter Festival 2025 internal use.

---

## 🤝 Contact

For questions or schedule changes, contact:
- **Sarah Chen** - Festival Coordinator
- **Marcus Thompson** - Festival Security Lead

---

**END OF README**
