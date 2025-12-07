/**
 * Gesture Detection Utilities
 *
 * Analyzes hand keypoints to detect specific gestures:
 * - Closed Fist: All fingers curled in
 * - Open Palm: All fingers extended
 */

export interface Keypoint {
	x: number;
	y: number;
	z?: number;
	name?: string;
}

export enum GestureType {
	CLOSED_FIST = "CLOSED_FIST",
	OPEN_PALM = "OPEN_PALM",
	THUMBS_UP = "THUMBS_UP",
	THUMBS_DOWN = "THUMBS_DOWN",
	UNKNOWN = "UNKNOWN",
}

export interface GestureResult {
	type: GestureType;
	confidence: number;
	hand: "Left" | "Right" | "Unknown";
}

// Gesture detection thresholds interface
export interface GestureThresholds {
	fistCurlThreshold: number;
	fistMinFingers: number;
	palmExtendThreshold: number;
	palmThumbMultiplier: number;
	thumbsUpFingerCurl: number;
	thumbsUpThumbExtend: number;
	thumbsUpMinFingers: number;
	thumbsUpYThreshold: number;
	thumbsUpXThreshold: number;
}

// Default thresholds
const DEFAULT_THRESHOLDS: GestureThresholds = {
	fistCurlThreshold: 0.4,
	fistMinFingers: 3,
	palmExtendThreshold: 0.3,
	palmThumbMultiplier: 1.5,
	thumbsUpFingerCurl: 0.6,
	thumbsUpThumbExtend: 0.25,
	thumbsUpMinFingers: 3,
	thumbsUpYThreshold: 0.05,
	thumbsUpXThreshold: 0.25, // Increased from 0.15 - more lenient horizontal thumb position
};

// Load thresholds from localStorage or use defaults
let currentThresholds: GestureThresholds = { ...DEFAULT_THRESHOLDS };

/**
 * Load trained thresholds from localStorage
 */
export function loadTrainedThresholds(): GestureThresholds {
	if (typeof window === "undefined") return DEFAULT_THRESHOLDS;

	try {
		const stored = localStorage.getItem("gesture-thresholds");
		if (stored) {
			const parsed = JSON.parse(stored);
			console.debug("✅ Loaded trained thresholds from localStorage:", parsed);
			console.debug("📊 Comparing to defaults:", {
				fistCurl: `${DEFAULT_THRESHOLDS.fistCurlThreshold} → ${parsed.fistCurlThreshold || DEFAULT_THRESHOLDS.fistCurlThreshold}`,
				thumbsUpFingerCurl: `${DEFAULT_THRESHOLDS.thumbsUpFingerCurl} → ${parsed.thumbsUpFingerCurl || DEFAULT_THRESHOLDS.thumbsUpFingerCurl}`,
				thumbsUpThumbExtend: `${DEFAULT_THRESHOLDS.thumbsUpThumbExtend} → ${parsed.thumbsUpThumbExtend || DEFAULT_THRESHOLDS.thumbsUpThumbExtend}`,
			});
			currentThresholds = { ...DEFAULT_THRESHOLDS, ...parsed };
			return currentThresholds;
		} else {
			console.debug("📝 No trained thresholds found - using defaults");
		}
	} catch (e) {
		console.warn("❌ Failed to load trained thresholds:", e);
	}

	console.debug("📝 Using default thresholds");
	return DEFAULT_THRESHOLDS;
}

/**
 * Get current thresholds (either trained or default)
 */
export function getCurrentThresholds(): GestureThresholds {
	return currentThresholds;
}

/**
 * Update thresholds (called when training completes)
 */
export function updateThresholds(newThresholds: Partial<GestureThresholds>) {
	currentThresholds = { ...currentThresholds, ...newThresholds };
	console.debug("🔄 Updated gesture thresholds:", currentThresholds);
}

/**
 * Reset to default thresholds
 */
export function resetThresholds() {
	currentThresholds = { ...DEFAULT_THRESHOLDS };
	if (typeof window !== "undefined") {
		localStorage.removeItem("gesture-thresholds");
		localStorage.removeItem("gesture-samples");
	}
	console.debug("♻️ Reset to default thresholds");
}

