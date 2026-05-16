import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Layout from '../components/Layout';

const subjectCards = [
  { icon: '🔢', label: 'Quantitative Aptitude', questions: 100, color: 'indigo' },
  { icon: '🧩', label: 'Reasoning',             questions: 100, color: 'purple' },
  { icon: '📝', label: 'English',                questions: 100, color: 'blue'   },
  { icon: '🌍', label: 'General Awareness',      questions: 100, color: 'cyan'   },
];

const advSubjects = [
  { icon: '📐', label: 'Advanced Quant',     color: 'violet'  },
  { icon: '✍️', label: 'Advanced English',   color: 'fuchsia' },
  { icon: '🧠', label: 'Advanced Reasoning', color: 'pink'    },
];

const colorMap = {
  indigo:  { bg: 'bg-indigo-500/10',  border: 'border-indigo-500/30',  text: 'text-indigo-400'  },
  purple:  { bg: 'bg-purple-500/10',  border: 'border-purple-500/30',  text: 'text-purple-400'  },
  blue:    { bg: 'bg-blue-500/10',    border: 'border-blue-500/30',    text: 'text-blue-400'    },
  cyan:    { bg: 'bg-cyan-500/10',    border: 'border-cyan-500/30',    text: 'text-cyan-400'    },
  violet:  { bg: 'bg-violet-500/10',  border: 'border-violet-500/30',  text: 'text-violet-400'  },
  fuchsia: { bg: 'bg-fuchsia-500/10', border: 'border-fuchsia-500/30', text: 'text-fuchsia-400' },
  pink:    { bg: 'bg-pink-500/10',    border: 'border-pink-500/30',    text: 'text-pink-400'    },
};

const difficultyCards = [
  {
    level: 'Easy',   icon: '🟢',
    bg: 'bg-green-500/10', border: 'border-green-500/30', text: 'text-green-400',
    btn: 'bg-green-600 hover:bg-green-500',
    desc: 'Formula-based beginner questions. Build your confidence here.',
    xp: '+5 XP/question',
  },
  {
    level: 'Medium', icon: '🟡',
    bg: 'bg-amber-500/10', border: 'border-amber-500/30', text: 'text-amber-400',
    btn: 'bg-amber-600 hover:bg-amber-500',
    desc: 'Standard SSC-level questions. This is the real preparation zone.',
    xp: '+10 XP/question',
  },
  {
    level: 'Hard',   icon: '🔴',
    bg: 'bg-rose-500/10', border: 'border-rose-500/30', text: 'text-rose-400',
    btn: 'bg-rose-600 hover:bg-rose-500',
    desc: 'Tricky time-based PYQs. For the serious challenger.',
    xp: '+20 XP/question',
  },
];

function StatBadge({ icon, value, label, bg, border, text }) {
  return (
    <div className={`flex flex-col items-center justify-center p-4 rounded-2xl border ${bg} ${border}`}>
      <span className="text-2xl mb-1">{icon}</span>
      <span className={`text-2xl font-bold ${text}`}>{value}</span>
      <span className="text-gray-600 text-xs mt-0.5">{label}</span>
    </div>
  );
}

