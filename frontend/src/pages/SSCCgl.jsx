import { useState } from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { useAuth } from '../context/AuthContext';

const tier1Subjects = [
  {
    icon: '🔢', label: 'Quantitative Aptitude', code: 'quant',
    topics: ['Number System', 'Percentage', 'Ratio & Proportion', 'Time & Work', 'Speed & Distance', 'Algebra', 'Geometry', 'Mensuration'],
    color: { bg: 'bg-indigo-500/10', border: 'border-indigo-500/30', text: 'text-indigo-400', btn: 'bg-indigo-600 hover:bg-indigo-500' },
    total: 100,
  },
  {
    icon: '🧩', label: 'Reasoning', code: 'reasoning',
    topics: ['Series', 'Analogy', 'Coding-Decoding', 'Blood Relations', 'Direction Sense', 'Syllogism', 'Matrix', 'Venn Diagram'],
    color: { bg: 'bg-purple-500/10', border: 'border-purple-500/30', text: 'text-purple-400', btn: 'bg-purple-600 hover:bg-purple-500' },
    total: 100,
  },
  {
    icon: '📝', label: 'English', code: 'english',
    topics: ['Synonyms', 'Antonyms', 'Spotting Errors', 'Fill in the Blanks', 'Comprehension', 'One Word Substitution', 'Idioms', 'Active/Passive'],
    color: { bg: 'bg-blue-500/10', border: 'border-blue-500/30', text: 'text-blue-400', btn: 'bg-blue-600 hover:bg-blue-500' },
    total: 100,
  },
  {
    icon: '🌍', label: 'General Awareness', code: 'ga',
    topics: ['History', 'Geography', 'Indian Polity', 'Economy', 'Science & Tech', 'Current Affairs', 'Sports', 'Awards & Honours'],
    color: { bg: 'bg-cyan-500/10', border: 'border-cyan-500/30', text: 'text-cyan-400', btn: 'bg-cyan-600 hover:bg-cyan-500' },
    total: 100,
  },
];

const tier2Subjects = [
  {
    icon: '📐', label: 'Advanced Quantitative Aptitude',
    topics: ['Advanced Algebra', 'Trigonometry', 'Geometry', 'Statistics', 'Data Interpretation'],
    color: { bg: 'bg-violet-500/10', border: 'border-violet-500/30', text: 'text-violet-400', btn: 'bg-violet-600 hover:bg-violet-500' },
    total: 80,
  },
  {
    icon: '✍️', label: 'Advanced English',
    topics: ['Reading Comprehension', 'Cloze Test', 'Para Jumbles', 'Sentence Improvement', 'Vocabulary'],
    color: { bg: 'bg-fuchsia-500/10', border: 'border-fuchsia-500/30', text: 'text-fuchsia-400', btn: 'bg-fuchsia-600 hover:bg-fuchsia-500' },
    total: 60,
  },
  {
    icon: '🧠', label: 'Advanced Reasoning',
    topics: ['Analytical Reasoning', 'Critical Thinking', 'Statement & Conclusion', 'Logical Puzzles'],
    color: { bg: 'bg-pink-500/10', border: 'border-pink-500/30', text: 'text-pink-400', btn: 'bg-pink-600 hover:bg-pink-500' },
    total: 60,
  },
];

const difficultyInfo = [
  { level: 'easy',   icon: '🟢', label: 'Easy',   xp: 5,  color: 'text-green-400', bg: 'bg-green-500/10', border: 'border-green-500/30' },
  { level: 'medium', icon: '🟡', label: 'Medium', xp: 10, color: 'text-amber-400', bg: 'bg-amber-500/10', border: 'border-amber-500/30' },
  { level: 'hard',   icon: '🔴', label: 'Hard',   xp: 20, color: 'text-rose-400',  bg: 'bg-rose-500/10',  border: 'border-rose-500/30'  },
];

function SubjectCard({ subject }) {
  const [expanded, setExpanded] = useState(false);
  const { color } = subject;

  return (
    <div className={`${color.bg} border ${color.border} rounded-2xl p-5 card-hover hover:border-opacity-60 transition-all`}>
      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center gap-3">
          <span className="text-3xl">{subject.icon}</span>
          <div>
            <h3 className={`font-bold ${color.text}`}>{subject.label}</h3>
            <p className="text-gray-600 text-xs">{subject.total} questions</p>
          </div>
        </div>
      </div>

      <div className="flex gap-2 mb-3 flex-wrap">
        {difficultyInfo.map(d => (
          <span key={d.level} className={`text-xs font-medium px-2 py-0.5 rounded-full ${d.bg} ${d.color} border ${d.border}`}>
            {d.icon} +{d.xp} XP
          </span>
        ))}
      </div>

      <button
        onClick={() => setExpanded(e => !e)}
        className="text-gray-600 text-xs hover:text-gray-300 transition-colors flex items-center gap-1 mb-3"
      >
        {expanded ? '▲ Hide topics' : '▼ View topics'}
      </button>
      {expanded && (
        <div className="flex flex-wrap gap-1.5 mb-4">
          {subject.topics.map(t => (
            <span key={t} className="text-xs bg-white/5 text-gray-400 border border-white/10 rounded-full px-2.5 py-0.5">{t}</span>
          ))}
        </div>
      )}

      <Link
        to="/daily-challenge"
        className={`w-full flex items-center justify-center gap-2 ${color.btn} text-white font-semibold py-2.5 rounded-xl transition-all duration-150 text-sm`}
      >
        Practice Now →
      </Link>
    </div>
  );
}

