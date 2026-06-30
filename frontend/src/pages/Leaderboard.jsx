import { useState, useEffect } from 'react';
import Layout from '../components/Layout';
import { useLang } from '../context/LanguageContext';
import api from '../utils/api';

const FILTERS = ['Daily', 'Weekly', 'Monthly'];
const podiumColors = [
  { bg: 'bg-yellow-400', text: 'text-yellow-700', label: '🥇', shadow: 'shadow-yellow-200' },
  { bg: 'bg-gray-300',   text: 'text-gray-600',   label: '🥈', shadow: 'shadow-gray-200'   },
  { bg: 'bg-amber-400',  text: 'text-amber-800',  label: '🥉', shadow: 'shadow-amber-200'  },
];

export default function Leaderboard() {
  const { t } = useLang();
  const [filter, setFilter]   = useState('Weekly');
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState('');

  useEffect(() => {
    setLoading(true);
    setError('');
    api.get(`/leaderboard?filter=${filter.toLowerCase()}`)
      .then(res => setEntries(res.data.entries))
      .catch(() => setError(t('lb.error')))
      .finally(() => setLoading(false));
  }, [filter]);

  const mainEntries = entries.filter(e => !e.is_outside_top);
  const top3  = mainEntries.slice(0, 3);
  const rest  = mainEntries.slice(3);
  const meRow = entries.find(e => e.is_current_user);

  const resetLabel = filter === 'Daily' ? t('lb.reset.daily') : filter === 'Weekly' ? t('lb.reset.weekly') : t('lb.reset.monthly');

  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in">
        {/* Header */}
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900">{t('lb.title')} <span className="gradient-text">🏆</span></h1>
          <p className="text-gray-400 text-sm mt-1">{t('lb.sub')}</p>
        </div>

        {/* Filter tabs */}
        <div className="flex gap-1 mb-8 bg-gray-100 border border-gray-200 rounded-xl p-1 w-fit">
          {FILTERS.map(f => (
            <button key={f} onClick={() => setFilter(f)}
              className={`px-5 py-2 rounded-lg text-sm font-semibold transition-all duration-150
                ${filter === f ? 'bg-teal-700 text-white shadow-md shadow-teal-200' : 'text-gray-500 hover:text-gray-800'}`}>
              {t('lb.' + f.toLowerCase())}
            </button>
          ))}
        </div>

        {/* Your rank card */}
        {meRow && (
          <div className="accent-card p-4 flex items-center gap-4 mb-6">
            <div className="w-10 h-10 rounded-full bg-teal-700 flex items-center justify-center text-white font-bold text-sm shrink-0 shadow-md shadow-teal-200">
              {meRow.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-gray-900 font-bold text-sm">{meRow.name} <span className="text-teal-700 text-xs font-semibold">{t('lb.you')}</span></p>
              <p className="text-gray-400 text-xs">{meRow.current_streak}🔥 streak · {meRow.accuracy?.toFixed(1)}% accuracy</p>
            </div>
            <div className="text-right shrink-0">
              <p className="gradient-text font-bold text-lg">Rank #{meRow.rank}</p>
              <p className="text-amber-600 text-xs font-semibold">{meRow.xp?.toLocaleString()} XP</p>
            </div>
          </div>
        )}

        {loading ? (
          <div className="text-center py-16 text-gray-400 animate-pulse">{t('lb.loading')}</div>
        ) : error ? (
          <div className="text-center py-16 text-red-500">{error}</div>
        ) : entries.length === 0 ? (
          <div className="text-center py-16 text-gray-400">
            <p className="text-2xl mb-2">🏜️</p>
            <p>{t('lb.empty')}</p>
          </div>
        ) : (
          <>
            {/* Podium */}
            {top3.length === 3 && (
              <div className="grid grid-cols-3 gap-3 mb-8">
                {[top3[1], top3[0], top3[2]].map((entry, visualIdx) => {
                  const realRank = visualIdx === 0 ? 1 : visualIdx === 1 ? 0 : 2;
                  const podium   = podiumColors[realRank];
                  const isCenter = visualIdx === 1;
                  return (
                    <div key={entry.rank}
                      className={`flex flex-col items-center bg-white border-2 rounded-2xl p-4 shadow-md ${podium.shadow}
                        ${isCenter ? 'border-yellow-300 -translate-y-3' : 'border-gray-100'}`}>
                      <span className="text-2xl mb-2">{podium.label}</span>
                      <div className={`w-12 h-12 rounded-full ${podium.bg} flex items-center justify-center font-bold text-sm mb-2`}>
                        {entry.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
                      </div>
                      <p className="text-gray-800 font-bold text-xs text-center">{entry.name}</p>
                      <p className={`${podium.text} font-bold text-sm mt-1`}>{entry.xp?.toLocaleString()}</p>
                      <p className="text-gray-400 text-xs">XP</p>
                      <span className="text-orange-500 text-xs mt-1">🔥{entry.current_streak}</span>
                    </div>
                  );
                })}
              </div>
            )}

            {/* Table */}
            <div className="bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
              <div className="grid grid-cols-[2rem_1fr_auto_auto_auto] gap-3 px-4 py-3 border-b border-gray-100 text-xs font-bold text-gray-400 uppercase tracking-wider">
                <span>#</span><span>{t('lb.col.player')}</span>
                <span className="text-right hidden sm:block">{t('lb.col.streak')}</span>
                <span className="text-right hidden sm:block">{t('lb.col.acc')}</span>
                <span className="text-right">XP</span>
              </div>
              {rest.map((entry) => (
                <div key={`${entry.rank}-${entry.user_id}`}
                  className={`grid grid-cols-[2rem_1fr_auto_auto_auto] gap-3 items-center px-4 py-3.5 border-b border-gray-50 last:border-0
                    ${entry.is_current_user ? 'bg-teal-50' : 'hover:bg-gray-50'}`}>
                  <span className="text-gray-400 text-sm font-semibold">{entry.rank}</span>
                  <div className="flex items-center gap-3 min-w-0">
                    <div className={`w-8 h-8 rounded-full shrink-0 flex items-center justify-center text-xs font-bold
                      ${entry.is_current_user ? 'bg-teal-700 text-white' : 'bg-gray-100 text-gray-500'}`}>
                      {entry.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
                    </div>
                    <p className={`text-sm font-semibold truncate ${entry.is_current_user ? 'text-teal-700' : 'text-gray-800'}`}>
                      {entry.name} {entry.is_current_user && <span className="text-teal-500 text-xs">{t('lb.you')}</span>}
                    </p>
                  </div>
                  <span className="text-orange-500 text-xs hidden sm:block text-right font-semibold">🔥 {entry.current_streak}</span>
                  <span className="text-emerald-600 text-xs hidden sm:block text-right font-semibold">{entry.accuracy?.toFixed(1)}%</span>
                  <span className="text-amber-600 text-sm font-bold text-right">{entry.xp?.toLocaleString()}</span>
                </div>
              ))}
            </div>
          </>
        )}
        <p className="text-center text-gray-400 text-xs mt-4">
          {resetLabel}
        </p>
      </div>
    </Layout>
  );
}
