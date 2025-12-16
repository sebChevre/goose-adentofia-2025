import { useState } from 'react';

interface CaptureButtonProps {
  onCapture: () => Promise<void>;
  disabled?: boolean;
  className?: string;
}

export function CaptureButton({ onCapture, disabled = false, className = '' }: CaptureButtonProps) {
  const [isCapturing, setIsCapturing] = useState(false);
  
  const handleCapture = async () => {
    if (isCapturing || disabled) return;
    
    setIsCapturing(true);
    try {
      await onCapture();
    } finally {
      setIsCapturing(false);
    }
  };
  
  return (
    <button
      className={`capture-button ${isCapturing ? 'capture-button--capturing' : ''} ${className}`}
      onClick={handleCapture}
      disabled={disabled || isCapturing}
    >
      <div className="capture-button__ring">
        <div className="capture-button__inner">
          {isCapturing ? (
            <div className="capture-button__spinner" />
          ) : (
            <span className="capture-button__icon">📸</span>
          )}
        </div>
      </div>
      <span className="capture-button__label">
        {isCapturing ? 'Capturing...' : 'Capture Photo'}
      </span>
    </button>
  );
}
