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
      return;
    }
    
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    
    // Set canvas size to match video
    if (canvas.width !== coordinateSystem.canvas.width || 
        canvas.height !== coordinateSystem.canvas.height) {
      canvas.width = coordinateSystem.canvas.width;
      canvas.height = coordinateSystem.canvas.height;
    }
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Render selected filter if any
    if (selectedFilter && filtersRef.current.has(selectedFilter)) {
      const filter = filtersRef.current.get(selectedFilter)!;
      filter.render(ctx, detectedFaces, coordinateSystem, performance.now());
    }
    
    // Continue animation
    animationFrameRef.current = requestAnimationFrame(renderFrame);
  }, [canvasRef, videoRef, selectedFilter, detectedFaces, coordinateSystem, isActive]);
  
  // Start/stop rendering
  useEffect(() => {
    if (isActive && selectedFilter) {
      renderFrame();
    } else {
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
  }, [isActive, selectedFilter, renderFrame]);
  
  return null; // This component only manages rendering, no UI
}
