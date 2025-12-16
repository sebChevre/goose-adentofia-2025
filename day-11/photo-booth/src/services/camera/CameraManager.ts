import type { CameraDevice, CameraPermission, StreamConstraints } from '../../types/camera';
import { StreamManager } from './StreamManager';

const SELECTED_CAMERA_KEY = 'goose-camera-selected-device';

export class CameraManager {
  private streamManager = new StreamManager();
  
  async checkPermission(): Promise<CameraPermission> {
    if (!navigator.permissions) {
      // Fallback for browsers without Permissions API
      return { state: 'unknown', canRequest: true };
    }
    
    try {
      const permission = await navigator.permissions.query({ name: 'camera' as PermissionName });
      return {
        state: permission.state as any,
        canRequest: permission.state === 'prompt'
      };
    } catch {
      return { state: 'unknown', canRequest: true };
    }
  }
  
  async requestPermission(): Promise<boolean> {
    try {
      // Request minimal stream to trigger permission
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'environment' },
        audio: false
      });
      
      // Immediately stop the stream
      stream.getTracks().forEach(track => track.stop());
      return true;
    } catch {
      return false;
    }
  }
  
  async enumerateDevices(): Promise<CameraDevice[]> {
    try {
      const devices = await navigator.mediaDevices.enumerateDevices();
      
      return devices
        .filter(device => device.kind === 'videoinput')
        .map(device => ({
          deviceId: device.deviceId,
          label: device.label || `Camera ${device.deviceId.slice(0, 8)}`,
          groupId: device.groupId,
          facingMode: this.inferFacingMode(device.label)
        }));
    } catch {
      return [];
    }
  }
  
  async startCamera(deviceId?: string, facingMode?: 'user' | 'environment'): Promise<MediaStream> {
    const constraints = this.buildConstraints(deviceId, facingMode);
    return await this.streamManager.requestStream(constraints);
  }
  
  stopCamera(): void {
    this.streamManager.stopStream();
  }
  
  getCurrentStream(): MediaStream | null {
    return this.streamManager.getCurrentStream();
  }
  
  saveSelectedDevice(device: CameraDevice): void {
    localStorage.setItem(SELECTED_CAMERA_KEY, JSON.stringify(device));
  }
  
  getSelectedDevice(): CameraDevice | null {
    try {
      const saved = localStorage.getItem(SELECTED_CAMERA_KEY);
      return saved ? JSON.parse(saved) : null;
    } catch {
      return null;
    }
  }
  
  clearSelectedDevice(): void {
    localStorage.removeItem(SELECTED_CAMERA_KEY);
  }
  
  private buildConstraints(deviceId?: string, facingMode?: 'user' | 'environment'): StreamConstraints {
    const constraints: StreamConstraints = {
      video: {
        width: { ideal: 1920, max: 1920 },
        height: { ideal: 1080, max: 1080 },
        frameRate: { ideal: 30 }
      },
      audio: false
    };
    
    if (deviceId) {
      constraints.video.deviceId = { exact: deviceId };
    } else if (facingMode) {
      constraints.video.facingMode = facingMode;
    }
    
    return constraints;
  }
  
  private inferFacingMode(label: string): 'user' | 'environment' | undefined {
    const lowerLabel = label.toLowerCase();
    
    if (lowerLabel.includes('front') || lowerLabel.includes('user') || lowerLabel.includes('selfie')) {
      return 'user';
    }
    
    if (lowerLabel.includes('back') || lowerLabel.includes('rear') || lowerLabel.includes('environment')) {
      return 'environment';
    }
    
    return undefined;
  }
}
