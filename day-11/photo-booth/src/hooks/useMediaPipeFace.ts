import { useEffect, useRef, useState } from "react";
import { FaceLandmarker, FilesetResolver } from "@mediapipe/tasks-vision";
import type { FaceResults, FaceTrackerConfig } from "../types/detection";
import { DEFAULT_FACE_CONFIG } from "../types/detection";

interface UseMediaPipeFaceOptions {
	config?: Partial<FaceTrackerConfig>;
	onResults?: (results: FaceResults) => void;
}

interface UseMediaPipeFaceReturn {
	canvasRef: React.RefObject<HTMLCanvasElement | null>;
	results: FaceResults | null;
	isReady: boolean;
	error: Error | null;
	fps: number;
}

export function useMediaPipeFace(
	videoElement: HTMLVideoElement | null,
	options: UseMediaPipeFaceOptions = {},
): UseMediaPipeFaceReturn {
	const canvasRef = useRef<HTMLCanvasElement>(null);
	const faceLandmarkerRef = useRef<FaceLandmarker | null>(null);
	const animationFrameIdRef = useRef<number>(0);

	const [results, setResults] = useState<FaceResults | null>(null);
	const [isReady, setIsReady] = useState(false);
	const [error, setError] = useState<Error | null>(null);
	const [fps, setFps] = useState(0);

	const lastFrameTimeRef = useRef<number>(0);
	const frameCountRef = useRef(0);
	const fpsUpdateIntervalRef = useRef<number>(0);
	const lastFaceCountRef = useRef<number>(0);
	const resultsRef = useRef<FaceResults | null>(null);

	useEffect(() => {
		if (typeof window === "undefined" || !videoElement) {
			return;
		}

		setIsReady(false);
		setResults(null);
		setFps(0);
		frameCountRef.current = 0;
		lastFrameTimeRef.current = 0;
		fpsUpdateIntervalRef.current = 0;

		let cancelled = false;

		const initializeFaceDetection = async () => {
			try {
				setError(null);
				// Load WASM fileset and face landmarker
				const filesetResolver = await FilesetResolver.forVisionTasks(
					"https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm",
				);
				const faceLandmarker = await FaceLandmarker.createFromOptions(
					filesetResolver,
					{
						baseOptions: {
							modelAssetPath:
								"https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task",
							delegate: "GPU",
						},
						numFaces:
							options.config?.maxNumFaces || DEFAULT_FACE_CONFIG.maxNumFaces,
						runningMode: "VIDEO",
						outputFaceBlendshapes: false,
						outputFacialTransformationMatrixes: false,
					},
				);
				faceLandmarkerRef.current = faceLandmarker;
				setIsReady(true);

				const processFrame = () => {
					if (
						!faceLandmarkerRef.current ||
						!videoElement ||
						videoElement.readyState < 2
					) {
						animationFrameIdRef.current = requestAnimationFrame(processFrame);
						return;
					}
					try {
						const now = performance.now();
						const faces = faceLandmarkerRef.current.detectForVideo(
							videoElement,
							now,
						);

						if (lastFrameTimeRef.current > 0) {
							frameCountRef.current++;
							if (now - fpsUpdateIntervalRef.current > 1000) {
								setFps(frameCountRef.current);
								frameCountRef.current = 0;
								fpsUpdateIntervalRef.current = now;
							}
						} else {
							fpsUpdateIntervalRef.current = now;
						}
						lastFrameTimeRef.current = now;

						const faceResults: FaceResults = {
							faceLandmarks: faces.faceLandmarks,
							faceBlendshapes: faces.faceBlendshapes,
							facialTransformationMatrixes: faces.facialTransformationMatrixes,
						};
						resultsRef.current = faceResults;
						const currentFaceCount = faces.faceLandmarks.length;
						if (currentFaceCount !== lastFaceCountRef.current) {
							lastFaceCountRef.current = currentFaceCount;
							setResults(faceResults);
						}
						if (options.onResults) {
							options.onResults(resultsRef.current);
						}
						if (canvasRef.current) {
							if (faces.faceLandmarks.length > 0) {
								drawResultsMP(
									canvasRef.current,
									videoElement,
									faces.faceLandmarks,
								);
							} else {
								clearCanvas(canvasRef.current);
							}
						}
					} catch (err) {
						// Frame error
					}
					if (!cancelled) {
						animationFrameIdRef.current = requestAnimationFrame(processFrame);
					}
				};
				processFrame();
			} catch (err) {
				setError(
					err instanceof Error
						? err
						: new Error("Failed to initialize WASM face detection"),
				);
			}
		};
		initializeFaceDetection();
		return () => {
			cancelled = true;
			if (animationFrameIdRef.current) {
				cancelAnimationFrame(animationFrameIdRef.current);
				animationFrameIdRef.current = 0;
			}
			if (faceLandmarkerRef.current) {
				faceLandmarkerRef.current.close();
				faceLandmarkerRef.current = null;
			}
			if (canvasRef.current) {
				clearCanvas(canvasRef.current);
			}
		};
	}, [videoElement, options.config?.maxNumFaces]);

	return {
		canvasRef,
		results,
		isReady,
		error,
		fps,
	};
}

