import type { FaceDetectionPoint, FaceBoundingBox } from '../../types/detection';
import type { CoordinateSystem } from '../../types/camera';

export class CoordinateMapper {
  /**
   * Convert MediaPipe normalized coordinates to screen coordinates
   */
  static normalizedToScreen(
    point: FaceDetectionPoint,
    coordinateSystem: CoordinateSystem
  ): FaceDetectionPoint {
    const { scale, offsetX, offsetY, videoWidth, videoHeight } = coordinateSystem;
    
    return {
      x: (point.x * videoWidth * scale) + offsetX,
      y: (point.y * videoHeight * scale) + offsetY
    };
  }

  /**
   * Convert MediaPipe normalized bounding box to screen coordinates
   */
  static normalizedBboxToScreen(
    bbox: FaceBoundingBox,
    coordinateSystem: CoordinateSystem
  ): FaceBoundingBox {
    const { scale, offsetX, offsetY, videoWidth, videoHeight } = coordinateSystem;
    
    return {
      x: (bbox.x * videoWidth * scale) + offsetX,
      y: (bbox.y * videoHeight * scale) + offsetY,
      width: bbox.width * videoWidth * scale,
      height: bbox.height * videoHeight * scale
    };
  }

  /**
   * Convert MediaPipe results to normalized coordinates [0,1]
   * MediaPipe face detection returns coordinates in image space
   */
  static mediaPipeToNormalized(
    detection: any,
    imageWidth: number,
    imageHeight: number
  ): { bbox: FaceBoundingBox; keypoints: any } {
    const bbox = detection.boundingBox;
    const landmarks = detection.landmarks;

    const normalizedBbox: FaceBoundingBox = {
      x: bbox.originX / imageWidth,
      y: bbox.originY / imageHeight,
      width: bbox.width / imageWidth,
      height: bbox.height / imageHeight
    };

    const normalizedKeypoints: any = {
      landmarks: landmarks?.map((landmark: any) => ({
        x: landmark.x,
        y: landmark.y
      })) || []
    };

    // Extract key facial points if available
    if (landmarks && landmarks.length >= 468) {
      // MediaPipe face mesh landmark indices
      const LEFT_EYE_INDEX = 33;
      const RIGHT_EYE_INDEX = 362;
      const NOSE_TIP_INDEX = 1;
      const MOUTH_CENTER_INDEX = 13;

      normalizedKeypoints.leftEye = {
        x: landmarks[LEFT_EYE_INDEX].x,
        y: landmarks[LEFT_EYE_INDEX].y
      };

      normalizedKeypoints.rightEye = {
        x: landmarks[RIGHT_EYE_INDEX].x,
        y: landmarks[RIGHT_EYE_INDEX].y
      };

      normalizedKeypoints.nose = {
        x: landmarks[NOSE_TIP_INDEX].x,
        y: landmarks[NOSE_TIP_INDEX].y
      };

      normalizedKeypoints.mouth = {
        x: landmarks[MOUTH_CENTER_INDEX].x,
        y: landmarks[MOUTH_CENTER_INDEX].y
      };
    }

    return { bbox: normalizedBbox, keypoints: normalizedKeypoints };
  }

  /**
   * Check if a normalized point is within valid bounds
   */
  static isValidNormalizedPoint(point: FaceDetectionPoint): boolean {
    return point.x >= 0 && point.x <= 1 && point.y >= 0 && point.y <= 1;
  }

  /**
   * Check if a normalized bounding box is valid
   */
  static isValidNormalizedBbox(bbox: FaceBoundingBox): boolean {
    return (
      bbox.x >= 0 && 
      bbox.y >= 0 && 
      bbox.x + bbox.width <= 1 && 
      bbox.y + bbox.height <= 1 &&
      bbox.width > 0 && 
      bbox.height > 0
    );
  }

  /**
   * Calculate the center point of a bounding box
   */
  static getBboxCenter(bbox: FaceBoundingBox): FaceDetectionPoint {
    return {
      x: bbox.x + bbox.width / 2,
      y: bbox.y + bbox.height / 2
    };
  }

  /**
   * Calculate the area of a bounding box
   */
  static getBboxArea(bbox: FaceBoundingBox): number {
    return bbox.width * bbox.height;
  }

  /**
   * Check if two bounding boxes overlap
   */
  static doBboxesOverlap(bbox1: FaceBoundingBox, bbox2: FaceBoundingBox): boolean {
    return !(
      bbox1.x + bbox1.width < bbox2.x ||
      bbox2.x + bbox2.width < bbox1.x ||
      bbox1.y + bbox1.height < bbox2.y ||
      bbox2.y + bbox2.height < bbox1.y
    );
  }

  /**
   * Calculate IoU (Intersection over Union) of two bounding boxes
   */
  static calculateIoU(bbox1: FaceBoundingBox, bbox2: FaceBoundingBox): number {
    if (!this.doBboxesOverlap(bbox1, bbox2)) {
      return 0;
    }

    const intersectionX = Math.max(bbox1.x, bbox2.x);
    const intersectionY = Math.max(bbox1.y, bbox2.y);
    const intersectionWidth = Math.min(bbox1.x + bbox1.width, bbox2.x + bbox2.width) - intersectionX;
    const intersectionHeight = Math.min(bbox1.y + bbox1.height, bbox2.y + bbox2.height) - intersectionY;

    const intersectionArea = intersectionWidth * intersectionHeight;
    const union = this.getBboxArea(bbox1) + this.getBboxArea(bbox2) - intersectionArea;

    return union === 0 ? 0 : intersectionArea / union;
  }
}
