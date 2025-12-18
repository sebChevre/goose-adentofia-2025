import type { CoordinateSystem, Point } from '../types/camera';

export function calculateCoordinateSystem(
  video: HTMLVideoElement,
  canvas: HTMLCanvasElement
): CoordinateSystem {
  const canvasRect = canvas.getBoundingClientRect();
  const devicePixelRatio = window.devicePixelRatio || 1;
  
  // Use the logical size for coordinate system calculations
  const canvasWidth = canvasRect.width;
  const canvasHeight = canvasRect.height;
  const videoWidth = video.videoWidth;
  const videoHeight = video.videoHeight;
  
  // Calculate scale to maintain aspect ratio
  const scaleX = canvasWidth / videoWidth;
  const scaleY = canvasHeight / videoHeight;
  const scale = Math.max(scaleX, scaleY);
  
  // Calculate centering offsets
  const scaledWidth = videoWidth * scale;
  const scaledHeight = videoHeight * scale;
  const offsetX = (canvasWidth - scaledWidth) / 2;
  const offsetY = (canvasHeight - scaledHeight) / 2;
  
  return {
    canvasWidth,
    canvasHeight,
    videoWidth,
    videoHeight,
    canvas: {
      width: canvasWidth, // Use logical size for calculations
      height: canvasHeight
    },
    devicePixelRatio,
    scale,
    offsetX,
    offsetY
  };
}

export function screenToVideoCoordinates(
  screenPoint: Point,
  coordinateSystem: CoordinateSystem
): Point {
  const { scale, offsetX, offsetY } = coordinateSystem;
  
  return {
    x: (screenPoint.x - offsetX) / scale,
    y: (screenPoint.y - offsetY) / scale
  };
}

export function videoToScreenCoordinates(
  videoPoint: Point,
  coordinateSystem: CoordinateSystem
): Point {
  const { scale, offsetX, offsetY } = coordinateSystem;
  
  return {
    x: videoPoint.x * scale + offsetX,
    y: videoPoint.y * scale + offsetY
  };
}

export function isPointInVideoArea(
  point: Point,
  coordinateSystem: CoordinateSystem
): boolean {
  const { offsetX, offsetY, scale, videoWidth, videoHeight } = coordinateSystem;
  
  return (
    point.x >= offsetX &&
    point.x <= offsetX + videoWidth * scale &&
    point.y >= offsetY &&
    point.y <= offsetY + videoHeight * scale
  );
}
