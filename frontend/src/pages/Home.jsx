import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useLang } from '../context/LanguageContext';
import Layout from '../components/Layout';
import api from '../utils/api';

const colorMap = {
  indigo:  { bg: 'bg-indigo-50',  border: 'border-indigo-200',  text: 'text-indigo-600'  },
  purple:  { bg: 'bg-purple-50',  border: 'border-purple-200',  text: 'text-purple-600'  },
  blue:    { bg: 'bg-blue-50',    border: 'border-blue-200',    text: 'text-blue-600'    },
  teal:    { bg: 'bg-teal-50',    border: 'border-teal-200',    text: 'text-teal-700'    },
  violet:  { bg: 'bg-violet-50',  border: 'border-violet-200',  text: 'text-violet-600'  },
  fuchsia: { bg: 'bg-fuchsia-50', border: 'border-fuchsia-200', text: 'text-fuchsia-600' },
  pink:    { bg: 'bg-pink-50',    border: 'border-pink-200',    text: 'text-pink-600'    },
};

const DOW_SHORT = ['S', 'M', 'T', 'W', 'T', 'F', 'S'];

function localDateKey(d) {
  const pad = n => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

function StreakCalendar({ activeDates }) {
  const activeSet = new Set(activeDates);
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const WEEKS = 5;
  const days = [];
  for (let i = WEEKS * 7 - 1; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(today.getDate() - i);
    const key = localDateKey(d);
    days.push({ key, dow: d.getDay(), active: activeSet.has(key), isToday: i === 0 });
  }

  const grid = Array.from({ length: 7 }, () => Array(WEEKS).fill(null));
  days.forEach((day, idx) => { grid[day.dow][Math.floor(idx / 7)] = day; });

  return (
    <div className="flex gap-1.5">
      {/* Day-of-week labels — only M / W / F */}
      <div className="flex flex-col gap-1 mr-0.5">
        {DOW_SHORT.map((d, i) => (
          <div key={i} className="h-[18px] flex items-center">
            <span className="text-gray-300 text-[9px] w-2.5">{[1, 3, 5].includes(i) ? d : ''}</span>
          </div>
        ))}
      </div>

      {/* Week columns */}
      {Array.from({ length: WEEKS }).map((_, col) => (
        <div key={col} className="flex flex-col gap-1">
          {Array.from({ length: 7 }).map((_, row) => {
            const day = grid[row][col];
            if (!day) return <div key={row} className="w-[18px] h-[18px]" />;
            const done = day.active;
            return (
              <div
                key={row}
                title={day.key}
                className={`w-[18px] h-[18px] rounded-full flex items-center justify-center transition-all
                  ${done ? 'bg-teal-600' : 'bg-gray-100 border border-gray-200'}
                  ${day.isToday ? 'ring-2 ring-teal-400 ring-offset-1' : ''}`}
              >
                {done && (
                  <svg className="w-2.5 h-2.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3.5}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                  </svg>
                )}
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
}

export default function Home() {
  const { user } = useAuth();
  const { t } = useLang();

  const [activity, setActivity] = useState(null);

  useEffect(() => {
    api.get('/users/activity')
      .then(r => setActivity(r.data))
      .catch(() => {});
  }, []);

  const streak        = user?.current_streak ?? 0;
  const highestStreak = activity?.highest_streak ?? user?.highest_streak ?? 0;
  const todayDone     = activity?.today_done ?? false;

  const subjectCards = [
    { icon: '🔢', label: t('ssc.subj.quant'),     color: 'indigo' },
    { icon: '🧩', label: t('ssc.subj.reasoning'), color: 'purple' },
    { icon: '📝', label: t('ssc.subj.english'),   color: 'blue'   },
    { icon: '🌍', label: t('ssc.subj.ga'),         color: 'teal'   },
  ];

  const advSubjects = [
    { icon: '📐', label: t('ssc.adv.quant'),     color: 'violet'  },
    { icon: '✍️', label: t('ssc.adv.english'),   color: 'fuchsia' },
    { icon: '🧠', label: t('ssc.adv.reasoning'), color: 'pink'    },
  ];

  const difficultyCards = [
    {
      level: 'Easy', icon: '🟢',
      bg: 'bg-emerald-50', border: 'border-emerald-200', text: 'text-emerald-700',
      btn: 'bg-emerald-500 hover:bg-emerald-600 shadow-emerald-200',
      label: t('diff.easy'), desc: t('home.easy.desc'),
      practiceLabel: t('home.practice.easy'), xp: '+5 XP/question',
    },
    {
      level: 'Medium', icon: '🟡',
      bg: 'bg-amber-50', border: 'border-amber-200', text: 'text-amber-700',
      btn: 'bg-amber-500 hover:bg-amber-600 shadow-amber-200',
      label: t('diff.medium'), desc: t('home.medium.desc'),
      practiceLabel: t('home.practice.medium'), xp: '+10 XP/question',
    },
    {
      level: 'Hard', icon: '🔴',
      bg: 'bg-red-50', border: 'border-red-200', text: 'text-red-700',
      btn: 'bg-red-500 hover:bg-red-600 shadow-red-200',
      label: t('diff.hard'), desc: t('home.hard.desc'),
      practiceLabel: t('home.practice.hard'), xp: '+20 XP/question',
    },
  ];

  return (
    <Layout>
      {/* Welcome */}
      <div className="mb-4">
        <h1 className="text-xl font-bold text-gray-900">
          Hey <span className="gradient-text">{user?.name?.split(' ')[0]}</span> 👋
        </h1>
      </div>

      {/* ── STREAK CARD ── */}
      <div className="bg-white border border-gray-200 rounded-2xl p-4 shadow-sm mb-4">
        {/* Top row: flame + streak + stats */}
        <div className="flex items-center gap-3 mb-3">
          <span className={`text-2xl ${streak > 0 ? 'streak-pulse' : ''}`}>🔥</span>
          <div>
            <span className="text-xl font-black text-gray-900">{streak}</span>
            <span className="text-gray-400 text-xs ml-1.5">{t('home.streak.days')}</span>
          </div>
          <div className="ml-auto flex items-center gap-4">
            <div className="text-right">
              <p className="text-[10px] text-gray-400">{t('home.streak.best')}</p>
              <p className="text-sm font-bold text-amber-500">🏆 {highestStreak}d</p>
            </div>
            <div className="text-right">
              <p className="text-[10px] text-gray-400">{t('home.xp.total')}</p>
              <p className="text-sm font-bold text-teal-700">⭐ {(user?.xp ?? 0).toLocaleString()}</p>
            </div>
          </div>
        </div>

        {/* Calendar heatmap */}
        <p className="text-[10px] font-semibold text-gray-300 uppercase tracking-wider mb-1.5">{t('home.last5weeks')}</p>
        <StreakCalendar activeDates={activity?.active_dates ?? []} />
      </div>

      {/* ── DAILY CHALLENGE CARD ── */}
      <div className={`rounded-2xl border-2 p-5 mb-6 transition-all ${
        todayDone
          ? 'bg-emerald-50 border-emerald-200'
          : 'accent-card'
      }`}>
        <div className="flex items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className={`w-14 h-14 rounded-2xl flex items-center justify-center text-3xl shrink-0 ${
              todayDone ? 'bg-emerald-100 border border-emerald-200' : 'bg-teal-50 border border-teal-200'
            }`}>
              {todayDone ? '✅' : '⚡'}
            </div>
            <div>
              <p className={`text-xs font-bold uppercase tracking-wider mb-0.5 ${todayDone ? 'text-emerald-600' : 'text-teal-700'}`}>
                {t('home.challenge.badge')}
              </p>
              <h2 className="text-gray-900 font-bold text-lg leading-tight">{t('home.challenge.title')}</h2>
              {todayDone ? (
                <p className="text-emerald-600 text-sm font-semibold mt-0.5">{t('home.challenge.done')}</p>
              ) : (
                <p className="text-gray-500 text-sm mt-0.5">5 Questions · <span className="text-amber-600 font-bold">+50 XP</span></p>
              )}
            </div>
          </div>
          {!todayDone && (
            <Link
              to="/daily-challenge"
              className="shrink-0 bg-teal-700 hover:bg-teal-800 text-white font-semibold px-5 py-3 rounded-xl transition-all text-sm shadow-lg shadow-teal-200 whitespace-nowrap"
            >
              {t('home.challenge.btn')}
            </Link>
          )}
        </div>
      </div>

      {/* SSC CGL heading */}
      <div className="flex items-center gap-3 mb-5">
        <div className="w-8 h-8 rounded-lg bg-teal-50 border border-teal-200 flex items-center justify-center text-sm">📚</div>
        <div>
          <h2 className="text-gray-900 font-bold text-lg">{t('home.arena.title')}</h2>
          <p className="text-gray-400 text-xs">{t('home.arena.sub')}</p>
        </div>
      </div>

      {/* Tier Cards */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5 mb-8">
        <div className="bg-white border border-gray-200 hover:border-teal-300 rounded-2xl p-6 card-hover transition-all shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <div>
              <span className="text-xs font-semibold text-teal-700 bg-teal-50 border border-teal-200 rounded-full px-2.5 py-1">{t('home.tier1.badge')}</span>
              <h3 className="text-gray-900 font-bold text-xl mt-2">{t('home.tier1.title')}</h3>
              <p className="text-gray-400 text-sm">{t('home.tier1.sub')}</p>
            </div>
            <span className="text-4xl">📖</span>
          </div>
          <div className="grid grid-cols-2 gap-2 mb-5">
            {subjectCards.map(s => {
              const c = colorMap[s.color];
              return (
                <div key={s.color} className={`flex items-center gap-2 rounded-xl px-3 py-2 ${c.bg} border ${c.border}`}>
                  <span className="text-lg">{s.icon}</span>
                  <p className={`text-xs font-semibold ${c.text}`}>{s.label.split(' ')[0]}</p>
                </div>
              );
            })}
          </div>
          <div className="flex items-center justify-between mb-2 text-sm">
            <span className="text-gray-400">{user?.total_questions || 0} {t('home.solved')}</span>
            <span className="text-teal-700 font-semibold">{(user?.accuracy ?? 0).toFixed(0)}% accuracy</span>
          </div>
          <div className="w-full bg-gray-100 rounded-full h-1.5 mb-5">
            <div className="bg-teal-600 h-1.5 rounded-full progress-fill" style={{ width: `${Math.min(((user?.total_questions || 0) / 400) * 100, 100)}%` }} />
          </div>
          <Link to="/ssc-cgl" className="w-full flex items-center justify-center gap-2 bg-teal-700 hover:bg-teal-800 text-white font-semibold py-2.5 rounded-xl transition-all text-sm shadow-md shadow-teal-200">
            {t('home.tier1.btn')}
          </Link>
        </div>

        <div className="bg-white border border-gray-200 hover:border-amber-300 rounded-2xl p-6 card-hover transition-all shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <div>
              <span className="text-xs font-semibold text-amber-600 bg-amber-50 border border-amber-200 rounded-full px-2.5 py-1">{t('home.tier2.badge')}</span>
              <h3 className="text-gray-900 font-bold text-xl mt-2">{t('home.tier2.title')}</h3>
              <p className="text-gray-400 text-sm">{t('home.tier2.sub')}</p>
            </div>
            <span className="text-4xl">🚀</span>
          </div>
          <div className="grid grid-cols-1 gap-2 mb-5">
            {advSubjects.map(s => {
              const c = colorMap[s.color];
              return (
                <div key={s.color} className={`flex items-center gap-2 rounded-xl px-3 py-2.5 ${c.bg} border ${c.border}`}>
                  <span className="text-lg">{s.icon}</span>
                  <p className={`text-sm font-semibold ${c.text}`}>{s.label}</p>
                </div>
              );
            })}
          </div>
          <div className="bg-amber-50 border border-amber-200 rounded-xl px-4 py-3 mb-5">
            <p className="text-amber-700 text-xs font-semibold">{t('home.tier2.warn')}</p>
          </div>
          <Link to="/ssc-cgl" className="w-full flex items-center justify-center gap-2 bg-amber-500 hover:bg-amber-600 text-white font-semibold py-2.5 rounded-xl transition-all text-sm shadow-md shadow-amber-200">
            {t('home.tier2.btn')}
          </Link>
        </div>
      </div>

      {/* Quick Practice */}
      <h2 className="text-gray-900 font-bold text-lg mb-4">{t('home.quickpractice')}</h2>
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        {difficultyCards.map(d => (
          <div key={d.level} className={`${d.bg} border ${d.border} rounded-2xl p-5 card-hover shadow-sm`}>
            <div className="flex items-center gap-2 mb-3">
              <span className="text-xl">{d.icon}</span>
              <h3 className={`font-bold ${d.text}`}>{d.label}</h3>
            </div>
            <p className="text-gray-500 text-xs mb-3">{d.desc}</p>
            <p className={`text-xs font-bold ${d.text} mb-4`}>{d.xp}</p>
            <Link to="/daily-challenge" className={`w-full flex items-center justify-center py-2 rounded-xl text-white text-sm font-semibold transition-colors shadow-md ${d.btn}`}>
              {d.practiceLabel}
            </Link>
          </div>
        ))}
      </div>
    </Layout>
  );
}
