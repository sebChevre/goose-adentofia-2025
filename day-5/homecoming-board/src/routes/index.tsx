import { createFileRoute, Link } from "@tanstack/react-router";
import { useState, useCallback, useEffect, useMemo } from "react";
import { HandTracker } from "../components/HandTracker";
import { FlightBoard } from "../components/FlightBoard";
import { useMediaPipe } from "../hooks/useMediaPipe";
import { useGestures } from "../hooks/useGestures";
import { useSettings } from "../contexts/SettingsContext";
import { setSoundEnabled } from "../utils/gestureAudio";
import {
	type GestureResult,
	loadTrainedThresholds,
	GestureType,
} from "../utils/gestureDetection";

export const Route = createFileRoute("/")({ component: App });

function App() {
	const [videoElement, setVideoElement] = useState<HTMLVideoElement | null>(
		null,
	);
	const [currentGestureForBoard, setCurrentGestureForBoard] =
		useState<GestureType | null>(null);
	const [isModalOpen, setIsModalOpen] = useState(false);
	const { soundEnabled } = useSettings();

	// Load trained thresholds on mount
	useEffect(() => {
		const loaded = loadTrainedThresholds();
		console.debug("📚 Loaded trained thresholds:", loaded);
	}, []);

	// Sync sound settings with audio utility
	useEffect(() => {
		setSoundEnabled(soundEnabled);
	}, [soundEnabled]);

	// MediaPipe hand tracking
	const { canvasRef, results, isReady, error, fps } =
		useMediaPipe(videoElement);

	// Create ignored gestures set when modal is open
	const ignoredGestures = useMemo(() => {
		if (isModalOpen) {
			return new Set([
				GestureType.THUMBS_UP,
				GestureType.OPEN_PALM,
				GestureType.CLOSED_FIST,
			]);
		}
		return undefined;
	}, [isModalOpen]);

	// Gesture detection with callback
	const handleGesture = useCallback((gesture: GestureResult) => {
		console.debug(
			`✨ Gesture detected: ${gesture.type} - ${gesture.hand} hand`,
		);
		setCurrentGestureForBoard(gesture.type);
	}, []);

	const { currentGesture, allGestures } = useGestures(results, {
		onGesture: handleGesture,
		debounceMs: 300,
		ignoredGestures,
	});

	const handleGestureProcessed = useCallback(() => {
		// Clear the gesture after it's been processed by FlightBoard
		setCurrentGestureForBoard(null);
	}, []);

	const handleModalStateChange = useCallback((isOpen: boolean) => {
		setIsModalOpen(isOpen);
	}, []);

	const handsDetected = results?.multiHandLandmarks?.length || 0;

	return (
		<div className="min-h-screen bg-gradient-to-b from-background via-primary/10 to-background">
			{/* Header */}
			<header className="sr-only">Gesture-Controlled Flight Tracker</header>

			{/* Main Content */}
			<main className="py-8 px-6">
				<div className="max-w-7xl mx-auto">
					{/* Hidden Hand Tracker - runs in background for gesture detection */}
					<div className="hidden">
						<HandTracker
							onVideoReady={setVideoElement}
							canvasRef={canvasRef}
							showCanvas={false}
							showFps={false}
							fps={fps}
							handsDetected={handsDetected}
							isReady={isReady}
							error={error}
							currentGesture={currentGesture}
							allGestures={allGestures}
							className=""
						/>
					</div>

					<div className="mb-6 flex justify-between items-center">
						<div className="inline-flex items-center gap-3 px-4 py-2 bg-card/50 backdrop-blur-sm border border-border rounded-full">
							<span className="text-sm text-muted-foreground">
								Gesture Control
							</span>
							{isReady ? (
								<span className="flex items-center gap-2 text-green-500 dark:text-green-400 text-sm">
									<span className="inline-block w-2 h-2 bg-green-500 dark:bg-green-400 rounded-full animate-pulse"></span>
									Active
								</span>
							) : error ? (
								<span className="text-red-500 dark:text-red-400 text-sm">
									Inactive
								</span>
							) : (
								<span className="text-yellow-500 dark:text-yellow-400 text-sm">
									Starting...
								</span>
							)}
						</div>
					</div>

					{/* Flight Board - Full Width */}
					<div className="bg-card/30 backdrop-blur-sm border border-border rounded-xl p-6">
						<FlightBoard
							gesture={currentGestureForBoard}
							onGestureProcessed={handleGestureProcessed}
							onModalStateChange={handleModalStateChange}
						/>
					</div>
				</div>
			</main>

			{/* Footer */}
			<footer className="py-6 px-6 text-center border-t border-border mt-12 backdrop-blur-sm bg-card/30">
				<p className="text-muted-foreground text-sm">
					Built with TanStack Start • MediaPipe Hands • OpenSky Network • Day 5:
					Advent of AI 2025
				</p>
			</footer>
		</div>
	);
}
