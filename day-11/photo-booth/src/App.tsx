import { useState } from 'react';
import { CameraView } from './components/Camera/CameraView';
import { FilterSelector } from './components/Filters/FilterSelector';
import { FilterManager, WINTER_FILTERS } from './components/Filters/FilterManager';
import { CaptureButton } from './components/Capture/CaptureButton';
import { PhotoPreview } from './components/Capture/PhotoPreview';
import { useCamera } from './hooks/useCamera';
import { useFaceDetection } from './hooks/useFaceDetection';
import { usePhotoCapture } from './hooks/usePhotoCapture';
import type { CoordinateSystem } from './types/camera';
import './App.css';

function App() {
  const [selectedFilter, setSelectedFilter] = useState<string | null>(null);
  const [coordinateSystem, setCoordinateSystem] = useState<CoordinateSystem | null>(null);
  
  const camera = useCamera();
  const faceDetection = useFaceDetection(camera.refs.videoRef, coordinateSystem);
  const photoCapture = usePhotoCapture();
  
  // Debug: Log filter changes
  console.log('Selected filter:', selectedFilter);
  
  const handleCapture = async () => {
    await photoCapture.capturePhoto(
      camera.refs.videoRef,
      camera.refs.canvasRef,
      coordinateSystem
    );
  };
  
  return (
    <div className="app">
      <header className="app-header">
        <h1>🎿 Winter Photo Booth ❄️</h1>
      </header>
      
      <main className="app-main">
        <div className="camera-container">
          <CameraView 
            camera={camera}
            onCoordinateSystemChange={setCoordinateSystem}
            showControls={true}
          />
          
          <FilterManager
            canvasRef={camera.refs.canvasRef}
            videoRef={camera.refs.videoRef}
            selectedFilter={selectedFilter}
            detectedFaces={faceDetection.detectedFaces}
            coordinateSystem={coordinateSystem}
            isActive={camera.state.isActive}
          />
        </div>
        
        {camera.state.isActive && (
          <>
            <FilterSelector
              filters={WINTER_FILTERS}
              selectedFilter={selectedFilter}
              onFilterSelect={setSelectedFilter}
              className="app-filters"
            />
            
            <CaptureButton
              onCapture={handleCapture}
              disabled={!camera.state.isActive || photoCapture.state.isCapturing}
              className="app-capture"
            />
          </>
        )}
        

        
        {camera.state.error && (
          <div className="app-error">
            <p>Camera Error: {camera.state.error.message}</p>
            <button onClick={() => camera.actions.startCamera()}>
              Try Again
            </button>
          </div>
        )}
        
        {photoCapture.state.error && (
          <div className="app-error">
            <p>Capture Error: {photoCapture.state.error}</p>
          </div>
        )}
      </main>
      
      <PhotoPreview
        photoUrl={photoCapture.state.capturedPhoto}
        onClose={photoCapture.clearPhoto}
        onSave={photoCapture.savePhoto}
        onShare={photoCapture.sharePhoto}
      />
    </div>
  );
}

export default App
