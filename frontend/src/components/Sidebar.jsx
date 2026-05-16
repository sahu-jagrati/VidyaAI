import { NavLink, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const navItems = [
  { to: '/home',            icon: '🏠', label: 'Home'            },
  { to: '/ssc-cgl',         icon: '📚', label: 'SSC CGL'         },
  { to: '/daily-challenge', icon: '⚡', label: 'Daily Challenge'  },
  { to: '/leaderboard',     icon: '🏆', label: 'Leaderboard'     },
  { to: '/profile',         icon: '👤', label: 'Profile'         },
  { to: '/contact',         icon: '✉️', label: 'Contact'          },
];

export default function Sidebar({ isOpen, onClose }) {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/70 z-30 lg:hidden"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <aside className={`
        fixed top-16 left-0 bottom-0 z-40
        w-60 bg-[#0d0020] border-r border-purple-900/40
        flex flex-col
        transform transition-transform duration-250 ease-in-out
        ${isOpen ? 'translate-x-0' : '-translate-x-full'}
        lg:translate-x-0
      `}>
        {/* Nav */}
        <nav className="flex-1 overflow-y-auto py-4 px-3 space-y-1">
          {navItems.map(item => (
            <NavLink
              key={item.to}
              to={item.to}
              onClick={onClose}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all duration-150
                ${isActive
                  ? 'bg-rose-500/15 text-rose-400 border border-rose-500/30 shadow-sm'
                  : 'text-gray-500 hover:text-white hover:bg-white/5'
                }`
              }
            >
              <span className="text-lg w-6 text-center">{item.icon}</span>
              <span>{item.label}</span>
            </NavLink>
          ))}
        </nav>

        {/* Bottom section */}
        <div className="p-3 border-t border-purple-900/40 space-y-1">
          <NavLink
            to="/about"
            onClick={onClose}
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all duration-150
              ${isActive
                ? 'bg-rose-500/15 text-rose-400 border border-rose-500/30'
                : 'text-gray-500 hover:text-white hover:bg-white/5'
              }`
            }
          >
            <span className="text-lg w-6 text-center">ℹ️</span>
            <span>About</span>
          </NavLink>
          <button
            onClick={handleLogout}
            className="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-red-400 hover:text-red-300 hover:bg-red-500/10 transition-all duration-150"
          >
            <span className="text-lg w-6 text-center">🚪</span>
            <span>Logout</span>
          </button>
        </div>
      </aside>
    </>
  );
}
