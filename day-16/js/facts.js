// Fun Facts Rotation Logic
// Displays rotating festival facts with smooth transitions

// Fun facts data array
const festivalFacts = [
    "Last year's festival had 5,000 visitors!",
    "We served 2,000 cups of hot cocoa!",
    "The ice sculpture took 12 hours to carve!",
    "50 volunteers made this festival possible!",
    "The yeti mascot won by popular vote!",
    "Over 1,000 marshmallows were roasted at the fire pit!",
    "The festival featured 25 local artisan vendors!",
    "We collected 500 toys for the holiday toy drive!",
    "The opening parade had 15 festive floats!",
    "Local musicians performed 30+ live songs!",
    "The gingerbread house contest had 42 entries!",
    "We used 10,000 twinkling lights for decorations!",
    "The snow maze was visited by over 3,000 people!",
    "Free photos with Santa were taken 800+ times!",
    "The ice skating rink welcomed 2,500 skaters!",
    "We donated $10,000 to local charities!"
];

// Configuration
const ROTATION_INTERVAL = 6000; // 6 seconds (within 5-8 second range)
const FADE_DURATION = 500; // 0.5 seconds for fade transitions

// State
let currentFactIndex = 0;
let rotationTimer = null;

// DOM Element
const factDisplay = document.getElementById('fact-display');

/**
 * Gets a random fact different from the current one
 * @returns {string} - A random fact
 */
function getRandomFact() {
    let newIndex;
    do {
        newIndex = Math.floor(Math.random() * festivalFacts.length);
    } while (newIndex === currentFactIndex && festivalFacts.length > 1);
    
    currentFactIndex = newIndex;
    return festivalFacts[currentFactIndex];
}

/**
 * Gets the next fact in sequence
 * @returns {string} - The next fact
 */
function getNextFact() {
    currentFactIndex = (currentFactIndex + 1) % festivalFacts.length;
    return festivalFacts[currentFactIndex];
}

/**
 * Updates the fact display with fade transition
 * @param {string} newFact - The new fact to display
 */
function updateFactDisplay(newFact) {
    if (!factDisplay) return;
    
    // Fade out
    factDisplay.classList.add('fade-out');
    
    // Wait for fade out, then update text and fade in
    setTimeout(() => {
        factDisplay.textContent = newFact;
        factDisplay.classList.remove('fade-out');
    }, FADE_DURATION);
}

/**
 * Rotates to the next fact
 */
function rotateFact() {
    const nextFact = getNextFact();
    updateFactDisplay(nextFact);
}

/**
 * Starts the fact rotation
 */
function startFactRotation() {
    // Display first fact immediately
    if (factDisplay && festivalFacts.length > 0) {
        factDisplay.textContent = festivalFacts[currentFactIndex];
    }
    
    // Set up rotation interval
    rotationTimer = setInterval(rotateFact, ROTATION_INTERVAL);
}

/**
 * Stops the fact rotation
 */
function stopFactRotation() {
    if (rotationTimer) {
        clearInterval(rotationTimer);
        rotationTimer = null;
    }
}

/**
 * Adds a new fact to the collection
 * @param {string} fact - The fact to add
 */
function addFact(fact) {
    if (fact && typeof fact === 'string') {
        festivalFacts.push(fact);
    }
}

/**
 * Gets all facts
 * @returns {Array} - Array of all facts
 */
function getAllFacts() {
    return [...festivalFacts];
}

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startFactRotation);
} else {
    startFactRotation();
}

// Pause rotation when page is hidden (performance optimization)
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        stopFactRotation();
    } else {
        startFactRotation();
    }
});

// Export for testing/external use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        festivalFacts,
        addFact,
        getAllFacts,
        startFactRotation,
        stopFactRotation
    };
}
