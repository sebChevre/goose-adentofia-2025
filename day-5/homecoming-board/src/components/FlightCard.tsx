import { useRef, useEffect } from "react";
import type { ProcessedFlight } from "../hooks/useFlightData";

interface FlightCardProps {
	flight: ProcessedFlight;
	isSelected?: boolean;
	onClick?: () => void;
}

export function FlightCard({
	flight,
	isSelected = false,
	onClick,
}: FlightCardProps) {
	const cardRef = useRef<HTMLDivElement>(null);

	// Scroll into view when the card becomes selected
	useEffect(() => {
		if (isSelected && cardRef.current) {
			cardRef.current.scrollIntoView({
				behavior: "smooth",
				block: "nearest",
				inline: "nearest",
			});
		}
	}, [isSelected]);

	return (
		<div
			ref={cardRef}
			onClick={onClick}
			className={`
        relative overflow-hidden
        bg-card
        backdrop-blur-sm
        border-2 rounded-xl p-6
        transition-all duration-300 ease-in-out
        cursor-pointer
        ${
					isSelected
						? "border-primary shadow-lg shadow-primary/50 scale-105"
						: "border-border hover:border-primary hover:shadow-lg hover:shadow-primary/30"
				}
        ${onClick ? "hover:scale-102" : ""}
      `}
		>
			{/* Winter decoration - snowflakes */}
			<div className="absolute top-2 right-2 text-primary/20 text-2xl">❄️</div>

			{/* Header */}
			<div className="flex justify-between items-start mb-4">
				<div>
					<h3 className="text-2xl font-bold text-primary mb-1">
						{flight.callsign}
					</h3>
					<p className="text-sm text-muted-foreground flex items-center gap-2">
						<span>🌍</span>
						<span>{flight.country}</span>
					</p>
				</div>

				{/* Status Badge */}
				<div
					className={`
            px-3 py-1.5 rounded-full text-xs font-semibold uppercase tracking-wide
            flex items-center gap-1.5
            ${
							flight.onGround
								? "bg-green-100 dark:bg-green-900/50 text-green-700 dark:text-green-300 border border-green-300 dark:border-green-700/50"
								: "bg-blue-100 dark:bg-blue-900/50 text-blue-700 dark:text-blue-300 border border-blue-300 dark:border-blue-700/50"
						}
          `}
				>
					<span className="text-base">{flight.onGround ? "🛬" : "✈️"}</span>
					<span>{flight.status}</span>
				</div>
			</div>

			{/* Flight Details Grid */}
			<div className="grid grid-cols-2 gap-4 mb-4">
				<div className="bg-secondary rounded-lg p-3 border border-border">
					<p className="text-xs text-muted-foreground mb-1">Altitude</p>
					<p className="text-lg font-semibold text-foreground">
						{flight.altitude !== null
							? `${Math.round(flight.altitude).toLocaleString()}m`
							: "N/A"}
					</p>
				</div>

				<div className="bg-secondary rounded-lg p-3 border border-border">
					<p className="text-xs text-muted-foreground mb-1">Speed</p>
					<p className="text-lg font-semibold text-foreground">
						{flight.velocity !== null
							? `${Math.round(flight.velocity * 3.6)} km/h`
							: "N/A"}
					</p>
				</div>
			</div>

			{/* Additional Info */}
			<div className="flex justify-between items-center text-sm">
				<div>
					<p className="text-muted-foreground">Heading</p>
					<p className="font-semibold text-foreground">
						{flight.heading !== null ? `${Math.round(flight.heading)}°` : "N/A"}
					</p>
				</div>

				<div className="text-right">
					<p className="text-muted-foreground">Last Contact</p>
					<p className="font-semibold text-foreground">
						{flight.lastContact.toLocaleTimeString()}
					</p>
				</div>
			</div>

			{/* Position Info (optional detailed view) */}
			{isSelected && flight.position && (
				<div className="mt-4 pt-4 border-t border-border">
					<p className="text-xs text-muted-foreground mb-1">📍 Position</p>
					<p className="text-xs font-mono text-primary">
						{flight.position.lat.toFixed(4)}°, {flight.position.lng.toFixed(4)}°
					</p>
					<p className="text-xs text-muted-foreground/70 mt-1">
						ID: {flight.id}
					</p>
				</div>
			)}

			{/* Selection indicator */}
			{isSelected && (
				<div className="absolute inset-0 border-2 border-primary rounded-xl pointer-events-none animate-pulse" />
			)}
		</div>
	);
}
