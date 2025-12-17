// Face Detection Types
export interface FaceDetectionPoint {
  x: number; // normalized [0,1]
  y: number; // normalized [0,1]
  z?: number; // depth (optional)
}

export interface FaceBoundingBox {
  x: number;      // normalized [0,1] - top-left
  y: number;      // normalized [0,1] - top-left
  width: number;  // normalized [0,1]
  height: number; // normalized [0,1]
}

export interface FaceKeypoints {
  landmarks?: FaceDetectionPoint[]; // 478 points from MediaPipe Face Landmarker
  leftEye?: FaceDetectionPoint;
  rightEye?: FaceDetectionPoint;
  nose?: FaceDetectionPoint;
  mouth?: FaceDetectionPoint;
  forehead?: FaceDetectionPoint;
  chin?: FaceDetectionPoint;
}

export interface DetectedFace {
  id: string;
  bbox: FaceBoundingBox;
  keypoints: FaceKeypoints;
  confidence: number;
}

export interface FaceDetectionResult {
  faces: DetectedFace[];
  timestamp: number;
  processingTime: number;
}

export interface FaceDetectionState {
  isModelLoaded: boolean;
  isDetecting: boolean;
  lastResult: FaceDetectionResult | null;
  error: string | null;
  modelLoadProgress: number;
}

export interface FaceDetectionOptions {
  minDetectionConfidence: number;
  minTrackingConfidence: number;
  maxNumFaces: number;
  throttleMs: number;
  enableDebug: boolean;
}

export interface UseFaceDetectionReturn {
  state: FaceDetectionState;
  actions: {
    startDetection: () => void;
    stopDetection: () => void;
    toggleDebug: () => void;
    updateOptions: (options: Partial<FaceDetectionOptions>) => void;
  };
  debug: {
    drawBoundingBoxes: (canvas: HTMLCanvasElement, coordinateSystem: any) => void;
    drawKeypoints: (canvas: HTMLCanvasElement, coordinateSystem: any) => void;
  };
}

// MediaPipe specific types for useMediaPipeFace hook
export interface FaceTrackerConfig {
  maxNumFaces: number;
  minDetectionConfidence: number;
  minTrackingConfidence: number;
}

export const DEFAULT_FACE_CONFIG: FaceTrackerConfig = {
  maxNumFaces: 3,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5,
};

export interface FaceResults {
  faceLandmarks: any[][]; // Array of face landmarks (478 points per face)
  faceBlendshapes?: any[]; // Optional blendshapes data
  facialTransformationMatrixes?: any[]; // Optional transformation matrices
}
