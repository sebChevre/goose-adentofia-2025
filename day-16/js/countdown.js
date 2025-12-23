// Countdown Timer Logic
// Target: December 1, 2026, 10:00 AM

const targetDate = new Date('2026-12-01T10:00:00').getTime();

// DOM Elements
const daysElement = document.getElementById('days');
const hoursElement = document.getElementById('hours');
const minutesElement = document.getElementById('minutes');
const secondsElement = document.getElementById('seconds');

/**
 * Pads a number with leading zero if less than 10
 * @param {number} num - The number to pad
 * @returns {string} - Padded number as string
 */
function padNumber(num) {
    return num < 10 ? '0' + num : num.toString();
}

/**
 * Calculates the time remaining until target date
 * @returns {Object} - Object with days, hours, minutes, seconds
 */
function calculateTimeRemaining() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    // Handle case where countdown has ended
    if (distance < 0) {
        return {
            days: 0,
            hours: 0,
            minutes: 0,
            seconds: 0,
            ended: true
        };
    }

    // Calculate time units
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    return {
        days,
        hours,
        minutes,
        seconds,
        ended: false
    };
}

/**
 * Updates the countdown display
 */
function updateCountdown() {
    const timeRemaining = calculateTimeRemaining();

    // Update DOM elements
    daysElement.textContent = padNumber(timeRemaining.days);
    hoursElement.textContent = padNumber(timeRemaining.hours);
    minutesElement.textContent = padNumber(timeRemaining.minutes);
    secondsElement.textContent = padNumber(timeRemaining.seconds);

    // Handle countdown end
    if (timeRemaining.ended) {
        clearInterval(countdownInterval);
        displayCountdownEndMessage();
    }
}

/**
 * Displays a message when countdown ends
 */
function displayCountdownEndMessage() {
    const countdownSection = document.querySelector('.countdown-section__title');
    if (countdownSection) {
        countdownSection.textContent = '🎉 The Festival Has Begun! 🎉';
    }
}

// Initialize countdown
updateCountdown();

// Update countdown every second
const countdownInterval = setInterval(updateCountdown, 1000);

// Export for testing (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { calculateTimeRemaining, padNumber };
}
