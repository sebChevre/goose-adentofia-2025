import type { FilterRenderer, DetectedFace } from '../../../types/filters';
import type { CoordinateSystem } from '../../../types/camera';

interface Sparkle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  life: number;
  maxLife: number;
  size: number;
  twinkle: number;
  color: string;
  pulseSpeed: number;
}

export class SparkleEffectFilter implements FilterRenderer {
  private sparkles: Sparkle[] = [];
  private lastSparkleTime = 0;
  
  constructor() {
    // Initialize filter
  }
  
  render(
    ctx: CanvasRenderingContext2D,
    faces: DetectedFace[],
    coordinateSystem: CoordinateSystem,
    timestamp: number
  ): void {
    // Generate new sparkles periodically
    if (timestamp - this.lastSparkleTime > 100) {
      this.generateSparkles(faces, coordinateSystem);
      this.lastSparkleTime = timestamp;
    }
    
    // Update and render existing sparkles
    this.updateSparkles(timestamp);
    this.renderSparkles(ctx, timestamp);
  }
  
  private generateSparkles(faces: DetectedFace[], coordinateSystem: CoordinateSystem) {
    faces.forEach(face => {
      // Generate sparkles around face area
      const faceArea = this.getFaceArea(face, coordinateSystem);
      const sparkleCount = 2 + Math.random() * 3;
      
      for (let i = 0; i < sparkleCount; i++) {
        this.createSparkle(faceArea, coordinateSystem);
      }
    });
    
    // Limit total sparkles
    if (this.sparkles.length > 50) {
      this.sparkles = this.sparkles.slice(-50);
    }
  }
  
  private getFaceArea(face: DetectedFace, coordinateSystem: CoordinateSystem) {
    const bounds = face.boundingBox;
    return {
      x: bounds.x * coordinateSystem.canvas.width,
      y: bounds.y * coordinateSystem.canvas.height,
      width: bounds.width * coordinateSystem.canvas.width,
      height: bounds.height * coordinateSystem.canvas.height
    };
  }
  
  private createSparkle(
    faceArea: { x: number; y: number; width: number; height: number },
    _coordinateSystem: CoordinateSystem
  ) {
    // Create sparkles in an area around the face
    const padding = Math.min(faceArea.width, faceArea.height) * 0.3;
    const areaX = faceArea.x - padding;
    const areaY = faceArea.y - padding;
    const areaWidth = faceArea.width + padding * 2;
    const areaHeight = faceArea.height + padding * 2;
    
    const sparkle: Sparkle = {
      x: areaX + Math.random() * areaWidth,
      y: areaY + Math.random() * areaHeight,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      size: 3 + Math.random() * 8,
      life: 1,
      maxLife: 2000 + Math.random() * 3000, // 2-5 seconds
      twinkle: Math.random() * Math.PI * 2,
      color: this.getRandomSparkleColor(),
      pulseSpeed: 0.002 + Math.random() * 0.003
    };
    
    this.sparkles.push(sparkle);
  }
  
  private getRandomSparkleColor(): string {
    const colors = [
      '#FFFFFF', // Pure white
      '#E3F2FD', // Light blue
      '#F8F9FA', // Off white
      '#E8F5E8', // Light mint
      '#FFF8E1', // Light yellow
      '#F3E5F5'  // Light purple
    ];
    return colors[Math.floor(Math.random() * colors.length)];
  }
  
  private updateSparkles(_timestamp: number) {
    this.sparkles = this.sparkles.filter(sparkle => {
      // Update position
      sparkle.x += sparkle.vx;
      sparkle.y += sparkle.vy;
      
      // Update life
      sparkle.life -= 16; // Assume ~60fps
      
      // Update twinkle
      sparkle.twinkle += sparkle.pulseSpeed * 16;
      
      // Keep alive sparkles
      return sparkle.life > 0;
    });
  }
  
  private renderSparkles(ctx: CanvasRenderingContext2D, _timestamp: number) {
    ctx.save();
    
    this.sparkles.forEach(sparkle => {
      const progress = sparkle.life / sparkle.maxLife;
      const twinkleIntensity = (Math.sin(sparkle.twinkle) + 1) / 2;
      
      // Fade out over lifetime
      const alpha = progress * twinkleIntensity;
      
      ctx.save();
      ctx.translate(sparkle.x, sparkle.y);
      ctx.globalAlpha = alpha;
      
      this.drawSparkle(ctx, sparkle);
      
      ctx.restore();
    });
    
    ctx.restore();
  }
  
  private drawSparkle(ctx: CanvasRenderingContext2D, sparkle: Sparkle) {
    const size = sparkle.size;
    
    // Draw 4-pointed star sparkle
    ctx.fillStyle = sparkle.color;
    ctx.strokeStyle = sparkle.color;
    ctx.lineWidth = 1;
    
    ctx.beginPath();
    
    // Main cross
    ctx.moveTo(-size, 0);
    ctx.lineTo(size, 0);
    ctx.moveTo(0, -size);
    ctx.lineTo(0, size);
    
    // Diagonal cross (smaller)
    const diagSize = size * 0.6;
    ctx.moveTo(-diagSize * 0.7, -diagSize * 0.7);
    ctx.lineTo(diagSize * 0.7, diagSize * 0.7);
    ctx.moveTo(diagSize * 0.7, -diagSize * 0.7);
    ctx.lineTo(-diagSize * 0.7, diagSize * 0.7);
    
    ctx.stroke();
    
    // Add center glow
    const gradient = ctx.createRadialGradient(0, 0, 0, 0, 0, size * 0.5);
    gradient.addColorStop(0, sparkle.color);
    gradient.addColorStop(1, 'transparent');
    
    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.arc(0, 0, size * 0.5, 0, Math.PI * 2);
    ctx.fill();
  }
  
  cleanup(): void {
    this.sparkles = [];
  }
}
