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
    
    if (video && canvas && video.videoWidth && video.videoHeight) {
      const system = calculateCoordinateSystem(video, canvas);
      setCoordinateSystem(system);
      onCoordinateSystemChange?.(system);
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
      updateCoordinateSystem();
    };
    
    const handleResize = () => {
      requestAnimationFrame(updateCoordinateSystem);
    };
    
    video.addEventListener('loadedmetadata', handleLoadedMetadata);
    window.addEventListener('orientationchange', handleResize);
    window.addEventListener('resize', handleResize);
    
    return () => {
      video.removeEventListener('loadedmetadata', handleLoadedMetadata);
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
