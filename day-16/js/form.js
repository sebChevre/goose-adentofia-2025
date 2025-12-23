// Email Signup Form Logic
// Handles form validation, submission, and localStorage

// Configuration
const STORAGE_KEY = 'festivalSignups';

// DOM Elements
const signupForm = document.getElementById('signup-form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const formMessage = document.getElementById('form-message');
const buttonText = submitButton?.querySelector('.button-text');
const buttonLoading = submitButton?.querySelector('.button-loading');

/**
 * Validates email format
 * @param {string} email - Email address to validate
 * @returns {boolean} - True if valid email format
 */
function isValidEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Shows form message
 * @param {string} message - Message to display
 * @param {string} type - Message type ('success' or 'error')
 */
function showMessage(message, type) {
    if (!formMessage) return;
    
    formMessage.textContent = message;
    formMessage.className = 'form-message ' + type;
    
    // Auto-hide success messages after 5 seconds
    if (type === 'success') {
        setTimeout(() => {
            formMessage.style.display = 'none';
        }, 5000);
    }
}

/**
 * Sets loading state on submit button
 * @param {boolean} isLoading - Loading state
 */
function setLoadingState(isLoading) {
    if (!submitButton || !buttonText || !buttonLoading) return;
    
    if (isLoading) {
        submitButton.disabled = true;
        buttonText.style.display = 'none';
        buttonLoading.style.display = 'inline';
    } else {
        submitButton.disabled = false;
        buttonText.style.display = 'inline';
        buttonLoading.style.display = 'none';
    }
}

/**
 * Gets stored signups from localStorage
 * @returns {Array} - Array of signup objects
 */
function getStoredSignups() {
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        return stored ? JSON.parse(stored) : [];
    } catch (error) {
        console.error('Error reading from localStorage:', error);
        return [];
    }
}

/**
 * Saves signup to localStorage
 * @param {Object} signup - Signup data
 * @returns {boolean} - True if successful
 */
function saveSignup(signup) {
    try {
        const signups = getStoredSignups();
        
        // Check if email already exists
        const emailExists = signups.some(s => s.email === signup.email);
        if (emailExists) {
            return false;
        }
        
        signups.push({
            ...signup,
            timestamp: new Date().toISOString()
        });
        
        localStorage.setItem(STORAGE_KEY, JSON.stringify(signups));
        return true;
    } catch (error) {
        console.error('Error saving to localStorage:', error);
        return false;
    }
}

/**
 * Handles form submission
 * @param {Event} e - Submit event
 */
async function handleSubmit(e) {
    e.preventDefault();
    
    // Get form values
    const name = nameInput?.value.trim() || '';
    const email = emailInput?.value.trim() || '';
    
    // Validate email
    if (!email) {
        showMessage('Please enter your email address.', 'error');
        emailInput?.focus();
        return;
    }
    
    if (!isValidEmail(email)) {
        showMessage('Please enter a valid email address.', 'error');
        emailInput?.focus();
        return;
    }
    
    // Set loading state
    setLoadingState(true);
    
    // Simulate network delay (remove in production with real backend)
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // Save to localStorage
    const signup = { name, email };
    const saved = saveSignup(signup);
    
    if (saved) {
        showMessage('🎉 Success! You\'ll be notified when tickets go on sale!', 'success');
        signupForm?.reset();
    } else {
        showMessage('This email is already registered!', 'error');
    }
    
    // Remove loading state
    setLoadingState(false);
}

/**
 * Initializes the form
 */
function initForm() {
    if (signupForm) {
        signupForm.addEventListener('submit', handleSubmit);
    }
    
    // Add real-time email validation
    if (emailInput) {
        emailInput.addEventListener('blur', () => {
            const email = emailInput.value.trim();
            if (email && !isValidEmail(email)) {
                emailInput.style.borderColor = '#ef5350';
            } else {
                emailInput.style.borderColor = '';
            }
        });
        
        emailInput.addEventListener('input', () => {
            emailInput.style.borderColor = '';
            if (formMessage?.classList.contains('error')) {
                formMessage.style.display = 'none';
            }
        });
    }
}

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initForm);
} else {
    initForm();
}

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        isValidEmail,
        getStoredSignups,
        saveSignup
    };
}
