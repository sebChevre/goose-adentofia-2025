import type { UseCameraReturn } from '../../types/camera';

interface CameraControlsProps {
  camera: UseCameraReturn;
}

export function CameraControls({ camera }: CameraControlsProps) {
  const { state, actions } = camera;
  
  const handleCameraSwitch = (deviceId: string) => {
    actions.switchCamera(deviceId);
  };
  
  const toggleCamera = () => {
    if (state.isActive) {
      actions.stopCamera();
    } else {
      actions.startCamera();
    }
  };
  
  if (state.permission.state === 'denied') {
    return (
      <div className="camera-controls">
        <button 
          className="camera-controls__button camera-controls__button--permission"
          onClick={actions.requestPermission}
          disabled={!state.permission.canRequest}
        >
          Allow Camera Access
        </button>
      </div>
    );
  }
  
  return (
    <div className="camera-controls">
      <div className="camera-controls__row">
        <button
          className={`camera-controls__button camera-controls__button--toggle ${
            state.isActive ? 'camera-controls__button--stop' : 'camera-controls__button--start'
          }`}
          onClick={toggleCamera}
          disabled={state.isLoading}
        >
          {state.isLoading ? '...' : state.isActive ? 'Stop' : 'Start'}
        </button>
        
        <button
          className="camera-controls__button camera-controls__button--refresh"
          onClick={actions.refreshDevices}
          disabled={state.isLoading}
        >
          ↻
        </button>
      </div>
      
      {state.devices.length > 1 && (
        <div className="camera-controls__row">
          <select
            className="camera-controls__select"
            value={state.selectedDevice?.deviceId || ''}
            onChange={(e) => handleCameraSwitch(e.target.value)}
            disabled={state.isLoading}
          >
            {state.devices.map((device) => (
              <option key={device.deviceId} value={device.deviceId}>
                {device.label}
              </option>
            ))}
          </select>
        </div>
      )}
      
      {state.error && (
        <div className="camera-controls__error">
          {state.error.message}
        </div>
      )}
    </div>
  );
}