export default function SSCCgl() {
  const { user } = useAuth();
  const [activeTab, setActiveTab] = useState('tier1');

  return (
    <Layout>
      <div className="fade-in">
        {/* Header */}
        <div className="mb-6">
          <span className="text-xs text-rose-400 bg-rose-500/10 border border-rose-500/25 rounded-full px-2.5 py-1 font-medium">SSC CGL</span>
          <h1 className="text-2xl font-bold text-white mt-2">SSC CGL Preparation Arena</h1>
          <p className="text-gray-500 text-sm mt-1">Choose your tier and continue your streak 🔥</p>
        </div>

        {/* User stats bar */}
        <div className="flex flex-wrap gap-3 mb-7">
          {[
            { icon: '🎯', val: `${user?.accuracy}%`,            label: 'Accuracy' },
            { icon: '📋', val: user?.total_questions,           label: 'Solved'   },
            { icon: '🔥', val: `${user?.current_streak} days`,  label: 'Streak'   },
            { icon: '⭐', val: user?.xp?.toLocaleString(),      label: 'Total XP' },
          ].map(s => (
            <div key={s.label} className="flex items-center gap-2 bg-[#130022] border border-purple-800/30 rounded-xl px-4 py-2.5">
              <span className="text-lg">{s.icon}</span>
              <div>
                <p className="text-white font-semibold text-sm leading-tight">{s.val}</p>
                <p className="text-gray-600 text-xs">{s.label}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Tab switcher */}
        <div className="flex gap-1.5 mb-6 bg-[#130022] border border-purple-800/30 rounded-xl p-1 w-fit">
          <button
            onClick={() => setActiveTab('tier1')}
            className={`px-5 py-2 rounded-lg text-sm font-medium transition-all duration-150
              ${activeTab === 'tier1'
                ? 'bg-linear-to-r from-rose-600 to-violet-600 text-white shadow-lg'
                : 'text-gray-500 hover:text-white'}`}
          >
            📖 Tier 1 — Main
          </button>
          <button
            onClick={() => setActiveTab('tier2')}
            className={`px-5 py-2 rounded-lg text-sm font-medium transition-all duration-150
              ${activeTab === 'tier2'
                ? 'bg-violet-600 text-white shadow-lg'
                : 'text-gray-500 hover:text-white'}`}
          >
            🚀 Tier 2 — Advanced
          </button>
        </div>

        {/* Tier 1 */}
        {activeTab === 'tier1' && (
          <div>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-white font-bold text-lg">Tier 1 Subjects</h2>
              <Link to="/daily-challenge" className="text-rose-400 text-sm hover:text-rose-300 transition-colors">
                Today's Challenge ⚡
              </Link>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
              {tier1Subjects.map(s => <SubjectCard key={s.code} subject={s} />)}
            </div>

            <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5">
              <h3 className="text-white font-bold mb-4">XP Rewards Per Difficulty</h3>
              <div className="grid grid-cols-3 gap-3">
                {difficultyInfo.map(d => (
                  <div key={d.level} className={`${d.bg} border ${d.border} rounded-xl p-4 text-center`}>
                    <span className="text-2xl">{d.icon}</span>
                    <p className={`font-bold text-lg mt-1 ${d.color}`}>+{d.xp} XP</p>
                    <p className="text-gray-600 text-xs mt-0.5 capitalize">{d.label}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Tier 2 */}
        {activeTab === 'tier2' && (
          <div>
            <div className="bg-amber-500/10 border border-amber-500/25 rounded-xl px-4 py-3 mb-5 flex items-center gap-3">
              <span className="text-xl">⚠️</span>
              <p className="text-amber-400 text-sm font-medium">Recommended after completing Tier 1 preparation.</p>
            </div>
            <div className="grid grid-cols-1 gap-4">
              {tier2Subjects.map(s => <SubjectCard key={s.label} subject={s} />)}
            </div>
          </div>
        )}
      </div>
    </Layout>
  );
}
