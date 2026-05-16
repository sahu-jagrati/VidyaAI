import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Navbar({ onMenuToggle }) {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [showDropdown, setShowDropdown] = useState(false);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-[#0d0020]/95 backdrop-blur border-b border-purple-900/40 h-16 flex items-center px-4 gap-4">
      {/* Hamburger (mobile) */}
      <button
        onClick={onMenuToggle}
        className="lg:hidden p-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/5 transition-colors"
      >
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      {/* Logo */}
      <Link to="/home" className="flex items-center gap-2 shrink-0">
        <div className="w-8 h-8 rounded-lg bg-linear-to-br from-rose-500 to-violet-600 flex items-center justify-center text-white font-bold text-sm shadow-lg">
          V
        </div>
        <span className="font-bold text-lg hidden sm:block gradient-text">
          VidyaAi
        </span>
      </Link>

      {/* Exam badge */}
      <div className="hidden md:flex items-center gap-1.5 bg-rose-500/10 border border-rose-500/25 rounded-full px-3 py-1">
        <span className="text-rose-400 text-xs font-medium">SSC CGL</span>
      </div>

      <div className="flex-1" />

      {/* Stats */}
      {user && (
        <div className="flex items-center gap-2 sm:gap-3">
          {/* Streak */}
          <div className="flex items-center gap-1.5 bg-orange-500/10 border border-orange-500/30 rounded-full px-3 py-1.5">
            <span className="streak-pulse text-base">🔥</span>
            <span className="text-orange-400 font-semibold text-sm">{user.current_streak}</span>
          </div>

          {/* XP */}
          <div className="flex items-center gap-1.5 bg-yellow-500/10 border border-yellow-500/30 rounded-full px-3 py-1.5">
            <span className="text-base">⭐</span>
            <span className="text-yellow-400 font-semibold text-sm">{user.xp.toLocaleString()}</span>
          </div>

          {/* Accuracy */}
          <div className="hidden sm:flex items-center gap-1.5 bg-violet-500/10 border border-violet-500/30 rounded-full px-3 py-1.5">
            <span className="text-base">🎯</span>
            <span className="text-violet-400 font-semibold text-sm">{user.accuracy?.toFixed(0)}%</span>
          </div>
        </div>
      )}

      {/* Profile dropdown */}
      {user && (
        <div className="relative">
          <button
            onClick={() => setShowDropdown(!showDropdown)}
            className="w-9 h-9 rounded-full bg-linear-to-br from-rose-500 to-violet-600 flex items-center justify-center text-white font-bold text-sm hover:opacity-90 transition-opacity shadow-lg"
          >
            {user.name.split(' ').map(n => n[0]).join('').slice(0, 2)}
          </button>
          {showDropdown && (
            <div className="absolute right-0 top-12 w-48 bg-[#130022] border border-purple-800/40 rounded-xl shadow-2xl py-1 z-50">
              <div className="px-4 py-2 border-b border-purple-900/40">
                <p className="text-white text-sm font-medium truncate">{user.name}</p>
                <p className="text-gray-500 text-xs truncate">{user.email}</p>
              </div>
              <Link to="/profile" onClick={() => setShowDropdown(false)}
                className="flex items-center gap-2 px-4 py-2 text-gray-300 hover:text-white hover:bg-white/5 text-sm transition-colors">
                👤 Profile
              </Link>
              <button onClick={handleLogout}
                className="w-full flex items-center gap-2 px-4 py-2 text-red-400 hover:text-red-300 hover:bg-red-500/10 text-sm transition-colors">
                🚪 Logout
              </button>
            </div>
          )}
        </div>
      )}
    </nav>
  );
}
