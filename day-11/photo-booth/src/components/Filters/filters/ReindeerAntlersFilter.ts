import type { FilterRenderer, DetectedFace } from '../../../types/filters';
import type { CoordinateSystem } from '../../../types/camera';

export class ReindeerAntlersFilter implements FilterRenderer {
  constructor() {
    // Initialize filter
  }
  
  render(
    ctx: CanvasRenderingContext2D,
    faces: DetectedFace[],
    coordinateSystem: CoordinateSystem,
    _timestamp: number
  ): void {
    faces.forEach(face => {
      this.renderAntlers(ctx, face, coordinateSystem);
    });
  }
  
  private renderAntlers(
    ctx: CanvasRenderingContext2D,
    face: DetectedFace,
    coordinateSystem: CoordinateSystem
  ): void {
    const headTop = this.getHeadTop(face, coordinateSystem);
    if (!headTop) return;
    
    const antlerWidth = headTop.width * 0.4;
    const antlerHeight = headTop.width * 0.6;
    
    ctx.save();
    
    // Left antler
    this.drawAntler(
      ctx, 
      headTop.x - headTop.width * 0.25, 
      headTop.y - antlerHeight * 0.3,
      antlerWidth,
      antlerHeight,
      false // left side
    );
    
    // Right antler
    this.drawAntler(
      ctx, 
      headTop.x + headTop.width * 0.25, 
      headTop.y - antlerHeight * 0.3,
      antlerWidth,
      antlerHeight,
      true // right side
    );
    
    ctx.restore();
  }
  
  private getHeadTop(face: DetectedFace, coordinateSystem: CoordinateSystem) {
    const bounds = face.boundingBox;
    const faceWidth = bounds.width * coordinateSystem.canvas.width;
    const faceHeight = bounds.height * coordinateSystem.canvas.height;
    
    return {
      x: (bounds.x + bounds.width / 2) * coordinateSystem.canvas.width,
      y: bounds.y * coordinateSystem.canvas.height - faceHeight * 0.1,
      width: faceWidth
    };
  }
  
  private drawAntler(
    ctx: CanvasRenderingContext2D,
    x: number,
    y: number,
    _width: number,
    height: number,
    isRight: boolean
  ) {
    const branchCount = 4;
    const baseAngle = isRight ? -Math.PI / 6 : Math.PI / 6;
    
    ctx.strokeStyle = '#8D6E63';
    ctx.fillStyle = '#6D4C41';
    ctx.lineWidth = 4;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    
    // Main antler stem
    ctx.beginPath();
    ctx.moveTo(x, y);
    
    const stemEndX = x + Math.cos(baseAngle) * height * 0.8;
    const stemEndY = y + Math.sin(baseAngle) * height * 0.8;
    
    ctx.lineTo(stemEndX, stemEndY);
    ctx.stroke();
    
    // Antler branches
    for (let i = 0; i < branchCount; i++) {
      const branchProgress = (i + 1) / (branchCount + 1);
      const branchStartX = x + (stemEndX - x) * branchProgress;
      const branchStartY = y + (stemEndY - y) * branchProgress;
      
      const branchLength = height * 0.3 * (1 - branchProgress * 0.5);
      const branchAngle = baseAngle + (isRight ? -1 : 1) * Math.PI / 4;
      
      const branchEndX = branchStartX + Math.cos(branchAngle) * branchLength;
      const branchEndY = branchStartY + Math.sin(branchAngle) * branchLength;
      
      ctx.beginPath();
      ctx.moveTo(branchStartX, branchStartY);
      ctx.lineTo(branchEndX, branchEndY);
      ctx.stroke();
      
      // Add small points at branch ends
      ctx.beginPath();
      ctx.arc(branchEndX, branchEndY, 3, 0, Math.PI * 2);
      ctx.fill();
    }
    
    // Add main tip
    ctx.beginPath();
    ctx.arc(stemEndX, stemEndY, 4, 0, Math.PI * 2);
    ctx.fill();
  }
  
  cleanup(): void {
    // No cleanup needed for this filter
  }
}
