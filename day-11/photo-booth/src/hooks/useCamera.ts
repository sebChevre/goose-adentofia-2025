import { useState, useEffect, useRef, useCallback } from 'react';
import type { CameraState, UseCameraReturn } from '../types/camera';
import { CameraManager } from '../services/camera/CameraManager';

const initialState: CameraState = {
  stream: null,
  devices: [],
  selectedDevice: null,
  isLoading: false,
  permission: { state: 'unknown', canRequest: true },
  error: null,
  isActive: false
};

export function useCamera(): UseCameraReturn {
  const [state, setState] = useState<CameraState>(initialState);
  const cameraManager = useRef(new CameraManager());
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  
  const updateState = useCallback((updates: Partial<CameraState>) => {
    console.log('updateState called with:', updates);
    setState(prev => {
      const newState = { ...prev, ...updates };
      console.log('Camera state updated:', { 
        wasActive: prev.isActive, 
        nowActive: newState.isActive,
        hasStream: !!newState.stream 
      });
      // Force log the actual state that will be returned
      console.log('FINAL STATE BEING SET:', newState);
      return newState;
    });
  }, []);
  
  const checkPermission = useCallback(async () => {
    const permission = await cameraManager.current.checkPermission();
    updateState({ permission });
    return permission.state === 'granted';
  }, [updateState]);
  
  const requestPermission = useCallback(async (): Promise<boolean> => {
    updateState({ isLoading: true, error: null });
    
    try {
      const granted = await cameraManager.current.requestPermission();
      const permission = await cameraManager.current.checkPermission();
      updateState({ permission, isLoading: false });
      return granted;
    } catch (error) {
      updateState({ 
        isLoading: false,
        error: {
          code: 'PERMISSION_DENIED',
          message: 'Failed to request camera permission',
          name: 'PermissionError'
        }
      });
      return false;
    }
  }, [updateState]);
  
  const refreshDevices = useCallback(async () => {
    try {
      const devices = await cameraManager.current.enumerateDevices();
      const savedDevice = cameraManager.current.getSelectedDevice();
      
      // Find saved device in current devices list
      const selectedDevice = savedDevice 
        ? devices.find(d => d.deviceId === savedDevice.deviceId) || null
        : devices.find(d => d.facingMode === 'environment') || devices[0] || null;
      
      updateState({ devices, selectedDevice });
    } catch (error) {
      console.error('Failed to enumerate devices:', error);
    }
  }, [updateState]);
  
  const startCamera = useCallback(async (deviceId?: string): Promise<boolean> => {
    console.log('startCamera called with deviceId:', deviceId);
    
    return new Promise<boolean>((resolve) => {
      setState(currentState => {
        console.log('startCamera setState called, currentState.isActive:', currentState.isActive);
        
        const targetDeviceId = deviceId || currentState.selectedDevice?.deviceId;
        console.log('Starting camera with targetDeviceId:', targetDeviceId);
        
        // Async camera start
        (async () => {
          try {
            const stream = await cameraManager.current.startCamera(targetDeviceId);
            console.log('Camera stream obtained:', stream);
            
            // Update video element
            if (videoRef.current) {
              videoRef.current.srcObject = stream;
              await new Promise<void>((videoResolve) => {
                const video = videoRef.current!;
                const onLoadedMetadata = () => {
                  video.removeEventListener('loadedmetadata', onLoadedMetadata);
                  console.log('Video metadata loaded');
                  videoResolve();
                };
                video.addEventListener('loadedmetadata', onLoadedMetadata);
              });
            }
            
            console.log('Setting camera as active');
            setState(prevState => ({
              ...prevState,
              stream,
              isActive: true,
              isLoading: false,
              error: null
            }));
            
            resolve(true);
          } catch (error: any) {
            console.error('Camera start failed:', error);
            setState(prevState => ({
              ...prevState,
              stream: null,
              isLoading: false,
              isActive: false,
              error: {
                code: error.code || 'UNKNOWN',
                message: error.message || 'Failed to start camera',
                name: error.name || 'CameraError'
              }
            }));
            
            resolve(false);
          }
        })();
        
        return {
          ...currentState,
          isLoading: true,
          error: null
        };
      });
    });
  }, []);
  
  const stopCamera = useCallback(() => {
    cameraManager.current.stopCamera();
    
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
    
    updateState({ 
      stream: null, 
      isActive: false,
      error: null
    });
  }, [updateState]);
  
  const switchCamera = useCallback(async (deviceId: string): Promise<boolean> => {
    setState(currentState => {
      const device = currentState.devices.find(d => d.deviceId === deviceId);
      if (!device) return currentState;
      
      // Save selection
      cameraManager.current.saveSelectedDevice(device);
      
      // Restart camera with new device (async)
      if (currentState.isActive) {
        startCamera(deviceId);
      }
      
      return { ...currentState, selectedDevice: device };
    });
    
    return true;
  }, [startCamera]);
  
  // Initialize on mount
  useEffect(() => {
    const initialize = async () => {
      await checkPermission();
      await refreshDevices();
    };
    
    initialize();
  }, [checkPermission, refreshDevices]);
  
  // Handle device changes
  useEffect(() => {
    const handleDeviceChange = () => {
      refreshDevices();
    };
    
    navigator.mediaDevices.addEventListener('devicechange', handleDeviceChange);
    return () => {
      navigator.mediaDevices.removeEventListener('devicechange', handleDeviceChange);
    };
  }, [refreshDevices]);
  
  // Cleanup on unmount
  useEffect(() => {
    return () => {
      stopCamera();
    };
  }, [stopCamera]);
  
  return {
    state,
    actions: {
      requestPermission,
      startCamera,
      stopCamera,
      switchCamera,
      refreshDevices
    },
    refs: {
      videoRef,
      canvasRef
    }
  };
}