// Auto-load trained thresholds when module initializes (browser only)
if (typeof window !== "undefined") {
	// Use a small delay to ensure localStorage is available
	setTimeout(() => {
		loadTrainedThresholds();
	}, 0);
}

// Hand landmark indices (MediaPipe standard)
const LANDMARK_INDICES = {
	WRIST: 0,
	THUMB_TIP: 4,
	INDEX_TIP: 8,
	MIDDLE_TIP: 12,
	RING_TIP: 16,
	PINKY_TIP: 20,
	THUMB_MCP: 2,
	INDEX_MCP: 5,
	MIDDLE_MCP: 9,
	RING_MCP: 13,
	PINKY_MCP: 17,
};

/**
 * Calculate Euclidean distance between two points
 */
function distance(p1: Keypoint, p2: Keypoint): number {
	const dx = p1.x - p2.x;
	const dy = p1.y - p2.y;
	return Math.sqrt(dx * dx + dy * dy);
}

/**
 * Calculate the curl ratio of a finger
 * Returns value between 0 (extended) and 1 (curled)
 */
function getFingerCurlRatio(
	keypoints: Keypoint[],
	tipIndex: number,
	mcpIndex: number,
	wristIndex: number = LANDMARK_INDICES.WRIST,
): number {
	const tip = keypoints[tipIndex];
	const mcp = keypoints[mcpIndex];
	const wrist = keypoints[wristIndex];

	// Distance from fingertip to wrist
	const tipToWrist = distance(tip, wrist);

	// Distance from MCP (knuckle) to wrist
	const mcpToWrist = distance(mcp, wrist);

	// When finger is extended: tipToWrist > mcpToWrist (tip is far from wrist)
	// When finger is curled: tipToWrist < mcpToWrist (tip is close to wrist)
	//
	// We want: 0 = extended, 1 = curled
	// So if tipToWrist is 1.5x mcpToWrist (extended): ratio = 1.5, inverted = -0.5 -> clamp to 0
	// If tipToWrist is 0.5x mcpToWrist (curled): ratio = 0.5, inverted = 0.5 -> 0.5 curl
	// If tipToWrist is equal to mcpToWrist: ratio = 1.0, inverted = 0 -> 0 curl
	//
	// Better approach: normalize based on expected range
	// Extended finger: ratio ~1.5-2.0, Curled: ratio ~0.6-0.9
	const ratio = tipToWrist / mcpToWrist;

	// Map ratio to curl value
	// If ratio > 1.3 (extended): curl = 0
	// If ratio < 0.9 (curled): curl = 1
	// Linear interpolation between
	const curl = Math.max(0, Math.min(1, (1.3 - ratio) / 0.4));

	return curl;
}

/**
 * Detect if hand is making a closed fist gesture
 * All fingers should be curled in
 */
export function detectClosedFist(
	keypoints: Keypoint[],
	threshold: number = 0.4,
): boolean {
	if (keypoints.length < 21) return false;

	const fingerCurls = [
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.INDEX_TIP,
			LANDMARK_INDICES.INDEX_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.MIDDLE_TIP,
			LANDMARK_INDICES.MIDDLE_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.RING_TIP,
			LANDMARK_INDICES.RING_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.PINKY_TIP,
			LANDMARK_INDICES.PINKY_MCP,
		),
	];

	// Thumb is special - it can be in various positions in a fist
	// Just check if at least 3 out of 4 main fingers are curled
	const curledFingers = fingerCurls.filter((curl) => curl > threshold).length;

	// A fist should have at least 3 fingers curled (more lenient than requiring all 4)
	return curledFingers >= 3;
}

/**
 * Detect if hand is making an open palm gesture
 * All fingers should be extended
 */