export default function Home() {
  const { user } = useAuth();

  return (
    <Layout>
      {/* Welcome */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-white">
          Hey <span className="gradient-text">{user?.name?.split(' ')[0]}</span> 👋
        </h1>
        <p className="text-gray-500 text-sm mt-1">
          {user?.current_streak > 0
            ? `You're on a ${user.current_streak}-day streak! Don't break it! 🔥`
            : 'Start your streak today — solve at least 1 question!'}
        </p>
      </div>

      {/* Stats row */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8">
        <StatBadge icon="🔥" value={user?.current_streak} label="Day Streak"
          bg="bg-orange-500/10" border="border-orange-500/25" text="text-orange-400" />
        <StatBadge icon="⭐" value={user?.xp?.toLocaleString()} label="Total XP"
          bg="bg-yellow-500/10" border="border-yellow-500/25" text="text-yellow-400" />
        <StatBadge icon="🏆" value={`${(user?.accuracy ?? 0).toFixed(0)}%`} label="Accuracy"
          bg="bg-violet-500/10" border="border-violet-500/25" text="text-violet-400" />
        <StatBadge icon="📋" value={user?.total_questions ?? 0} label="Solved"
          bg="bg-rose-500/10" border="border-rose-500/25" text="text-rose-400" />
      </div>

      {/* Daily Challenge widget — gradient border */}
      <div className="gradient-border mb-8">
        <div className="gradient-border-inner p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className="w-14 h-14 rounded-2xl bg-linear-to-br from-rose-500/20 to-violet-500/20 border border-rose-500/30 flex items-center justify-center text-3xl shrink-0">
              ⚡
            </div>
            <div>
              <p className="text-xs text-rose-400 font-semibold uppercase tracking-wider mb-0.5">Today's Challenge</p>
              <h2 className="text-white font-bold text-lg leading-tight">5 Questions · Mixed Subjects</h2>
              <p className="text-gray-500 text-sm mt-0.5">
                Complete to earn <span className="text-yellow-400 font-semibold">+50 XP</span> and protect your streak!
              </p>
            </div>
          </div>
          <Link
            to="/daily-challenge"
            className="shrink-0 bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 text-white font-semibold px-6 py-3 rounded-xl transition-all duration-200 text-sm shadow-lg glow-rose"
          >
            Start Now →
          </Link>
        </div>
      </div>

      {/* SSC CGL heading */}
      <div className="flex items-center gap-3 mb-5">
        <div className="w-8 h-8 rounded-lg bg-rose-500/15 border border-rose-500/25 flex items-center justify-center text-sm">📚</div>
        <div>
          <h2 className="text-white font-bold text-lg">SSC CGL Preparation Arena</h2>
          <p className="text-gray-600 text-xs">Choose your phase and continue your streak.</p>
        </div>
      </div>

      {/* Tier Cards */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5 mb-8">
        {/* Tier 1 */}
        <div className="bg-[#130022] border border-purple-800/30 hover:border-rose-500/40 rounded-2xl p-6 card-hover transition-all">
          <div className="flex items-center justify-between mb-4">
            <div>
              <span className="text-xs font-medium text-rose-400 bg-rose-500/10 border border-rose-500/25 rounded-full px-2.5 py-1">
                Tier 1 · Main
              </span>
              <h3 className="text-white font-bold text-xl mt-2">SSC CGL Tier 1</h3>
              <p className="text-gray-500 text-sm">4 subjects · 400 questions</p>
            </div>
            <span className="text-4xl">📖</span>
          </div>

          <div className="grid grid-cols-2 gap-2 mb-5">
            {subjectCards.map(s => {
              const c = colorMap[s.color];
              return (
                <div key={s.label} className={`flex items-center gap-2 rounded-xl px-3 py-2 ${c.bg} border ${c.border}`}>
                  <span className="text-lg">{s.icon}</span>
                  <div>
                    <p className={`text-xs font-medium ${c.text}`}>{s.label.split(' ')[0]}</p>
                    <p className="text-gray-600 text-xs">{s.questions} Qs</p>
                  </div>
                </div>
              );
            })}
          </div>

          <div className="flex items-center justify-between mb-2 text-sm">
            <span className="text-gray-500">{user?.total_questions || 0} solved</span>
            <span className="text-rose-400 font-medium">{user?.accuracy}% accuracy</span>
          </div>
          <div className="w-full bg-[#1e0030] rounded-full h-1.5 mb-5">
            <div
              className="bg-linear-to-r from-rose-500 to-violet-500 h-1.5 rounded-full progress-fill"
              style={{ width: `${Math.min(((user?.total_questions || 0) / 400) * 100, 100)}%` }}
            />
          </div>

          <Link
            to="/ssc-cgl"
            className="w-full flex items-center justify-center gap-2 bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 text-white font-semibold py-2.5 rounded-xl transition-all duration-200 text-sm"
          >
            Start Practising →
          </Link>
        </div>

        {/* Tier 2 */}
        <div className="bg-[#130022] border border-purple-800/30 hover:border-violet-500/40 rounded-2xl p-6 card-hover transition-all">
          <div className="flex items-center justify-between mb-4">
            <div>
              <span className="text-xs font-medium text-violet-400 bg-violet-500/10 border border-violet-500/25 rounded-full px-2.5 py-1">
                Tier 2 · Advanced
              </span>
              <h3 className="text-white font-bold text-xl mt-2">SSC CGL Tier 2</h3>
              <p className="text-gray-500 text-sm">3 subjects · Advanced level</p>
            </div>
            <span className="text-4xl">🚀</span>
          </div>

          <div className="grid grid-cols-1 gap-2 mb-5">
            {advSubjects.map(s => {
              const c = colorMap[s.color];
              return (
                <div key={s.label} className={`flex items-center gap-2 rounded-xl px-3 py-2.5 ${c.bg} border ${c.border}`}>
                  <span className="text-lg">{s.icon}</span>
                  <p className={`text-sm font-medium ${c.text}`}>{s.label}</p>
                </div>
              );
            })}
          </div>

          <div className="bg-amber-500/10 border border-amber-500/25 rounded-xl px-4 py-3 mb-5">
            <p className="text-amber-400 text-xs font-medium">⚠️ Recommended after Tier 1 completion</p>
          </div>

          <Link
            to="/ssc-cgl"
            className="w-full flex items-center justify-center gap-2 bg-violet-600 hover:bg-violet-500 text-white font-semibold py-2.5 rounded-xl transition-all duration-150 text-sm"
          >
            Continue Advanced Prep →
          </Link>
        </div>
      </div>

      {/* Quick Difficulty Practice */}
      <h2 className="text-white font-bold text-lg mb-4">Quick Practice</h2>
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        {difficultyCards.map(d => (
          <div key={d.level} className={`${d.bg} border ${d.border} rounded-2xl p-5 card-hover`}>
            <div className="flex items-center gap-2 mb-3">
              <span className="text-xl">{d.icon}</span>
              <h3 className={`font-bold ${d.text}`}>{d.level}</h3>
            </div>
            <p className="text-gray-500 text-xs mb-3">{d.desc}</p>
            <p className={`text-xs font-semibold ${d.text} mb-4`}>{d.xp}</p>
            <Link
              to="/daily-challenge"
              className={`w-full flex items-center justify-center py-2 rounded-xl text-white text-sm font-medium transition-colors ${d.btn}`}
            >
              Practice {d.level}
            </Link>
          </div>
        ))}
      </div>
    </Layout>
  );
}
