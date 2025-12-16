import { useRef, useCallback } from 'react';
import type { CoordinateSystem } from '../../types/camera';

interface PhotoCaptureProps {
  videoRef: React.RefObject<HTMLVideoElement>;
  overlayCanvasRef: React.RefObject<HTMLCanvasElement>;
  coordinateSystem: CoordinateSystem | null;
  onPhotoCapture: (dataUrl: string) => void;
}

export function PhotoCapture({
  videoRef,
  overlayCanvasRef,
  coordinateSystem,
  onPhotoCapture
}: PhotoCaptureProps) {
  const outputCanvasRef = useRef<HTMLCanvasElement>(null);
  
  const capturePhoto = useCallback(async () => {
    const video = videoRef.current;
    const overlayCanvas = overlayCanvasRef.current;
    
    if (!video || !overlayCanvas || !coordinateSystem) {
      console.error('Missing required elements for photo capture');
      return;
    }
    
    // Create output canvas if it doesn't exist
    let outputCanvas = outputCanvasRef.current;
    if (!outputCanvas) {
      outputCanvas = document.createElement('canvas');
      outputCanvasRef.current = outputCanvas;
    }
    
    const outputCtx = outputCanvas.getContext('2d');
    if (!outputCtx) {
      console.error('Failed to get 2D context for output canvas');
      return;
    }
    
    // Set output canvas size to match video dimensions
    outputCanvas.width = video.videoWidth;
    outputCanvas.height = video.videoHeight;
    
    // Draw video frame
    outputCtx.drawImage(video, 0, 0, outputCanvas.width, outputCanvas.height);
    
    // Calculate overlay scaling
    const scaleX = outputCanvas.width / coordinateSystem.canvas.width;
    const scaleY = outputCanvas.height / coordinateSystem.canvas.height;
    
    // Draw overlay with proper scaling
    outputCtx.save();
    outputCtx.scale(scaleX, scaleY);
    outputCtx.drawImage(overlayCanvas, 0, 0);
    outputCtx.restore();
    
    // Convert to data URL and trigger callback
    const dataUrl = outputCanvas.toDataURL('image/jpeg', 0.9);
    onPhotoCapture(dataUrl);
    
    // Flash effect
    showFlashEffect();
  }, [videoRef, overlayCanvasRef, coordinateSystem, onPhotoCapture]);
  
  const showFlashEffect = () => {
    // Create flash overlay
    const flash = document.createElement('div');
    flash.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: white;
      opacity: 0.8;
      z-index: 9999;
      pointer-events: none;
      animation: flash 0.2s ease-out;
    `;
    
    // Add flash animation
    const style = document.createElement('style');
    style.textContent = `
      @keyframes flash {
        0% { opacity: 0.8; }
        50% { opacity: 1; }
        100% { opacity: 0; }
      }
    `;
    document.head.appendChild(style);
    document.body.appendChild(flash);
    
    // Remove flash after animation
    setTimeout(() => {
      document.body.removeChild(flash);
      document.head.removeChild(style);
    }, 200);
  };
  
  return {
    capturePhoto,
    outputCanvasRef
  };
}
