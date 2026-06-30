import { useState, useEffect } from 'react';
import Layout from '../components/Layout';
import { useAuth } from '../context/AuthContext';
import { useLang } from '../context/LanguageContext';
import api from '../utils/api';
import { subscribeToPush, unsubscribeFromPush, setReminder, getMySubscription } from '../utils/pushNotifications';

const MONTH_NAMES = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const DOW_LABELS  = ['S','M','T','W','T','F','S'];
const HEAT_WEEKS  = 16;

function heatColor(count) {
  if (!count)    return 'bg-gray-100';
  if (count < 3) return 'bg-teal-200';
  if (count < 6) return 'bg-teal-400';
  if (count < 10) return 'bg-teal-600';
  return 'bg-teal-800';
}

function localDateKey(d) {
  const pad = n => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

function SubmissionHeatmap({ submissionCounts }) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const TOTAL = HEAT_WEEKS * 7;

  const days = [];
  for (let i = TOTAL - 1; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(today.getDate() - i);
    const key = localDateKey(d);
    days.push({ key, dow: d.getDay(), month: d.getMonth(), count: submissionCounts[key] || 0, isToday: i === 0 });
  }

  // grid[dow][col]
  const grid = Array.from({ length: 7 }, () => Array(HEAT_WEEKS).fill(null));
  days.forEach((day, idx) => { grid[day.dow][Math.floor(idx / 7)] = day; });

  // Month label: show when month changes between columns
  const monthLabels = Array.from({ length: HEAT_WEEKS }, (_, col) => {
    const first = grid.find(r => r[col])?.[col];
    if (!first) return null;
    const prev  = col > 0 ? grid.find(r => r[col - 1])?.[col - 1] : null;
    return (!prev || first.month !== prev.month) ? MONTH_NAMES[first.month] : null;
  });

  const totalSubmissions = Object.values(submissionCounts).reduce((s, c) => s + c, 0);
  const activeDays       = Object.keys(submissionCounts).length;

  return (
    <div className="overflow-x-auto">
      <div className="inline-block min-w-max">
        {/* Summary */}
        <div className="flex items-center gap-4 mb-3">
          <p className="text-gray-900 font-bold text-sm">{totalSubmissions} submissions</p>
          <p className="text-gray-400 text-xs">{activeDays} active days in the last {HEAT_WEEKS} weeks</p>
        </div>

        {/* Month row */}
        <div className="flex gap-0.75 mb-1 pl-6">
          {Array.from({ length: HEAT_WEEKS }).map((_, col) => (
            <div key={col} className="w-3.5">
              {monthLabels[col] && <span className="text-[9px] text-gray-400">{monthLabels[col]}</span>}
            </div>
          ))}
        </div>

        <div className="flex gap-0.75">
          {/* Day labels */}
          <div className="flex flex-col gap-0.75 mr-1">
            {DOW_LABELS.map((d, i) => (
              <div key={i} className="h-3.5 flex items-center">
                <span className="text-[9px] text-gray-300 w-4">{[1, 3, 5].includes(i) ? d : ''}</span>
              </div>
            ))}
          </div>

          {/* Week columns */}
          {Array.from({ length: HEAT_WEEKS }).map((_, col) => (
            <div key={col} className="flex flex-col gap-0.75">
              {Array.from({ length: 7 }).map((_, row) => {
                const day = grid[row][col];
                if (!day) return <div key={row} className="w-3.5 h-3.5" />;
                return (
                  <div
                    key={row}
                    title={`${day.key}: ${day.count} submission${day.count !== 1 ? 's' : ''}`}
                    className={`w-3.5 h-3.5 rounded-sm transition-colors ${heatColor(day.count)} ${
                      day.isToday ? 'ring-1 ring-teal-500' : ''
                    }`}
                  />
                );
              })}
            </div>
          ))}
        </div>

        {/* Legend */}
        <div className="flex items-center gap-1 mt-2 pl-6">
          <span className="text-[9px] text-gray-400 mr-0.5">Less</span>
          {['bg-gray-100','bg-teal-200','bg-teal-400','bg-teal-600','bg-teal-800'].map(c => (
            <div key={c} className={`w-3.5 h-3.5 rounded-sm ${c}`} />
          ))}
          <span className="text-[9px] text-gray-400 ml-0.5">More</span>
        </div>
      </div>
    </div>
  );
}

