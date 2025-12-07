import { createFileRoute, Link } from '@tanstack/react-router'
import { useState, useCallback, useEffect, useMemo } from 'react'
import { HandTracker } from '../components/HandTracker'
import { FlightBoard } from '../components/FlightBoard'
import { SettingsButton } from '../components/SettingsButton'
import { useMediaPipe } from '../hooks/useMediaPipe'
import { useGestures } from '../hooks/useGestures'
import { useSettings } from '../contexts/SettingsContext'
import { setSoundEnabled } from '../utils/gestureAudio'
import { GestureResult, loadTrainedThresholds, GestureType } from '../utils/gestureDetection'

export const Route = createFileRoute('/')({ component: App })

function App() {
  const [videoElement, setVideoElement] = useState<HTMLVideoElement | null>(null)
  const [currentGestureForBoard, setCurrentGestureForBoard] = useState<GestureType | null>(null)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const { soundEnabled } = useSettings()

  // Load trained thresholds on mount
  useEffect(() => {
    const loaded = loadTrainedThresholds();
    console.log('📚 Loaded trained thresholds:', loaded);
  }, []);

  // Sync sound settings with audio utility
  useEffect(() => {
    setSoundEnabled(soundEnabled)
  }, [soundEnabled])

  // MediaPipe hand tracking
  const { canvasRef, results, isReady, error, fps } = useMediaPipe(videoElement)

  // Create ignored gestures set when modal is open
  const ignoredGestures = useMemo(() => {
    if (isModalOpen) {
      return new Set([
        GestureType.THUMBS_UP,
        GestureType.OPEN_PALM,
        GestureType.CLOSED_FIST,
      ]);
    }
    return undefined;
  }, [isModalOpen]);

  // Gesture detection with callback
  const handleGesture = useCallback((gesture: GestureResult) => {
    console.log(`✨ Gesture detected: ${gesture.type} - ${gesture.hand} hand`)
    setCurrentGestureForBoard(gesture.type)
  }, [])

  const { currentGesture, allGestures } = useGestures(results, {
    onGesture: handleGesture,
    debounceMs: 300,
    ignoredGestures,
  })

  const handleGestureProcessed = useCallback(() => {
    // Clear the gesture after it's been processed by FlightBoard
    setCurrentGestureForBoard(null)
  }, [])

  const handleModalStateChange = useCallback((isOpen: boolean) => {
    setIsModalOpen(isOpen)
  }, [])

  const handsDetected = results?.multiHandLandmarks?.length || 0

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-900 via-blue-900 to-slate-900">
      {/* Header */}
      <header className="py-8 px-6 text-center border-b border-slate-700/50 backdrop-blur-sm bg-slate-900/30">
        <div className="max-w-7xl mx-auto">
          <div className="flex items-center justify-center gap-4 mb-4">
            <span className="text-5xl">✈️</span>
            <h1 className="text-5xl md:text-6xl font-black text-white">
              <span className="bg-gradient-to-r from-cyan-400 via-blue-400 to-cyan-300 bg-clip-text text-transparent">
                The Homecoming Board
              </span>
            </h1>
            <span className="text-5xl">🧤</span>
          </div>
          <p className="text-xl text-cyan-200 mb-2 font-semibold">
            Gesture-Controlled Flight Tracker
          </p>
          <p className="text-sm text-blue-300">
            ❄️ Winter Festival Edition - No touching required! 🎄
          </p>
          
          {/* Navigation */}
          <div className="mt-4">
            <Link 
              to="/gesture-training" 
              className="inline-flex items-center gap-2 px-6 py-3 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-lg transition-colors"
            >
              <span>🎓</span> Practice Gestures
            </Link>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="py-8 px-6">
        <div className="max-w-7xl mx-auto">
          
          {/* Hidden Hand Tracker - runs in background for gesture detection */}
          <div className="hidden">
            <HandTracker 
              onVideoReady={setVideoElement}
              canvasRef={canvasRef}
              showCanvas={false}
              showFps={false}
              fps={fps}
              handsDetected={handsDetected}
              isReady={isReady}
              error={error}
              currentGesture={currentGesture}
              allGestures={allGestures}
              className=""
            />
          </div>

          {/* Gesture Status Badge and Settings */}
          <div className="mb-6 flex justify-between items-center">
            <SettingsButton />
            <div className="inline-flex items-center gap-3 px-4 py-2 bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-full">
              <span className="text-sm text-gray-300">Gesture Control</span>
              {isReady ? (
                <span className="flex items-center gap-2 text-green-400 text-sm">
                  <span className="inline-block w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
                  Active
                </span>
              ) : error ? (
                <span className="text-red-400 text-sm">Inactive</span>
              ) : (
                <span className="text-yellow-400 text-sm">Starting...</span>
              )}
            </div>
          </div>

          {/* Flight Board - Full Width */}
          <div className="bg-slate-800/30 backdrop-blur-sm border border-slate-700/50 rounded-xl p-6">
            <FlightBoard
              gesture={currentGestureForBoard}
              onGestureProcessed={handleGestureProcessed}
              onModalStateChange={handleModalStateChange}
            />
          </div>

          {/* Quick Gesture Reference */}
          <div className="mt-8 p-6 bg-gradient-to-r from-blue-900/30 to-cyan-900/30 border border-blue-700/50 rounded-xl backdrop-blur-sm">
            <h2 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
              <span>🧤</span> Gesture Controls
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
              <div className="bg-slate-800/50 rounded-lg p-4 text-center">
                <div className="text-4xl mb-2">👊</div>
                <h3 className="font-bold text-cyan-300 mb-1">Fist</h3>
                <p className="text-gray-300">Next Flight</p>
              </div>
              <div className="bg-slate-800/50 rounded-lg p-4 text-center">
                <div className="text-4xl mb-2">🖐️</div>
                <h3 className="font-bold text-green-300 mb-1">Palm</h3>
                <p className="text-gray-300">Previous Flight</p>
              </div>
              <div className="bg-slate-800/50 rounded-lg p-4 text-center">
                <div className="text-4xl mb-2">👍</div>
                <h3 className="font-bold text-yellow-300 mb-1">Thumbs Up</h3>
                <p className="text-gray-300">View Details</p>
              </div>
            </div>
            <div className="mt-4 text-center">
              <Link 
                to="/gesture-training" 
                className="text-cyan-300 hover:text-cyan-200 underline text-sm"
              >
                Need help? Try the Gesture Training Mode →
              </Link>
            </div>
          </div>

        </div>
      </main>

      {/* Footer */}
      <footer className="py-6 px-6 text-center border-t border-slate-700/50 mt-12 backdrop-blur-sm bg-slate-900/30">
        <p className="text-gray-400 text-sm">
          Built with TanStack Start • MediaPipe Hands • OpenSky Network • Day 5: Advent of AI 2025
        </p>
      </footer>
    </div>
  )
}
