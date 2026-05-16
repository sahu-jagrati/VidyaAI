import { useState, useEffect } from 'react';
import Layout from '../components/Layout';
import { useAuth } from '../context/AuthContext';
import api from '../utils/api';

const SUBJECT_MAP = {
  'Quantitative Aptitude': 'Quant',
  'Reasoning':             'Reasoning',
  'English':               'English',
  'General Awareness':     'GA',
};

const colorMap = {
  'Quant':     { bar: 'bg-indigo-500', text: 'text-indigo-400' },
  'Reasoning': { bar: 'bg-purple-500', text: 'text-purple-400' },
  'English':   { bar: 'bg-blue-500',   text: 'text-blue-400'   },
  'GA':        { bar: 'bg-cyan-500',   text: 'text-cyan-400'   },
};

function computeBadges(user) {
  return [
    {
      id: 1, icon: '🎯', label: 'First Step',
      desc: 'Answer your first question',
      earned: (user?.total_questions || 0) > 0,
    },
    {
      id: 2, icon: '🔥', label: 'Week Warrior',
      desc: '7-day streak',
      earned: (user?.highest_streak || 0) >= 7,
    },
    {
      id: 3, icon: '💯', label: 'Century Club',
      desc: 'Solve 100 questions',
      earned: (user?.total_questions || 0) >= 100,
    },
    {
      id: 4, icon: '🎖️', label: 'Accuracy King',
      desc: '80%+ overall accuracy',
      earned: (user?.accuracy || 0) >= 80,
    },
    {
      id: 5, icon: '⚡', label: 'Streak Master',
      desc: '30-day streak',
      earned: (user?.highest_streak || 0) >= 30,
    },
    {
      id: 6, icon: '⭐', label: 'XP Collector',
      desc: 'Earn 1000 XP',
      earned: (user?.xp || 0) >= 1000,
    },
  ];
}

function AccuracyBar({ subject, data }) {
  const c = colorMap[subject] || { bar: 'bg-rose-500', text: 'text-rose-400' };
  return (
    <div className="space-y-1.5">
      <div className="flex justify-between items-center">
        <span className="text-gray-300 text-sm font-medium">{subject}</span>
        <div className="flex items-center gap-3">
          <span className="text-gray-600 text-xs">{data.correct}/{data.solved} correct</span>
          <span className={`${c.text} text-sm font-semibold`}>{data.accuracy}%</span>
        </div>
      </div>
      <div className="w-full bg-[#1e0030] rounded-full h-2">
        <div className={`${c.bar} h-2 rounded-full progress-fill`} style={{ width: `${data.accuracy}%` }} />
      </div>
    </div>
  );
}

function StatCard({ icon, value, label, bg, border, text }) {
  return (
    <div className={`rounded-2xl border ${bg} ${border} p-4 text-center`}>
      <span className="text-2xl">{icon}</span>
      <p className={`text-2xl font-bold mt-1 ${text}`}>{value}</p>
      <p className="text-gray-600 text-xs mt-0.5">{label}</p>
    </div>
  );
}