export function detectOpenPalm(
	keypoints: Keypoint[],
	threshold: number = 0.3,
): boolean {
	if (keypoints.length < 21) return false;

	const fingerCurls = [
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.INDEX_TIP,
			LANDMARK_INDICES.INDEX_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.MIDDLE_TIP,
			LANDMARK_INDICES.MIDDLE_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.RING_TIP,
			LANDMARK_INDICES.RING_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.PINKY_TIP,
			LANDMARK_INDICES.PINKY_MCP,
		),
	];

	const thumbCurl = getFingerCurlRatio(
		keypoints,
		LANDMARK_INDICES.THUMB_TIP,
		LANDMARK_INDICES.THUMB_MCP,
	);

	// All fingers should be extended (curl ratio below threshold)
	// With new curl calc: 0 = extended, 1 = curled, so we want values < threshold
	const allFingersExtended = fingerCurls.every((curl) => curl < threshold);
	const thumbExtended = thumbCurl < threshold * 1.5; // Thumb can be slightly more curled

	return allFingersExtended && thumbExtended;
}

/**
 * Detect if hand is making a thumbs up gesture
 * Thumb extended upward, all other fingers curled
 */
export function detectThumbsUp(
	keypoints: Keypoint[],
	curlThreshold: number = 0.5,
): boolean {
	if (keypoints.length < 21) return false;

	const fingerCurls = [
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.INDEX_TIP,
			LANDMARK_INDICES.INDEX_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.MIDDLE_TIP,
			LANDMARK_INDICES.MIDDLE_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.RING_TIP,
			LANDMARK_INDICES.RING_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.PINKY_TIP,
			LANDMARK_INDICES.PINKY_MCP,
		),
	];

	const thumbCurl = getFingerCurlRatio(
		keypoints,
		LANDMARK_INDICES.THUMB_TIP,
		LANDMARK_INDICES.THUMB_MCP,
	);

	// All four fingers should be curled
	const allFingersCurled = fingerCurls.every((curl) => curl > curlThreshold);

	// Thumb should be extended (low curl value)
	const thumbExtended = thumbCurl < 0.3;

	// Additionally check that thumb is pointing upward (Y coordinate check)
	const thumbTip = keypoints[LANDMARK_INDICES.THUMB_TIP];
	const wrist = keypoints[LANDMARK_INDICES.WRIST];
	const thumbMcp = keypoints[LANDMARK_INDICES.THUMB_MCP];

	// Thumb tip should be significantly above (lower Y value) than thumb base and wrist
	// (In screen coordinates, lower Y = higher on screen)
	const thumbPointingUp = thumbTip.y < thumbMcp.y && thumbTip.y < wrist.y;

	return allFingersCurled && thumbExtended && thumbPointingUp;
}

/**
 * Detect if hand is making a thumbs down gesture
 * Thumb extended downward, all other fingers curled
 */
export function detectThumbsDown(
	keypoints: Keypoint[],
	curlThreshold: number = 0.5,
): boolean {
	if (keypoints.length < 21) return false;

	const fingerCurls = [
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.INDEX_TIP,
			LANDMARK_INDICES.INDEX_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.MIDDLE_TIP,
			LANDMARK_INDICES.MIDDLE_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.RING_TIP,
			LANDMARK_INDICES.RING_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.PINKY_TIP,
			LANDMARK_INDICES.PINKY_MCP,
		),
	];

	const thumbCurl = getFingerCurlRatio(
		keypoints,
		LANDMARK_INDICES.THUMB_TIP,
		LANDMARK_INDICES.THUMB_MCP,
	);

	// All four fingers should be curled
	const allFingersCurled = fingerCurls.every((curl) => curl > curlThreshold);

	// Thumb should be extended (low curl value)
	const thumbExtended = thumbCurl < 0.3;

	// Additionally check that thumb is pointing downward (Y coordinate check)
	const thumbTip = keypoints[LANDMARK_INDICES.THUMB_TIP];
	const wrist = keypoints[LANDMARK_INDICES.WRIST];
	const thumbMcp = keypoints[LANDMARK_INDICES.THUMB_MCP];

	// Thumb tip should be significantly below (higher Y value) than thumb base and wrist
	// (In screen coordinates, higher Y = lower on screen)
	const thumbPointingDown = thumbTip.y > thumbMcp.y && thumbTip.y > wrist.y;

	return allFingersCurled && thumbExtended && thumbPointingDown;
}

