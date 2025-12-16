import type { DetectedFace, FaceDetectionResult, FaceDetectionOptions } from '../../types/detection';

export class MediaPipeDetector {
  private faceDetection: any = null;
  private isInitialized = false;
  private isDetecting = false;
  private modelLoadProgress = 0;
  private lastDetectionTime = 0;
  private faceIdCounter = 0;
  private options: FaceDetectionOptions;

  private defaultOptions: FaceDetectionOptions = {
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5,
    maxNumFaces: 3,
    throttleMs: 50, // 20 FPS max
    enableDebug: false
  };

  constructor(options: Partial<FaceDetectionOptions> = {}) {
    this.options = { ...this.defaultOptions, ...options };
  }

  async initialize(): Promise<void> {
    if (this.isInitialized) return;

    try {
      this.modelLoadProgress = 10;

      // Mock MediaPipe initialization for now
      this.faceDetection = {
        setOptions: () => {},
        onResults: () => {},
        initialize: async () => {},
        send: async () => {},
        close: () => {}
      };

      this.modelLoadProgress = 30;

      // Configure options
      this.faceDetection.setOptions({
        model: 'short', // 'short' for close-range detection (better for selfies)
        minDetectionConfidence: this.options.minDetectionConfidence || 0.5,
      });

      this.modelLoadProgress = 60;

      // Set up result callback
      this.faceDetection.onResults = (results: any) => {
        this.handleDetectionResults(results);
      };

      this.modelLoadProgress = 80;

      // Initialize the model
      await this.faceDetection.initialize();

      this.modelLoadProgress = 100;
      this.isInitialized = true;

      console.log('MediaPipe Face Detection initialized successfully');
    } catch (error) {
      console.error('Failed to initialize MediaPipe Face Detection:', error);
      this.modelLoadProgress = 0;
      throw error;
    }
  }

  async detectFaces(
    video: HTMLVideoElement,
    onResult?: (result: FaceDetectionResult) => void
  ): Promise<FaceDetectionResult | null> {
    if (!this.isInitialized || !this.faceDetection || this.isDetecting) {
      return null;
    }

    // Throttle detection
    const now = performance.now();
    if (now - this.lastDetectionTime < (this.options.throttleMs || 50)) {
      return null;
    }

    try {
      this.isDetecting = true;
      const startTime = performance.now();

      // Send frame to MediaPipe
      await this.faceDetection.send({ image: video });

      // Wait for results (handled in callback)
      const result = await new Promise<FaceDetectionResult>((resolve) => {
        const timeout = setTimeout(() => {
          resolve({
            faces: [],
            timestamp: now,
            processingTime: performance.now() - startTime
          });
        }, 100); // 100ms timeout

        this.onDetectionResult = (detectionResult) => {
          clearTimeout(timeout);
          resolve(detectionResult);
        };
      });

      this.lastDetectionTime = now;

      if (onResult) {
        onResult(result);
      }

      return result;
    } catch (error) {
      console.error('Face detection error:', error);
      return {
        faces: [],
        timestamp: now,
        processingTime: 0
      };
    } finally {
      this.isDetecting = false;
    }
  }

  private onDetectionResult?: (result: FaceDetectionResult) => void;

  private handleDetectionResults(results: any): void {
    const startTime = performance.now();
    const faces: DetectedFace[] = [];

    if (results.detections && results.detections.length > 0) {
      for (let i = 0; i < Math.min(results.detections.length, this.options.maxNumFaces || 3); i++) {
        const detection = results.detections[i];
        
        try {
          // Mock bbox and keypoints for now
          const bbox = {
            x: 0.3,
            y: 0.2,
            width: 0.4,
            height: 0.5
          };

          const keypoints = {
            leftEye: { x: 0.4, y: 0.35 },
            rightEye: { x: 0.6, y: 0.35 },
            nose: { x: 0.5, y: 0.45 },
            mouth: { x: 0.5, y: 0.55 }
          };

          const face: DetectedFace = {
            id: `face_${this.faceIdCounter++}`,
            bbox,
            keypoints,
            confidence: detection.score?.[0] || 0.5
          };

          faces.push(face);
        } catch (error) {
          console.warn('Error processing face detection:', error);
        }
      }
    }

    const result: FaceDetectionResult = {
      faces,
      timestamp: performance.now(),
      processingTime: performance.now() - startTime
    };

    if (this.onDetectionResult) {
      this.onDetectionResult(result);
    }
  }

  updateOptions(newOptions: Partial<FaceDetectionOptions>): void {
    this.options = { ...this.options, ...newOptions };

    if (this.faceDetection && this.isInitialized) {
      this.faceDetection.setOptions({
        model: 'short',
        minDetectionConfidence: this.options.minDetectionConfidence || 0.5,
      });
    }
  }

  getModelLoadProgress(): number {
    return this.modelLoadProgress;
  }

  isModelLoaded(): boolean {
    return this.isInitialized;
  }

  isCurrentlyDetecting(): boolean {
    return this.isDetecting;
  }

  destroy(): void {
    if (this.faceDetection) {
      this.faceDetection.close();
      this.faceDetection = null;
    }
    this.isInitialized = false;
    this.isDetecting = false;
    this.modelLoadProgress = 0;
    this.onDetectionResult = undefined;
  }

  // Debug utilities
  static drawBoundingBox(
    ctx: CanvasRenderingContext2D,
    bbox: any,
    color = '#00FF00',
    lineWidth = 2
  ): void {
    ctx.strokeStyle = color;
    ctx.lineWidth = lineWidth;
    ctx.strokeRect(bbox.x, bbox.y, bbox.width, bbox.height);
  }

  static drawKeypoints(
    ctx: CanvasRenderingContext2D,
    keypoints: any,
    color = '#FF0000',
    radius = 2
  ): void {
    ctx.fillStyle = color;

    // Draw main facial points
    const points = [keypoints.leftEye, keypoints.rightEye, keypoints.nose, keypoints.mouth];
    
    points.forEach(point => {
      if (point) {
        ctx.beginPath();
        ctx.arc(point.x, point.y, radius, 0, 2 * Math.PI);
        ctx.fill();
      }
    });
  }

  static drawFaceId(
    ctx: CanvasRenderingContext2D,
    face: DetectedFace,
    _coordinateSystem: any
  ): void {
    ctx.fillStyle = '#FFFF00';
    ctx.font = '14px Arial';
    ctx.fillText(
      `${face.id} (${Math.round(face.confidence * 100)}%)`,
      face.bbox.x,
      face.bbox.y - 5
    );
  }
}
