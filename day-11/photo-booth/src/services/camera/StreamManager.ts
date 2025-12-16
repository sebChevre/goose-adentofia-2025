import type { StreamConstraints, CameraError } from '../../types/camera';

export class StreamManager {
  private currentStream: MediaStream | null = null;
  
  async requestStream(constraints: StreamConstraints): Promise<MediaStream> {
    try {
      // Stop existing stream first
      this.stopStream();
      
      // iOS Safari specific adjustments
      const adjustedConstraints = this.adjustConstraintsForIOS(constraints);
      
      const stream = await navigator.mediaDevices.getUserMedia(adjustedConstraints);
      this.currentStream = stream;
      
      return stream;
    } catch (error) {
      throw this.mapToCustomError(error as DOMException);
    }
  }
  
  stopStream(): void {
    if (this.currentStream) {
      this.currentStream.getTracks().forEach(track => {
        track.stop();
      });
      this.currentStream = null;
    }
  }
  
  getCurrentStream(): MediaStream | null {
    return this.currentStream;
  }
  
  private adjustConstraintsForIOS(constraints: StreamConstraints): StreamConstraints {
    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
    
    if (!isIOS) {
      return constraints;
    }
    
    // iOS Safari has issues with exact constraints, prefer ideal
    const adjusted = { ...constraints };
    
    if (adjusted.video.deviceId && 'exact' in adjusted.video.deviceId) {
      // Keep exact deviceId but adjust other constraints
      adjusted.video = {
        ...adjusted.video,
        width: { ideal: 1920, max: 1920 },
        height: { ideal: 1080, max: 1080 },
        frameRate: { ideal: 30 }
      };
    }
    
    return adjusted;
  }
  
  private mapToCustomError(error: DOMException): CameraError {
    switch (error.name) {
      case 'NotAllowedError':
        return {
          code: 'PERMISSION_DENIED',
          message: 'Camera access denied by user',
          name: error.name
        };
      case 'NotFoundError':
        return {
          code: 'NOT_FOUND',
          message: 'No camera device found',
          name: error.name
        };
      case 'NotReadableError':
        return {
          code: 'NOT_READABLE',
          message: 'Camera is already in use',
          name: error.name
        };
      case 'OverconstrainedError':
        return {
          code: 'OVERCONSTRAINED',
          message: 'Camera constraints cannot be satisfied',
          name: error.name
        };
      default:
        return {
          code: 'UNKNOWN',
          message: error.message || 'Unknown camera error',
          name: error.name
        };
    }
  }
}