/**
 * Detect gesture from hand keypoints (uses trained thresholds if available)
 */
export function detectGesture(
	keypoints: Keypoint[],
	handedness: "Left" | "Right" | "Unknown" = "Unknown",
): GestureResult {
	if (!keypoints || keypoints.length < 21) {
		console.warn("⚠️ Invalid keypoints:", keypoints?.length);
		return {
			type: GestureType.UNKNOWN,
			confidence: 0,
			hand: handedness,
		};
	}

	// Get current thresholds (trained or default)
	const thresholds = getCurrentThresholds();

	// Debug: Calculate and log finger curls
	const fingerCurls = [
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.INDEX_TIP,
			LANDMARK_INDICES.INDEX_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.MIDDLE_TIP,
			LANDMARK_INDICES.MIDDLE_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.RING_TIP,
			LANDMARK_INDICES.RING_MCP,
		),
		getFingerCurlRatio(
			keypoints,
			LANDMARK_INDICES.PINKY_TIP,
			LANDMARK_INDICES.PINKY_MCP,
		),
	];
	const thumbCurl = getFingerCurlRatio(
		keypoints,
		LANDMARK_INDICES.THUMB_TIP,
		LANDMARK_INDICES.THUMB_MCP,
	);

	console.debug(
		"👆 Finger curls [Index, Middle, Ring, Pinky, Thumb]:",
		[...fingerCurls, thumbCurl].map((c) => c.toFixed(2)).join(", "),
	);

	// Check for thumbs up first (most specific - needs curled fingers + extended thumb pointing up)
	const thumbTip = keypoints[LANDMARK_INDICES.THUMB_TIP];
	const thumbMcp = keypoints[LANDMARK_INDICES.THUMB_MCP];
	const wrist = keypoints[LANDMARK_INDICES.WRIST];
	const indexMcp = keypoints[LANDMARK_INDICES.INDEX_MCP];

	const thumbPointingUp = thumbTip.y < thumbMcp.y && thumbTip.y < wrist.y;
	const thumbPointingDown = thumbTip.y > thumbMcp.y && thumbTip.y > wrist.y;

	// Thumbs up detection with trained thresholds
	const fingersCurledCount = fingerCurls.filter(
		(c) => c > thresholds.thumbsUpFingerCurl,
	).length;
	const thumbExtended = thumbCurl < thresholds.thumbsUpThumbExtend;

	// Normalize Y coordinate differences (in case coords are in pixel space)
	// Get the range of Y coordinates to determine if we need normalization
	const allYCoords = keypoints.map((p) => p.y);
	const maxY = Math.max(...allYCoords);
	const yScale = maxY > 2 ? maxY : 1; // If max > 2, assume pixel coordinates
	const xScale =
		Math.max(...keypoints.map((p) => p.x)) > 2
			? Math.max(...keypoints.map((p) => p.x))
			: 1;

	const thumbPointingUpStrict =
		thumbTip.y < thumbMcp.y - thresholds.thumbsUpYThreshold * yScale &&
		thumbTip.y < wrist.y - thresholds.thumbsUpYThreshold * yScale &&
		thumbTip.y < indexMcp.y;

	// Normalize X distance to 0-1 range if coordinates are in pixels
	const thumbXDistance = Math.abs(thumbTip.x - thumbMcp.x) / xScale;
	const thumbNotTooExtended = thumbXDistance < thresholds.thumbsUpXThreshold;

	const isThumbsUp =
		fingersCurledCount >= thresholds.thumbsUpMinFingers &&
		thumbExtended &&
		thumbPointingUpStrict &&
		thumbNotTooExtended;

	console.debug(
		"👍 Is thumbs up?",
		isThumbsUp,
		`(fingers > ${thresholds.thumbsUpFingerCurl}: ${fingersCurledCount}/${thresholds.thumbsUpMinFingers}, thumb < ${thresholds.thumbsUpThumbExtend}: ${thumbCurl < thresholds.thumbsUpThumbExtend}, pointing up: ${thumbPointingUpStrict})`,
	);

	if (isThumbsUp) {
		return {
			type: GestureType.THUMBS_UP,
			confidence: 0.9,
			hand: handedness,
		};
	}

	// Check for thumbs down (similar to thumbs up but pointing down)
	const isThumbsDown = detectThumbsDown(
		keypoints,
		thresholds.thumbsUpFingerCurl,
	);
	console.debug(
		"👎 Is thumbs down?",
		isThumbsDown,
		`(fingers > ${thresholds.thumbsUpFingerCurl}: ${fingerCurls.every((c) => c > thresholds.thumbsUpFingerCurl)}, thumb < 0.3: ${thumbCurl < 0.3}, pointing down: ${thumbPointingDown})`,
	);

	if (isThumbsDown) {
		return {
			type: GestureType.THUMBS_DOWN,
			confidence: 0.9,
			hand: handedness,
		};
	}

	// Check for closed fist (at least N out of 4 fingers curled) with trained thresholds
	// IMPORTANT: Also check that thumb is NOT extended (to distinguish from thumbs up)
	const fistCurledCount = fingerCurls.filter(
		(c) => c > thresholds.fistCurlThreshold,
	).length;
	const thumbNotExtended = thumbCurl > 0.3; // Thumb should be curled or neutral, not extended
	const isFist =
		fistCurledCount >= thresholds.fistMinFingers && thumbNotExtended;

	console.debug(
		"✊ Is fist?",
		isFist,
		`(${fistCurledCount}/4 fingers curled > ${thresholds.fistCurlThreshold}, threshold: at least ${thresholds.fistMinFingers}, thumb not extended: ${thumbNotExtended})`,
	);

	if (isFist) {
		return {
			type: GestureType.CLOSED_FIST,
			confidence: 0.9,
			hand: handedness,
		};
	}

	// Check for open palm with trained thresholds
	const allFingersExtended = fingerCurls.every(
		(c) => c < thresholds.palmExtendThreshold,
	);
	const palmThumbExtended =
		thumbCurl < thresholds.palmExtendThreshold * thresholds.palmThumbMultiplier;
	const isPalm = allFingersExtended && palmThumbExtended;

	console.debug(
		"🖐️ Is palm?",
		isPalm,
		`(fingers < ${thresholds.palmExtendThreshold}: ${allFingersExtended}, thumb < ${(thresholds.palmExtendThreshold * thresholds.palmThumbMultiplier).toFixed(2)}: ${palmThumbExtended})`,
	);

	if (isPalm) {
		return {
			type: GestureType.OPEN_PALM,
			confidence: 0.85,
			hand: handedness,
		};
	}

	// No gesture detected
	return {
		type: GestureType.UNKNOWN,
		confidence: 0,
		hand: handedness,
	};
}

/**
 * Debounce gesture detection to prevent rapid firing
 */
export class GestureDebouncer {
	private lastGesture: GestureType = GestureType.UNKNOWN;
	private lastGestureTime: number = 0;
	private readonly debounceMs: number;

	constructor(debounceMs: number = 300) {
		this.debounceMs = debounceMs;
	}

	/**
	 * Process gesture with debouncing
	 * Returns gesture only if it's different from last or enough time has passed
	 */
	process(gesture: GestureResult): GestureResult | null {
		const now = Date.now();
		const timeSinceLastGesture = now - this.lastGestureTime;

		// If same gesture and within debounce window, ignore
		if (
			gesture.type === this.lastGesture &&
			timeSinceLastGesture < this.debounceMs
		) {
			return null;
		}

		// If unknown gesture, don't update
		if (gesture.type === GestureType.UNKNOWN) {
			return null;
		}

		// New gesture detected!
		this.lastGesture = gesture.type;
		this.lastGestureTime = now;

		return gesture;
	}

	reset() {
		this.lastGesture = GestureType.UNKNOWN;
		this.lastGestureTime = 0;
	}
}
