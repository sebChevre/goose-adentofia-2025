import { useState, useCallback } from 'react';

interface PhotoCaptureState {
  isCapturing: boolean;
  capturedPhoto: string | null;
  error: string | null;
}

interface UsePhotoCaptureReturn {
  state: PhotoCaptureState;
  capturePhoto: (
    videoRef: React.RefObject<HTMLVideoElement | null>,
    overlayCanvasRef: React.RefObject<HTMLCanvasElement | null>,
    coordinateSystem: any
  ) => Promise<void>;
  savePhoto: () => void;
  sharePhoto: () => Promise<void>;
  clearPhoto: () => void;
}

export function usePhotoCapture(): UsePhotoCaptureReturn {
  const [state, setState] = useState<PhotoCaptureState>({
    isCapturing: false,
    capturedPhoto: null,
    error: null
  });
  
  const capturePhoto = useCallback(async (
    videoRef: React.RefObject<HTMLVideoElement | null>,
    overlayCanvasRef: React.RefObject<HTMLCanvasElement | null>,
    coordinateSystem: any
  ) => {
    setState(prev => ({ ...prev, isCapturing: true, error: null }));
    
    try {
      const video = videoRef.current;
      const overlayCanvas = overlayCanvasRef.current;
      
      console.log('Capture attempt:', {
        hasVideo: !!video,
        hasCanvas: !!overlayCanvas,
        hasCoordinateSystem: !!coordinateSystem,
        videoReady: video?.readyState === 4,
        videoWidth: video?.videoWidth,
        videoHeight: video?.videoHeight
      });
      
      if (!video) {
        throw new Error('Video element not found');
      }
      
      if (video.readyState !== 4) {
        throw new Error('Video not ready');
      }
      
      if (!video.videoWidth || !video.videoHeight) {
        throw new Error('Video has no dimensions');
      }
      
      // Create output canvas
      const outputCanvas = document.createElement('canvas');
      const outputCtx = outputCanvas.getContext('2d');
      
      if (!outputCtx) {
        throw new Error('Failed to get 2D context for output canvas');
      }
      
      // Set output canvas size to match video dimensions
      outputCanvas.width = video.videoWidth;
      outputCanvas.height = video.videoHeight;
      
      // Draw video frame
      outputCtx.drawImage(video, 0, 0, outputCanvas.width, outputCanvas.height);
      
      // Draw overlay if available and has coordinate system
      if (overlayCanvas && coordinateSystem) {
        // Calculate overlay scaling
        const scaleX = outputCanvas.width / coordinateSystem.canvas.width;
        const scaleY = outputCanvas.height / coordinateSystem.canvas.height;
        
        // Draw overlay with proper scaling
        outputCtx.save();
        outputCtx.scale(scaleX, scaleY);
        outputCtx.drawImage(overlayCanvas, 0, 0);
        outputCtx.restore();
      }
      
      // Convert to data URL
      const dataUrl = outputCanvas.toDataURL('image/jpeg', 0.9);
      
      // Show flash effect
      showFlashEffect();
      
      setState(prev => ({
        ...prev,
        isCapturing: false,
        capturedPhoto: dataUrl
      }));
      
    } catch (error) {
      setState(prev => ({
        ...prev,
        isCapturing: false,
        error: error instanceof Error ? error.message : 'Failed to capture photo'
      }));
    }
  }, []);
  
  const savePhoto = useCallback(() => {
    if (!state.capturedPhoto) return;
    
    try {
      // Create download link
      const link = document.createElement('a');
      link.href = state.capturedPhoto;
      link.download = `winter-photo-${Date.now()}.jpg`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (error) {
      console.error('Failed to save photo:', error);
      setState(prev => ({
        ...prev,
        error: 'Failed to save photo'
      }));
    }
  }, [state.capturedPhoto]);
  
  const sharePhoto = useCallback(async () => {
    if (!state.capturedPhoto) return;
    
    try {
      // Check if Web Share API is available
      if (navigator.share && navigator.canShare) {
        // Convert data URL to blob
        const response = await fetch(state.capturedPhoto);
        const blob = await response.blob();
        const file = new File([blob], `winter-photo-${Date.now()}.jpg`, { type: 'image/jpeg' });
        
        if (navigator.canShare({ files: [file] })) {
          await navigator.share({
            title: 'Winter Photo Booth',
            text: 'Check out my winter photo!',
            files: [file]
          });
          return;
        }
      }
      
      // Fallback: copy to clipboard
      const response = await fetch(state.capturedPhoto);
      const blob = await response.blob();
      
      if (navigator.clipboard && navigator.clipboard.write) {
        await navigator.clipboard.write([
          new ClipboardItem({ 'image/jpeg': blob })
        ]);
        alert('Photo copied to clipboard!');
      } else {
        throw new Error('Sharing not supported on this device');
      }
      
    } catch (error) {
      console.error('Failed to share photo:', error);
      setState(prev => ({
        ...prev,
        error: 'Failed to share photo'
      }));
    }
  }, [state.capturedPhoto]);
  
  const clearPhoto = useCallback(() => {
    setState(prev => ({
      ...prev,
      capturedPhoto: null,
      error: null
    }));
  }, []);
  
  return {
    state,
    capturePhoto,
    savePhoto,
    sharePhoto,
    clearPhoto
  };
}

function showFlashEffect() {
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
    if (document.body.contains(flash)) {
      document.body.removeChild(flash);
    }
    if (document.head.contains(style)) {
      document.head.removeChild(style);
    }
  }, 200);
}
