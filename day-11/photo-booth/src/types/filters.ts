export interface FaceDetectionData {
  x: number;
  y: number;
  width: number;
  height: number;
  landmarks?: {
    leftEye: { x: number; y: number };
    rightEye: { x: number; y: number };
    nose: { x: number; y: number };
    mouth: { x: number; y: number };
    chin: { x: number; y: number };
    forehead: { x: number; y: number };
  };
  rotation?: number;
  scale?: number;
}

export interface FilterConfig {
  id: string;
  name: string;
  description: string;
  icon: string;
  category?: 'winter' | 'summer' | 'holiday' | 'fun';
  thumbnail?: string;
  enabled?: boolean;
  performance?: 'low' | 'medium' | 'high';
  animation?: {
    duration: number;
    easing: 'linear' | 'ease-in' | 'ease-out' | 'ease-in-out';
    loop: boolean;
  };
}

export interface DetectedFace {
  boundingBox: {
    x: number;
    y: number;
    width: number;
    height: number;
  };
  landmarks?: {
    leftEye: { x: number; y: number };
    rightEye: { x: number; y: number };
    nose: { x: number; y: number };
    mouth: { x: number; y: number };
    chin: { x: number; y: number };
    forehead: { x: number; y: number };
  };
  confidence?: number;
}

export interface FilterState {
  activeFilter: string | null;
  animationTime: number;
  isActive: boolean;
  performance: {
    fps: number;
    lastFrameTime: number;
  };
}

export interface FilterRenderer {
  render(ctx: CanvasRenderingContext2D, faces: DetectedFace[], coordinateSystem: any, timestamp: number): void;
  cleanup(): void;
}

export interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  life: number;
  maxLife: number;
  size: number;
  rotation: number;
  rotationSpeed: number;
  opacity: number;
}
