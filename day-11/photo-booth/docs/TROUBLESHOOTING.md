# Troubleshooting Guide

This guide helps resolve common issues when using the Fun House Photo Booth application.

## 📷 Camera Permission Issues

### Chrome Desktop

**Problem**: Camera permission denied
```
DOMException: Permission denied
```

**Solutions**:
1. **Check browser settings**
   - Go to `chrome://settings/content/camera`
   - Ensure site is not blocked
   - Remove site from blocked list if present

2. **Reset permissions**
   - Click the camera icon in address bar
   - Select "Always allow" or "Allow"
   - Refresh the page

3. **Clear browser data**
   ```
   Settings → Privacy and Security → Clear browsing data
   Select: Cookies, Site data, Cached images
   ```

### Firefox Desktop

**Problem**: Camera access blocked
```
NotAllowedError: The request is not allowed
```

**Solutions**:
1. **Check permissions**
   - Click the camera icon in address bar
   - Select "Allow" and "Remember this decision"

2. **Reset permissions**
   - Go to `about:preferences#privacy`
   - Scroll to Permissions → Camera
   - Find your site and remove or change to "Allow"

### Safari Desktop

**Problem**: Camera permission prompt not appearing

**Solutions**:
1. **Enable camera access**
   - Safari → Preferences → Websites → Camera
   - Set to "Allow" for your site

2. **Reset website settings**
   - Safari → Preferences → Privacy
   - Click "Manage Website Data"
   - Remove your site and refresh

## 📱 Mobile Browser Issues

### iOS Safari

**Problem**: Camera not working at all
```
NotSupportedError: The operation is not supported
```

**Critical Requirements**:
1. **HTTPS is mandatory**
   - HTTP will NOT work on iOS Safari
   - Use `localhost` for development
   - Deploy with SSL certificate

2. **User gesture required**
   ```typescript
   // ❌ Won't work - no user interaction
   useEffect(() => {
     getUserMedia();
   }, []);

   // ✅ Works - triggered by user action
   const handleClick = () => {
     getUserMedia();
   };
   ```

**Solutions**:
1. **Check iOS version**
   - iOS 11+ required for WebRTC
   - Update iOS if below version 11

2. **Verify HTTPS**
   ```bash
   # Check if site is served over HTTPS
   window.location.protocol === 'https:'
   ```

3. **Test with minimal code**
   ```typescript
   const testCamera = async () => {
     try {
       const stream = await navigator.mediaDevices.getUserMedia({
         video: { facingMode: 'user' }
       });
       console.log('Camera working!');
       stream.getTracks().forEach(track => track.stop());
     } catch (error) {
       console.error('Camera failed:', error);
     }
   };
   ```

### Android Chrome

**Problem**: Camera permission works but video is black

**Solutions**:
1. **Check constraints**
   ```typescript
   const constraints = {
     video: {
       width: { ideal: 1280 },
       height: { ideal: 720 },
       facingMode: 'user'
     }
   };
   ```

2. **Fallback constraints**
   ```typescript
   const fallbackConstraints = {
     video: true // Minimal constraints
   };
   ```

## 🎥 Camera Selection Issues

### Multiple Cameras Not Detected

**Problem**: Only one camera available when device has multiple

**Solutions**:
1. **Enumerate devices properly**
   ```typescript
   const getAvailableCameras = async () => {
     try {
       // Request permissions first
       await navigator.mediaDevices.getUserMedia({ video: true });
       
       // Then enumerate devices
       const devices = await navigator.mediaDevices.enumerateDevices();
       const cameras = devices.filter(device => device.kind === 'videoinput');
       
       return cameras;
     } catch (error) {
       console.error('Error enumerating cameras:', error);
       return [];
     }
   };
   ```

2. **Check device labels**
   ```typescript
   // Labels only available after permission granted
   const stream = await navigator.mediaDevices.getUserMedia({ video: true });
   const devices = await navigator.mediaDevices.enumerateDevices();
   
   // Stop the stream
   stream.getTracks().forEach(track => track.stop());
   ```

### Camera Selection Not Persisting

