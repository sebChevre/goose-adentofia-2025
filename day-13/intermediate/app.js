// ===========================
// Festival Staff Scheduling - JavaScript
// Intermediate Phase
// ===========================

// Load staff data
let staffData = null;
let shiftChangeRequests = [];

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', async () => {
    await loadStaffData();
    initializeInteractiveSchedule();
    initializeShiftChangeSystem();
    initializeMobileFeatures();
    loadShiftChangeRequests();
});

// Load staff data from JSON
async function loadStaffData() {
    try {
        const response = await fetch('staff_data.json');
        staffData = await response.json();
        console.log('Staff data loaded:', staffData);
    } catch (error) {
        console.error('Error loading staff data:', error);
    }
}

// ===========================
// 2.1 Interactive Schedule
// ===========================

function initializeInteractiveSchedule() {
    // Add click handlers to all staff assignment cells
    const assignedCells = document.querySelectorAll('.assigned, .critical, .lunch, .early-setup, .training');
    
    assignedCells.forEach(cell => {
        cell.style.cursor = 'pointer';
        cell.addEventListener('click', showStaffDetails);
        
        // Add hover effect
        cell.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.02)';
            this.style.transition = 'transform 0.2s ease';
        });
        
        cell.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
}

function showStaffDetails(event) {
    const cellText = event.target.textContent.trim();
    
    // Extract staff name from cell (handle cases like "Marcus (6am+)" or "Sarah (LUNCH)")
    const nameMatch = cellText.match(/^([A-Za-z]+)/);
    if (!nameMatch) return;
    
    const staffName = nameMatch[1];
    
    // Find staff member in data
    if (!staffData || !staffData.staff) return;
    
    const staffMember = staffData.staff.find(s => s.name.includes(staffName));
    
    if (staffMember) {
        displayStaffModal(staffMember, cellText);
    }
}

function displayStaffModal(staff, shiftInfo) {
    // Create modal HTML
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            <div class="modal-header">
                <h3>${staff.name}</h3>
                <span class="role-badge">${staff.role}</span>
            </div>
            <div class="modal-body">
                <div class="modal-section">
                    <h4>📋 Current Shift</h4>
                    <p>${shiftInfo}</p>
                </div>
                
                <div class="modal-section">
                    <h4>📅 Availability</h4>
                    <p><strong>Days:</strong> ${staff.availability.days.join(', ')}</p>
                    <p><strong>Hours:</strong> ${staff.availability.hours.start} - ${staff.availability.hours.end}</p>
                </div>
                
                ${staff.preferences ? `
                <div class="modal-section">
                    <h4>⭐ Preferences</h4>
                    <p>${staff.preferences}</p>
                </div>
                ` : ''}
                
                ${staff.constraints ? `
                <div class="modal-section">
                    <h4>⚠️ Constraints</h4>
                    <p>${staff.constraints}</p>
                </div>
                ` : ''}
                
                <div class="modal-section">
                    <h4>🎯 Skills</h4>
                    <div class="skills-list">
                        ${staff.skills.map(skill => `<span class="skill-badge">${skill}</span>`).join('')}
                    </div>
                </div>
                
                <div class="modal-section">
                    <h4>📞 Contact</h4>
                    <p><em>Contact information would be displayed here</em></p>
                    <p>Email: ${staff.name.toLowerCase().replace(' ', '.')}@festival.com</p>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeModal()">Close</button>
                <button class="btn btn-primary" onclick="initiateShiftChange('${staff.name}')">Request Shift Change</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    // Close on background click
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
    
    // Prevent body scroll when modal is open
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.querySelector('.modal-overlay');
    if (modal) {
        modal.remove();
        document.body.style.overflow = 'auto';
    }
}

// ===========================
// 2.2 Shift Change Management
// ===========================

function initializeShiftChangeSystem() {
    // Add shift change button to navigation if it doesn't exist
    const nav = document.querySelector('nav');
    if (nav && !document.getElementById('shift-change-btn')) {
        const shiftChangeBtn = document.createElement('a');
        shiftChangeBtn.id = 'shift-change-btn';
        shiftChangeBtn.href = '#';
        shiftChangeBtn.textContent = 'Shift Changes';
        shiftChangeBtn.addEventListener('click', (e) => {
            e.preventDefault();
            showShiftChangeInterface();
        });
        nav.appendChild(shiftChangeBtn);
    }
}

