import { useEffect, useRef, useState } from 'react';
import { HandLandmarker, FilesetResolver } from '@mediapipe/tasks-vision';
import type { HandResults, HandTrackerConfig } from '../types/hand';
import { DEFAULT_HAND_CONFIG } from '../types/hand';


interface UseMediaPipeOptions {
  config?: Partial<HandTrackerConfig>;
  onResults?: (results: HandResults) => void;
}


interface UseMediaPipeReturn {
  canvasRef: React.RefObject<HTMLCanvasElement | null>;
  results: HandResults | null;
  isReady: boolean;
  error: Error | null;
  fps: number;
}


export function useMediaPipe(
  videoElement: HTMLVideoElement | null,
  options: UseMediaPipeOptions = {}
): UseMediaPipeReturn {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const handLandmarkerRef = useRef<HandLandmarker | null>(null);
  const animationFrameIdRef = useRef<number>(0);

  const [results, setResults] = useState<HandResults | null>(null);
  const [isReady, setIsReady] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [fps, setFps] = useState(0);

  const lastFrameTimeRef = useRef<number>(0);
  const frameCountRef = useRef(0);
  const fpsUpdateIntervalRef = useRef<number>(0);
  const lastHandCountRef = useRef<number>(0);
  const resultsRef = useRef<HandResults | null>(null);

  useEffect(() => {
    if (typeof window === 'undefined' || !videoElement) {
      return;
    }

    setIsReady(false);
    setResults(null);
    setFps(0);
    frameCountRef.current = 0;
    lastFrameTimeRef.current = 0;
    fpsUpdateIntervalRef.current = 0;

    let cancelled = false;

    const initializeHandDetection = async () => {
      try {
        setError(null);
        // Load WASM fileset and hand landmarker
        const filesetResolver = await FilesetResolver.forVisionTasks(
          'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm'
        );
        const handLandmarker = await HandLandmarker.createFromOptions(filesetResolver, {
          baseOptions: {
            modelAssetPath: 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task',
            delegate: 'wasm',
          },
          numHands: options.config?.maxNumHands || DEFAULT_HAND_CONFIG.maxNumHands,
        });
        handLandmarkerRef.current = handLandmarker;
        setIsReady(true);

        const processFrame = () => {
          if (!handLandmarkerRef.current || !videoElement || videoElement.readyState < 2) {
            animationFrameIdRef.current = requestAnimationFrame(processFrame);
            return;
          }
          try {
            const hands = handLandmarkerRef.current.detect(videoElement);
            const now = performance.now();
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

            const handResults: HandResults = {
              multiHandLandmarks: hands.landmarks,
              multiHandedness: hands.handedness.map((h: any) => ({
                label: h[0].categoryName || 'Unknown',
                score: h[0].score || 0,
              })),
            };
            resultsRef.current = handResults;
            const currentHandCount = hands.landmarks.length;
            if (currentHandCount !== lastHandCountRef.current) {
              lastHandCountRef.current = currentHandCount;
              setResults(handResults);
            }
            if (options.onResults) {
              options.onResults(resultsRef.current);
            }
            if (canvasRef.current) {
              if (hands.landmarks.length > 0) {
                drawResultsMP(canvasRef.current, videoElement, hands.landmarks);
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
        setError(err instanceof Error ? err : new Error('Failed to initialize WASM hand detection'));
      }
    };
    initializeHandDetection();
    return () => {
      cancelled = true;
      if (animationFrameIdRef.current) {
        cancelAnimationFrame(animationFrameIdRef.current);
        animationFrameIdRef.current = 0;
      }
      if (handLandmarkerRef.current) {
        handLandmarkerRef.current.close();
        handLandmarkerRef.current = null;
      }
      if (canvasRef.current) {
        clearCanvas(canvasRef.current);
      }
    };
  }, [videoElement, options.config?.maxNumHands]);

  return {
    canvasRef,
    results,
    isReady,
    error,
    fps,
  };
}


function clearCanvas(canvas: HTMLCanvasElement) {
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function drawResultsMP(canvas: HTMLCanvasElement, video: HTMLVideoElement, landmarks: any[][]) {
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (const hand of landmarks) {
    drawConnectionsMP(ctx, hand);
    for (const keypoint of hand) {
      const x = keypoint.x * canvas.width;
      const y = keypoint.y * canvas.height;
      if (x == null || y == null || isNaN(x) || isNaN(y)) continue;
      ctx.beginPath();
      ctx.arc(x, y, 5, 0, 2 * Math.PI);
      ctx.fillStyle = '#00FF00';
      ctx.fill();
      ctx.strokeStyle = '#FFFFFF';
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  }
}

function drawConnectionsMP(ctx: CanvasRenderingContext2D, keypoints: any[]) {
  const connections = [
    [0, 1], [1, 2], [2, 3], [3, 4],
    [0, 5], [5, 6], [6, 7], [7, 8],
    [0, 9], [9, 10], [10, 11], [11, 12],
    [0, 13], [13, 14], [14, 15], [15, 16],
    [0, 17], [17, 18], [18, 19], [19, 20],
    [5, 9], [9, 13], [13, 17],
  ];
  ctx.strokeStyle = '#00FF00';
  ctx.lineWidth = 2;
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