**Problem**: Selected camera resets on page reload

**Solution**: Implement persistence
```typescript
const CAMERA_STORAGE_KEY = 'goose-camera-selected-device';

const saveSelectedCamera = (deviceId: string) => {
  localStorage.setItem(CAMERA_STORAGE_KEY, deviceId);
};

const getSelectedCamera = (): string | null => {
  return localStorage.getItem(CAMERA_STORAGE_KEY);
};

const selectCamera = async (deviceId: string) => {
  try {
    const constraints = {
      video: { deviceId: { exact: deviceId } }
    };
    
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    saveSelectedCamera(deviceId);
    
    return stream;
  } catch (error) {
    // Fallback to default camera
    console.warn('Selected camera not available, using default');
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    return stream;
  }
};
```

## 🎭 Face Detection Issues

### MediaPipe Not Loading

**Problem**: Face detection model fails to load
```
Error loading MediaPipe model
```

**Solutions**:
1. **Check network connectivity**
   - Ensure internet connection
   - Check if CDN is accessible
   - Try different network (mobile data vs WiFi)

2. **CDN configuration**
   ```typescript
   const detector = new FaceDetection({
     locateFile: (file: string) => {
       // Try multiple CDN sources
       return `https://cdn.jsdelivr.net/npm/@mediapipe/face_detection/${file}`;
     }
   });
   ```

3. **HTTPS requirement**
   - MediaPipe requires secure context
   - Ensure site is served over HTTPS

### Low Detection Performance

**Problem**: Face detection is slow or choppy

**Solutions**:
1. **Adjust detection frequency**
   ```typescript
   const useFaceDetection = (videoRef, options = {}) => {
     const { throttleMs = 100 } = options; // Reduce frequency
     // ... detection logic
   };
   ```

2. **Optimize video resolution**
   ```typescript
   const constraints = {
     video: {
       width: { max: 640 },  // Reduce for performance
       height: { max: 480 },
       frameRate: { max: 15 } // Lower frame rate
     }
   };
   ```

3. **Check device performance**
   ```typescript
   const isLowEndDevice = () => {
     return navigator.hardwareConcurrency <= 2 || 
            (navigator as any).deviceMemory <= 2;
   };
   ```

### No Faces Detected

**Problem**: Face detection not finding faces

**Solutions**:
1. **Lighting conditions**
   - Ensure adequate lighting
   - Avoid backlighting
   - Test in different lighting conditions

2. **Camera positioning**
   - Face should be centered in frame
   - Maintain reasonable distance from camera
   - Ensure face is not partially obscured

3. **Detection thresholds**
   ```typescript
   const detectionOptions = {
     minDetectionConfidence: 0.3, // Lower threshold
     minTrackingConfidence: 0.3,
     maxNumFaces: 1 // Reduce for performance
   };
   ```

## 🎨 Filter Rendering Issues

### Filters Not Appearing

**Problem**: AR filters not visible on face

**Solutions**:
1. **Check coordinate mapping**
   ```typescript
   const coordinateSystem = calculateCoordinateSystem(video, canvas);
   console.log('Coordinate system:', coordinateSystem);
   ```

2. **Verify face detection data**
   ```typescript
   if (faceData && faceData.x && faceData.y) {
     console.log('Face detected at:', faceData.x, faceData.y);
   } else {
     console.log('No valid face data');
   }
   ```

3. **Debug filter rendering**
   ```typescript
   const debugFilter = (ctx: CanvasRenderingContext2D, face: FaceData) => {
     // Draw debug rectangle
     ctx.strokeStyle = 'red';
     ctx.strokeRect(face.x, face.y, face.width, face.height);
   };
   ```

### Poor Filter Performance

**Problem**: Filters cause lag or dropped frames

**Solutions**:
1. **Optimize particle systems**
   ```typescript
   const maxParticles = isLowEndDevice() ? 5 : 10;
   const updateFrequency = isLowEndDevice() ? 2 : 1; // Skip frames
   ```

2. **Reduce rendering complexity**
   ```typescript
   // Use simpler shapes on low-end devices
   const useSimpleShapes = (navigator as any).deviceMemory < 4;
   ```

3. **Canvas optimization**
   ```typescript
   // Clear only necessary areas
   const clearRect = (ctx: CanvasRenderingContext2D, area: Rect) => {
     ctx.clearRect(area.x, area.y, area.width, area.height);
   };
   ```

## 📸 Photo Capture Issues

### Capture Not Working

**Problem**: Photo capture button doesn't respond

**Solutions**:
1. **Check dependencies**
   ```typescript
   const canCapture = videoRef.current && 
                     videoRef.current.videoWidth > 0 &&
                     videoRef.current.videoHeight > 0;
   ```

2. **Verify canvas context**
   ```typescript
   const canvas = document.createElement('canvas');
   const ctx = canvas.getContext('2d');
   if (!ctx) {
     throw new Error('Canvas not supported');
   }
   ```

3. **Check video element state**
   ```typescript
   const videoElement = videoRef.current;
   if (videoElement.readyState !== 4) {
     console.log('Video not ready for capture');
     return;
   }
   ```

### Low Quality Captures

**Problem**: Captured images are blurry or low resolution

**Solutions**:
1. **Use video dimensions**
   ```typescript
   const captureHighRes = () => {
     const video = videoRef.current;
     canvas.width = video.videoWidth;  // Use native resolution
     canvas.height = video.videoHeight;
     // ... capture logic
   };
   ```

2. **Adjust capture quality**
   ```typescript
   const captureOptions = {
     format: 'png', // Higher quality than JPEG
     quality: 0.95   // Maximum quality
   };
   ```

## 🔧 Performance Issues

### High CPU Usage

**Problem**: Browser becomes slow when camera is active

**Solutions**:
1. **Optimize video element**
   ```typescript
   const videoElement = useRef<HTMLVideoElement>(null);
   
   useEffect(() => {
     if (videoElement.current) {
       // Reduce video size for better performance
       videoElement.current.width = 640;
       videoElement.current.height = 480;
       
       // Disable unnecessary features
       videoElement.current.controls = false;
       videoElement.current.autoplay = true;
       videoElement.current.muted = true;
     }
   }, []);
   ```

2. **Stop streams when not needed**
   ```typescript
   useEffect(() => {
     return () => {
       // Cleanup on unmount
       if (stream) {
         stream.getTracks().forEach(track => {
           track.stop();
         });
       }
     };
   }, [stream]);
   ```

### Memory Leaks

**Problem**: Memory usage increases over time

**Solutions**:
1. **Proper cleanup**
   ```typescript
   const cleanup = useCallback(() => {
     if (streamRef.current) {
       streamRef.current.getTracks().forEach(track => {
         track.stop();
       });
       streamRef.current = null;
     }
     
     if (videoRef.current) {
       videoRef.current.srcObject = null;
     }
     
     if (detectorRef.current) {
       detectorRef.current.close();
       detectorRef.current = null;
     }
   }, []);
   
   useEffect(() => {
     return cleanup;
   }, [cleanup]);
   ```

2. **Monitor memory usage**
   ```typescript
   const monitorMemory = () => {
     if ('memory' in performance) {
       console.log('Memory usage:', (performance as any).memory);
     }
   };
   
   // Check memory every 30 seconds
   setInterval(monitorMemory, 30000);
   ```

## 🌐 Browser Compatibility

### Older Browser Support

**Problem**: Features not working on older browsers

**Solutions**:
1. **Feature detection**
   ```typescript
   const checkCameraSupport = () => {
     if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
       throw new Error('Camera not supported in this browser');
     }
     
     return true;
   };
   
   const checkMediaPipeSupport = () => {
     // Check WebAssembly support
     if (typeof WebAssembly !== 'object') {
       throw new Error('WebAssembly not supported');
     }
     
     return true;
   };
   ```

2. **Polyfills**
   ```bash
   npm install webrtc-adapter
   ```
   ```typescript
   import 'webrtc-adapter';
   ```

### WebRTC Compatibility

**Problem**: Different behavior across browsers

**Solutions**:
1. **Unified constraints**
   ```typescript
   const getCompatibleConstraints = (facingMode: string) => {
     return {
       video: {
         facingMode,
         width: { min: 320, ideal: 1280, max: 1920 },
         height: { min: 240, ideal: 720, max: 1080 }
       }
     };
   };
   ```

2. **Browser-specific handling**
   ```typescript
   const getBrowserInfo = () => {
     const isFirefox = navigator.userAgent.includes('Firefox');
     const isChrome = navigator.userAgent.includes('Chrome');
     const isSafari = navigator.userAgent.includes('Safari') && !isChrome;
     
     return { isFirefox, isChrome, isSafari };
   };
   ```

## 🚨 Common Error Messages

### "NotFoundError: Requested device not found"

**Causes**:
- Camera disconnected
- Device ID no longer valid
- Camera in use by another application

**Solutions**:
1. Re-enumerate devices
2. Fallback to default camera
3. Show user-friendly error message

### "NotReadableError: Could not start video source"

**Causes**:
- Camera in use by another tab/application
- Hardware issue
- Driver problems

**Solutions**:
1. Close other tabs using camera
2. Restart browser
3. Check camera in other applications

### "OverconstrainedError: Constraints cannot be satisfied"

**Causes**:
- Requested resolution not supported
- Invalid facing mode
- Device doesn't support constraints

**Solutions**:
```typescript
const handleOverconstrainedError = async (error: OverconstrainedError) => {
  console.log('Constraint failed:', error.constraint);
  
  // Try with relaxed constraints
  const fallbackConstraints = { video: true };
  return await navigator.mediaDevices.getUserMedia(fallbackConstraints);
};
```

## 🛠️ Debug Mode

### Enable Debug Logging

Add to your application:
```typescript
const DEBUG = import.meta.env.MODE === 'development';

