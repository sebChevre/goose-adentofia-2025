// Sound Effects Toggle
// Optional festive background music and sound effects

const soundToggle = document.getElementById('sound-toggle');
const soundIcon = soundToggle?.querySelector('.sound-icon');
const SOUND_KEY = 'festivalSound';

// Audio elements
let backgroundMusic = null;
let clickSound = null;

/**
 * Gets the saved sound preference
 * @returns {boolean}
 */
function getSoundPreference() {
    const saved = localStorage.getItem(SOUND_KEY);
    return saved === 'true';
}

/**
 * Creates audio elements
 */
function initAudio() {
    // Create a simple beep sound using Web Audio API
    // In production, you would use actual audio files
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    // Store context for later use
    window.audioContext = audioContext;
}

/**
 * Plays a festive beep sound
 */
function playClickSound() {
    if (!getSoundPreference() || !window.audioContext) return;
    
    const audioContext = window.audioContext;
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    // Create a pleasant bell-like sound
    oscillator.frequency.value = 800;
    oscillator.type = 'sine';
    
    gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
    
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.2);
}

/**
 * Toggles sound on/off
 */
function toggleSound() {
    const currentState = getSoundPreference();
    const newState = !currentState;
    
    localStorage.setItem(SOUND_KEY, newState.toString());
    updateSoundIcon(newState);
    
    if (newState) {
        playClickSound();
    }
}

/**
 * Updates the sound icon
 * @param {boolean} isEnabled
 */
function updateSoundIcon(isEnabled) {
    if (!soundIcon) return;
    soundIcon.textContent = isEnabled ? '🔊' : '🔇';
}

/**
 * Initializes sound system
 */
function initSound() {
    const isEnabled = getSoundPreference();
    updateSoundIcon(isEnabled);
    
    if (isEnabled) {
        initAudio();
    }
    
    // Add click listener to toggle
    if (soundToggle) {
        soundToggle.addEventListener('click', () => {
            if (!window.audioContext) {
                initAudio();
            }
            toggleSound();
        });
    }
    
    // Add click sounds to buttons
    const buttons = document.querySelectorAll('button, .form-button');
    buttons.forEach(button => {
        if (button.id !== 'sound-toggle') {
            button.addEventListener('click', playClickSound);
        }
    });
}

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSound);
} else {
    initSound();
}
