import { useSettings } from '../contexts/SettingsContext'

export function SettingsButton({showLabel = false}: {showLabel?: boolean}) {
  const { soundEnabled, toggleSound } = useSettings()

  return (
    <button
      onClick={toggleSound}
      className="inline-flex items-center gap-2 px-4 py-2"
      title={soundEnabled ? 'Disable sounds' : 'Enable sounds'}
    >
      <span className="text-xl" aria-hidden="true">
        {soundEnabled ? '🔊' : '🔇'}
      </span>
      <span className={showLabel ? "ml-2" : "sr-only"}>
        {soundEnabled ? 'Sound On' : 'Sound Off'}
      </span>
    </button>
  )
}
