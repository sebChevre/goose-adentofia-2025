import { useEffect } from 'react'
import { useLocalStorage } from '../hooks/useLocalStorage'

export function ThemeToggle() {

  // Use localStorage for theme state
  const [isDark, setIsDark] = useLocalStorage('theme', false)

  useEffect(() => {
    // Apply theme to document
    if (isDark) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }, [isDark])

  const toggleTheme = () => {
    setIsDark(prev => !prev)
  }

  return (
    <button
      onClick={toggleTheme}
      className="flex items-center justify-center w-10 h-10 rounded-full bg-secondary hover:bg-primary/20 border border-border transition-all duration-300 hover:scale-110"
      aria-label={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
      title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
    >
      <span className="text-xl transition-transform duration-300 hover:rotate-12">
        {isDark ? '☀️' : '🌙'}
      </span>
    </button>
  )
}