function initiateShiftChange(staffName) {
    closeModal();
    showShiftChangeForm(staffName);
}

function showShiftChangeForm(staffName = '') {
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            <div class="modal-header">
                <h3>Request Shift Change</h3>
            </div>
            <div class="modal-body">
                <form id="shift-change-form" class="shift-change-form">
                    <div class="form-group">
                        <label for="requestor-name">Your Name:</label>
                        <select id="requestor-name" required>
                            <option value="">Select your name...</option>
                            ${staffData.staff.map(s => `<option value="${s.name}" ${s.name === staffName ? 'selected' : ''}>${s.name}</option>`).join('')}
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="shift-day">Day:</label>
                        <select id="shift-day" required>
                            <option value="">Select day...</option>
                            <option value="Monday">Monday</option>
                            <option value="Tuesday">Tuesday</option>
                            <option value="Wednesday">Wednesday</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="shift-time">Time Slot:</label>
                        <select id="shift-time" required>
                            <option value="">Select time...</option>
                            <option value="5:00-9:00 AM">5:00-9:00 AM</option>
                            <option value="9:00-12:00 PM">9:00-12:00 PM</option>
                            <option value="12:00-1:00 PM">12:00-1:00 PM</option>
                            <option value="1:00-5:00 PM">1:00-5:00 PM</option>
                            <option value="5:00-8:00 PM">5:00-8:00 PM</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="reason">Reason:</label>
                        <textarea id="reason" rows="3" required placeholder="Why do you need to change this shift?"></textarea>
                    </div>
                    
                    <div class="form-group">
                        <label for="replacement">Suggested Replacement (optional):</label>
                        <select id="replacement">
                            <option value="">Let coordinator find replacement...</option>
                            ${staffData.staff.map(s => `<option value="${s.name}">${s.name}</option>`).join('')}
                        </select>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeModal()">Cancel</button>
                <button class="btn btn-primary" onclick="submitShiftChangeRequest()">Submit Request</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
}

function submitShiftChangeRequest() {
    const form = document.getElementById('shift-change-form');
    
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }
    
    const request = {
        id: Date.now(),
        requestor: document.getElementById('requestor-name').value,
        day: document.getElementById('shift-day').value,
        time: document.getElementById('shift-time').value,
        reason: document.getElementById('reason').value,
        replacement: document.getElementById('replacement').value,
        status: 'pending',
        timestamp: new Date().toISOString()
    };
    
    shiftChangeRequests.push(request);
    saveShiftChangeRequests();
    
    closeModal();
    showSuccessMessage('Shift change request submitted! Coordinator will review shortly.');
    
    // Show eligible replacements
    setTimeout(() => {
        showEligibleReplacements(request);
    }, 1000);
}

function showEligibleReplacements(request) {
    // Find staff members who could potentially cover this shift
    const eligibleStaff = staffData.staff.filter(staff => {
        return staff.name !== request.requestor &&
               staff.availability.days.includes(request.day);
    });
    
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            <div class="modal-header">
                <h3>Eligible Replacements for ${request.requestor}</h3>
                <p>${request.day}, ${request.time}</p>
            </div>
            <div class="modal-body">
                <p><strong>Available staff members who can work on ${request.day}:</strong></p>
                <div class="staff-grid">
                    ${eligibleStaff.map(staff => `
                        <div class="staff-card">
                            <h4>${staff.name}</h4>
                            <span class="role">${staff.role}</span>
                            <p><strong>Hours:</strong> ${staff.availability.hours.start} - ${staff.availability.hours.end}</p>
                            <p><strong>Skills:</strong> ${staff.skills.slice(0, 2).join(', ')}</p>
                            <button class="btn btn-sm btn-primary" onclick="assignReplacement(${request.id}, '${staff.name}')">Select</button>
                        </div>
                    `).join('')}
                </div>
                ${eligibleStaff.length === 0 ? '<p><em>No eligible replacements found. Manual coordination required.</em></p>' : ''}
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeModal()">Close</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
}

function assignReplacement(requestId, replacementName) {
    const request = shiftChangeRequests.find(r => r.id === requestId);
    if (request) {
        request.replacement = replacementName;
        request.status = 'pending_approval';
        saveShiftChangeRequests();
        closeModal();
        showSuccessMessage(`${replacementName} suggested as replacement. Awaiting coordinator approval.`);
    }
}

