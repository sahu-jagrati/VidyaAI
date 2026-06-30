import { useState, useRef, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useLang } from '../context/LanguageContext';

export default function Navbar({ onMenuToggle, sidebarOpen }) {
  const { user, logout } = useAuth();
  const { t, lang, switchLang } = useLang();
  const navigate = useNavigate();
  const [showDropdown, setShowDropdown] = useState(false);
  const [showPyq, setShowPyq] = useState(false);
  const pyqRef = useRef(null);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  // Close PYQ dropdown when clicking outside
  useEffect(() => {
    function handleClick(e) {
      if (pyqRef.current && !pyqRef.current.contains(e.target)) setShowPyq(false);
    }
    document.addEventListener('mousedown', handleClick);
    return () => document.removeEventListener('mousedown', handleClick);
  }, []);

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white border-b border-gray-200 shadow-sm h-16 flex items-center px-4 gap-3">
      {/* Hamburger — visible on all screen sizes */}
      <button
        onClick={onMenuToggle}
        className="p-2 rounded-lg text-gray-500 hover:text-gray-900 hover:bg-gray-100 transition-colors"
        aria-label="Toggle sidebar"
      >
        <div className="w-5 h-5 flex flex-col justify-center gap-1 relative">
          <span className={`block h-0.5 bg-current rounded-full transition-all duration-300 origin-center
            ${sidebarOpen ? 'rotate-45 translate-y-1.5' : ''}`} />
          <span className={`block h-0.5 bg-current rounded-full transition-all duration-300
            ${sidebarOpen ? 'opacity-0 scale-x-0' : ''}`} />
          <span className={`block h-0.5 bg-current rounded-full transition-all duration-300 origin-center
            ${sidebarOpen ? '-rotate-45 -translate-y-1.5' : ''}`} />
        </div>
      </button>

      {/* Logo */}
      <Link to="/home" className="flex items-center gap-2 shrink-0">
        <div className="w-8 h-8 rounded-lg bg-teal-700 flex items-center justify-center text-white font-bold text-sm shadow-md shadow-teal-200">
          V
        </div>
        <span className="font-bold text-lg hidden sm:block gradient-text">VidyaAi</span>
      </Link>

      {/* Exam badge */}
      <div className="hidden md:flex items-center gap-1.5 bg-teal-50 border border-teal-200 rounded-full px-3 py-1">
        <span className="text-teal-700 text-xs font-semibold">SSC CGL</span>
      </div>

      <div className="flex-1" />

      {/* Streak counter */}
      {user && user.current_streak > 0 && (
        <div className="flex items-center gap-1 bg-orange-50 border border-orange-200 rounded-full px-2.5 py-1">
          <span className="text-sm streak-pulse">🔥</span>
          <span className="text-orange-600 text-xs font-bold">{user.current_streak}</span>
        </div>
      )}

      {/* Language toggle */}
      <div className="flex items-center gap-1 bg-gray-100 rounded-lg p-0.5 border border-gray-200 mr-1">
        <button onClick={() => switchLang('en')} className={`px-2.5 py-1 rounded-md text-xs font-bold transition-all duration-150 ${lang === 'en' ? 'bg-teal-700 text-white shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}>EN</button>
        <button onClick={() => switchLang('hi')} className={`px-2.5 py-1 rounded-md text-xs font-bold transition-all duration-150 ${lang === 'hi' ? 'bg-teal-700 text-white shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}>हिं</button>
      </div>

      {/* PYQ Dropdown — right side */}
      <div className="relative" ref={pyqRef}>
        <button
          onClick={() => setShowPyq(v => !v)}
          className={`hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm font-semibold transition-all duration-150 border
            ${showPyq
              ? 'bg-teal-700 text-white border-teal-700'
              : 'bg-white text-gray-600 border-gray-200 hover:border-teal-300 hover:text-teal-700'}`}
        >
          {t('app.nav.pyq')}
          <svg className={`w-3.5 h-3.5 transition-transform duration-150 ${showPyq ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        {showPyq && (
          <div className="absolute right-0 top-11 w-52 bg-white border border-gray-200 rounded-xl shadow-xl py-1.5 z-50">
            <p className="px-4 py-1.5 text-xs font-bold text-gray-400 uppercase tracking-wider">{t('app.nav.pyq.header')}</p>
            <Link
              to="/pyq/mains"
              onClick={() => setShowPyq(false)}
              className="flex items-center gap-3 px-4 py-2.5 text-gray-700 hover:bg-teal-50 hover:text-teal-700 text-sm font-medium transition-colors"
            >
              <span className="w-7 h-7 rounded-lg bg-teal-50 border border-teal-200 flex items-center justify-center text-sm">📖</span>
              <div>
                <p className="font-semibold text-sm">{t('app.nav.pyq.mains')}</p>
                <p className="text-xs text-gray-400">{t('app.nav.pyq.mains.sub')}</p>
              </div>
            </Link>
            <Link
              to="/pyq/advanced"
              onClick={() => setShowPyq(false)}
              className="flex items-center gap-3 px-4 py-2.5 text-gray-700 hover:bg-amber-50 hover:text-amber-700 text-sm font-medium transition-colors"
            >
              <span className="w-7 h-7 rounded-lg bg-amber-50 border border-amber-200 flex items-center justify-center text-sm">🚀</span>
              <div>
                <p className="font-semibold text-sm">{t('app.nav.pyq.adv')}</p>
                <p className="text-xs text-gray-400">{t('app.nav.pyq.adv.sub')}</p>
              </div>
            </Link>
          </div>
        )}
      </div>

      {/* Login button — shown when NOT logged in */}
      {!user && (
        <Link
          to="/login"
          className="bg-teal-700 hover:bg-teal-800 text-white text-sm font-semibold px-4 py-2 rounded-lg transition-colors shadow-sm shadow-teal-200"
        >
          {t('app.nav.login')}
        </Link>
      )}

      {/* Profile dropdown — shown when logged in */}
      {user && (
        <div className="relative">
          <button
            onClick={() => setShowDropdown(!showDropdown)}
            className="w-9 h-9 rounded-full bg-teal-700 flex items-center justify-center text-white font-bold text-sm hover:bg-teal-800 transition-colors shadow-md shadow-teal-200"
          >
            {user.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
          </button>
          {showDropdown && (
            <div className="absolute right-0 top-12 w-48 bg-white border border-gray-200 rounded-xl shadow-xl py-1 z-50">
              <div className="px-4 py-2 border-b border-gray-100">
                <p className="text-gray-900 text-sm font-medium truncate">{user.name}</p>
                <p className="text-gray-400 text-xs truncate">{user.email}</p>
              </div>
              <Link to="/profile" onClick={() => setShowDropdown(false)}
                className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:text-gray-900 hover:bg-gray-50 text-sm transition-colors">
                {t('app.nav.profile')}
              </Link>
              <button onClick={handleLogout}
                className="w-full flex items-center gap-2 px-4 py-2 text-red-500 hover:text-red-600 hover:bg-red-50 text-sm transition-colors">
                {t('app.nav.logout')}
              </button>
            </div>
          )}
        </div>
      )}
    </nav>
  );
}
