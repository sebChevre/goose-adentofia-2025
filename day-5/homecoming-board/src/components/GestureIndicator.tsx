import { useEffect, useState } from "react";
import type { GestureType } from "../utils/gestureDetection";

interface GestureIndicatorProps {
	gesture: GestureType | null;
	handedness?: "Left" | "Right" | "Unknown";
}

/**
 * GestureIndicator - Visual feedback for detected gestures
 * Shows current gesture with animations and icons
 */
export function GestureIndicator({
	gesture,
	handedness = "Unknown",
}: GestureIndicatorProps) {
	const [showPulse, setShowPulse] = useState(false);

	// Trigger pulse animation on gesture change
	useEffect(() => {
		if (gesture && gesture !== "UNKNOWN") {
			setShowPulse(true);
			const timer = setTimeout(() => setShowPulse(false), 600);
			return () => clearTimeout(timer);
		}
	}, [gesture]);

	if (!gesture || gesture === "UNKNOWN") {
		return (
			<div className="bg-card border border-border rounded-xl p-6 text-center">
				<div className="text-6xl mb-3 opacity-50 grayscale">👋</div>
				<p className="text-muted-foreground text-sm">
					Show a hand gesture to control the board
				</p>
			</div>
		);
	}

	const gestureInfo = getGestureInfo(gesture);

	return (
		<div
			className={`
        relative bg-gradient-to-br ${gestureInfo.bgGradient} 
        border-2 ${gestureInfo.borderColor} rounded-xl p-6 text-center
        transition-all duration-300
        ${showPulse ? "scale-110 shadow-2xl" : "scale-100"}
      `}
		>
			{/* Pulse effect */}
			{showPulse && (
				<div
					className={`
            absolute inset-0 rounded-xl ${gestureInfo.pulseColor}
            animate-ping opacity-75
          `}
				/>
			)}

			{/* Gesture Icon */}
			<div className={`text-8xl mb-4 ${showPulse ? "animate-bounce" : ""}`}>
				{gestureInfo.icon}
			</div>

			{/* Gesture Name */}
			<h3 className={`text-2xl font-black ${gestureInfo.textColor} mb-2`}>
				{gestureInfo.name}
			</h3>

			{/* Gesture Action */}
			<p className="text-foreground/90 dark:text-white/80 text-sm mb-3">
				{gestureInfo.action}
			</p>

			{/* Hand Info */}
			<div className="flex items-center justify-center gap-2 text-xs text-muted-foreground">
				<span>{handedness === "Left" ? "🤚" : "✋"}</span>
				<span>{handedness} Hand</span>
			</div>

			{/* Decorative elements */}
			<div className="absolute top-2 right-2 text-2xl opacity-20">
				{gestureInfo.icon}
			</div>
			<div className="absolute bottom-2 left-2 text-2xl opacity-20">
				{gestureInfo.icon}
			</div>
		</div>
	);
}

function getGestureInfo(gesture: GestureType) {
	switch (gesture) {
		case "CLOSED_FIST":
			return {
				icon: "✊",
				name: "Closed Fist",
				action: "Scrolling to next flight",
				bgGradient:
					"from-orange-200/60 to-red-200/60 dark:from-orange-900/60 dark:to-red-900/60",
				borderColor: "border-orange-500",
				textColor: "text-orange-800 dark:text-orange-200",
				pulseColor: "bg-orange-500/50",
			};
		case "OPEN_PALM":
			return {
				icon: "🖐️",
				name: "Open Palm",
				action: "Scrolling to previous flight",
				bgGradient:
					"from-blue-200/60 to-cyan-200/60 dark:from-blue-900/60 dark:to-cyan-900/60",
				borderColor: "border-cyan-500",
				textColor: "text-cyan-800 dark:text-cyan-200",
				pulseColor: "bg-cyan-500/50",
			};
		case "THUMBS_UP":
			return {
				icon: "👍",
				name: "Thumbs Up",
				action: "Opening flight details",
				bgGradient:
					"from-green-200/60 to-emerald-200/60 dark:from-green-900/60 dark:to-emerald-900/60",
				borderColor: "border-green-500",
				textColor: "text-green-800 dark:text-green-200",
				pulseColor: "bg-green-500/50",
			};
		case "THUMBS_DOWN":
			return {
				icon: "👎",
				name: "Thumbs Down",
				action: "Closing flight details",
				bgGradient:
					"from-red-200/60 to-rose-200/60 dark:from-red-900/60 dark:to-rose-900/60",
				borderColor: "border-red-500",
				textColor: "text-red-800 dark:text-red-200",
				pulseColor: "bg-red-500/50",
			};
		default:
			return {
				icon: "❓",
				name: "Unknown",
				action: "",
				bgGradient:
					"from-gray-200 to-gray-300 dark:from-slate-800 dark:to-slate-900",
				borderColor: "border-border",
				textColor: "text-muted-foreground",
				pulseColor: "bg-muted/50",
			};
	}
}
