export class PerformanceMonitor {
  private metrics: Map<string, number[]> = new Map();
  private maxSamples = 100;

  recordMetric(name: string, value: number): void {
    if (!this.metrics.has(name)) {
      this.metrics.set(name, []);
    }

    const samples = this.metrics.get(name)!;
    samples.push(value);

    // Keep only recent samples
    if (samples.length > this.maxSamples) {
      samples.shift();
    }
  }

  getAverage(name: string): number {
    const samples = this.metrics.get(name);
    if (!samples || samples.length === 0) return 0;

    return samples.reduce((sum, value) => sum + value, 0) / samples.length;
  }

  getLatest(name: string): number {
    const samples = this.metrics.get(name);
    if (!samples || samples.length === 0) return 0;

    return samples[samples.length - 1];
  }

  getFPS(name: string = 'frame'): number {
    const avgTime = this.getAverage(name);
    return avgTime > 0 ? 1000 / avgTime : 0;
  }

  clear(name?: string): void {
    if (name) {
      this.metrics.delete(name);
    } else {
      this.metrics.clear();
    }
  }

  getAllMetrics(): Record<string, { average: number; latest: number; fps?: number }> {
    const result: Record<string, any> = {};

    for (const [name, samples] of this.metrics.entries()) {
      if (samples.length > 0) {
        const average = this.getAverage(name);
        result[name] = {
          average,
          latest: this.getLatest(name),
        };

        // Add FPS for timing metrics
        if (name.includes('time') || name === 'frame') {
          result[name].fps = average > 0 ? 1000 / average : 0;
        }
      }
    }

    return result;
  }
}

export class FrameRateThrottler {
  private lastFrameTime = 0;
  private targetInterval: number;

  constructor(targetFPS: number) {
    this.targetInterval = 1000 / targetFPS;
  }

  shouldProcess(currentTime: number): boolean {
    if (currentTime - this.lastFrameTime >= this.targetInterval) {
      this.lastFrameTime = currentTime;
      return true;
    }
    return false;
  }

  setTargetFPS(fps: number): void {
    this.targetInterval = 1000 / fps;
  }

  getTargetFPS(): number {
    return 1000 / this.targetInterval;
  }
}

export class AdaptiveQuality {
  private performanceMonitor: PerformanceMonitor;
  private currentQuality = 1.0;
  private targetProcessingTime = 50; // 50ms target for 20fps
  private adjustmentFactor = 0.1;

  constructor(performanceMonitor: PerformanceMonitor) {
    this.performanceMonitor = performanceMonitor;
  }

  adjustQuality(): number {
    const avgProcessingTime = this.performanceMonitor.getAverage('detection');
    
    if (avgProcessingTime === 0) {
      return this.currentQuality;
    }

    if (avgProcessingTime > this.targetProcessingTime * 1.2) {
      // Performance is poor, reduce quality
      this.currentQuality = Math.max(0.5, this.currentQuality - this.adjustmentFactor);
    } else if (avgProcessingTime < this.targetProcessingTime * 0.8) {
      // Performance is good, increase quality
      this.currentQuality = Math.min(1.0, this.currentQuality + this.adjustmentFactor);
    }

    return this.currentQuality;
  }

  getCurrentQuality(): number {
    return this.currentQuality;
  }

  setTargetProcessingTime(ms: number): void {
    this.targetProcessingTime = ms;
  }

  reset(): void {
    this.currentQuality = 1.0;
  }
}

export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number,
  immediate = false
): (...args: Parameters<T>) => void {
  let timeout: ReturnType<typeof setTimeout> | null = null;
  
  return function executedFunction(...args: Parameters<T>) {
    const later = () => {
      timeout = null;
      if (!immediate) func(...args);
    };

    const callNow = immediate && !timeout;

    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(later, wait);

    if (callNow) func(...args);
  };
}

export function throttle<T extends (...args: any[]) => any>(
  func: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle: boolean;
  
  return function executedFunction(...args: Parameters<T>) {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

export class MemoryMonitor {
  private lastCheck = 0;
  private checkInterval = 5000; // Check every 5 seconds

  checkMemoryUsage(): { used: number; total: number; percentage: number } | null {
    const now = performance.now();
    
    if (now - this.lastCheck < this.checkInterval) {
      return null;
    }

    this.lastCheck = now;

    // Use Performance Memory API if available
    if ('memory' in performance) {
      const memory = (performance as any).memory;
      return {
        used: memory.usedJSHeapSize,
        total: memory.totalJSHeapSize,
        percentage: (memory.usedJSHeapSize / memory.totalJSHeapSize) * 100
      };
    }

    return null;
  }

  shouldReduceQuality(): boolean {
    const memory = this.checkMemoryUsage();
    return memory ? memory.percentage > 80 : false;
  }
}

// Global performance monitor instance
export const globalPerformanceMonitor = new PerformanceMonitor();
export const memoryMonitor = new MemoryMonitor();
