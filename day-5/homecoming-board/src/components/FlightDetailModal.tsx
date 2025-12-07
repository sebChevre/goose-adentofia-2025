import type { ProcessedFlight } from "../hooks/useFlightData";
import {
	Dialog,
	DialogContent,
	DialogDescription,
	DialogHeader,
	DialogTitle,
} from "./ui/dialog";
import {
	Drawer,
	DrawerContent,
	DrawerDescription,
	DrawerHeader,
	DrawerTitle,
	DrawerClose,
} from "./ui/drawer";
import { useEffect, useState } from "react";

interface FlightDetailModalProps {
	flight: ProcessedFlight | null;
	open: boolean;
	onOpenChange: (open: boolean) => void;
}

export function FlightDetailModal({
	flight,
	open,
	onOpenChange,
}: FlightDetailModalProps) {
	// Custom hook for media query
	function useMediaQuery(query: string) {
		const [matches, setMatches] = useState(false);
		useEffect(() => {
			const media = window.matchMedia(query);
			if (media.matches !== matches) {
				setMatches(media.matches);
			}
			const listener = () => setMatches(media.matches);
			media.addEventListener("change", listener);
			return () => media.removeEventListener("change", listener);
		}, [matches, query]);
		return matches;
	}

	const isMobile = useMediaQuery("(max-width: 640px)"); // Tailwind 'sm' breakpoint
	if (!flight) return null;

	// Render Drawer for mobile, Dialog for desktop
	if (isMobile) {
		const drawerContent = (
			<div className="grid gap-1 px-1">
				{/* Status Section */}
				<section aria-labelledby="status-heading">
					<h3 id="status-heading" className="sr-only">
						Status
					</h3>
					<div className="text-center">
						<span className="text-sm text-muted-foreground">
							Last contact:{" "}
							<time dateTime={flight.lastContact.toISOString()}>
								{flight.lastContact.toLocaleString()}
							</time>
						</span>
					</div>
				</section>

				{/* Flight Parameters Grid */}
				<section aria-labelledby="parameters-heading">
					<h2 id="parameters-heading" className="sr-only">
						Flight Parameters
					</h2>
					<div className="grid grid-cols-2 gap-1">
						<div className="bg-secondary rounded-lg p-4 border border-border">
							<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
								<span role="img" aria-label="Altitude">
									📏
								</span>
								<span>Altitude</span>
							</p>
							<p className="text-2xl font-bold text-foreground">
								{flight.altitude !== null
									? `${Math.round(flight.altitude).toLocaleString()}m`
									: "N/A"}
							</p>
							{flight.altitude !== null && (
								<p className="text-xs text-muted-foreground/70 mt-1">
									{Math.round(flight.altitude * 3.28084).toLocaleString()} ft
								</p>
							)}
						</div>

						<div className="bg-secondary rounded-lg p-4 border border-border">
							<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
								<span role="img" aria-label="Speed">
									⚡
								</span>
								<span>Speed</span>
							</p>
							<p className="text-2xl font-bold text-foreground">
								{flight.velocity !== null
									? `${Math.round(flight.velocity * 3.6)} km/h`
									: "N/A"}
							</p>
							{flight.velocity !== null && (
								<p className="text-xs text-muted-foreground/70 mt-1">
									{Math.round(flight.velocity * 1.94384)} knots
								</p>
							)}
						</div>

						<div className="bg-secondary rounded-lg p-4 border border-border">
							<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
								<span role="img" aria-label="Heading">
									🧭
								</span>
								<span>Heading</span>
							</p>
							<p className="text-2xl font-bold text-foreground">
								{flight.heading !== null
									? `${Math.round(flight.heading)}°`
									: "N/A"}
							</p>
							{flight.heading !== null && (
								<p className="text-xs text-muted-foreground/70 mt-1">
									{getCardinalDirection(flight.heading)}
								</p>
							)}
						</div>

						<div className="bg-secondary rounded-lg p-4 border border-border">
							<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
								<span role="img" aria-label="Country">
									🌍
								</span>
								<span>Country</span>
							</p>
							<p className="text-xl font-bold text-foreground truncate">
								{flight.country}
							</p>
						</div>
					</div>
				</section>

				{/* Position Information */}
				{flight.position && (
					<section
						className="bg-secondary rounded-lg p-4 border border-border"
						aria-labelledby="position-heading"
					>
						<h3
							id="position-heading"
							className="text-sm font-semibold text-foreground mb-3 flex items-center gap-2"
						>
							<span role="img" aria-label="Position">
								📍
							</span>
							<span>Position</span>
						</h3>
						<div className="space-y-2">
							<div className="flex justify-between items-center">
								<span className="text-sm text-muted-foreground">Latitude</span>
								<span className="text-sm font-mono text-primary">
									{flight.position.lat.toFixed(6)}°
								</span>
							</div>
							<div className="flex justify-between items-center">
								<span className="text-sm text-muted-foreground">Longitude</span>
								<span className="text-sm font-mono text-primary">
									{flight.position.lng.toFixed(6)}°
								</span>
							</div>
						</div>
					</section>
				)}

				{/* Technical Information */}
				<section
					className="bg-secondary rounded-lg p-4 border border-border"
					aria-labelledby="technical-heading"
				>
					<h3
						id="technical-heading"
						className="text-sm font-semibold text-foreground mb-3"
					>
						Technical Info
					</h3>
					<div className="space-y-2">
						<div className="flex justify-between items-center">
							<span className="text-sm text-muted-foreground">ICAO24 ID</span>
							<span className="text-sm font-mono text-foreground">
								{flight.id}
							</span>
						</div>
						<div className="flex justify-between items-center">
							<span className="text-sm text-muted-foreground">Callsign</span>
							<span className="text-sm font-mono text-foreground">
								{flight.callsign}
							</span>
						</div>
					</div>
				</section>
			</div>
		);

		return (
			<Drawer open={open} onOpenChange={onOpenChange}>
				<DrawerContent className="bg-card border-2 border-primary/30 shadow-2xl shadow-primary/20">
					<DrawerHeader>
						<div className="flex items-center justify-between gap-1">
							<DrawerTitle className="text-3xl font-bold text-primary">
								{flight.callsign}
							</DrawerTitle>
							<div
								className={`
              px-4 py-2 rounded-full text-sm font-semibold uppercase tracking-wide
              ${
								flight.onGround
									? "bg-green-100 dark:bg-green-700/60 text-green-700 dark:text-green-200 border border-green-300 dark:border-green-600/70"
									: "bg-blue-100 dark:bg-blue-700/60 text-blue-700 dark:text-blue-200 border border-blue-300 dark:border-blue-600/70"
							}
            `}
								role="status"
								aria-label={`Flight status: ${flight.status}`}
							>
								{flight.status}
							</div>
						</div>
						<DrawerDescription>
							Flight Details • {flight.country}
						</DrawerDescription>
					</DrawerHeader>
					{drawerContent}
					<DrawerClose className="mt-4">Close</DrawerClose>
				</DrawerContent>
			</Drawer>
		);
	}

	const modalContent = (
		<>
			{/* Status Section */}
			<section
				className="bg-secondary rounded-lg p-4 border border-border"
				aria-labelledby="status-heading"
			>
				<h3
					id="status-heading"
					className="text-sm font-semibold text-foreground mb-3"
				>
					Status
				</h3>
				<div className="flex items-center gap-3">
					<div
						className={`
              px-4 py-2 rounded-full text-sm font-semibold uppercase tracking-wide
              ${
								flight.onGround
									? "bg-green-100 dark:bg-green-700/60 text-green-700 dark:text-green-200 border border-green-300 dark:border-green-600/70"
									: "bg-blue-100 dark:bg-blue-700/60 text-blue-700 dark:text-blue-200 border border-blue-300 dark:border-blue-600/70"
							}
            `}
						role="status"
						aria-label={`Flight status: ${flight.status}`}
					>
						{flight.status}
					</div>
					<span className="text-sm text-muted-foreground">
						Last contact:{" "}
						<time dateTime={flight.lastContact.toISOString()}>
							{flight.lastContact.toLocaleString()}
						</time>
					</span>
				</div>
			</section>

			{/* Flight Parameters Grid */}
			<section aria-labelledby="parameters-heading">
				<h2 id="parameters-heading" className="sr-only">
					Flight Parameters
				</h2>
				<div className="grid grid-cols-2 gap-4">
					<div className="bg-secondary rounded-lg p-4 border border-border">
						<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
							<span role="img" aria-label="Altitude">
								📏
							</span>
							<span>Altitude</span>
						</p>
						<p className="text-2xl font-bold text-foreground">
							{flight.altitude !== null
								? `${Math.round(flight.altitude).toLocaleString()}m`
								: "N/A"}
						</p>
						{flight.altitude !== null && (
							<p className="text-xs text-muted-foreground/70 mt-1">
								{Math.round(flight.altitude * 3.28084).toLocaleString()} ft
							</p>
						)}
					</div>

					<div className="bg-secondary rounded-lg p-4 border border-border">
						<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
							<span role="img" aria-label="Speed">
								⚡
							</span>
							<span>Speed</span>
						</p>
						<p className="text-2xl font-bold text-foreground">
							{flight.velocity !== null
								? `${Math.round(flight.velocity * 3.6)} km/h`
								: "N/A"}
						</p>
						{flight.velocity !== null && (
							<p className="text-xs text-muted-foreground/70 mt-1">
								{Math.round(flight.velocity * 1.94384)} knots
							</p>
						)}
					</div>

					<div className="bg-secondary rounded-lg p-4 border border-border">
						<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
							<span role="img" aria-label="Heading">
								🧭
							</span>
							<span>Heading</span>
						</p>
						<p className="text-2xl font-bold text-foreground">
							{flight.heading !== null
								? `${Math.round(flight.heading)}°`
								: "N/A"}
						</p>
						{flight.heading !== null && (
							<p className="text-xs text-muted-foreground/70 mt-1">
								{getCardinalDirection(flight.heading)}
							</p>
						)}
					</div>

					<div className="bg-secondary rounded-lg p-4 border border-border">
						<p className="text-xs text-muted-foreground mb-2 flex items-center gap-2">
							<span role="img" aria-label="Country">
								🌍
							</span>
							<span>Country</span>
						</p>
						<p className="text-xl font-bold text-foreground truncate">
							{flight.country}
						</p>
					</div>
				</div>
			</section>

			{/* Position Information */}
			{flight.position && (
				<section
					className="bg-secondary rounded-lg p-4 border border-border"
					aria-labelledby="position-heading"
				>
					<h3
						id="position-heading"
						className="text-sm font-semibold text-foreground mb-3 flex items-center gap-2"
					>
						<span role="img" aria-label="Position">
							📍
						</span>
						<span>Position</span>
					</h3>
					<div className="space-y-2">
						<div className="flex justify-between items-center">
							<span className="text-sm text-muted-foreground">Latitude</span>
							<span className="text-sm font-mono text-primary">
								{flight.position.lat.toFixed(6)}°
							</span>
						</div>
						<div className="flex justify-between items-center">
							<span className="text-sm text-muted-foreground">Longitude</span>
							<span className="text-sm font-mono text-primary">
								{flight.position.lng.toFixed(6)}°
							</span>
						</div>
					</div>
				</section>
			)}

			{/* Technical Information */}
			<section
				className="bg-secondary rounded-lg p-4 border border-border"
				aria-labelledby="technical-heading"
			>
				<h3
					id="technical-heading"
					className="text-sm font-semibold text-foreground mb-3"
				>
					Technical Info
				</h3>
				<div className="space-y-2">
					<div className="flex justify-between items-center">
						<span className="text-sm text-muted-foreground">ICAO24 ID</span>
						<span className="text-sm font-mono text-foreground">
							{flight.id}
						</span>
					</div>
					<div className="flex justify-between items-center">
						<span className="text-sm text-muted-foreground">Callsign</span>
						<span className="text-sm font-mono text-foreground">
							{flight.callsign}
						</span>
					</div>
				</div>
			</section>

			{/* Winter decoration */}
			<div
				className="text-center text-2xl opacity-20 pointer-events-none select-none"
				aria-hidden="true"
			>
				❄️ ❄️ ❄️
			</div>
		</>
	);

	return (
		<Dialog open={open} onOpenChange={onOpenChange}>
			<DialogContent
				className="sm:max-w-2xl bg-card border-2 border-primary/30 shadow-2xl shadow-primary/20"
				aria-describedby="flight-details-description"
			>
				<DialogHeader>
					<div className="flex items-center justify-between">
						<DialogTitle className="text-3xl font-bold text-primary">
							{flight.callsign}
						</DialogTitle>
						<span
							className="text-4xl"
							role="img"
							aria-label={
								flight.onGround ? "Aircraft landed" : "Aircraft in flight"
							}
						>
							{flight.onGround ? "🛬" : "✈️"}
						</span>
					</div>
					<DialogDescription
						id="flight-details-description"
						className="text-muted-foreground"
					>
						Flight Details • {flight.country}
					</DialogDescription>
				</DialogHeader>
				{modalContent}
			</DialogContent>
		</Dialog>
	);
}

/**
 * Helper function to convert heading degrees to cardinal direction
 */
function getCardinalDirection(degrees: number): string {
	const directions = [
		"N",
		"NNE",
		"NE",
		"ENE",
		"E",
		"ESE",
		"SE",
		"SSE",
		"S",
		"SSW",
		"SW",
		"WSW",
		"W",
		"WNW",
		"NW",
		"NNW",
	];
	const index = Math.round(degrees / 22.5) % 16;
	return directions[index];
}