const debugLog = (message: string, data?: any) => {
  if (DEBUG) {
    console.log(`[Photo Booth Debug] ${message}`, data);
  }
};

// Usage
debugLog('Requesting camera access', constraints);
debugLog('Stream obtained', stream);
debugLog('Face detected', faceData);
```

### Browser Developer Tools

1. **Chrome DevTools**
   - F12 → Console tab
   - Network tab for failed requests
   - Application tab for localStorage

2. **Test camera in console**
   ```javascript
   // Quick camera test
   navigator.mediaDevices.getUserMedia({video:true})
     .then(stream => {
       console.log('Success!', stream);
       stream.getTracks().forEach(t => t.stop());
     })
     .catch(console.error);
   ```

3. **MediaPipe debug**
   ```javascript
   // Check if MediaPipe can load
   import('@mediapipe/face_detection')
     .then(() => console.log('MediaPipe available'))
     .catch(err => console.error('MediaPipe failed', err));
   ```

## 📞 Getting Help

### Before Asking for Help

1. **Check browser console** for error messages
2. **Test in different browsers** to isolate issues
3. **Verify HTTPS** is being used
4. **Try in incognito/private mode** to rule out extensions
5. **Test on different devices** if possible

### Information to Include

When reporting issues, include:
- Browser name and version
- Operating system
- Device type (desktop/mobile)
- Exact error message
- Steps to reproduce
- Whether it works in other browsers
- Network conditions (WiFi vs mobile data)

### Quick Diagnostic

Run this in browser console:
```javascript
// Diagnostic script
const diagnostic = async () => {
  const results = {
    userAgent: navigator.userAgent,
    protocol: location.protocol,
    mediaDevices: !!navigator.mediaDevices,
    getUserMedia: !!navigator.mediaDevices?.getUserMedia,
    webAssembly: typeof WebAssembly === 'object',
    localStorage: typeof Storage !== 'undefined'
  };
  
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    results.cameras = devices.filter(d => d.kind === 'videoinput').length;
  } catch (err) {
    results.cameras = 'Error: ' + err.message;
  }
  
  console.table(results);
  return results;
};

diagnostic();
```

---

Still having issues? [Open an issue](../../issues) with the above diagnostic information.
