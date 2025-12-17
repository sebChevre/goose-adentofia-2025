import React, { useRef, useEffect, useCallback } from 'react';
import type { FilterConfig, FilterRenderer, DetectedFace } from '../../types/filters';
import type { CoordinateSystem } from '../../types/camera';
import { SnowflakeCrownFilter } from './filters/SnowflakeCrownFilter';
import { ReindeerAntlersFilter } from './filters/ReindeerAntlersFilter';
import { FrostyBeardFilter } from './filters/FrostyBeardFilter';
import { SparkleEffectFilter } from './filters/SparkleEffectFilter';

interface FilterManagerProps {
  canvasRef: React.RefObject<HTMLCanvasElement | null>;
  videoRef: React.RefObject<HTMLVideoElement | null>;
  selectedFilter: string | null;
  detectedFaces: DetectedFace[];
  coordinateSystem: CoordinateSystem | null;
  isActive: boolean;
}

// Winter filter configurations
export const WINTER_FILTERS: FilterConfig[] = [
  {
    id: 'snowflake-crown',
    name: 'Snowflake Crown',
    icon: '👑',
    description: 'Elegant snowflake crown above your head'
  },
  {
    id: 'reindeer-antlers',
    name: 'Reindeer Antlers',
    icon: '🦌',
    description: 'Festive reindeer antlers'
  },
  {
    id: 'frosty-beard',
    name: 'Frosty Beard',
    icon: '🧔‍♂️',
    description: 'Icy winter beard'
  },
  {
    id: 'sparkle-effect',
    name: 'Winter Sparkles',
    icon: '✨',
    description: 'Magical winter sparkles around you'
  }
];

export function FilterManager({
  canvasRef,
  videoRef,
  selectedFilter,
  detectedFaces,
  coordinateSystem,
  isActive
}: FilterManagerProps) {
  const filtersRef = useRef(new Map<string, FilterRenderer>());
  const animationFrameRef = useRef<number | undefined>();
  
  // Debug filter manager state
  console.log('FilterManager render:', {
    selectedFilter,
    isActive,
    hasCanvas: !!canvasRef.current,
    hasVideo: !!videoRef.current,
    hasCoordinateSystem: !!coordinateSystem,
    facesCount: detectedFaces.length,
    canvasSize: canvasRef.current ? `${canvasRef.current.width}x${canvasRef.current.height}` : 'none'
  });
  
  // Initialize filter renderers
  useEffect(() => {
    const filters = new Map<string, FilterRenderer>();
    
    filters.set('snowflake-crown', new SnowflakeCrownFilter());
    filters.set('reindeer-antlers', new ReindeerAntlersFilter());
    filters.set('frosty-beard', new FrostyBeardFilter());
    filters.set('sparkle-effect', new SparkleEffectFilter());
    
    filtersRef.current = filters;
    
    // Cleanup on unmount
    return () => {
      filters.forEach(filter => {
        if (filter.cleanup) {
          filter.cleanup();
        }
      });
    };
  }, []); // eslint-disable-line react-hooks/exhaustive-deps
  
  // Render function
  const renderFrame = useCallback(() => {
    const canvas = canvasRef.current;
    const video = videoRef.current;
    
    if (!canvas || !video || !coordinateSystem || !isActive) {
      console.log('🎨 Filter render skipped:', {
        hasCanvas: !!canvas,
        hasVideo: !!video,
        hasCoordinateSystem: !!coordinateSystem,
        isActive
      });
      if (isActive && selectedFilter) {
        animationFrameRef.current = requestAnimationFrame(renderFrame);
      }
      return;
    }
    
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    
    // Set canvas size to match coordinate system
    const logicalWidth = coordinateSystem.canvas.width;
    const logicalHeight = coordinateSystem.canvas.height;
    const devicePixelRatio = coordinateSystem.devicePixelRatio;
    
    // Set the display size (CSS pixels)
    canvas.style.width = logicalWidth + 'px';
    canvas.style.height = logicalHeight + 'px';
    
    // Set the actual size in memory (physical pixels)
    if (canvas.width !== logicalWidth * devicePixelRatio || 
        canvas.height !== logicalHeight * devicePixelRatio) {
      canvas.width = logicalWidth * devicePixelRatio;
      canvas.height = logicalHeight * devicePixelRatio;
      
      // Scale the context back to logical pixels
      ctx.scale(devicePixelRatio, devicePixelRatio);
      
      console.log('📏 Canvas resized to:', canvas.width, 'x', canvas.height, 'physical pixels,', logicalWidth, 'x', logicalHeight, 'logical pixels');
    }
    
    // Clear canvas (use logical dimensions)
    ctx.clearRect(0, 0, logicalWidth, logicalHeight);
    
    // Debug info (can be removed in production)
    if (process.env.NODE_ENV === 'development') {
      ctx.save();
      ctx.fillStyle = 'rgba(0, 0, 255, 0.1)';
      ctx.fillRect(5, 5, 250, 30);
      ctx.fillStyle = 'white';
      ctx.font = '12px Arial';
      ctx.fillText(`Filter: ${selectedFilter || 'none'} | Faces: ${detectedFaces.length}`, 10, 25);
      ctx.restore();
    }
    
    // Render selected filter if any
    if (selectedFilter && filtersRef.current.has(selectedFilter)) {
      const filter = filtersRef.current.get(selectedFilter)!;
      console.log('🎨 Rendering filter:', selectedFilter, 'with', detectedFaces.length, 'faces');
      filter.render(ctx, detectedFaces, coordinateSystem, performance.now());
    } else if (selectedFilter) {
      // Draw a test shape to verify filter rendering is being called
      ctx.save();
      ctx.fillStyle = 'rgba(255, 0, 0, 0.5)';
      ctx.fillRect(50, 50, 100, 100);
      ctx.fillStyle = 'white';
      ctx.font = '16px Arial';
      ctx.fillText('FILTER AREA', 60, 100);
      ctx.restore();
    }
    
    // Continue animation
    animationFrameRef.current = requestAnimationFrame(renderFrame);
  }, [canvasRef, videoRef, selectedFilter, detectedFaces, coordinateSystem, isActive]);
  
  // Start/stop rendering
  useEffect(() => {
    console.log('🔄 FilterManager effect triggered:', { isActive, selectedFilter, hasCoordinateSystem: !!coordinateSystem });
    
    if (isActive && selectedFilter && coordinateSystem) {
      console.log('🎨 Starting filter rendering...');
      renderFrame();
    } else {
      console.log('🛑 Stopping filter rendering');
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current);
      }
      // Clear canvas when inactive
      const canvas = canvasRef.current;
      if (canvas) {
        const ctx = canvas.getContext('2d');
        ctx?.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
    
    return () => {
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current);
      }
    };
  }, [isActive, selectedFilter, coordinateSystem, renderFrame]);
  
  return null; // This component only manages rendering, no UI
}
