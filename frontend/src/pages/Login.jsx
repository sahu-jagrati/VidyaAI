import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const features = [
  { icon: '⚡', text: 'Daily bite-sized challenges — just 5 questions/day' },
  { icon: '🔥', text: 'Streak system to build rock-solid consistency' },
  { icon: '🏆', text: 'Live leaderboard — compete with thousands' },
  { icon: '🎯', text: 'Track weak topics and improve accuracy daily' },
];

export default function Login() {
  const { login, signup } = useAuth();
  const navigate = useNavigate();
  const [mode, setMode]   = useState('login');
  const [form, setForm]   = useState({ name: '', email: '', password: '' });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = e => setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));

  const handleSubmit = async e => {
    e.preventDefault();
    setError('');
    if (!form.email || !form.password) { setError('Please fill all fields.'); return; }
    if (mode === 'signup' && !form.name) { setError('Name is required.'); return; }
    setLoading(true);
    try {
      if (mode === 'login') await login(form.email, form.password);
      else await signup(form.name, form.email, form.password);
      navigate('/home');
    } catch (err) {
      const msg = err?.response?.data?.detail
        || (err?.code === 'ERR_NETWORK' ? 'Cannot reach server — is the backend running on port 8000?' : null)
        || err?.message
        || 'Something went wrong. Please try again.';
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#0b0015] flex">

      {/* LEFT PANEL */}
      <div className="hidden lg:flex lg:w-1/2 flex-col justify-between p-12 relative overflow-hidden bg-[#0d0020]">
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-40 -left-20 w-96 h-96 bg-rose-600/20 rounded-full blur-3xl" />
          <div className="absolute top-1/2 -right-20 w-80 h-80 bg-violet-600/25 rounded-full blur-3xl" />
          <div className="absolute -bottom-20 left-1/3 w-64 h-64 bg-fuchsia-600/15 rounded-full blur-3xl" />
        </div>
        <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wMiI+PHBhdGggZD0iTTM2IDM0djZoLTZ2LTZoNnptMCAwdi02aDZ2NmgtNnptLTYgMHY2aC02di02aDZ6Ii8+PC9nPjwvZz48L3N2Zz4=')] opacity-30" />

        <div className="relative flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-linear-to-br from-rose-500 to-violet-600 flex items-center justify-center text-white font-bold text-xl shadow-lg">
            V
          </div>
          <span className="font-bold text-2xl gradient-text">VidyaAi</span>
        </div>

        <div className="relative space-y-6">
          <div>
            <h1 className="text-4xl font-bold text-white leading-tight">
              Build consistency.<br />
              <span className="gradient-text-warm">Crack exams daily.</span>
            </h1>
            <p className="mt-4 text-gray-400 text-lg">
              The Duolingo for SSC CGL. 5 questions a day keeps failure away.
            </p>
          </div>
          <div className="space-y-3">
            {features.map((f, i) => (
              <div key={i} className="flex items-center gap-3 bg-white/5 rounded-xl px-4 py-3 border border-white/8 backdrop-blur-sm">
                <span className="text-xl">{f.icon}</span>
                <span className="text-gray-200 text-sm">{f.text}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="relative bg-white/5 border border-white/10 rounded-2xl p-4 backdrop-blur-sm">
          <p className="text-gray-400 text-xs font-medium mb-3 uppercase tracking-wider">🏆 Today's Top Rankers</p>
          {[
            { name: 'Priya Sharma', xp: '4,850 XP', streak: '42🔥', medal: '🥇' },
            { name: 'Amit Kumar',   xp: '4,620 XP', streak: '38🔥', medal: '🥈' },
            { name: 'Sneha Patel',  xp: '4,410 XP', streak: '35🔥', medal: '🥉' },
          ].map((u, i) => (
            <div key={i} className="flex items-center gap-3 py-2 border-b border-white/5 last:border-0">
              <span className="text-lg">{u.medal}</span>
              <span className="text-white text-sm flex-1">{u.name}</span>
              <span className="text-yellow-400 text-xs">{u.xp}</span>
              <span className="text-orange-400 text-xs">{u.streak}</span>
            </div>
          ))}
        </div>
      </div>

      {/* RIGHT PANEL */}
      <div className="w-full lg:w-1/2 flex items-center justify-center p-6">
        <div className="w-full max-w-md">
          <div className="lg:hidden flex items-center gap-2 justify-center mb-8">
            <div className="w-10 h-10 rounded-xl bg-linear-to-br from-rose-500 to-violet-600 flex items-center justify-center text-white font-bold shadow-lg">V</div>
            <span className="font-bold text-2xl gradient-text">VidyaAi</span>
          </div>

          <div className="bg-[#0d0020] border border-purple-800/40 rounded-2xl p-8 shadow-2xl">
            <h2 className="text-2xl font-bold text-white mb-1">
              {mode === 'login' ? 'Welcome back 👋' : 'Join VidyaAi 🚀'}
            </h2>
            <p className="text-gray-500 text-sm mb-6">
              {mode === 'login' ? 'Log in to continue your streak!' : 'Create your free account and start practising today.'}
            </p>

            <form onSubmit={handleSubmit} className="space-y-4">
              {mode === 'signup' && (
                <div>
                  <label className="block text-gray-400 text-xs font-medium mb-1.5 uppercase tracking-wider">Full Name</label>
                  <input
                    name="name" value={form.name} onChange={handleChange}
                    placeholder="Rahul Sharma"
                    className="w-full bg-white/5 border border-purple-800/40 rounded-xl px-4 py-3 text-white placeholder-gray-600 text-sm focus:outline-none focus:border-rose-500/60 transition-colors"
                  />
                </div>
              )}

              <div>
                <label className="block text-gray-400 text-xs font-medium mb-1.5 uppercase tracking-wider">Email</label>
                <input
                  name="email" type="email" value={form.email} onChange={handleChange}
                  placeholder="you@example.com"
                  className="w-full bg-white/5 border border-purple-800/40 rounded-xl px-4 py-3 text-white placeholder-gray-600 text-sm focus:outline-none focus:border-rose-500/60 transition-colors"
                />
              </div>

              <div>
                <label className="block text-gray-400 text-xs font-medium mb-1.5 uppercase tracking-wider">Password</label>
                <input
                  name="password" type="password" value={form.password} onChange={handleChange}
                  placeholder="••••••••"
                  className="w-full bg-white/5 border border-purple-800/40 rounded-xl px-4 py-3 text-white placeholder-gray-600 text-sm focus:outline-none focus:border-rose-500/60 transition-colors"
                />
              </div>

              {error && (
                <div className="bg-red-500/10 border border-red-500/30 rounded-xl px-4 py-3 text-red-400 text-sm">
                  {error}
                </div>
              )}

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold py-3 rounded-xl transition-all duration-200 text-sm shadow-lg"
              >
                {loading ? (
                  <span className="flex items-center justify-center gap-2">
                    <svg className="animate-spin h-4 w-4" viewBox="0 0 24 24" fill="none">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z" />
                    </svg>
                    {mode === 'login' ? 'Logging in...' : 'Creating account...'}
                  </span>
                ) : (
                  mode === 'login' ? 'Log In' : 'Create Account'
                )}
              </button>
            </form>

            <div className="mt-6 text-center">
              <p className="text-gray-500 text-sm">
                {mode === 'login' ? "Don't have an account?" : 'Already have an account?'}{' '}
                <button
                  onClick={() => { setMode(mode === 'login' ? 'signup' : 'login'); setError(''); }}
                  className="text-rose-400 font-medium hover:text-rose-300 transition-colors"
                >
                  {mode === 'login' ? 'Create one' : 'Log in'}
                </button>
              </p>
            </div>
          </div>

          <p className="text-center text-gray-700 text-xs mt-6">Free forever · No credit card required</p>
        </div>
      </div>
    </div>
  );
}
