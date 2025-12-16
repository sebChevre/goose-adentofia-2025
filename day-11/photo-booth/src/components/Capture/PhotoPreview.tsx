import { useState } from 'react';

interface PhotoPreviewProps {
  photoUrl: string | null;
  onClose: () => void;
  onSave: () => void;
  onShare?: () => void;
}

export function PhotoPreview({ photoUrl, onClose, onSave, onShare }: PhotoPreviewProps) {
  const [isSharing, setIsSharing] = useState(false);
  
  if (!photoUrl) return null;
  
  const handleShare = async () => {
    if (!onShare) return;
    
    setIsSharing(true);
    try {
      await onShare();
    } finally {
      setIsSharing(false);
    }
  };
  
  return (
    <div className="photo-preview-overlay">
      <div className="photo-preview">
        <div className="photo-preview__header">
          <h3>Your Winter Photo</h3>
          <button 
            className="photo-preview__close"
            onClick={onClose}
            aria-label="Close preview"
          >
            ✕
          </button>
        </div>
        
        <div className="photo-preview__image-container">
          <img 
            src={photoUrl} 
            alt="Captured photo" 
            className="photo-preview__image"
          />
        </div>
        
        <div className="photo-preview__actions">
          <button 
            className="photo-preview__button photo-preview__button--secondary"
            onClick={onClose}
          >
            Take Another
          </button>
          
          <button 
            className="photo-preview__button photo-preview__button--primary"
            onClick={onSave}
          >
            💾 Save Photo
          </button>
          
          {onShare && (
            <button 
              className="photo-preview__button photo-preview__button--accent"
              onClick={handleShare}
              disabled={isSharing}
            >
              {isSharing ? '📤 Sharing...' : '📱 Share'}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
