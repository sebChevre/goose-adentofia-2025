// Face Detection Types
export interface FaceDetectionPoint {
  x: number; // normalized [0,1]
  y: number; // normalized [0,1]
}

export interface FaceBoundingBox {
  x: number;      // normalized [0,1] - top-left
  y: number;      // normalized [0,1] - top-left  
  width: number;  // normalized [0,1]
  height: number; // normalized [0,1]
}

export interface FaceKeypoints {
  landmarks?: FaceDetectionPoint[]; // 468 points from MediaPipe
  leftEye?: FaceDetectionPoint;
  rightEye?: FaceDetectionPoint;
  nose?: FaceDetectionPoint;
  mouth?: FaceDetectionPoint;
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
