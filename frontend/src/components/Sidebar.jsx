import { NavLink, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useLang } from '../context/LanguageContext';

export default function Sidebar({ isOpen, onClose }) {
  const { logout } = useAuth();
  const { t } = useLang();
  const navigate = useNavigate();

  const navItems = [
    { to: '/home',            icon: '🏠', label: t('sidebar.home')        },
    { to: '/ssc-cgl',         icon: '📚', label: t('sidebar.ssccgl')      },
    { to: '/topic-wise',      icon: '🎯', label: t('sidebar.topicwise')   },
    { to: '/daily-challenge', icon: '⚡', label: t('sidebar.challenge')   },
    { to: '/daily-news',      icon: '📰', label: t('sidebar.news')        },
    { to: '/leaderboard',     icon: '🏆', label: t('sidebar.leaderboard') },
    { to: '/profile',         icon: '👤', label: t('sidebar.profile')     },
    { to: '/contact',         icon: '✉️', label: t('sidebar.contact')     },
  ];

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <>
      {isOpen && (
        <div className="fixed inset-0 bg-black/40 z-30 lg:hidden" onClick={onClose} />
      )}

      <aside className={`
        fixed top-16 left-0 bottom-0 z-40
        w-60 bg-white border-r border-gray-200
        flex flex-col
        transform transition-transform duration-250 ease-in-out
        ${isOpen ? 'translate-x-0' : '-translate-x-full'}
      `}>
        <nav className="flex-1 overflow-y-auto py-4 px-3 space-y-0.5">
          {navItems.map(item => (
            <NavLink
              key={item.to}
              to={item.to}
              onClick={onClose}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all duration-150
                ${isActive
                  ? 'bg-teal-50 text-teal-700 border border-teal-200 shadow-sm'
                  : 'text-gray-500 hover:text-gray-900 hover:bg-gray-50'
                }`
              }
            >
              <span className="text-lg w-6 text-center">{item.icon}</span>
              <span>{item.label}</span>
            </NavLink>
          ))}
        </nav>

        <div className="p-3 border-t border-gray-100 space-y-0.5">
          <NavLink
            to="/about"
            onClick={onClose}
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all duration-150
              ${isActive
                ? 'bg-teal-50 text-teal-700 border border-teal-200'
                : 'text-gray-500 hover:text-gray-900 hover:bg-gray-50'
              }`
            }
          >
            <span className="text-lg w-6 text-center">ℹ️</span>
            <span>{t('sidebar.about')}</span>
          </NavLink>
          <button
            onClick={handleLogout}
            className="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-red-500 hover:text-red-600 hover:bg-red-50 transition-all duration-150"
          >
            <span className="text-lg w-6 text-center">🚪</span>
            <span>{t('sidebar.logout')}</span>
          </button>
        </div>
      </aside>
    </>
  );
}
