import type { FilterRenderer, DetectedFace } from '../../../types/filters';
import type { CoordinateSystem } from '../../../types/camera';

interface Snowflake {
  x: number;
  y: number;
  vx: number;
  vy: number;
  life: number;
  maxLife: number;
  size: number;
  rotation: number;
  rotationSpeed: number;
  opacity: number;
}

export class SnowflakeCrownFilter implements FilterRenderer {
  private snowflakes: Snowflake[] = [];
  private lastUpdate = 0;
  
  constructor() {
    // Initialize filter
  }
  
  render(
    ctx: CanvasRenderingContext2D,
    faces: DetectedFace[],
    coordinateSystem: CoordinateSystem,
    timestamp: number
  ): void {
    const deltaTime = timestamp - this.lastUpdate;
    this.lastUpdate = timestamp;
    
    faces.forEach(face => {
      this.renderCrown(ctx, face, coordinateSystem, deltaTime);
    });
  }
  
  private renderCrown(
    ctx: CanvasRenderingContext2D,
    face: DetectedFace,
    coordinateSystem: CoordinateSystem,
    deltaTime: number
  ): void {
    // Get head position (top of face)
    const headTop = this.getHeadTop(face, coordinateSystem);
    if (!headTop) return;
    
    // Create crown snowflakes if needed
    if (this.snowflakes.length < 12) {
      this.createCrownSnowflakes(headTop);
    }
    
    // Update and render snowflakes
    this.updateSnowflakes(deltaTime);
    this.drawSnowflakes(ctx, headTop);
  }
  
  private getHeadTop(face: DetectedFace, coordinateSystem: CoordinateSystem) {
    // Use forehead landmarks or face bounds
    const bounds = face.boundingBox;
    const faceWidth = bounds.width * coordinateSystem.canvas.width;
    const faceHeight = bounds.height * coordinateSystem.canvas.height;
    
    return {
      x: (bounds.x + bounds.width / 2) * coordinateSystem.canvas.width,
      y: bounds.y * coordinateSystem.canvas.height - faceHeight * 0.2, // Above forehead
      width: faceWidth
    };
  }
  
  private createCrownSnowflakes(headPosition: { x: number; y: number; width: number }) {
    const crownRadius = headPosition.width * 0.6;
    const snowflakeCount = 12;
    
    this.snowflakes = [];
    
    for (let i = 0; i < snowflakeCount; i++) {
      const angle = (i / snowflakeCount) * Math.PI * 2;
      const radius = crownRadius * (0.8 + Math.random() * 0.4); // Vary radius
      
      this.snowflakes.push({
        x: headPosition.x + Math.cos(angle) * radius,
        y: headPosition.y + Math.sin(angle) * radius * 0.3, // Flatter crown shape
        vx: 0,
        vy: 0,
        size: 12 + Math.random() * 8,
        rotation: Math.random() * Math.PI * 2,
        rotationSpeed: (Math.random() - 0.5) * 0.02,
        opacity: 0.8 + Math.random() * 0.2,
        life: 1,
        maxLife: 1
      });
    }
  }
  
  private updateSnowflakes(deltaTime: number) {
    this.snowflakes.forEach(snowflake => {
      snowflake.rotation += snowflake.rotationSpeed * deltaTime;
      
      // Gentle floating motion
      snowflake.y += Math.sin(performance.now() * 0.001 + snowflake.x * 0.01) * 0.1;
    });
  }
  
  private drawSnowflakes(ctx: CanvasRenderingContext2D, _headPosition: { x: number; y: number }) {
    ctx.save();
    
    this.snowflakes.forEach(snowflake => {
      ctx.save();
      ctx.translate(snowflake.x, snowflake.y);
      ctx.rotate(snowflake.rotation);
      ctx.globalAlpha = snowflake.opacity;
      
      this.drawSnowflake(ctx, snowflake.size);
      
      ctx.restore();
    });
    
    ctx.restore();
  }
  
  private drawSnowflake(ctx: CanvasRenderingContext2D, size: number) {
    const arms = 6;
    const armLength = size;
    
    ctx.strokeStyle = '#E3F2FD';
    ctx.fillStyle = '#FFFFFF';
    ctx.lineWidth = 2;
    
    // Draw snowflake arms
    for (let i = 0; i < arms; i++) {
      ctx.save();
      ctx.rotate((i * Math.PI * 2) / arms);
      
      // Main arm
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(armLength, 0);
      ctx.stroke();
      
      // Side branches
      ctx.beginPath();
      ctx.moveTo(armLength * 0.7, 0);
      ctx.lineTo(armLength * 0.9, -armLength * 0.2);
      ctx.moveTo(armLength * 0.7, 0);
      ctx.lineTo(armLength * 0.9, armLength * 0.2);
      ctx.stroke();
      
      ctx.restore();
    }
    
    // Center circle
    ctx.beginPath();
    ctx.arc(0, 0, size * 0.15, 0, Math.PI * 2);
    ctx.fill();
  }
  
  cleanup(): void {
    this.snowflakes = [];
  }
}
