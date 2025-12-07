import { useEffect, useState } from "react";

/**
 * Hook to detect window/tab focus state
 * Returns true when window has focus, false otherwise
 */
export function useWindowFocus() {
	const [hasFocus, setHasFocus] = useState(() => {
		// Check initial focus state (only on client side)
		if (typeof document !== "undefined") {
			return document.hasFocus();
		}
		return true;
	});

	useEffect(() => {
		const handleFocus = () => {
			console.debug("👁️ Window gained focus - resuming camera");
			setHasFocus(true);
		};

		const handleBlur = () => {
			console.debug("👁️ Window lost focus - pausing camera");
			setHasFocus(false);
		};

		// Listen for focus/blur events on window
		window.addEventListener("focus", handleFocus);
		window.addEventListener("blur", handleBlur);

		// Also listen for visibilitychange (handles tab switching)
		const handleVisibilityChange = () => {
			if (document.hidden) {
				console.debug("📑 Tab hidden - pausing camera");
				setHasFocus(false);
			} else {
				console.debug("📑 Tab visible - resuming camera");
				setHasFocus(true);
			}
		};

		document.addEventListener("visibilitychange", handleVisibilityChange);

		return () => {
			window.removeEventListener("focus", handleFocus);
			window.removeEventListener("blur", handleBlur);
			document.removeEventListener("visibilitychange", handleVisibilityChange);
		};
	}, []);

	return hasFocus;
}
