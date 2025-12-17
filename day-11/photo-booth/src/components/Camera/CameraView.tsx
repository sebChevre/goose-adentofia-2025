import React, { useEffect, useRef, useState } from 'react';
import { calculateCoordinateSystem } from '../../utils/coordinates';
import { CameraControls } from './CameraControls';
import { CameraOverlay } from './CameraOverlay';
import type { CoordinateSystem, UseCameraReturn } from '../../types/camera';

interface CameraViewProps {
  camera: UseCameraReturn;
  onCoordinateSystemChange?: (system: CoordinateSystem) => void;
  showControls?: boolean;
  className?: string;
}

export function CameraView({ 
  camera,
  onCoordinateSystemChange, 
  showControls = true,
  className = ''
}: CameraViewProps) {
  const { state, actions, refs } = camera;
  const [coordinateSystem, setCoordinateSystem] = useState<CoordinateSystem | null>(null);
  const resizeObserver = useRef<ResizeObserver | null>(null);
  
  // Update coordinate system when video loads or canvas resizes
  const updateCoordinateSystem = React.useCallback(() => {
    const video = refs.videoRef.current;
    const canvas = refs.canvasRef.current;

    console.log('🎯 Updating coordinate system:', {
      hasVideo: !!video,
      hasCanvas: !!canvas,
      videoSize: video ? `${video.videoWidth}x${video.videoHeight}` : 'none',
      canvasSize: canvas ? `${canvas.width}x${canvas.height}` : 'none',
      canvasBounds: canvas?.getBoundingClientRect(),
      videoReadyState: video?.readyState,
      onCoordinateSystemChangeExists: !!onCoordinateSystemChange
    });

    if (video && canvas && video.videoWidth && video.videoHeight) {
      // Set canvas size to match container  
      const canvasRect = canvas.getBoundingClientRect();
      const devicePixelRatio = window.devicePixelRatio || 1;
      
      console.log('📐 Canvas rect:', canvasRect);
      
      // Set logical size
      canvas.style.width = canvasRect.width + 'px';
      canvas.style.height = canvasRect.height + 'px';
      
      // Set actual size in memory (scaled for high-DPI displays)
      canvas.width = canvasRect.width * devicePixelRatio;
      canvas.height = canvasRect.height * devicePixelRatio;
      
      // Scale the context to ensure correct drawing operations
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.scale(devicePixelRatio, devicePixelRatio);
      }
      
      const system = calculateCoordinateSystem(video, canvas);
      console.log('✅ Coordinate system calculated:', system);
      console.log('📤 Setting coordinate system in local state and calling onCoordinateSystemChange');
      
      setCoordinateSystem(system);
      if (onCoordinateSystemChange) {
        onCoordinateSystemChange(system);
        console.log('📤 onCoordinateSystemChange called');
      } else {
        console.warn('⚠️ onCoordinateSystemChange is undefined!');
      }
    } else {
      console.log('❌ Cannot calculate coordinate system - missing requirements:', {
        hasVideo: !!video,
        hasCanvas: !!canvas,
        videoWidth: video?.videoWidth,
        videoHeight: video?.videoHeight
      });
    }
  }, [refs.videoRef, refs.canvasRef, onCoordinateSystemChange]);
  
  // Set up resize observer
  useEffect(() => {
    const canvas = refs.canvasRef.current;
    if (!canvas) return;
    
    resizeObserver.current = new ResizeObserver(() => {
      requestAnimationFrame(updateCoordinateSystem);
    });
    
    resizeObserver.current.observe(canvas);
    
    return () => {
      resizeObserver.current?.disconnect();
    };
  }, [updateCoordinateSystem, refs.canvasRef]);
  
  // Update coordinate system when video metadata loads
  useEffect(() => {
    const video = refs.videoRef.current;
    if (!video) return;
    
    const handleLoadedMetadata = () => {
      console.log('📹 Video loadedmetadata event fired');
      updateCoordinateSystem();
    };
    
    const handleResize = () => {
      console.log('🔄 Window resize event fired');
      requestAnimationFrame(updateCoordinateSystem);
    };
    
    // Also try to update when video can play
    const handleCanPlay = () => {
      console.log('🎬 Video canplay event fired');
      requestAnimationFrame(updateCoordinateSystem);
    };
    
    video.addEventListener('loadedmetadata', handleLoadedMetadata);
    video.addEventListener('canplay', handleCanPlay);
    window.addEventListener('orientationchange', handleResize);
    window.addEventListener('resize', handleResize);
    
    // Try to update immediately if video is already loaded
    if (video.readyState >= 2) {
      console.log('📹 Video already has metadata, updating coordinate system');
      requestAnimationFrame(updateCoordinateSystem);
    }
    
    return () => {
      video.removeEventListener('loadedmetadata', handleLoadedMetadata);
      video.removeEventListener('canplay', handleCanPlay);
      window.removeEventListener('orientationchange', handleResize);
      window.removeEventListener('resize', handleResize);
    };
  }, [updateCoordinateSystem]);
  
  // Debug camera state
  useEffect(() => {
    console.log('Camera state:', {
      permission: state.permission.state,
      devices: state.devices.length,
      isActive: state.isActive,
      isLoading: state.isLoading,
      error: state.error
    });
  }, [state]);

  // Auto-start camera when permission is granted and devices are available
  useEffect(() => {
    if (state.permission.state === 'granted' && 
        state.devices.length > 0 && 
        !state.isActive && 
        !state.isLoading) {
      console.log('Auto-starting camera...');
      actions.startCamera();
    }
  }, [state.permission.state, state.devices.length, state.isActive, state.isLoading, actions]);

  // Force coordinate system update when camera becomes active
  useEffect(() => {
    if (state.isActive) {
      console.log('📹 Camera is now active, forcing coordinate system update');
      // Give the video a moment to be ready, then update multiple times to ensure it works
      const timeoutId1 = setTimeout(() => {
        updateCoordinateSystem();
      }, 500);
      
      const timeoutId2 = setTimeout(() => {
        updateCoordinateSystem();
      }, 1000);
      
      const timeoutId3 = setTimeout(() => {
        updateCoordinateSystem();
      }, 2000);
      
      return () => {
        clearTimeout(timeoutId1);
        clearTimeout(timeoutId2);
        clearTimeout(timeoutId3);
      };
    }
  }, [state.isActive, updateCoordinateSystem]);
  
  if (state.permission.state === 'denied') {
    return (
      <div className={`camera-view camera-view--permission-denied ${className}`}>
        <div className="camera-view__message">
          <h3>Camera Access Denied</h3>
          <p>Please allow camera access to use this feature.</p>
          <button onClick={actions.requestPermission}>
            Request Permission
          </button>
        </div>
      </div>
    );
  }
  
  if (state.permission.state === 'unknown' || state.permission.canRequest) {
    return (
      <div className={`camera-view camera-view--permission-prompt ${className}`}>
        <div className="camera-view__message">
          <h3>Camera Access Required</h3>
          <p>We need access to your camera to take photos.</p>
          <button 
            onClick={async () => {
              const granted = await actions.requestPermission();
              if (granted) {
                await actions.refreshDevices();
              }
            }}
            disabled={state.isLoading}
          >
            {state.isLoading ? 'Requesting...' : 'Allow Camera Access'}
          </button>
          {state.error && (
            <p className="error-message">
              Error: {state.error.message}
            </p>
          )}
        </div>
      </div>
    );
  }
  
  if (state.error) {
    return (
      <div className={`camera-view camera-view--error ${className}`}>
        <div className="camera-view__message">
          <h3>Camera Error</h3>
          <p>{state.error.message}</p>
          <button onClick={() => actions.startCamera()}>
            Retry
          </button>
        </div>
      </div>
    );
  }
  
  // Determine if we should mirror based on camera facing mode
  const isRearCamera = state.selectedDevice?.facingMode === 'environment';
  const videoClassName = `camera-view__video ${isRearCamera ? 'camera-view__video--rear' : ''}`;
  const canvasClassName = `camera-view__canvas ${isRearCamera ? 'camera-view__canvas--rear' : ''}`;

  return (
    <div className={`camera-view ${className}`}>
      <div className="camera-view__container">
        <video
          ref={refs.videoRef}
          className={videoClassName}
          autoPlay
          playsInline
          muted
        />
        
        <canvas
          ref={refs.canvasRef}
          className={canvasClassName}
        />
        
        <CameraOverlay 
          coordinateSystem={coordinateSystem}
          isActive={state.isActive}
        />
        
        {state.isLoading && (
          <div className="camera-view__loading">
            <div className="spinner" />
            <span>Starting camera...</span>
          </div>
        )}
      </div>
      
      {showControls && (
        <CameraControls camera={camera} />
      )}
    </div>
  );
}
