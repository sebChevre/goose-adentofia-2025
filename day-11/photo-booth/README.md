# Fun House Photo Booth

A modern winter-themed camera web application with AR filters, face detection, and real-time photo capture.

## 🎯 Features

- **Real-time Camera Access**: Access device cameras with permission handling
- **Face Detection**: MediaPipe-powered face detection with AR overlay positioning
- **Winter AR Filters**: 4 beautiful winter-themed filters:
  - ❄️ Snowflake Crown - Animated snowflakes above your head
  - 🦌 Reindeer Antlers - Festive antlers with gentle animation
  - 🧔‍♂️ Frosty Beard - Animated winter beard effect
  - ✨ Sparkle Magic - Orbital sparkles around your face
- **Camera Controls**: Switch between front/back cameras, adjust settings
- **Photo Capture**: High-quality image capture with filter compositing
- **Mobile-First**: Optimized for mobile devices with responsive design
- **Winter Theme**: Beautiful icy blue theme with snow effects

## 🚀 Quick Start

### Prerequisites

- **Node.js**: Version 18.0 or higher
- **Modern Browser**: Chrome 60+, Firefox 55+, Safari 11+, Edge 79+
- **HTTPS**: Required for camera access (auto-provided by Vite dev server)

### Installation

1. **Clone and install dependencies**
   ```bash
   cd photo-booth
   npm install
   ```

2. **Start development server**
   ```bash
   npm run dev
   ```

3. **Open in browser**
   Navigate to `http://localhost:5173` and allow camera access when prompted

## 🛠️ Available Scripts

- `npm run dev` - Start development server with HMR
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint
- `npm run lint:fix` - Fix ESLint issues automatically
- `npm run typecheck` - Run TypeScript type checking
- `npm run test` - Run tests with Vitest
- `npm run format` - Format code with Prettier
- `npm run clean` - Clean build artifacts

## 📁 Project Structure

```
src/
├── components/
│   ├── Camera/           # Camera components
│   │   ├── CameraView.tsx
│   │   ├── CameraControls.tsx
│   │   └── CameraOverlay.tsx
│   ├── Filters/          # Filter selection UI
│   ├── Capture/          # Photo capture components
│   └── UI/              # Reusable UI components
├── hooks/               # Custom React hooks
│   ├── useCamera.ts
│   ├── useFaceDetection.ts
│   └── useCapture.ts
├── services/            # Core services
│   ├── camera/          # Camera management
│   ├── faceDetection/   # MediaPipe integration
│   ├── filters/         # AR filter system
│   └── capture/         # Photo capture logic
├── types/              # TypeScript definitions
├── utils/              # Utility functions
└── theme/              # Winter theme system
```

## 📱 Camera Permissions

### Browser Support

| Browser | Desktop | Mobile | Notes |
|---------|---------|---------|-------|
| Chrome | ✅ Full | ✅ Full | Best performance |
| Firefox | ✅ Full | ✅ Full | Good compatibility |
| Safari | ✅ Limited | ⚠️ HTTPS Only | iOS requires HTTPS |
| Edge | ✅ Full | ✅ Full | Same as Chrome |

### Permission Setup

1. **Allow camera access** when prompted
2. **Ensure HTTPS** - required on mobile Safari
3. **Check camera settings** in browser if issues occur

### Troubleshooting Camera Issues

#### Permission Denied
```bash
# Check browser settings
Chrome: chrome://settings/content/camera
Firefox: about:preferences#privacy
Safari: Safari → Preferences → Websites → Camera
```

#### iOS Safari Specific
- **HTTPS Required**: Camera will not work over HTTP
- **User Gesture**: Camera access must be triggered by button click
- **Background Limits**: Camera may pause when tab is backgrounded

## 🎨 Winter Theme

The app features a cohesive winter theme inspired by Day-4 design:

