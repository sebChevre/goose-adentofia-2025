import type { FilterRenderer, DetectedFace } from '../../../types/filters';
import type { CoordinateSystem } from '../../../types/camera';

export class FrostyBeardFilter implements FilterRenderer {
  constructor() {
    // Initialize filter
  }
  
  private beardParticles: Array<{
    x: number;
    y: number;
    size: number;
    opacity: number;
    offsetX: number;
    offsetY: number;
  }> = [];
  
  render(
    ctx: CanvasRenderingContext2D,
    faces: DetectedFace[],
    coordinateSystem: CoordinateSystem,
    timestamp: number
  ): void {
    faces.forEach(face => {
      this.renderBeard(ctx, face, coordinateSystem, timestamp);
    });
  }
  
  private renderBeard(
    ctx: CanvasRenderingContext2D,
    face: DetectedFace,
    coordinateSystem: CoordinateSystem,
    timestamp: number
  ): void {
    const beardArea = this.getBeardArea(face, coordinateSystem);
    if (!beardArea) return;
    
    // Generate beard particles if needed
    if (this.beardParticles.length < 100) {
      this.generateBeardParticles(beardArea);
    }
    
    this.drawBeard(ctx, beardArea, timestamp);
  }
  
  private getBeardArea(face: DetectedFace, coordinateSystem: CoordinateSystem) {
    const bounds = face.boundingBox;
    const faceWidth = bounds.width * coordinateSystem.canvas.width;
    const faceHeight = bounds.height * coordinateSystem.canvas.height;
    
    // Beard area starts from chin area
    const chinY = (bounds.y + bounds.height * 0.7) * coordinateSystem.canvas.height;
    const beardHeight = faceHeight * 0.6;
    
    return {
      x: (bounds.x + bounds.width / 2) * coordinateSystem.canvas.width,
      y: chinY,
      width: faceWidth * 0.7,
      height: beardHeight
    };
  }
  
  private generateBeardParticles(beardArea: { x: number; y: number; width: number; height: number }) {
    this.beardParticles = [];
    
    const particleCount = 100;
    
    for (let i = 0; i < particleCount; i++) {
      // Create beard shape - wider at top, narrower at bottom
      const progress = Math.random();
      const yOffset = progress * beardArea.height;
      const widthAtY = beardArea.width * (1 - progress * 0.3); // Taper towards bottom
      
      // Random position within beard shape
      const angle = (Math.random() - 0.5) * Math.PI;
      const distance = Math.random() * widthAtY / 2;
      
      this.beardParticles.push({
        x: Math.cos(angle) * distance,
        y: yOffset,
        size: 2 + Math.random() * 4,
        opacity: 0.4 + Math.random() * 0.4,
        offsetX: (Math.random() - 0.5) * 20,
        offsetY: (Math.random() - 0.5) * 20
      });
    }
  }
  
  private drawBeard(
    ctx: CanvasRenderingContext2D,
    beardArea: { x: number; y: number; width: number; height: number },
    timestamp: number
  ) {
    ctx.save();
    
    // Create gradient for icy effect
    const gradient = ctx.createRadialGradient(
      beardArea.x, beardArea.y + beardArea.height / 3,
      0,
      beardArea.x, beardArea.y + beardArea.height / 3,
      beardArea.width / 2
    );
    gradient.addColorStop(0, 'rgba(255, 255, 255, 0.9)');
    gradient.addColorStop(0.5, 'rgba(225, 245, 254, 0.7)');
    gradient.addColorStop(1, 'rgba(179, 229, 252, 0.5)');
    
    // Draw main beard shape
    ctx.fillStyle = gradient;
    ctx.beginPath();
    
    // Beard outline - rounded bottom
    const startX = beardArea.x - beardArea.width / 2;
    const endX = beardArea.x + beardArea.width / 2;
    const topY = beardArea.y;
    const bottomY = beardArea.y + beardArea.height;
    
    ctx.moveTo(startX, topY);
    ctx.lineTo(endX, topY);
    ctx.quadraticCurveTo(endX, bottomY - 20, beardArea.x + beardArea.width / 3, bottomY);
    ctx.quadraticCurveTo(beardArea.x, bottomY + 10, beardArea.x - beardArea.width / 3, bottomY);
    ctx.quadraticCurveTo(startX, bottomY - 20, startX, topY);
    
    ctx.fill();
    
    // Add icy texture with particles
    this.beardParticles.forEach(particle => {
      const particleX = beardArea.x + particle.x + particle.offsetX * Math.sin(timestamp * 0.001);
      const particleY = beardArea.y + particle.y + particle.offsetY * Math.cos(timestamp * 0.0015);
      
      ctx.save();
      ctx.globalAlpha = particle.opacity;
      ctx.fillStyle = '#FFFFFF';
      ctx.beginPath();
      ctx.arc(particleX, particleY, particle.size, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    });
    
    // Add icy highlights
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 5]);
    
    // Icicle-like strokes
    for (let i = 0; i < 8; i++) {
      const x = startX + (i / 7) * beardArea.width;
      const length = 10 + Math.random() * 15;
      
      ctx.beginPath();
      ctx.moveTo(x, bottomY - 5);
      ctx.lineTo(x + (Math.random() - 0.5) * 10, bottomY + length);
      ctx.stroke();
    }
    
    ctx.restore();
  }
  
  cleanup(): void {
    this.beardParticles = [];
  }
}
