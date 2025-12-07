import { useState, useEffect } from "react";
import { useFlightData } from "../hooks/useFlightData";
import { FlightCard } from "./FlightCard";
import { FlightDetailModal } from "./FlightDetailModal";
import { GestureType } from "../utils/gestureDetection";

interface FlightBoardProps {
	onFlightSelect?: (flightId: string) => void;
	onGestureNavigate?: (direction: "up" | "down") => void;
	gesture?: GestureType | null;
	onGestureProcessed?: () => void;
	onModalStateChange?: (isOpen: boolean) => void;
}

export function FlightBoard({
	onFlightSelect,
	onGestureNavigate,
	gesture,
	onGestureProcessed,
	onModalStateChange,
}: FlightBoardProps) {
	const [selectedIndex, setSelectedIndex] = useState(0);
	const [isModalOpen, setIsModalOpen] = useState(false);

	const {
		data: flights,
		isLoading,
		error,
		refetch,
		dataUpdatedAt,
		isFetching,
	} = useFlightData({
		refetchInterval: 30000, // 30 seconds
	});

	// Notify parent when modal state changes
	useEffect(() => {
		onModalStateChange?.(isModalOpen);
	}, [isModalOpen, onModalStateChange]);

	// Reset selected index if flights change
	useEffect(() => {
		if (flights && selectedIndex >= flights.length) {
			setSelectedIndex(Math.max(0, flights.length - 1));
		}
	}, [flights, selectedIndex]);

	// Handle gesture input from parent
	useEffect(() => {
		console.debug(
			"🎮 Gesture effect triggered - gesture:",
			gesture,
			"flights:",
			flights?.length,
		);

		if (!gesture) {
			console.debug("  ⏭️ No gesture, skipping");
			return;
		}

		if (!flights || flights.length === 0) {
			console.debug("  ⏭️ No flights, skipping");
			return;
		}

		console.debug("  ✅ Processing gesture:", gesture);

		// Map gestures to navigation actions
		if (gesture === GestureType.CLOSED_FIST) {
			console.debug("  ✊ Closed fist - navigate down");
			handleNavigate("down");
		} else if (gesture === GestureType.OPEN_PALM) {
			console.debug("  ✋ Open palm - navigate up");
			handleNavigate("up");
		} else if (gesture === GestureType.THUMBS_UP) {
			console.debug("  👍 Thumbs up - opening modal for selected flight");
			// Open the modal for the currently selected flight
			if (flights && flights[selectedIndex]) {
				setIsModalOpen(true);
			}
		} else if (gesture === GestureType.THUMBS_DOWN) {
			console.debug("  👎 Thumbs down - closing modal");
			// Close the modal if it's open
			if (isModalOpen) {
				setIsModalOpen(false);
			}
		} else {
			console.debug("  ❓ Unknown gesture type:", gesture);
		}

		// Mark gesture as processed
		console.debug("  🧹 Calling onGestureProcessed");
		onGestureProcessed?.();
	}, [
		gesture,
		flights,
		selectedIndex,
		isModalOpen,
		refetch,
		onGestureProcessed,
	]);

	// Navigate between flights
	const handleNavigate = (direction: "up" | "down") => {
		console.debug("  📍 handleNavigate called with direction:", direction);
		console.debug("  📍 Current selectedIndex:", selectedIndex);
		console.debug("  📍 Total flights:", flights?.length);

		if (!flights || flights.length === 0) {
			console.debug("  ❌ No flights available");
			return;
		}

		let newIndex = selectedIndex;
		if (direction === "down") {
			newIndex = Math.min(selectedIndex + 1, flights.length - 1);
			console.debug("  ⬇️ Scrolling DOWN: from", selectedIndex, "to", newIndex);
		} else {
			newIndex = Math.max(selectedIndex - 1, 0);
			console.debug("  ⬆️ Scrolling UP: from", selectedIndex, "to", newIndex);
		}

		setSelectedIndex(newIndex);
		onGestureNavigate?.(direction);
	};

	// Expose navigation to parent via callback
	useEffect(() => {
		// Handle keyboard input
		const handleKeyboard = (e: KeyboardEvent) => {
			if (e.key === "Escape") {
				// ESC closes modal
				if (isModalOpen) {
					setIsModalOpen(false);
				}
			} else if (e.key === "ArrowDown") {
				handleNavigate("down");
			} else if (e.key === "ArrowUp") {
				handleNavigate("up");
			}
		};

		window.addEventListener("keydown", handleKeyboard);
		return () => window.removeEventListener("keydown", handleKeyboard);
	}, [flights, isModalOpen]);

	// Loading State
	if (isLoading) {
		return (
			<div className="w-full bg-card backdrop-blur-sm rounded-xl border-2 border-border p-12">
				<div className="flex flex-col items-center justify-center">
					<div className="relative">
						<div className="animate-spin rounded-full h-20 w-20 border-4 border-primary border-t-transparent"></div>
						<div className="absolute inset-0 flex items-center justify-center text-4xl">
							✈️
						</div>
					</div>
					<p className="mt-6 text-xl text-foreground font-semibold">
						Loading flight data...
					</p>
					<p className="mt-2 text-sm text-muted-foreground">
						Fetching from OpenSky Network
					</p>
				</div>
			</div>
		);
	}

	// Error State
	if (error) {
		return (
			<div className="w-full bg-card backdrop-blur-sm rounded-xl border-2 border-destructive/50 p-8">
				<div className="text-center">
					<div className="text-6xl mb-4">❌</div>
					<h3 className="text-2xl font-bold text-destructive mb-2">
						Failed to Load Flight Data
					</h3>
					<p className="text-foreground mb-4">{error.message}</p>
					<button
						onClick={() => refetch()}
						className="bg-destructive hover:bg-destructive/90 text-white font-semibold px-6 py-3 rounded-lg transition-colors"
					>
						🔄 Retry
					</button>
				</div>
			</div>
		);
	}

	// Empty State
	if (!flights || flights.length === 0) {
		return (
			<div className="w-full bg-card backdrop-blur-sm rounded-xl border-2 border-border p-12">
				<div className="text-center">
					<div className="text-6xl mb-4">✈️</div>
					<h3 className="text-2xl font-bold text-foreground mb-2">
						No Flights in Area
					</h3>
					<p className="text-muted-foreground mb-4">
						No aircraft detected in the JFK area at this time
					</p>
					<button
						onClick={() => refetch()}
						className="bg-primary hover:bg-primary/90 text-primary-foreground font-semibold px-6 py-3 rounded-lg transition-colors"
					>
						🔄 Refresh
					</button>
				</div>
			</div>
		);
	}

	// Success State - Display Flights
	return (
		<div className="w-full">
			{/* Header */}
			<div className="mb-6 bg-card backdrop-blur-sm rounded-xl border-2 border-border p-4">
				<div className="flex justify-between items-center">
					<div>
						<h2 className="text-2xl font-bold text-foreground mb-1 flex items-center gap-2">
							<span>✈️</span>
							<span>Live Flights</span>
							{isFetching && (
								<span className="text-sm text-primary animate-pulse">
									(updating...)
								</span>
							)}
						</h2>
						<p className="text-sm text-muted-foreground">
							{flights.length} {flights.length === 1 ? "flight" : "flights"}{" "}
							detected near JFK
						</p>
					</div>

					<div className="text-right">
						<p className="text-xs text-muted-foreground">Last Updated</p>
						<p className="text-sm text-foreground font-mono">
							{dataUpdatedAt
								? new Date(dataUpdatedAt).toLocaleTimeString()
								: "Never"}
						</p>
						<button
							onClick={() => refetch()}
							className="mt-2 bg-primary hover:bg-primary/90 text-primary-foreground text-sm font-semibold px-4 py-2 rounded-lg transition-colors"
						>
							🔄 Refresh
						</button>
					</div>
				</div>

				{/* Navigation Hint */}
				<div className="mt-4 pt-4 border-t border-border flex flex-wrap items-center gap-4 text-xs text-muted-foreground">
					<div className="flex items-center gap-2">
						<kbd className="px-2 py-1 bg-secondary rounded border border-border">
							↑
						</kbd>
						<kbd className="px-2 py-1 bg-secondary rounded border border-border">
							↓
						</kbd>
						<span>Navigate</span>
					</div>
					<div className="flex items-center gap-2">
						<span className="text-primary">✋ Open Palm</span>
						<span>/</span>
						<span className="text-primary">✊ Closed Fist</span>
						<span>Navigate</span>
					</div>
					<div className="flex items-center gap-2">
						<span className="text-green-600 dark:text-green-400">
							👍 Thumbs Up
						</span>
						<span>View Details</span>
					</div>
					<div className="flex items-center gap-2">
						<span className="text-red-600 dark:text-red-400">
							👎 Thumbs Down
						</span>
						<span>Close Details</span>
					</div>
				</div>
			</div>

			{/* Flight Cards Grid */}
			<div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
				{flights.map((flight, index) => (
					<FlightCard
						key={flight.id}
						flight={flight}
						isSelected={index === selectedIndex}
						onClick={() => {
							setSelectedIndex(index);
							setIsModalOpen(true);
							onFlightSelect?.(flight.id);
						}}
					/>
				))}
			</div>

			{/* Flight Counter */}
			<div className="mt-6 text-center">
				<p className="text-sm text-muted-foreground">
					Showing flight {selectedIndex + 1} of {flights.length}
				</p>
			</div>

			{/* Flight Detail Modal */}
			<FlightDetailModal
				flight={flights[selectedIndex]}
				open={isModalOpen}
				onOpenChange={setIsModalOpen}
			/>
		</div>
	);
}
