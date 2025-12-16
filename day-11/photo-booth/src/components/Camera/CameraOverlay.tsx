import React, { useEffect, useRef } from 'react';
import type { CoordinateSystem } from '../../types/camera';

interface CameraOverlayProps {
  coordinateSystem: CoordinateSystem | null;
  isActive: boolean;
  children?: React.ReactNode;
}

export function CameraOverlay({ coordinateSystem, isActive, children }: CameraOverlayProps) {
  const overlayRef = useRef<HTMLDivElement>(null);
  
  // Update overlay dimensions based on coordinate system
  useEffect(() => {
    const overlay = overlayRef.current;
    if (!overlay || !coordinateSystem || !isActive) return;
    
    const { canvasWidth, canvasHeight, devicePixelRatio } = coordinateSystem;
    
    // Set overlay dimensions to match canvas
    overlay.style.width = `${canvasWidth}px`;
    overlay.style.height = `${canvasHeight}px`;
    
    // Handle high DPI displays
    if (devicePixelRatio > 1) {
      overlay.style.transform = `scale(${1 / devicePixelRatio})`;
      overlay.style.transformOrigin = 'top left';
    }
  }, [coordinateSystem, isActive]);
  
  if (!isActive || !coordinateSystem) {
    return null;
  }
  
  return (
    <div 
      ref={overlayRef}
      className="camera-overlay"
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        pointerEvents: 'none',
        zIndex: 10
      }}
    >
      {children}
    </div>
  );
}
