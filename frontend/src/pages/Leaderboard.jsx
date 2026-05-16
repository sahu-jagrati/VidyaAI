import { useState, useEffect } from 'react';
import Layout from '../components/Layout';
import api from '../utils/api';

const FILTERS = ['Daily', 'Weekly', 'Monthly'];

const podiumColors = [
  { bg: 'bg-yellow-500', text: 'text-yellow-400', label: '🥇', glow: 'shadow-yellow-500/20' },
  { bg: 'bg-gray-400',   text: 'text-gray-300',   label: '🥈', glow: 'shadow-gray-400/20'   },
  { bg: 'bg-orange-700', text: 'text-orange-400', label: '🥉', glow: 'shadow-orange-700/20'  },
];

export default function Leaderboard() {
  const [filter, setFilter]     = useState('Weekly');
  const [entries, setEntries]   = useState([]);
  const [loading, setLoading]   = useState(true);
  const [error, setError]       = useState('');

  useEffect(() => {
    setLoading(true);
    setError('');
    api.get(`/leaderboard?filter=${filter.toLowerCase()}`)
      .then(res => setEntries(res.data.entries))
      .catch(() => setError('Could not load leaderboard.'))
      .finally(() => setLoading(false));
  }, [filter]);

  const mainEntries = entries.filter(e => !e.is_outside_top);
  const top3   = mainEntries.slice(0, 3);
  const rest   = mainEntries.slice(3);
  const meRow  = entries.find(e => e.is_current_user);

  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in">
        {/* Header */}
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-white">
            Leaderboard <span className="gradient-text">🏆</span>
          </h1>
          <p className="text-gray-500 text-sm mt-1">Compete with thousands of SSC CGL aspirants</p>
        </div>

        {/* Filter tabs */}
        <div className="flex gap-1.5 mb-8 bg-[#130022] border border-purple-800/30 rounded-xl p-1 w-fit">
          {FILTERS.map(f => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={`px-5 py-2 rounded-lg text-sm font-medium transition-all duration-150
                ${filter === f
                  ? 'bg-linear-to-r from-rose-600 to-violet-600 text-white shadow-lg'
                  : 'text-gray-500 hover:text-white'}`}
            >
              {f}
            </button>
          ))}
        </div>

        {/* Your rank card */}
        {meRow && (
          <div className="gradient-border mb-6">
            <div className="gradient-border-inner p-4 flex items-center gap-4">
              <div className="w-10 h-10 rounded-full bg-linear-to-br from-rose-500 to-violet-600 flex items-center justify-center text-white font-bold text-sm shrink-0 shadow-lg">
                {meRow.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-white font-semibold text-sm">{meRow.name} <span className="text-rose-400 text-xs">(You)</span></p>
                <p className="text-gray-500 text-xs">{meRow.current_streak}🔥 streak · {meRow.accuracy?.toFixed(1)}% accuracy</p>
              </div>
              <div className="text-right shrink-0">
                <p className="gradient-text font-bold text-lg">Rank #{meRow.rank}</p>
                <p className="text-yellow-400 text-xs">{meRow.xp?.toLocaleString()} XP</p>
              </div>
            </div>
          </div>
        )}

        {loading ? (
          <div className="text-center py-16 text-gray-600 animate-pulse">Loading...</div>
        ) : error ? (
          <div className="text-center py-16 text-red-400">{error}</div>
        ) : entries.length === 0 ? (
          <div className="text-center py-16 text-gray-600">
            <p className="text-2xl mb-2">🏜️</p>
            <p>No data yet for this period. Be the first!</p>
          </div>
        ) : (
          <>
            {/* Podium (top 3) */}
            {top3.length === 3 && (
              <div className="grid grid-cols-3 gap-3 mb-8">
                {[top3[1], top3[0], top3[2]].map((entry, visualIdx) => {
                  const realRank = visualIdx === 0 ? 1 : visualIdx === 1 ? 0 : 2;
                  const podium   = podiumColors[realRank];
                  const isCenter = visualIdx === 1;
                  return (
                    <div
                      key={entry.rank}
                      className={`relative flex flex-col items-center bg-[#130022] border rounded-2xl p-4 transition-all shadow-lg ${podium.glow}
                        ${isCenter ? 'border-yellow-500/40 -translate-y-3' : 'border-purple-800/30'}`}
                    >
                      <span className="text-2xl mb-2">{podium.label}</span>
                      <div className={`w-12 h-12 rounded-full ${podium.bg} flex items-center justify-center text-gray-900 font-bold text-sm mb-2`}>
                        {entry.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
                      </div>
                      <p className="text-white font-semibold text-xs text-center leading-tight">{entry.name}</p>
                      <p className={`${podium.text} font-bold text-sm mt-1`}>{entry.xp?.toLocaleString()}</p>
                      <p className="text-gray-600 text-xs">XP</p>
                      <div className="mt-2 flex items-center gap-1">
                        <span className="text-orange-400 text-xs">🔥{entry.current_streak}</span>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}

            {/* Rankings table */}
            <div className="bg-[#130022] border border-purple-800/30 rounded-2xl overflow-hidden">
              <div className="grid grid-cols-[2rem_1fr_auto_auto_auto] gap-3 px-4 py-3 border-b border-purple-900/30 text-xs font-medium text-gray-600 uppercase tracking-wider">
                <span>#</span>
                <span>Player</span>
                <span className="text-right hidden sm:block">Streak</span>
                <span className="text-right hidden sm:block">Acc</span>
                <span className="text-right">XP</span>
              </div>

              {rest.map((entry) => (
                <div
                  key={`${entry.rank}-${entry.user_id}`}
                  className={`grid grid-cols-[2rem_1fr_auto_auto_auto] gap-3 items-center px-4 py-3.5 border-b border-purple-900/20 last:border-0 transition-colors
                    ${entry.is_current_user ? 'bg-rose-500/5' : 'hover:bg-white/2'}`}
                >
                  <span className="text-gray-500 text-sm font-medium">{entry.rank}</span>

                  <div className="flex items-center gap-3 min-w-0">
                    <div className={`w-8 h-8 rounded-full shrink-0 flex items-center justify-center text-xs font-bold
                      ${entry.is_current_user
                        ? 'bg-linear-to-br from-rose-500 to-violet-600 text-white'
                        : 'bg-white/5 text-gray-400'}`}>
                      {entry.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
                    </div>
                    <div className="min-w-0">
                      <p className={`text-sm font-medium truncate ${entry.is_current_user ? 'text-rose-300' : 'text-white'}`}>
                        {entry.name} {entry.is_current_user && <span className="text-rose-500 text-xs">(You)</span>}
                      </p>
                    </div>
                  </div>

                  <span className="text-orange-400 text-xs hidden sm:block text-right">🔥 {entry.current_streak}</span>
                  <span className="text-green-400 text-xs hidden sm:block text-right">{entry.accuracy?.toFixed(1)}%</span>
                  <span className="text-yellow-400 text-sm font-semibold text-right">{entry.xp?.toLocaleString()}</span>
                </div>
              ))}
            </div>
          </>
        )}

        <p className="text-center text-gray-700 text-xs mt-4">
          Resets every {filter === 'Daily' ? 'midnight' : filter === 'Weekly' ? 'Monday' : 'month'} · IST
        </p>
      </div>
    </Layout>
  );
}
