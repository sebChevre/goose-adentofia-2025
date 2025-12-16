import { useState, useEffect, useCallback, useRef } from 'react';
import type { 
  FaceDetectionState, 
  FaceDetectionOptions
} from '../types/detection';
import type { CoordinateSystem } from '../types/camera';
import type { DetectedFace } from '../types/filters';
import { FaceDetection } from '@mediapipe/face_detection';

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
  detections?: Array<{
    boundingBox: {
      xCenter: number;
      yCenter: number;
      width: number;
      height: number;
    };
    score: number[];
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
  const faceDetectionRef = useRef<FaceDetection | null>(null);
  const animationFrameRef = useRef<number>();
  
  const updateState = useCallback((updates: Partial<FaceDetectionState>) => {
    setState(prev => ({ ...prev, ...updates }));
  }, []);

  // Initialize MediaPipe Face Detection
  useEffect(() => {
    const initializeFaceDetection = async () => {
      try {
        updateState({ modelLoadProgress: 20 });
        
        const faceDetection = new FaceDetection({
          locateFile: (file: string) => {
            return `https://cdn.jsdelivr.net/npm/@mediapipe/face_detection/${file}`;
          }
        });

        updateState({ modelLoadProgress: 50 });

        faceDetection.setOptions({
          model: 'short',
          minDetectionConfidence: 0.5,
        });

        updateState({ modelLoadProgress: 80 });

        faceDetection.onResults((results: MediaPipeFaceResults) => {
          if (results.detections) {
            const faces: DetectedFace[] = results.detections.map(detection => {
              // Convert MediaPipe format (center + width/height) to corner format
              const centerX = detection.boundingBox.xCenter;
              const centerY = detection.boundingBox.yCenter;
              const width = detection.boundingBox.width;
              const height = detection.boundingBox.height;
              
              return {
                boundingBox: {
                  x: centerX - width / 2,
                  y: centerY - height / 2,
                  width,
                  height
                },
                confidence: detection.score[0] || 0.5
              };
            });
            
            setDetectedFaces(faces);
            console.log('Faces detected:', faces.length);
          } else {
            setDetectedFaces([]);
          }
        });

        await faceDetection.initialize();
        
        faceDetectionRef.current = faceDetection;
        updateState({ 
          isModelLoaded: true, 
          modelLoadProgress: 100,
          error: null
        });
        
        console.log('✅ Face detection initialized');
        
      } catch (error) {
        console.error('❌ Face detection initialization failed:', error);
        updateState({ 
          error: error instanceof Error ? error.message : 'Failed to initialize face detection',
          modelLoadProgress: 0
        });
        
        // Fallback to mock face for demo
        setDetectedFaces([{
          boundingBox: {
            x: 0.3,
            y: 0.2,
            width: 0.4,
            height: 0.6
          },
          confidence: 0.95
        }]);
      }
    };

    initializeFaceDetection();

    return () => {
      if (faceDetectionRef.current) {
        faceDetectionRef.current.close();
      }
    };
  }, [updateState]);

  const detectFaces = useCallback(async () => {
    const video = videoRef.current;
    const faceDetection = faceDetectionRef.current;
    
    if (!video || !faceDetection || !state.isDetecting || !coordinateSystem) {
      return;
    }

    if (video.readyState === 4) {
      try {
        await faceDetection.send({ image: video });
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
    const faceDetection = faceDetectionRef.current;
    if (!faceDetection) return;
    
    try {
      await faceDetection.setOptions({
        minDetectionConfidence: newOptions.minDetectionConfidence || 0.5,
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
    _canvas: HTMLCanvasElement, 
    _coordinateSystem: CoordinateSystem
  ) => {
    // Face detection doesn't provide keypoints, only bounding boxes
    // Could implement facial landmark detection separately if needed
  }, []);

  // Auto-start detection when model loads and video is ready
  useEffect(() => {
    if (state.isModelLoaded && !state.isDetecting && videoRef.current?.readyState === 4) {
      startDetection();
    }
  }, [state.isModelLoaded, state.isDetecting, startDetection]);

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
