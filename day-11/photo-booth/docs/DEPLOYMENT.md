# Deployment Guide

This guide covers deploying your Fun House Photo Booth to various hosting platforms.

## 🌐 GitHub Pages Deployment

### Prerequisites
- GitHub repository with your code
- GitHub Actions enabled

### Setup Steps

1. **Configure GitHub Pages**
   ```bash
   # In your repository settings
   Settings → Pages → Source: GitHub Actions
   ```

2. **Create GitHub Actions Workflow**
   Create `.github/workflows/deploy.yml`:
   ```yaml
   name: Deploy to GitHub Pages

   on:
     push:
       branches: [ main ]
     workflow_dispatch:

   permissions:
     contents: read
     pages: write
     id-token: write

   concurrency:
     group: "pages"
     cancel-in-progress: false

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout
           uses: actions/checkout@v4

         - name: Setup Node.js
           uses: actions/setup-node@v4
           with:
             node-version: '18'
             cache: 'npm'

         - name: Install dependencies
           run: npm ci

         - name: Build
           run: npm run build

         - name: Setup Pages
           uses: actions/configure-pages@v3

         - name: Upload artifact
           uses: actions/upload-pages-artifact@v2
           with:
             path: './dist'

     deploy:
       environment:
         name: github-pages
         url: ${{ steps.deployment.outputs.page_url }}
       runs-on: ubuntu-latest
       needs: build
       steps:
         - name: Deploy to GitHub Pages
           id: deployment
           uses: actions/deploy-pages@v2
   ```

3. **Configure Base URL**
   Update `vite.config.ts`:
   ```typescript
   export default defineConfig({
     base: '/photo-booth/',
     plugins: [react()],
     // ... other config
   })
   ```

4. **Push Changes**
   ```bash
   git add .
   git commit -m "Add GitHub Pages deployment"
   git push origin main
   ```

### Custom Domain Setup
1. Add `CNAME` file to `public/` directory with your domain
2. Configure DNS records with your domain provider
3. Enable HTTPS in repository settings

## 🚀 Netlify Deployment

### Method 1: Git Integration

