// Dark Mode Toggle
// Persists user preference in localStorage

const themeToggle = document.getElementById('theme-toggle');
const themeIcon = themeToggle?.querySelector('.theme-icon');
const THEME_KEY = 'festivalTheme';

/**
 * Gets the saved theme preference
 * @returns {string} - 'dark' or 'light'
 */
function getSavedTheme() {
    return localStorage.getItem(THEME_KEY) || 'light';
}

/**
 * Sets the theme
 * @param {string} theme - 'dark' or 'light'
 */
function setTheme(theme) {
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
        if (themeIcon) themeIcon.textContent = '☀️';
    } else {
        document.body.classList.remove('dark-mode');
        if (themeIcon) themeIcon.textContent = '🌙';
    }
    localStorage.setItem(THEME_KEY, theme);
}

/**
 * Toggles between light and dark theme
 */
function toggleTheme() {
    const currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
}

/**
 * Initializes the theme based on saved preference or system preference
 */
function initTheme() {
    const savedTheme = getSavedTheme();
    
    // If no saved preference, check system preference
    if (!localStorage.getItem(THEME_KEY)) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        setTheme(prefersDark ? 'dark' : 'light');
    } else {
        setTheme(savedTheme);
    }
    
    // Add click listener
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
}

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
} else {
    initTheme();
}

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem(THEME_KEY)) {
        setTheme(e.matches ? 'dark' : 'light');
    }
});