function clearCanvas(canvas: HTMLCanvasElement) {
	const ctx = canvas.getContext("2d");
	if (!ctx) return;
	ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function drawResultsMP(
	canvas: HTMLCanvasElement,
	video: HTMLVideoElement,
	landmarks: any[][],
) {
	const ctx = canvas.getContext("2d");
	if (!ctx) return;
	canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	for (const face of landmarks) {
		drawFaceConnectionsMP(ctx, face);
		// Draw key landmarks
		for (const keypoint of face) {
			const x = keypoint.x * canvas.width;
			const y = keypoint.y * canvas.height;
			if (x == null || y == null || isNaN(x) || isNaN(y)) continue;
			ctx.beginPath();
			ctx.arc(x, y, 2, 0, 2 * Math.PI);
			ctx.fillStyle = "#00FF00";
			ctx.fill();
		}
	}
}

function drawFaceConnectionsMP(ctx: CanvasRenderingContext2D, keypoints: any[]) {
	// MediaPipe Face Landmarker provides 478 landmarks
	// We'll draw key connections for the face mesh
	const connections = [
		// Face oval
		[10, 338],
		[338, 297],
		[297, 332],
		[332, 284],
		[284, 251],
		[251, 389],
		[389, 356],
		[356, 454],
		[454, 323],
		[323, 361],
		[361, 288],
		[288, 397],
		[397, 365],
		[365, 379],
		[379, 378],
		[378, 400],
		[400, 377],
		[377, 152],
		[152, 148],
		[148, 176],
		[176, 149],
		[149, 150],
		[150, 136],
		[136, 172],
		[172, 58],
		[58, 132],
		[132, 93],
		[93, 234],
		[234, 127],
		[127, 162],
		[162, 21],
		[21, 54],
		[54, 103],
		[103, 67],
		[67, 109],
		[109, 10],
		// Left eye
		[33, 133],
		[133, 160],
		[160, 159],
		[159, 158],
		[158, 157],
		[157, 173],
		[173, 33],
		// Right eye
		[362, 263],
		[263, 387],
		[387, 386],
		[386, 385],
		[385, 384],
		[384, 398],
		[398, 362],
		// Lips outer
		[61, 146],
		[146, 91],
		[91, 181],
		[181, 84],
		[84, 17],
		[17, 314],
		[314, 405],
		[405, 321],
		[321, 375],
		[375, 291],
		[291, 61],
	];

	ctx.strokeStyle = "#00FF00";
	ctx.lineWidth = 1;
	for (const [startIdx, endIdx] of connections) {
		const start = keypoints[startIdx];
		const end = keypoints[endIdx];
		if (!start || !end) continue;
		ctx.beginPath();
		ctx.moveTo(start.x * ctx.canvas.width, start.y * ctx.canvas.height);
		ctx.lineTo(end.x * ctx.canvas.width, end.y * ctx.canvas.height);
		ctx.stroke();
	}
}
