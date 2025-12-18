# Winter Festival 2025 - Staff Scheduling System
## Intermediate Phase ⭐⭐

This folder contains the **Intermediate Phase** implementation with interactive features, shift change management, mobile optimization, and PWA support.

## 🎉 Features

### Interactive Schedule
- Click any staff assignment to see detailed modal
- Staff bio, availability, skills, constraints
- Contact information
- "Request Shift Change" quick action

### Shift Change Management
- Request shift changes with reason
- System suggests eligible replacements
- Coordinator approval interface
- LocalStorage persistence
- Status tracking (Pending, Approved, Denied)

### Mobile Optimization
- Swipe navigation between days
- Touch-friendly buttons (44px+)
- Responsive modals and forms
- Progressive Web App (PWA) support
- Install to home screen

### Reminder System Preview
- Email reminder templates
- SMS reminder templates
- Configurable settings
- (Full sending requires backend in Advanced phase)

## 📂 Files

```
intermediate/
├── index.html          # Master schedule (interactive)
├── staff-list.html     # Staff directory (interactive)
├── monday.html         # Monday schedule (swipe enabled)
├── tuesday.html        # Tuesday schedule (swipe enabled)
├── wednesday.html      # Wednesday schedule (swipe enabled)
├── conflicts.html      # Conflict analysis report
├── styles.css          # Styles + interactive features
├── app.js              # 600+ lines of JavaScript
├── manifest.json       # PWA configuration
├── staff_data.json     # Staff data
└── README.md           # This file
```

## 🚀 How to Use

1. **View the Schedule:**
   ```bash
   cd /Users/nicktaylor/dev/advent-of-ai-2025/day-13/intermediate
   open index.html
   ```

2. **Try Interactive Features:**
   - Click any green/yellow/purple staff cell
   - Click "Shift Changes" in navigation
   - Submit a shift change request
   - View eligible replacements
   - Approve/deny requests (coordinator view)

3. **Mobile Testing:**
   - Open on mobile device or resize browser
   - Swipe left/right on daily pages
   - Try installing as PWA

4. **Reminder Settings:**
   - Click "Reminders" in navigation
   - View email/SMS preview templates
   - Configure notification preferences

## 🎯 Key Improvements over Beginner Phase

| Feature | Beginner | Intermediate |
|---------|----------|--------------|
| Interactivity | ❌ Static | ✅ Click to view details |
| Shift Changes | ❌ Manual | ✅ Request system |
| Mobile | ✅ Responsive | ✅ + Swipe + PWA |
| Notifications | ❌ None | ✅ Toast messages |
| Data Persistence | ❌ None | ✅ LocalStorage |

## 🛠️ Technology Stack

- **HTML5** - Semantic markup, PWA meta tags
- **CSS3** - Modals, animations, responsive design
- **Vanilla JavaScript** - Interactive features, no frameworks
- **LocalStorage** - Data persistence
- **Web APIs** - Fetch, Touch Events, BeforeInstallPrompt

## 📊 Success Criteria ✅

- [x] Interactive click handlers on schedule
- [x] Shift change request system
- [x] Mobile-responsive design
- [x] Swipe navigation
- [x] PWA installation capability
- [x] Toast notifications
- [x] LocalStorage persistence
- [x] Reminder preview system

## 🔮 Next Steps

**Advanced Phase** will add:
- Cloud deployment (public URL)
- Real-time WebSocket updates
- QR code check-in system
- Analytics dashboard
- Actual email/SMS sending
- Database backend
- User authentication

---

**Created:** December 18, 2025  
**Version:** 2.0 (Intermediate)  
**Status:** ✅ Complete