1. **Connect Repository**
   - Go to [Netlify](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Choose your Git provider and repository

2. **Configure Build Settings**
   ```
   Build command: npm run build
   Publish directory: dist
   Node version: 18
   ```

3. **Environment Variables** (if needed)
   ```
   NODE_VERSION=18
   NPM_FLAGS=--prefix=/opt/buildhome/.nodejs/bin
   ```

### Method 2: Manual Deployment

1. **Build locally**
   ```bash
   npm run build
   ```

2. **Deploy via Netlify CLI**
   ```bash
   npm install -g netlify-cli
   netlify deploy --prod --dir=dist
   ```

### Advanced Netlify Configuration

Create `netlify.toml` in your project root:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NODE_VERSION = "18"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[context.production.environment]
  NODE_ENV = "production"

[context.branch-deploy.environment]
  NODE_ENV = "development"
```

## 🔧 Build Optimization

### Environment-Specific Builds

1. **Production optimizations**
   ```typescript
   // vite.config.ts
   export default defineConfig({
     build: {
       minify: 'terser',
       sourcemap: false,
       rollupOptions: {
         output: {
           manualChunks: {
             vendor: ['react', 'react-dom'],
             mediapipe: ['@mediapipe/face_detection'],
           },
         },
       },
     },
   })
   ```

2. **Environment variables**
   Create `.env.production`:
   ```
   VITE_ENVIRONMENT=production
   VITE_DEBUG_MODE=false
   ```

### Performance Optimizations

1. **Code splitting**
   ```typescript
   // Lazy load filter components
   const FilterSelector = lazy(() => import('./components/Filters/FilterSelector'))
   const CapturePreview = lazy(() => import('./components/Capture/CapturePreview'))
   ```

2. **Asset optimization**
   - Compress images before including
   - Use WebP format when possible
   - Enable gzip compression in build

## 🛡️ Security Configuration

### HTTPS Setup

1. **GitHub Pages**: Automatically provided
2. **Netlify**: Automatically provided with Let's Encrypt
3. **Custom hosting**: Configure SSL certificate

### Content Security Policy

Add to your `index.html` or server configuration:
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               media-src 'self'; 
               camera 'self';
               script-src 'self' 'unsafe-inline' cdn.jsdelivr.net;
               style-src 'self' 'unsafe-inline';">
```

### Permissions Policy

```html
<meta http-equiv="Permissions-Policy" 
      content="camera=(self), microphone=()">
```

## 🔍 Monitoring and Analytics

### Error Tracking

1. **Sentry Integration**
   ```bash
   npm install @sentry/react
   ```

2. **Setup in main.tsx**
   ```typescript
   import * as Sentry from "@sentry/react";

   if (import.meta.env.PROD) {
     Sentry.init({
       dsn: "YOUR_DSN_HERE",
       environment: import.meta.env.MODE,
       integrations: [
         new Sentry.BrowserTracing(),
       ],
       tracesSampleRate: 0.1,
     });
   }
   ```

### Performance Monitoring

1. **Web Vitals**
   ```typescript
   import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

   const sendToAnalytics = (metric: any) => {
     console.log(metric);
     // Send to your analytics service
   };

   getCLS(sendToAnalytics);
   getFID(sendToAnalytics);
   getFCP(sendToAnalytics);
   getLCP(sendToAnalytics);
   getTTFB(sendToAnalytics);
   ```

## 🚨 Common Deployment Issues

### Build Failures

1. **Memory issues**
   ```bash
   # Increase Node.js memory limit
   NODE_OPTIONS="--max-old-space-size=4096" npm run build
   ```

2. **Type errors**
   ```bash
   # Check types before building
   npm run typecheck
   ```

3. **Missing dependencies**
   ```bash
   # Clean install
   rm -rf node_modules package-lock.json
   npm install
   ```

### Runtime Issues

1. **Camera not working on HTTPS**
   - Ensure proper SSL certificate
   - Check mixed content warnings
   - Verify camera permissions policy

2. **404 errors on refresh**
   ```toml
   # netlify.toml
   [[redirects]]
     from = "/*"
     to = "/index.html"
     status = 200
   ```

3. **MediaPipe loading issues**
   ```typescript
   // Ensure proper CDN configuration
   const detector = new FaceDetection({
     locateFile: (file: string) => {
       return `https://cdn.jsdelivr.net/npm/@mediapipe/face_detection/${file}`;
     }
   });
   ```

### Performance Issues

1. **Large bundle size**
   ```bash
   # Analyze bundle
   npm install -g webpack-bundle-analyzer
   npx vite-bundle-analyzer
   ```

2. **Slow initial load**
   - Implement code splitting
   - Use lazy loading
   - Optimize MediaPipe loading

3. **Memory leaks**
   ```typescript
   // Ensure proper cleanup
   useEffect(() => {
     return () => {
       stream?.getTracks().forEach(track => track.stop());
       detector?.close();
     };
   }, []);
   ```

## 📊 Deployment Checklist

### Pre-Deployment
- [ ] Build passes locally (`npm run build`)
- [ ] All tests pass (`npm test`)
- [ ] TypeScript compilation succeeds (`npm run typecheck`)
- [ ] Linting passes (`npm run lint`)
- [ ] No console errors in production build

### Camera Functionality
- [ ] Camera permissions work on HTTPS
- [ ] Multiple camera switching works
- [ ] Face detection loads and functions
- [ ] All filters render correctly
- [ ] Photo capture works with filters

### Cross-Platform Testing
- [ ] Desktop Chrome, Firefox, Safari, Edge
- [ ] Mobile Chrome (Android)
- [ ] Mobile Safari (iOS)
- [ ] Different screen sizes and orientations

### Performance
- [ ] App loads in under 3 seconds
- [ ] Camera starts in under 2 seconds
- [ ] Face detection runs at 20+ FPS
- [ ] No memory leaks during extended use
- [ ] Acceptable performance on low-end devices

### Production Configuration
- [ ] HTTPS enabled and working
- [ ] Security headers configured
- [ ] Error monitoring setup
- [ ] Analytics configured (if needed)
- [ ] SEO meta tags added
- [ ] Favicon and app icons included

### Documentation
- [ ] README updated with deployment URL
- [ ] Deployment instructions tested
- [ ] Troubleshooting guide updated
- [ ] License file included

## 🌍 CDN and Global Distribution

### Cloudflare Setup

1. **Add site to Cloudflare**
2. **Configure DNS settings**
3. **Enable optimizations**:
   - Auto Minify (CSS, JS, HTML)
   - Brotli compression
   - Polish (image optimization)

### Performance Optimizations

```toml
# netlify.toml - Additional headers
[[headers]]
  for = "/*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*.wasm"
  [headers.values]
    Content-Type = "application/wasm"
    Cache-Control = "public, max-age=31536000, immutable"
```

## 📈 Scaling Considerations

### Traffic Handling
- **Static hosting**: Can handle high traffic
- **CDN distribution**: Global edge locations
- **Caching strategy**: Aggressive caching for static assets

### MediaPipe Model Delivery
- **CDN hosting**: Use reliable CDN for model files
- **Fallback options**: Local fallback if CDN fails
- **Compression**: Enable compression for model files

### Monitoring
- **Uptime monitoring**: Set up alerts for downtime
- **Performance monitoring**: Track Core Web Vitals
- **Error tracking**: Monitor JavaScript errors

---

Need help? Check the [troubleshooting guide](TROUBLESHOOTING.md) or open an issue.
