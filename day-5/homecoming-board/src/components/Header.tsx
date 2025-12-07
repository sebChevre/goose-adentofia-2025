import { Link } from '@tanstack/react-router'
import { useState } from 'react'

export default function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  const navLinks = [
    { to: '/', label: 'Flight Board', emoji: '✈️' },
    { to: '/gesture-training', label: 'Practice Gestures', emoji: '🎓' },
  ]

  return (
    <nav className="bg-slate-900/95 backdrop-blur-sm border-b border-slate-700/50 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">

          {/* Logo/Brand */}
          <Link
            to="/"
            className="flex items-center gap-2 text-xl font-bold text-white hover:text-cyan-300 transition-colors"
          >
            <span className="text-2xl">✈️</span>
            <span className="hidden sm:inline">Homecoming Board</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-6">
            {navLinks.map((link) => (
              <Link
                key={link.to}
                to={link.to}
                className="flex items-center gap-2 px-4 py-2 rounded-lg text-white hover:bg-slate-800 transition-colors"
                activeProps={{
                  className: 'bg-slate-800 text-cyan-300',
                }}
              >
                <span>{link.emoji}</span>
                <span>{link.label}</span>
              </Link>
            ))}
          </div>

          {/* Mobile Hamburger Button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden p-2 rounded-lg text-white hover:bg-slate-800 transition-colors"
            aria-label="Toggle menu"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              {mobileMenuOpen ? (
                <path d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-slate-700/50">
            <div className="flex flex-col gap-2">
              {navLinks.map((link) => (
                <Link
                  key={link.to}
                  to={link.to}
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2 px-4 py-3 rounded-lg text-white hover:bg-slate-800 transition-colors"
                  activeProps={{
                    className: 'bg-slate-800 text-cyan-300',
                  }}
                >
                  <span>{link.emoji}</span>
                  <span>{link.label}</span>
                </Link>
              ))}
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}
