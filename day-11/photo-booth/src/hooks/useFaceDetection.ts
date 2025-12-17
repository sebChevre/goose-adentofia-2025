import { useState, useEffect, useCallback, useRef } from 'react';
import type {
  FaceDetectionState,
  FaceDetectionOptions
} from '../types/detection';
import type { CoordinateSystem } from '../types/camera';
import type { DetectedFace } from '../types/filters';
import { FaceDetector, FilesetResolver } from '@mediapipe/tasks-vision';

export interface UseFaceDetectionResult {
  state: FaceDetectionState;
  detectedFaces: DetectedFace[];
  actions: {
    startDetection: () => void;
    stopDetection: () => void;
    toggleDebug: () => void;
    updateOptions: (options: Partial<FaceDetectionOptions>) => void;
  };
  debug: {
    drawBoundingBoxes: (canvas: HTMLCanvasElement, coordinateSystem: CoordinateSystem) => void;
    drawKeypoints: (canvas: HTMLCanvasElement, coordinateSystem: CoordinateSystem) => void;
  };
}

interface MediaPipeFaceResults {
  detections: Array<{
    boundingBox: {
      originX: number;
      originY: number;
      width: number;
      height: number;
    };
    keypoints: Array<{
      x: number;
      y: number;
      score?: number;
    }>;
    categories: Array<{
      score: number;
      categoryName?: string;
    }>;
  }>;
}