const SUBJECT_MAP = {
  'Quantitative Aptitude': 'Quant',
  'Reasoning':             'Reasoning',
  'English':               'English',
  'General Awareness':     'GA',
};

const colorMap = {
  'Quant':     { bar: 'bg-indigo-500', text: 'text-indigo-600', bg: 'bg-indigo-50', border: 'border-indigo-200' },
  'Reasoning': { bar: 'bg-purple-500', text: 'text-purple-600', bg: 'bg-purple-50', border: 'border-purple-200' },
  'English':   { bar: 'bg-blue-500',   text: 'text-blue-600',   bg: 'bg-blue-50',   border: 'border-blue-200'   },
  'GA':        { bar: 'bg-teal-600',   text: 'text-teal-700',   bg: 'bg-teal-50',   border: 'border-teal-200'   },
};

function computeBadges(user, t) {
  return [
    { id: 1, icon: '🎯', label: t('badge.1.label'), desc: t('badge.1.desc'), earned: (user?.total_questions || 0) > 0  },
    { id: 2, icon: '🔥', label: t('badge.2.label'), desc: t('badge.2.desc'), earned: (user?.highest_streak  || 0) >= 7 },
    { id: 3, icon: '💯', label: t('badge.3.label'), desc: t('badge.3.desc'), earned: (user?.total_questions || 0) >= 100 },
    { id: 4, icon: '🎖️', label: t('badge.4.label'), desc: t('badge.4.desc'), earned: (user?.accuracy        || 0) >= 80 },
    { id: 5, icon: '⚡', label: t('badge.5.label'), desc: t('badge.5.desc'), earned: (user?.highest_streak  || 0) >= 30 },
    { id: 6, icon: '⭐', label: t('badge.6.label'), desc: t('badge.6.desc'), earned: (user?.xp              || 0) >= 1000 },
  ];
}

function AccuracyBar({ subject, data }) {
  const c = colorMap[subject] || { bar: 'bg-teal-600', text: 'text-teal-700', bg: 'bg-teal-50', border: 'border-teal-200' };
  return (
    <div className="space-y-1.5">
      <div className="flex justify-between items-center">
        <span className="text-gray-700 text-sm font-semibold">{subject}</span>
        <div className="flex items-center gap-3">
          <span className="text-gray-400 text-xs">{data.correct}/{data.solved} correct</span>
          <span className={`${c.text} text-sm font-bold`}>{data.accuracy}%</span>
        </div>
      </div>
      <div className="w-full bg-gray-100 rounded-full h-2">
        <div className={`${c.bar} h-2 rounded-full progress-fill`} style={{ width: `${data.accuracy}%` }} />
      </div>
    </div>
  );
}

function StatCard({ icon, value, label, bg, border, text }) {
  return (
    <div className={`rounded-2xl border-2 ${bg} ${border} p-4 text-center shadow-sm`}>
      <span className="text-2xl">{icon}</span>
      <p className={`text-2xl font-bold mt-1 ${text}`}>{value}</p>
      <p className="text-gray-400 text-xs mt-0.5">{label}</p>
    </div>
  );
}

