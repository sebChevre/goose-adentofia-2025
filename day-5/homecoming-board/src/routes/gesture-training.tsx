import { createFileRoute, Link } from '@tanstack/react-router'
import { useState, useCallback, useEffect } from 'react'
import { HandTracker } from '../components/HandTracker'
import { GestureTrainerOverlay } from '../components/GestureTrainerOverlay'
import { useMediaPipe } from '../hooks/useMediaPipe'
import { useGestures } from '../hooks/useGestures'
import { useSettings } from '../contexts/SettingsContext'
import { setSoundEnabled } from '../utils/gestureAudio'
import { loadTrainedThresholds, updateThresholds, resetThresholds } from '../utils/gestureDetection'

export const Route = createFileRoute('/gesture-training')({ component: GestureTraining })

function GestureTraining() {
  const [videoElement, setVideoElement] = useState<HTMLVideoElement | null>(null)
  const { soundEnabled } = useSettings()

  // Sync sound settings with audio utility
  useEffect(() => {
    setSoundEnabled(soundEnabled)
  }, [soundEnabled])

  // MediaPipe hand tracking
  const { canvasRef, results, isReady, error, fps } = useMediaPipe(videoElement)

  // Gesture detection with callback
  const handleGesture = useCallback((gesture: any) => {
    console.debug(`✨ Gesture detected: ${gesture.type} - ${gesture.hand} hand`)
  }, [])

  const { currentGesture, allGestures } = useGestures(results, {
    onGesture: handleGesture,
    debounceMs: 300,
  })

  const handsDetected = results?.multiHandLandmarks?.length || 0

  // Load trained thresholds on mount
  useEffect(() => {
    const loaded = loadTrainedThresholds();
    console.debug('📚 Loaded thresholds on page load:', loaded);
  }, []);

  const handleThresholdsLearned = useCallback((thresholds: any) => {
    console.debug('🎓 New thresholds learned:', thresholds);
    // Update the gesture detection system with new thresholds
    updateThresholds(thresholds);
    alert('✅ Training complete! Your custom gesture thresholds are now active.\n\nGo to the Flight Board to test them!');
  }, [])

  const handleResetTraining = useCallback(() => {
    if (confirm('Are you sure you want to reset gesture training?\n\nThis will delete all your trained gestures and restore default thresholds.')) {
      resetThresholds();
      alert('♻️ Training reset! Using default thresholds now.');
      // Reload the page to apply defaults
      window.location.reload();
    }
  }, [])

  return (
    <div className="min-screen bg-gradient-to-b from-background via-primary/10 to-background">
      {/* Header */}
      <header className="pt-4 px-6 text-center">
        <div className="max-w-7xl mx-auto">
            <h1 className='sr-only'>
                Gesture Training Mode
            </h1>
          <p>
            Perfect your gestures before using them on the flight board!
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="py-8 px-6">
        <div className="max-w-7xl mx-auto">
          {/* Hand Tracker with Training Overlay */}
          <div className="mb-8">
            <div className="bg-card/50 backdrop-blur-sm border border-border rounded-xl p-4">

            <div className='flex justify-between items-center py-1'>
                <span className="text-sm text-gray-400 font-normal ml-2">
                  (Live finger curl values & training overlay on video)
                </span>
                                      <button
              onClick={handleResetTraining}
              className="inline-flex items-center gap-2 px-4 py-2 text-sm font-semibold rounded-lg transition-colors"
            >
              <span>♻️</span> Reset Training
            </button>
            </div>


              <div className="relative">
                <HandTracker
                  onVideoReady={setVideoElement}
                  canvasRef={canvasRef}
                  showCanvas={true}
                  showFps={true}
                  fps={fps}
                  handsDetected={handsDetected}
                  isReady={isReady}
                  error={error}
                  currentGesture={currentGesture}
                  allGestures={allGestures}
                  className="rounded-lg overflow-hidden"
                />
                {/* Overlay the trainer on top of the video */}
                <GestureTrainerOverlay
                  handResults={results}
                  onThresholdsLearned={handleThresholdsLearned}
                />
              </div>
            </div>
          </div>

          {/* Training Tips */}
          <div>
            <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
              <span>💡</span> How to Use Training Mode
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
              <div className="rounded-lg p-4">
                <div className="text-3xl mb-2">👀</div>
                <h3 className="font-bold mb-2">Watch the Overlays</h3>
                <p className="">
                  <strong>Top-left</strong>: Live finger curl values (0.0=extended, 1.0=curled)<br/>
                  <strong>Top-right</strong>: Detected gesture & training controls
                </p>
              </div>
              <div className="rounded-lg p-4">
                <div className="text-3xl mb-2">🎓</div>
                <h3 className="font-bold mb-2">Start Training Mode</h3>
                <p className="">
                  Click "Start Training Mode" in the top-right overlay. You'll see correction buttons appear.
                </p>
              </div>
              <div className="rounded-lg p-4">
                <div className="text-3xl mb-2">✋</div>
                <h3 className="font-bold mb-2">Make & Correct Gestures</h3>
                <p className="">
                  Make a gesture. If it's wrong or unknown, click the correct button (Fist/Palm/Thumbs Up/Down).
                  Do this 3 times per gesture.
                </p>
              </div>
              <div className="rounded-lg p-4">
                <div className="text-3xl mb-2">✨</div>
                <h3 className="font-bold mb-2">Apply Learned Settings</h3>
                <p className="">
                  After collecting 9+ samples (3 per gesture × 3 gestures), click "Finish Training & Apply" to use your custom thresholds!
                </p>
              </div>
            </div>
          </div>

        </div>
      </main>

      {/* Footer */}
      <footer className="py-6 px-6 text-center border-t border-slate-700/50 mt-12 backdrop-blur-sm bg-slate-900/30">
        <p className="text-gray-400 text-sm">
          Built with TanStack Start • MediaPipe Hands • Day 5: Advent of AI 2025
        </p>
      </footer>
    </div>
  )
}