- **Colors**: Ice blue (#4A90E2), snow white, frost silver
- **Effects**: Animated snowfall background, glass morphism
- **Typography**: Clean, modern fonts with winter color palette
- **Components**: Frosted glass panels with soft shadows

## 📷 Face Detection

Uses **MediaPipe Face Detection** for optimal mobile performance:

- **Lightweight**: ~2MB model size
- **Fast**: Optimized for real-time detection
- **Accurate**: 468 facial landmarks
- **Mobile-First**: Runs efficiently on mobile devices

### Detection Features
- Real-time face tracking
- Bounding box detection
- Facial landmark extraction
- "No face detected" state handling
- Performance monitoring and optimization

## 🎭 AR Filters

### Filter System
- **Canvas-based rendering**: Lightweight and performant
- **Real-time animation**: Smooth 60fps animations
- **Face tracking**: Filters move with face position
- **Mobile optimized**: Efficient particle systems

### Available Filters

1. **Snowflake Crown** ❄️
   - Animated snowflakes floating above head
   - Gentle falling motion with wind effects
   - Ice-blue color palette

2. **Reindeer Antlers** 🦌
   - Brown antlers positioned above forehead
   - Subtle swaying animation
   - Multiple branch detail

3. **Frosty Beard** 🧔‍♂️
   - Winter beard on lower face
   - Breathing animation effect
   - Frost sparkles

4. **Sparkle Magic** ✨
   - Orbital sparkles around face
   - Multiple sparkle types (stars, diamonds, crosses)
   - Color-changing effects

## 📸 Photo Capture

### Capture Features
- **High-quality output**: Full resolution capture
- **Filter compositing**: Combines video + AR filters
- **Brightness/contrast**: Real-time adjustments
- **Download & Share**: Native sharing with fallback

### Capture Process
1. Video frame extraction
2. Filter overlay rendering
3. Brightness/contrast application
4. Canvas composition
5. Blob generation for download/share

## 🏗️ Build & Deployment

### Production Build
```bash
npm run build
```

### Deployment Options

#### GitHub Pages
```bash
# Configure base URL in vite.config.ts
base: '/photo-booth/'

# GitHub Actions will handle deployment
```

#### Netlify
```bash
# Build command: npm run build
# Publish directory: dist
# Auto-deploys on git push
```

### Environment Setup
- **HTTPS Required**: Camera access needs secure context
- **Build Optimization**: Code splitting and compression enabled
- **Asset Optimization**: Images compressed, lazy loading implemented

## 🔧 Development

### Code Style
- **TypeScript**: Full type safety
- **ESLint**: Code quality enforcement
- **Prettier**: Consistent formatting
- **Conventional Commits**: Clear commit messages

### Performance Monitoring
```typescript
// Built-in performance monitoring
const fps = globalPerformanceMonitor.getFPS();
const processingTime = faceDetection.getProcessingTime();
```

### Debug Mode
```typescript
// Enable debug overlays
faceDetection.actions.toggleDebug();
// Shows bounding boxes and facial landmarks
```

## 📖 API Reference

### Key Hooks

#### `useCamera()`
```typescript
const { state, actions, refs } = useCamera();
// state: camera status, devices, permissions
// actions: startCamera, stopCamera, switchCamera
// refs: videoRef, canvasRef for DOM access
```

#### `useFaceDetection(videoRef)`
```typescript
const detection = useFaceDetection(videoRef);
// Provides real-time face detection data
// Includes bounding boxes and landmarks
```

#### `useCapture(options)`
```typescript
const capture = useCapture({
  videoElement: refs.videoRef.current,
  overlayCanvas: refs.canvasRef.current
});
// Handles photo capture with filter compositing
```

## 🚨 Known Limitations

- **Single camera stream**: Most browsers limit to one active camera
- **Mobile performance**: High resolution may impact performance
- **Browser compatibility**: Some advanced features require modern browsers
- **iOS Safari quirks**: Requires HTTPS and user gesture

See [docs/LIMITATIONS.md](docs/LIMITATIONS.md) for detailed limitations.

## 📚 Documentation

- [Deployment Guide](docs/DEPLOYMENT.md) - Hosting and production setup
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Run tests: `npm test`
4. Commit changes: `git commit -m 'Add amazing feature'`
5. Push to branch: `git push origin feature/amazing-feature`
6. Open Pull Request

### Development Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm test

# Type checking
npm run typecheck

# Linting
npm run lint:fix
```

## 🎯 Roadmap

- [ ] Additional filter categories (Halloween, Birthday, etc.)
- [ ] Video recording with filters
- [ ] Advanced face detection features
- [ ] Social media integration
- [ ] Custom filter creation tools

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

Having issues?

1. Check the [troubleshooting guide](docs/TROUBLESHOOTING.md)
2. Ensure HTTPS is enabled (especially on mobile)
3. Verify camera permissions in browser settings
4. Try in incognito/private mode to rule out extensions
5. Test with different browsers to isolate issues

For bugs and feature requests, please [open an issue](../../issues).

---

Built with ❤️ using React, TypeScript, and MediaPipe

*Optimized for mobile • Winter themed • Real-time AR filters*
