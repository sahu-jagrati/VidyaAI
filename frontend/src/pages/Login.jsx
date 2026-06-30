import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useGoogleLogin } from '@react-oauth/google';
import { useAuth } from '../context/AuthContext';
import { useLang } from '../context/LanguageContext';

export default function Login() {
  const { login, signup, googleAuth } = useAuth();
  const { t } = useLang();
  const navigate = useNavigate();
  const [mode, setMode]         = useState('login');
  const [form, setForm]         = useState({ name: '', email: '', password: '' });
  const [error, setError]       = useState('');
  const [loading, setLoading]   = useState(false);
  const [gLoading, setGLoading] = useState(false);

  const features = [
    { icon: '⚡', text: t('login.feat.1') },
    { icon: '🔥', text: t('login.feat.2') },
    { icon: '🏆', text: t('login.feat.3') },
    { icon: '🎯', text: t('login.feat.4') },
  ];

  const handleGoogleSuccess = async (tokenResponse) => {
    setGLoading(true);
    setError('');
    try {
      await googleAuth(tokenResponse.access_token);
      navigate('/home');
    } catch (err) {
      const msg = err?.response?.data?.detail
        || (err?.code === 'ERR_NETWORK' ? 'Cannot reach server — is the backend running on port 8000?' : null)
        || err?.message
        || 'Google sign-in failed. Please try again.';
      setError(msg);
    } finally {
      setGLoading(false);
    }
  };

  const loginWithGoogle = useGoogleLogin({
    onSuccess: handleGoogleSuccess,
    onError: () => setError('Google sign-in was cancelled or failed.'),
  });

  const handleChange = e => setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));

  const handleSubmit = async e => {
    e.preventDefault();
    setError('');
    if (!form.email || !form.password) { setError(t('login.error.fill')); return; }
    if (mode === 'signup' && !form.name) { setError(t('login.error.name')); return; }
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
    <div className="min-h-screen flex">

      {/* LEFT PANEL — teal brand panel */}
      <div className="hidden lg:flex lg:w-1/2 flex-col justify-between p-12 bg-teal-700 relative overflow-hidden">
        {/* Background circles */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-24 -right-24 w-80 h-80 bg-teal-600/40 rounded-full" />
          <div className="absolute top-1/2 -left-16 w-64 h-64 bg-teal-800/30 rounded-full" />
          <div className="absolute -bottom-16 right-1/3 w-48 h-48 bg-amber-400/20 rounded-full" />
        </div>

        {/* Logo */}
        <div className="relative flex items-center gap-3">
          <div className="w-12 h-12 rounded-2xl bg-white flex items-center justify-center text-teal-700 font-bold text-2xl shadow-lg">
            V
          </div>
          <span className="font-bold text-3xl text-white">VidyaAi</span>
        </div>

        {/* Hero text */}
        <div className="relative space-y-6">
          <div>
            <h1 className="text-4xl font-bold text-white leading-tight">
              {t('login.panel.h1')}<br />
              <span className="text-amber-300">{t('login.panel.h2')}</span>
            </h1>
            <p className="mt-4 text-teal-100 text-lg">
              {t('login.panel.sub')}
            </p>
          </div>
          <div className="space-y-3">
            {features.map((f, i) => (
              <div key={i} className="flex items-center gap-3 bg-white/15 rounded-xl px-4 py-3 border border-white/20 backdrop-blur-sm">
                <span className="text-xl">{f.icon}</span>
                <span className="text-white text-sm font-medium">{f.text}</span>
              </div>
            ))}
          </div>
        </div>

      </div>

      {/* RIGHT PANEL — white form */}
      <div className="w-full lg:w-1/2 flex items-center justify-center p-6 bg-white">
        <div className="w-full max-w-md">
          {/* Mobile logo */}
          <div className="lg:hidden flex items-center gap-2 justify-center mb-8">
            <div className="w-10 h-10 rounded-xl bg-teal-700 flex items-center justify-center text-white font-bold shadow-lg">V</div>
            <span className="font-bold text-2xl gradient-text">VidyaAi</span>
          </div>

          <div className="mb-8">
            <h2 className="text-3xl font-bold text-gray-900">
              {mode === 'login' ? t('login.welcome') : t('login.join')}
            </h2>
            <p className="text-gray-500 text-sm mt-2">
              {mode === 'login' ? t('login.sub.login') : t('login.sub.signup')}
            </p>
          </div>

          {/* Social sign-in */}
          <div className="space-y-3 mb-6">
            <button
              type="button"
              onClick={() => loginWithGoogle()}
              disabled={gLoading}
              className="w-full flex items-center justify-center gap-3 bg-white border border-gray-200 hover:border-gray-300 hover:bg-gray-50 text-gray-700 font-semibold py-3 rounded-xl transition-all duration-200 text-sm shadow-sm disabled:opacity-60 disabled:cursor-not-allowed"
            >
              {gLoading ? (
                <svg className="animate-spin h-4 w-4 text-gray-500" viewBox="0 0 24 24" fill="none">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z" />
                </svg>
              ) : (
                <svg className="w-5 h-5 shrink-0" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"/>
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                </svg>
              )}
              {t('login.google')}
            </button>

            <button
              type="button"
              onClick={() => loginWithGoogle()}
              disabled={gLoading}
              className="w-full flex items-center justify-center gap-3 bg-white border border-gray-200 hover:border-gray-300 hover:bg-gray-50 text-gray-700 font-semibold py-3 rounded-xl transition-all duration-200 text-sm shadow-sm disabled:opacity-60 disabled:cursor-not-allowed"
            >
              <svg className="w-5 h-5 shrink-0" viewBox="0 0 48 48">
                <path fill="#EA4335" d="M24 5.5c3.7 0 6.9 1.3 9.5 3.4l7-7C36.7 1.5 30.7 0 24 0 14.7 0 6.7 5.3 2.7 13l8.1 6.3C12.8 12.4 17.9 5.5 24 5.5z"/>
                <path fill="#4285F4" d="M46.5 24.5c0-1.6-.1-3.1-.4-4.5H24v8.6h12.7c-.6 3-2.4 5.5-4.9 7.2l7.7 6c4.5-4.2 7-10.4 7-17.3z"/>
                <path fill="#34A853" d="M10.8 28.7A18.6 18.6 0 0 1 9.5 24c0-1.6.3-3.2.8-4.7L2.2 13A24 24 0 0 0 0 24c0 3.9.9 7.6 2.7 10.8l8.1-6.1z"/>
                <path fill="#FBBC05" d="M24 48c6.5 0 12-2.1 16-5.8l-7.7-6c-2.2 1.5-5 2.3-8.3 2.3-6.1 0-11.2-4-13.1-9.5l-8.1 6.3C6.7 42.7 14.7 48 24 48z"/>
              </svg>
              {t('login.gmail')}
            </button>
          </div>

          {/* Divider */}
          <div className="flex items-center gap-3 mb-6">
            <div className="flex-1 h-px bg-gray-200" />
            <span className="text-xs text-gray-400 font-medium">{t('login.or')}</span>
            <div className="flex-1 h-px bg-gray-200" />
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            {mode === 'signup' && (
              <div>
                <label className="block text-gray-700 text-sm font-semibold mb-1.5">{t('login.name')}</label>
                <input
                  name="name" value={form.name} onChange={handleChange}
                  placeholder="Rahul Sharma"
                  className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 text-sm focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-100 transition-all"
                />
              </div>
            )}

            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-1.5">{t('login.email')}</label>
              <input
                name="email" type="email" value={form.email} onChange={handleChange}
                placeholder="you@example.com"
                className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 text-sm focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-100 transition-all"
              />
            </div>

            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-1.5">{t('login.password')}</label>
              <input
                name="password" type="password" value={form.password} onChange={handleChange}
                placeholder="••••••••"
                className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 text-sm focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-100 transition-all"
              />
            </div>

            {error && (
              <div className="bg-red-50 border border-red-200 rounded-xl px-4 py-3 text-red-600 text-sm">
                {error}
              </div>
            )}

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-teal-700 hover:bg-teal-800 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold py-3 rounded-xl transition-all duration-200 text-sm shadow-lg shadow-teal-200 mt-2"
            >
              {loading ? (
                <span className="flex items-center justify-center gap-2">
                  <svg className="animate-spin h-4 w-4" viewBox="0 0 24 24" fill="none">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z" />
                  </svg>
                  {mode === 'login' ? t('login.loading.login') : t('login.loading.signup')}
                </span>
              ) : (
                mode === 'login' ? t('login.btn.login') : t('login.btn.signup')
              )}
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-gray-500 text-sm">
              {mode === 'login' ? t('login.no.account') : t('login.has.account')}{' '}
              <button
                onClick={() => { setMode(mode === 'login' ? 'signup' : 'login'); setError(''); }}
                className="text-teal-700 font-semibold hover:text-teal-800 transition-colors"
              >
                {mode === 'login' ? t('login.create.one') : t('login.log.in')}
              </button>
            </p>
          </div>

          <p className="text-center text-gray-400 text-xs mt-8">{t('login.free.tag')}</p>
        </div>
      </div>
    </div>
  );
}