export default function Profile() {
  const { user }          = useAuth();
  const { t }             = useLang();
  const [stats, setStats]       = useState(null);
  const [loading, setLoading]   = useState(true);
  const [activity, setActivity] = useState(null);

  // Notification state
  const [notifSubscribed, setNotifSubscribed] = useState(false);
  const [reminderTime,    setReminderTime]    = useState('08:00');
  const [notifLoading,    setNotifLoading]    = useState(false);
  const [notifStatus,     setNotifStatus]     = useState('');

  useEffect(() => {
    getMySubscription().then(s => {
      setNotifSubscribed(s.subscribed);
      if (s.reminder_time) setReminderTime(s.reminder_time);
    });
  }, []);

  const handleToggleNotif = async () => {
    setNotifLoading(true);
    setNotifStatus('');
    try {
      if (notifSubscribed) {
        await unsubscribeFromPush();
        setNotifSubscribed(false);
        setNotifStatus('Notifications disabled.');
      } else {
        await subscribeToPush(reminderTime);
        setNotifSubscribed(true);
        setNotifStatus('Notifications enabled! You will be reminded at ' + reminderTime + ' IST.');
      }
    } catch (e) {
      setNotifStatus(e.message || 'Failed. Make sure notifications are allowed in your browser.');
    } finally {
      setNotifLoading(false);
    }
  };

  const handleSaveReminder = async () => {
    setNotifLoading(true);
    try {
      await setReminder(reminderTime);
      setNotifStatus('Reminder time saved: ' + reminderTime + ' IST');
    } catch (e) {
      setNotifStatus('Failed to save reminder time.');
    } finally {
      setNotifLoading(false);
    }
  };

  useEffect(() => {
    api.get('/users/stats').then(res => setStats(res.data)).catch(() => {}).finally(() => setLoading(false));
    api.get('/users/activity').then(r => setActivity(r.data)).catch(() => {});
  }, []);

  const subjectStats = stats
    ? Object.fromEntries(Object.entries(stats.subject_stats || {}).map(([full, data]) => [SUBJECT_MAP[full] || full, data]))
    : {};

  const entries = Object.entries(subjectStats);
  const weakSubject   = entries.length ? entries.reduce((a, b) => a[1].accuracy < b[1].accuracy ? a : b) : null;
  const strongSubject = entries.length ? entries.reduce((a, b) => a[1].accuracy > b[1].accuracy ? a : b) : null;

  const badges = computeBadges(user, t);

  const joinedDate = user?.created_at
    ? new Date(user.created_at).toLocaleDateString('en-IN', { month: 'long', year: 'numeric' })
    : '';

  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in space-y-5">

        {/* Profile header */}
        <div className="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
          <div className="flex flex-col sm:flex-row items-center sm:items-start gap-5">
            <div className="w-20 h-20 rounded-2xl bg-teal-700 flex items-center justify-center text-white text-3xl font-bold shrink-0 shadow-lg shadow-teal-200">
              {user?.name?.split(' ').map(n => n[0]).join('').slice(0, 2)}
            </div>
            <div className="text-center sm:text-left flex-1">
              <h1 className="text-2xl font-bold text-gray-900">{user?.name}</h1>
              <p className="text-gray-400 text-sm">{user?.email}</p>
              <div className="flex flex-wrap justify-center sm:justify-start gap-2 mt-3">
                <span className="bg-teal-50 border border-teal-200 text-teal-700 text-xs font-semibold px-3 py-1 rounded-full">{t('profile.ssccgl')}</span>
                {joinedDate && (
                  <span className="bg-gray-50 border border-gray-200 text-gray-500 text-xs font-medium px-3 py-1 rounded-full">{t('profile.joined')} {joinedDate}</span>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* Stats grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <StatCard icon="🔥" value={user?.current_streak ?? 0}             label={t('profile.streak.current')} bg="bg-orange-50"  border="border-orange-200"  text="text-orange-600" />
          <StatCard icon="🏅" value={user?.highest_streak ?? 0}             label={t('profile.streak.best')}    bg="bg-red-50"     border="border-red-200"     text="text-red-600"    />
          <StatCard icon="⭐" value={(user?.xp ?? 0).toLocaleString()}       label={t('profile.xp.total')}       bg="bg-amber-50"   border="border-amber-200"   text="text-amber-600"  />
          <StatCard icon="📋" value={user?.total_questions ?? 0}             label={t('profile.solved')}         bg="bg-teal-50"    border="border-teal-200"    text="text-teal-700"   />
        </div>

        {/* Submission Heatmap */}
        <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
          <h2 className="text-gray-900 font-bold mb-0.5">{t('profile.activity')}</h2>
          <p className="text-gray-400 text-xs mb-4">{t('profile.heatmap.sub')}</p>
          <SubmissionHeatmap submissionCounts={activity?.submission_counts ?? {}} />
        </div>

        {/* Subject accuracy */}
        <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
          <h2 className="text-gray-900 font-bold mb-4">{t('profile.performance')}</h2>
          {loading ? (
            <p className="text-gray-400 text-sm animate-pulse">{t('profile.loading')}</p>
          ) : entries.length === 0 ? (
            <p className="text-gray-400 text-sm">{t('profile.no.stats')}</p>
          ) : (
            <>
              <div className="space-y-4">
                {entries.map(([subject, data]) => <AccuracyBar key={subject} subject={subject} data={data} />)}
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-5">
                {weakSubject && (
                  <div className="bg-red-50 border border-red-200 rounded-xl p-4">
                    <p className="text-red-500 text-xs font-bold uppercase tracking-wider mb-1">{t('profile.needs.work')}</p>
                    <p className="text-gray-800 font-bold">{weakSubject[0]}</p>
                    <p className="text-gray-400 text-xs mt-1">{weakSubject[1].accuracy}% accuracy</p>
                  </div>
                )}
                {strongSubject && (
                  <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-4">
                    <p className="text-emerald-600 text-xs font-bold uppercase tracking-wider mb-1">{t('profile.strong')}</p>
                    <p className="text-gray-800 font-bold">{strongSubject[0]}</p>
                    <p className="text-gray-400 text-xs mt-1">{strongSubject[1].accuracy}% accuracy</p>
                  </div>
                )}
              </div>
            </>
          )}
        </div>

        {/* Badges */}
        <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
          <h2 className="text-gray-900 font-bold mb-1">{t('profile.badges')}</h2>
          <p className="text-gray-400 text-xs mb-4">{badges.filter(b => b.earned).length}/{badges.length} {t('profile.badges.sub')}</p>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {badges.map(badge => (
              <div key={badge.id}
                className={`relative flex flex-col items-center gap-2 rounded-xl p-4 border-2 text-center transition-all
                  ${badge.earned ? 'bg-teal-50 border-teal-200 card-hover' : 'bg-gray-50 border-gray-100 opacity-50'}`}>
                <span className={`text-3xl ${!badge.earned ? 'grayscale' : ''}`}>{badge.icon}</span>
                <p className={`text-xs font-bold ${badge.earned ? 'text-gray-800' : 'text-gray-400'}`}>{badge.label}</p>
                <p className="text-gray-400 text-xs leading-tight">{badge.desc}</p>
                {badge.earned && (
                  <span className="absolute top-2 right-2 w-4 h-4 bg-emerald-500 rounded-full flex items-center justify-center">
                    <span className="text-white text-xs">✓</span>
                  </span>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Practice Reminders */}
        <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
          <h2 className="text-gray-900 font-bold mb-1">{t('profile.notif.title')}</h2>
          <p className="text-gray-400 text-xs mb-4">{t('profile.notif.desc')}</p>

          <div className="flex items-center justify-between mb-4">
            <div>
              <p className="text-sm font-semibold text-gray-700">{t('profile.notif.daily')}</p>
              <p className="text-xs text-gray-400 mt-0.5">
                {notifSubscribed ? t('profile.notif.on') : t('profile.notif.off')}
              </p>
            </div>
            <button
              onClick={handleToggleNotif}
              disabled={notifLoading}
              className={`relative w-12 h-6 rounded-full transition-all duration-300 focus:outline-none disabled:opacity-50
                ${notifSubscribed ? 'bg-teal-700' : 'bg-gray-200'}`}
            >
              <span className={`absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow transition-transform duration-300
                ${notifSubscribed ? 'translate-x-6' : 'translate-x-0'}`} />
            </button>
          </div>

          {notifSubscribed && (
            <div className="bg-teal-50 border border-teal-100 rounded-xl p-4 fade-in">
              <label className="block text-sm font-semibold text-gray-700 mb-2">{t('profile.notif.time')}</label>
              <div className="flex items-center gap-3">
                <input
                  type="time"
                  value={reminderTime}
                  onChange={e => setReminderTime(e.target.value)}
                  className="bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-gray-900 text-sm focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-100 transition-all"
                />
                <button
                  onClick={handleSaveReminder}
                  disabled={notifLoading}
                  className="bg-teal-700 hover:bg-teal-800 text-white text-sm font-semibold px-4 py-2.5 rounded-xl transition-colors disabled:opacity-50"
                >
                  {t('profile.save')}
                </button>
              </div>
              <p className="text-teal-600 text-xs mt-2">{t('profile.notif.footer').replace('{time}', reminderTime)}</p>
            </div>
          )}

          {notifStatus && (
            <p className={`text-xs mt-3 font-medium ${notifStatus.includes('Failed') || notifStatus.includes('denied') ? 'text-red-500' : 'text-teal-700'}`}>
              {notifStatus}
            </p>
          )}
        </div>

      </div>
    </Layout>
  );
}