export default function Profile() {
  const { user } = useAuth();
  const [stats, setStats]     = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('/users/stats')
      .then(res => setStats(res.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const subjectStats = stats
    ? Object.fromEntries(
        Object.entries(stats.subject_stats || {}).map(([full, data]) => [
          SUBJECT_MAP[full] || full, data,
        ])
      )
    : {};

  const entries = Object.entries(subjectStats);
  const weakSubject   = entries.length ? entries.reduce((a, b) => a[1].accuracy < b[1].accuracy ? a : b) : null;
  const strongSubject = entries.length ? entries.reduce((a, b) => a[1].accuracy > b[1].accuracy ? a : b) : null;

  const badges = computeBadges(user);

  const today = new Date();
  const calendarDays = Array.from({ length: 28 }, (_, i) => {
    const d = new Date(today);
    d.setDate(today.getDate() - (27 - i));
    return { date: d.getDate(), active: i >= 28 - (user?.current_streak || 0) };
  });

  const joinedDate = user?.created_at
    ? new Date(user.created_at).toLocaleDateString('en-IN', { month: 'long', year: 'numeric' })
    : '';

  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in space-y-6">
        {/* Profile header */}
        <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-6">
          <div className="flex flex-col sm:flex-row items-center sm:items-start gap-5">
            <div className="w-20 h-20 rounded-2xl bg-linear-to-br from-rose-500 to-violet-600 flex items-center justify-center text-white text-3xl font-bold shrink-0 shadow-xl">
              {user?.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
            </div>
            <div className="text-center sm:text-left flex-1">
              <h1 className="text-2xl font-bold text-white">{user?.name}</h1>
              <p className="text-gray-500 text-sm">{user?.email}</p>
              <div className="flex flex-wrap justify-center sm:justify-start gap-2 mt-3">
                <span className="bg-rose-500/10 border border-rose-500/25 text-rose-400 text-xs font-medium px-3 py-1 rounded-full">
                  📚 SSC CGL
                </span>
                {joinedDate && (
                  <span className="bg-white/5 border border-white/10 text-gray-400 text-xs font-medium px-3 py-1 rounded-full">
                    📅 Joined {joinedDate}
                  </span>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* Stats grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <StatCard icon="🔥" value={user?.current_streak ?? 0} label="Current Streak"
            bg="bg-orange-500/10" border="border-orange-500/25" text="text-orange-400" />
          <StatCard icon="🏅" value={user?.highest_streak ?? 0} label="Best Streak"
            bg="bg-red-500/10" border="border-red-500/25" text="text-red-400" />
          <StatCard icon="⭐" value={(user?.xp ?? 0).toLocaleString()} label="Total XP"
            bg="bg-yellow-500/10" border="border-yellow-500/25" text="text-yellow-400" />
          <StatCard icon="📋" value={user?.total_questions ?? 0} label="Questions Solved"
            bg="bg-green-500/10" border="border-green-500/25" text="text-green-400" />
        </div>

        {/* Streak Calendar */}
        <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5">
          <h2 className="text-white font-bold mb-1">Activity Streak</h2>
          <p className="text-gray-600 text-xs mb-4">Last 28 days</p>
          <div className="grid grid-cols-7 gap-1.5">
            {['S','M','T','W','T','F','S'].map((d, i) => (
              <span key={i} className="text-center text-gray-700 text-xs">{d}</span>
            ))}
            {calendarDays.map((day, i) => (
              <div
                key={i}
                title={`Day ${day.date}`}
                className={`aspect-square rounded-md flex items-center justify-center text-xs transition-all
                  ${day.active
                    ? 'bg-linear-to-br from-rose-600 to-violet-600 text-white shadow-sm'
                    : 'bg-[#1e0030] text-gray-700'}`}
              >
                {day.date}
              </div>
            ))}
          </div>
        </div>

        {/* Subject accuracy */}
        <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5">
          <h2 className="text-white font-bold mb-4">Subject Performance</h2>
          {loading ? (
            <p className="text-gray-600 text-sm animate-pulse">Loading stats...</p>
          ) : entries.length === 0 ? (
            <p className="text-gray-600 text-sm">Complete some questions to see your stats here.</p>
          ) : (
            <>
              <div className="space-y-4">
                {entries.map(([subject, data]) => (
                  <AccuracyBar key={subject} subject={subject} data={data} />
                ))}
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-5">
                {weakSubject && (
                  <div className="bg-red-500/10 border border-red-500/25 rounded-xl p-4">
                    <p className="text-red-400 text-xs font-medium uppercase tracking-wider mb-1">⚠️ Needs Work</p>
                    <p className="text-white font-semibold">{weakSubject[0]}</p>
                    <p className="text-gray-500 text-xs mt-1">{weakSubject[1].accuracy}% accuracy — keep practising!</p>
                  </div>
                )}
                {strongSubject && (
                  <div className="bg-green-500/10 border border-green-500/25 rounded-xl p-4">
                    <p className="text-green-400 text-xs font-medium uppercase tracking-wider mb-1">✅ Strong Area</p>
                    <p className="text-white font-semibold">{strongSubject[0]}</p>
                    <p className="text-gray-500 text-xs mt-1">{strongSubject[1].accuracy}% accuracy — excellent!</p>
                  </div>
                )}
              </div>
            </>
          )}
        </div>

        {/* Badges */}
        <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5">
          <h2 className="text-white font-bold mb-1">Badges</h2>
          <p className="text-gray-600 text-xs mb-4">{badges.filter(b => b.earned).length}/{badges.length} earned</p>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {badges.map(badge => (
              <div
                key={badge.id}
                className={`relative flex flex-col items-center gap-2 rounded-xl p-4 border text-center transition-all
                  ${badge.earned
                    ? 'bg-rose-500/10 border-rose-500/25 card-hover'
                    : 'bg-white/2 border-purple-900/20 opacity-40'}`}
              >
                <span className={`text-3xl ${!badge.earned ? 'grayscale' : ''}`}>{badge.icon}</span>
                <p className={`text-xs font-semibold ${badge.earned ? 'text-white' : 'text-gray-600'}`}>{badge.label}</p>
                <p className="text-gray-700 text-xs leading-tight">{badge.desc}</p>
                {badge.earned && (
                  <span className="absolute top-2 right-2 w-4 h-4 bg-green-500 rounded-full flex items-center justify-center">
                    <span className="text-white text-xs">✓</span>
                  </span>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
    </Layout>
  );
}