export function useFaceDetection(
  videoRef: React.RefObject<HTMLVideoElement | null>,
  coordinateSystem: CoordinateSystem | null
): UseFaceDetectionResult {
  const [state, setState] = useState<FaceDetectionState>({
    isModelLoaded: false,
    isDetecting: false,
    lastResult: null,
    error: null,
    modelLoadProgress: 0
  });

  const [detectedFaces, setDetectedFaces] = useState<DetectedFace[]>([]);
  const faceDetectorRef = useRef<FaceDetector | null>(null);
  const animationFrameRef = useRef<number>();
  const lastFrameTimeRef = useRef<number>(0);

  const updateState = useCallback((updates: Partial<FaceDetectionState>) => {
    setState(prev => ({ ...prev, ...updates }));
  }, []);

  // Initialize MediaPipe Face Detection
  useEffect(() => {
    let cancelled = false;

    const initializeFaceDetection = async () => {
      try {
        updateState({ modelLoadProgress: 20 });

        // Load WASM fileset for vision tasks
        const filesetResolver = await FilesetResolver.forVisionTasks(
          "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
        );

        updateState({ modelLoadProgress: 40 });

        // Create face detector with options
        const faceDetector = await FaceDetector.createFromOptions(filesetResolver, {
          baseOptions: {
            modelAssetPath: 'https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite',
            delegate: "GPU"
          },
          runningMode: "VIDEO",
          minDetectionConfidence: 0.5,
          minSuppressionThreshold: 0.3
        });

        updateState({ modelLoadProgress: 80 });

        if (cancelled) {
          faceDetector.close();
          return;
        }

        faceDetectorRef.current = faceDetector;
        updateState({
          isModelLoaded: true,
          modelLoadProgress: 100,
          error: null
        });

        console.log('✅ Face detection initialized');

      } catch (error) {
        console.error('❌ Face detection initialization failed:', error);
        if (!cancelled) {
          updateState({
            error: error instanceof Error ? error.message : 'Failed to initialize face detection',
            modelLoadProgress: 0
          });
        }
      }
    };

    initializeFaceDetection();

    return () => {
      cancelled = true;
      if (faceDetectorRef.current) {
        faceDetectorRef.current.close();
        faceDetectorRef.current = null;
      }
    };
  }, [updateState]);

  const detectFaces = useCallback(() => {
    const video = videoRef.current;
    const faceDetector = faceDetectorRef.current;

    if (!video || !faceDetector || !state.isDetecting || !coordinateSystem) {
      console.log('🚫 Face detection skipped:', { 
        hasVideo: !!video, 
        hasFaceDetector: !!faceDetector, 
        isDetecting: state.isDetecting, 
        hasCoordinateSystem: !!coordinateSystem 
      });
      if (state.isDetecting) {
        animationFrameRef.current = requestAnimationFrame(detectFaces);
      }
      return;
    }

    if (video.readyState === 4) {
      try {
        const now = performance.now();

        // Detect faces in the video frame
        const detections = faceDetector.detectForVideo(video, now);

        if (detections.detections && detections.detections.length > 0) {
          console.log(`🎯 Found ${detections.detections.length} face(s)`);
          const faces: DetectedFace[] = detections.detections.map(detection => {
            // MediaPipe uses normalized coordinates (0-1)
            const bbox = detection.boundingBox;

            // Extract keypoints if available
            // MediaPipe FaceDetector provides 6 keypoints:
            // 0: right eye, 1: left eye, 2: nose tip, 3: mouth center, 4: right eye tragion, 5: left eye tragion
            let landmarks = undefined;
            if (detection.keypoints && detection.keypoints.length >= 4) {
              const kp = detection.keypoints;
              landmarks = {
                rightEye: { x: kp[0].x, y: kp[0].y },
                leftEye: { x: kp[1].x, y: kp[1].y },
                nose: { x: kp[2].x, y: kp[2].y },
                mouth: { x: kp[3].x, y: kp[3].y },
                // Estimate chin and forehead based on bounding box
                chin: { x: bbox.originX + bbox.width / 2, y: bbox.originY + bbox.height },
                forehead: { x: bbox.originX + bbox.width / 2, y: bbox.originY }
              };
            }

            return {
              boundingBox: {
                x: bbox.originX,
                y: bbox.originY,
                width: bbox.width,
                height: bbox.height
              },
              landmarks,
              confidence: detection.categories[0]?.score || 0.5
            };
          });

          setDetectedFaces(faces);
        } else {
          setDetectedFaces([]);
        }

        lastFrameTimeRef.current = now;
      } catch (error) {
        console.error('Face detection error:', error);
      }
    }

    if (state.isDetecting) {
      animationFrameRef.current = requestAnimationFrame(detectFaces);
    }
  }, [videoRef, state.isDetecting, coordinateSystem]);

  const startDetection = useCallback(() => {
    if (!state.isModelLoaded) {
      console.warn('Face detection model not loaded yet');
      return;
    }
    
    updateState({ isDetecting: true, error: null });
    detectFaces();
    console.log('👁️ Face detection started');
  }, [state.isModelLoaded, updateState, detectFaces]);

  const stopDetection = useCallback(() => {
    updateState({ isDetecting: false });
    if (animationFrameRef.current) {
      cancelAnimationFrame(animationFrameRef.current);
    }
    console.log('👁️ Face detection stopped');
  }, [updateState]);

  const toggleDebug = useCallback(() => {
    // Mock debug toggle - could implement debug overlay
  }, []);

  const updateOptions = useCallback(async (newOptions: Partial<FaceDetectionOptions>) => {
    const faceDetector = faceDetectorRef.current;
    if (!faceDetector) return;

    try {
      faceDetector.setOptions({
        minDetectionConfidence: newOptions.minDetectionConfidence || 0.5,
        minSuppressionThreshold: newOptions.minTrackingConfidence || 0.3
      });
      console.log('Updated face detection options:', newOptions);
    } catch (error) {
      console.error('Failed to update options:', error);
    }
  }, []);

  const drawBoundingBoxes = useCallback((
    canvas: HTMLCanvasElement, 
    coordinateSystem: CoordinateSystem
  ) => {
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.save();
    ctx.strokeStyle = '#00ff00';
    ctx.lineWidth = 2;
    
    detectedFaces.forEach(face => {
      const x = face.boundingBox.x * coordinateSystem.canvas.width;
      const y = face.boundingBox.y * coordinateSystem.canvas.height;
      const width = face.boundingBox.width * coordinateSystem.canvas.width;
      const height = face.boundingBox.height * coordinateSystem.canvas.height;
      
      ctx.strokeRect(x, y, width, height);
      
      // Draw confidence
      ctx.fillStyle = '#00ff00';
      ctx.font = '14px Arial';
      ctx.fillText(`${(face.confidence * 100).toFixed(0)}%`, x, y - 5);
    });
    
    ctx.restore();
  }, [detectedFaces]);

  const drawKeypoints = useCallback((
    canvas: HTMLCanvasElement,
    coordinateSystem: CoordinateSystem
  ) => {
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.save();
    ctx.fillStyle = '#ff0000';

    detectedFaces.forEach(face => {
      if (!face.landmarks) return;

      // Draw facial landmark points
      Object.entries(face.landmarks).forEach(([key, point]) => {
        const x = point.x * coordinateSystem.canvas.width;
        const y = point.y * coordinateSystem.canvas.height;

        ctx.beginPath();
        ctx.arc(x, y, 4, 0, 2 * Math.PI);
        ctx.fill();

        // Label the keypoint
        ctx.fillStyle = '#ffff00';
        ctx.font = '10px Arial';
        ctx.fillText(key, x + 6, y + 3);
        ctx.fillStyle = '#ff0000';
      });
    });

    ctx.restore();
  }, [detectedFaces]);

  // Auto-start detection when model loads and video is ready
  useEffect(() => {
    const video = videoRef.current;
    if (!video || !state.isModelLoaded || state.isDetecting) {
      return;
    }

    const tryStartDetection = () => {
      if (video.readyState >= 3 && state.isModelLoaded && !state.isDetecting) {
        console.log('🎬 Video ready, starting face detection...');
        startDetection();
      }
    };

    // If video is already ready, start immediately
    if (video.readyState >= 3) {
      tryStartDetection();
    }

    // Otherwise, wait for video to be ready
    video.addEventListener('canplay', tryStartDetection);
    video.addEventListener('loadeddata', tryStartDetection);

    return () => {
      video.removeEventListener('canplay', tryStartDetection);
      video.removeEventListener('loadeddata', tryStartDetection);
    };
  }, [state.isModelLoaded, state.isDetecting, startDetection, videoRef]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      stopDetection();
    };
  }, [stopDetection]);

  return {
    state,
    detectedFaces,
    actions: {
      startDetection,
      stopDetection,
      toggleDebug,
      updateOptions
    },
    debug: {
      drawBoundingBoxes,
      drawKeypoints
    }
  };
}