function showShiftChangeInterface() {
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    
    const pendingRequests = shiftChangeRequests.filter(r => r.status === 'pending' || r.status === 'pending_approval');
    const approvedRequests = shiftChangeRequests.filter(r => r.status === 'approved');
    const deniedRequests = shiftChangeRequests.filter(r => r.status === 'denied');
    
    modal.innerHTML = `
        <div class="modal-content modal-large">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            <div class="modal-header">
                <h3>Shift Change Management</h3>
                <button class="btn btn-primary" onclick="closeModal(); showShiftChangeForm();">New Request</button>
            </div>
            <div class="modal-body">
                <div class="shift-changes-container">
                    <div class="shift-change-section">
                        <h4>⏳ Pending Requests (${pendingRequests.length})</h4>
                        ${pendingRequests.length === 0 ? '<p><em>No pending requests</em></p>' : ''}
                        ${pendingRequests.map(req => renderShiftChangeRequest(req)).join('')}
                    </div>
                    
                    <div class="shift-change-section">
                        <h4>✅ Approved (${approvedRequests.length})</h4>
                        ${approvedRequests.length === 0 ? '<p><em>No approved requests</em></p>' : ''}
                        ${approvedRequests.map(req => renderShiftChangeRequest(req)).join('')}
                    </div>
                    
                    <div class="shift-change-section">
                        <h4>❌ Denied (${deniedRequests.length})</h4>
                        ${deniedRequests.length === 0 ? '<p><em>No denied requests</em></p>' : ''}
                        ${deniedRequests.map(req => renderShiftChangeRequest(req)).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
}

function renderShiftChangeRequest(request) {
    return `
        <div class="shift-request-card status-${request.status}">
            <div class="request-header">
                <strong>${request.requestor}</strong>
                <span class="badge badge-${request.status}">${request.status.replace('_', ' ')}</span>
            </div>
            <div class="request-details">
                <p><strong>Shift:</strong> ${request.day}, ${request.time}</p>
                <p><strong>Reason:</strong> ${request.reason}</p>
                ${request.replacement ? `<p><strong>Replacement:</strong> ${request.replacement}</p>` : ''}
                <p class="request-time">Submitted: ${new Date(request.timestamp).toLocaleString()}</p>
            </div>
            ${request.status === 'pending' || request.status === 'pending_approval' ? `
                <div class="request-actions">
                    <button class="btn btn-sm btn-success" onclick="approveShiftChange(${request.id})">Approve</button>
                    <button class="btn btn-sm btn-danger" onclick="denyShiftChange(${request.id})">Deny</button>
                </div>
            ` : ''}
        </div>
    `;
}

function approveShiftChange(requestId) {
    const request = shiftChangeRequests.find(r => r.id === requestId);
    if (request) {
        request.status = 'approved';
        saveShiftChangeRequests();
        closeModal();
        showSuccessMessage(`Shift change approved for ${request.requestor}!`);
        setTimeout(() => showShiftChangeInterface(), 500);
    }
}

function denyShiftChange(requestId) {
    const request = shiftChangeRequests.find(r => r.id === requestId);
    if (request) {
        request.status = 'denied';
        saveShiftChangeRequests();
        closeModal();
        showSuccessMessage(`Shift change denied for ${request.requestor}.`);
        setTimeout(() => showShiftChangeInterface(), 500);
    }
}

function saveShiftChangeRequests() {
    localStorage.setItem('shiftChangeRequests', JSON.stringify(shiftChangeRequests));
}

function loadShiftChangeRequests() {
    const saved = localStorage.getItem('shiftChangeRequests');
    if (saved) {
        shiftChangeRequests = JSON.parse(saved);
    }
}

// ===========================
// 2.3 Mobile Features
// ===========================

function initializeMobileFeatures() {
    // Add swipe navigation for daily views
    if (window.location.pathname.includes('monday') || 
        window.location.pathname.includes('tuesday') || 
        window.location.pathname.includes('wednesday')) {
        initializeSwipeNavigation();
    }
    
    // Add hamburger menu for mobile
    addMobileMenu();
    
    // Add "Install App" prompt for PWA
    addInstallPrompt();
}

let touchStartX = 0;
let touchEndX = 0;

function initializeSwipeNavigation() {
    document.addEventListener('touchstart', e => {
        touchStartX = e.changedTouches[0].screenX;
    });
    
    document.addEventListener('touchend', e => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });
}

function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;
    
    if (Math.abs(diff) < swipeThreshold) return;
    
    const currentPage = window.location.pathname;
    
    if (diff > 0) {
        // Swipe left - next day
        if (currentPage.includes('monday')) window.location.href = 'tuesday.html';
        else if (currentPage.includes('tuesday')) window.location.href = 'wednesday.html';
    } else {
        // Swipe right - previous day
        if (currentPage.includes('wednesday')) window.location.href = 'tuesday.html';
        else if (currentPage.includes('tuesday')) window.location.href = 'monday.html';
    }
}

function addMobileMenu() {
    // This would add a hamburger menu for mobile - simplified for now
    const nav = document.querySelector('nav');
    if (nav && window.innerWidth < 768) {
        nav.classList.add('mobile-nav');
    }
}

let deferredPrompt;

function addInstallPrompt() {
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        
        // Show install button
        const installBtn = document.createElement('button');
        installBtn.className = 'btn btn-install';
        installBtn.textContent = '📱 Install App';
        installBtn.style.cssText = 'position: fixed; bottom: 20px; right: 20px; z-index: 999;';
        installBtn.addEventListener('click', async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                console.log(`User response: ${outcome}`);
                deferredPrompt = null;
                installBtn.remove();
            }
        });
        
        document.body.appendChild(installBtn);
    });
}

// ===========================
// Helper Functions
// ===========================

function showSuccessMessage(message) {
    const toast = document.createElement('div');
    toast.className = 'toast toast-success';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('toast-show');
    }, 100);
    
    setTimeout(() => {
        toast.classList.remove('toast-show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// ===========================
// 2.4 Reminder System Preview
// ===========================

function showReminderSettings() {
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            <div class="modal-header">
                <h3>📧 Reminder Settings</h3>
            </div>
            <div class="modal-body">
                <p><em>Automated reminder system (Email/SMS)</em></p>
                <p><strong>Note:</strong> Full email/SMS integration requires backend server (Advanced phase)</p>
                
                <div class="reminder-preview">
                    <h4>Preview: 24-Hour Reminder</h4>
                    <div class="email-preview">
                        <p><strong>To:</strong> marcus.thompson@festival.com</p>
                        <p><strong>Subject:</strong> Shift Reminder - Tomorrow at 6:00 AM</p>
                        <hr>
                        <p>Hi Marcus,</p>
                        <p>This is a reminder that you have a shift tomorrow:</p>
                        <ul>
                            <li><strong>Day:</strong> Monday</li>
                            <li><strong>Time:</strong> 6:00 AM - 6:00 PM</li>
                            <li><strong>Role:</strong> Security</li>
                            <li><strong>Location:</strong> Main Entrance</li>
                        </ul>
                        <p>Please confirm your attendance by replying to this email.</p>
                        <p>See you tomorrow!</p>
                        <p>- Festival Scheduling Team</p>
                    </div>
                    
                    <h4>Preview: Day-Of Reminder</h4>
                    <div class="sms-preview">
                        <p><strong>SMS to:</strong> +1-555-0123</p>
                        <p>Good morning Marcus! Your shift starts in 2 hours (6:00 AM). Location: Main Entrance. Reply OK to confirm.</p>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>
                        <input type="checkbox" checked> Send 24-hour advance reminder
                    </label>
                </div>
                <div class="form-group">
                    <label>
                        <input type="checkbox" checked> Send day-of morning reminder
                    </label>
                </div>
                <div class="form-group">
                    <label>
                        <input type="checkbox"> Send reminder on shift completion
                    </label>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeModal()">Close</button>
                <button class="btn btn-primary" onclick="closeModal(); showSuccessMessage('Reminder settings saved!');">Save Settings</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
}

// Add reminder settings to nav
document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('nav');
    if (nav && !document.getElementById('reminder-btn')) {
        const reminderBtn = document.createElement('a');
        reminderBtn.id = 'reminder-btn';
        reminderBtn.href = '#';
        reminderBtn.textContent = '📧 Reminders';
        reminderBtn.addEventListener('click', (e) => {
            e.preventDefault();
            showReminderSettings();
        });
        nav.appendChild(reminderBtn);
    }
});
