export interface CameraDevice {
  deviceId: string;
  label: string;
  groupId: string;
  facingMode?: 'user' | 'environment';
}

export interface CameraPermission {
  state: 'granted' | 'denied' | 'prompt' | 'unknown';
  canRequest: boolean;
}

export interface StreamConstraints {
  video: {
    deviceId?: { exact: string };
    facingMode?: { exact: 'user' | 'environment' } | 'user' | 'environment';
    width?: { ideal: number; max: number };
    height?: { ideal: number; max: number };
    frameRate?: { ideal: number };
  };
  audio: false;
}

export interface CameraState {
  stream: MediaStream | null;
  devices: CameraDevice[];
  selectedDevice: CameraDevice | null;
  isLoading: boolean;
  permission: CameraPermission;
  error: CameraError | null;
  isActive: boolean;
}

export interface CameraError {
  code: 'PERMISSION_DENIED' | 'NOT_FOUND' | 'NOT_READABLE' | 'OVERCONSTRAINED' | 'UNKNOWN';
  message: string;
  name: string;
}

export interface CoordinateSystem {
  canvasWidth: number;
  canvasHeight: number;
  videoWidth: number;
  videoHeight: number;
  canvas: {
    width: number;
    height: number;
  };
  devicePixelRatio: number;
  scale: number;
  offsetX: number;
  offsetY: number;
}

export interface Point {
  x: number;
  y: number;
}

export interface UseCameraReturn {
  state: CameraState;
  actions: {
    requestPermission: () => Promise<boolean>;
    startCamera: (deviceId?: string) => Promise<boolean>;
    stopCamera: () => void;
    switchCamera: (deviceId: string) => Promise<boolean>;
    refreshDevices: () => Promise<void>;
  };
  refs: {
    videoRef: React.RefObject<HTMLVideoElement | null>;
    canvasRef: React.RefObject<HTMLCanvasElement | null>;
  };
}
