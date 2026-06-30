import { useState } from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { useAuth } from '../context/AuthContext';
import { useLang } from '../context/LanguageContext';

const difficultyInfo = [
  { level: 'easy',   icon: '🟢', xp: 5,  color: 'text-emerald-700', bg: 'bg-emerald-50', border: 'border-emerald-200' },
  { level: 'medium', icon: '🟡', xp: 10, color: 'text-amber-700',   bg: 'bg-amber-50',   border: 'border-amber-200'   },
  { level: 'hard',   icon: '🔴', xp: 20, color: 'text-red-700',     bg: 'bg-red-50',     border: 'border-red-200'     },
];

function SubjectCard({ subject }) {
  const [expanded, setExpanded] = useState(false);
  const { t } = useLang();
  const { color } = subject;

  return (
    <div className={`${color.bg} border-2 ${color.border} rounded-2xl p-5 card-hover transition-all shadow-sm`}>
      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center gap-3">
          <span className="text-3xl">{subject.icon}</span>
          <div>
            <h3 className={`font-bold ${color.text}`}>{subject.label}</h3>
          </div>
        </div>
      </div>
      <div className="flex gap-2 mb-3 flex-wrap">
        {difficultyInfo.map(d => (
          <span key={d.level} className={`text-xs font-semibold px-2 py-0.5 rounded-full ${d.bg} ${d.color} border ${d.border}`}>
            {d.icon} +{d.xp} XP
          </span>
        ))}
      </div>
      <button onClick={() => setExpanded(e => !e)}
        className="text-gray-400 text-xs hover:text-gray-600 transition-colors flex items-center gap-1 mb-3">
        {expanded ? t('ssc.hide.topics') : t('ssc.view.topics')}
      </button>
      {expanded && (
        <div className="flex flex-wrap gap-1.5 mb-4">
          {subject.topics.map(topic => (
            <span key={topic} className="text-xs bg-white text-gray-500 border border-gray-200 rounded-full px-2.5 py-0.5">{topic}</span>
          ))}
        </div>
      )}
      <Link to="/daily-challenge"
        className={`w-full flex items-center justify-center gap-2 ${color.btn} text-white font-bold py-2.5 rounded-xl transition-all duration-150 text-sm shadow-md`}>
        {t('ssc.practice.now')}
      </Link>
    </div>
  );
}

export default function SSCCgl() {
  const { user } = useAuth();
  const { t } = useLang();
  const [activeTab, setActiveTab] = useState('tier1');

  const tier1Subjects = [
    {
      icon: '🔢', label: t('ssc.subj.quant'), code: 'quant',
      topics: ['Number System', 'Percentage', 'Ratio & Proportion', 'Time & Work', 'Speed & Distance', 'Algebra', 'Geometry', 'Mensuration'],
      color: { bg: 'bg-indigo-50', border: 'border-indigo-200', text: 'text-indigo-700', btn: 'bg-indigo-600 hover:bg-indigo-700 shadow-indigo-200' },
    },
    {
      icon: '🧩', label: t('ssc.subj.reasoning'), code: 'reasoning',
      topics: ['Series', 'Analogy', 'Coding-Decoding', 'Blood Relations', 'Direction Sense', 'Syllogism', 'Matrix', 'Venn Diagram'],
      color: { bg: 'bg-purple-50', border: 'border-purple-200', text: 'text-purple-700', btn: 'bg-purple-600 hover:bg-purple-700 shadow-purple-200' },
    },
    {
      icon: '📝', label: t('ssc.subj.english'), code: 'english',
      topics: ['Synonyms', 'Antonyms', 'Spotting Errors', 'Fill in the Blanks', 'Comprehension', 'One Word Substitution', 'Idioms', 'Active/Passive'],
      color: { bg: 'bg-blue-50', border: 'border-blue-200', text: 'text-blue-700', btn: 'bg-blue-600 hover:bg-blue-700 shadow-blue-200' },
    },
    {
      icon: '🌍', label: t('ssc.subj.ga'), code: 'ga',
      topics: ['History', 'Geography', 'Indian Polity', 'Economy', 'Science & Tech', 'Current Affairs', 'Sports', 'Awards & Honours'],
      color: { bg: 'bg-teal-50', border: 'border-teal-200', text: 'text-teal-700', btn: 'bg-teal-700 hover:bg-teal-800 shadow-teal-200' },
    },
  ];

  const tier2Subjects = [
    {
      icon: '📐', label: t('ssc.adv.quant'),
      topics: ['Advanced Algebra', 'Trigonometry', 'Geometry', 'Statistics', 'Data Interpretation'],
      color: { bg: 'bg-violet-50', border: 'border-violet-200', text: 'text-violet-700', btn: 'bg-violet-600 hover:bg-violet-700 shadow-violet-200' },
    },
    {
      icon: '✍️', label: t('ssc.adv.english'),
      topics: ['Reading Comprehension', 'Cloze Test', 'Para Jumbles', 'Sentence Improvement', 'Vocabulary'],
      color: { bg: 'bg-fuchsia-50', border: 'border-fuchsia-200', text: 'text-fuchsia-700', btn: 'bg-fuchsia-600 hover:bg-fuchsia-700 shadow-fuchsia-200' },
    },
    {
      icon: '🧠', label: t('ssc.adv.reasoning'),
      topics: ['Analytical Reasoning', 'Critical Thinking', 'Statement & Conclusion', 'Logical Puzzles'],
      color: { bg: 'bg-pink-50', border: 'border-pink-200', text: 'text-pink-700', btn: 'bg-pink-600 hover:bg-pink-700 shadow-pink-200' },
    },
  ];

  return (
    <Layout>
      <div className="fade-in">
        <div className="mb-6">
          <span className="text-xs font-bold text-teal-700 bg-teal-50 border border-teal-200 rounded-full px-2.5 py-1">{t('ssc.badge')}</span>
          <h1 className="text-2xl font-bold text-gray-900 mt-2">{t('ssc.title')}</h1>
          <p className="text-gray-400 text-sm mt-1">{t('ssc.sub')}</p>
        </div>

        {/* Stats bar */}
        <div className="flex flex-wrap gap-3 mb-7">
          {[
            { icon: '🎯', val: `${(user?.accuracy ?? 0).toFixed(0)}%`, label: t('ssc.accuracy'), bg: 'bg-teal-50',   border: 'border-teal-200',   text: 'text-teal-700'   },
            { icon: '📋', val: user?.total_questions ?? 0,              label: t('ssc.solved'),   bg: 'bg-blue-50',   border: 'border-blue-200',   text: 'text-blue-700'   },
            { icon: '🔥', val: `${user?.current_streak ?? 0}d`,        label: t('ssc.streak'),   bg: 'bg-orange-50', border: 'border-orange-200', text: 'text-orange-700' },
            { icon: '⭐', val: (user?.xp ?? 0).toLocaleString(),        label: t('ssc.xp'),       bg: 'bg-amber-50',  border: 'border-amber-200',  text: 'text-amber-700'  },
          ].map(s => (
            <div key={s.label} className={`flex items-center gap-2 ${s.bg} border ${s.border} rounded-xl px-4 py-2.5 shadow-sm`}>
              <span className="text-lg">{s.icon}</span>
              <div>
                <p className={`${s.text} font-bold text-sm leading-tight`}>{s.val}</p>
                <p className="text-gray-400 text-xs">{s.label}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Tab switcher */}
        <div className="flex gap-1 mb-6 bg-gray-100 border border-gray-200 rounded-xl p-1 w-fit">
          <button onClick={() => setActiveTab('tier1')}
            className={`px-5 py-2 rounded-lg text-sm font-bold transition-all duration-150
              ${activeTab === 'tier1' ? 'bg-teal-700 text-white shadow-md shadow-teal-200' : 'text-gray-500 hover:text-gray-800'}`}>
            {t('ssc.tier1.tab')}
          </button>
          <button onClick={() => setActiveTab('tier2')}
            className={`px-5 py-2 rounded-lg text-sm font-bold transition-all duration-150
              ${activeTab === 'tier2' ? 'bg-amber-500 text-white shadow-md shadow-amber-200' : 'text-gray-500 hover:text-gray-800'}`}>
            {t('ssc.tier2.tab')}
          </button>
        </div>

        {activeTab === 'tier1' && (
          <div>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-gray-900 font-bold text-lg">{t('ssc.tier1.title')}</h2>
              <Link to="/daily-challenge" className="text-teal-700 text-sm font-semibold hover:text-teal-800 transition-colors">
                {t('ssc.challenge.link')}
              </Link>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
              {tier1Subjects.map(s => <SubjectCard key={s.code} subject={s} />)}
            </div>
            <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
              <h3 className="text-gray-900 font-bold mb-4">{t('ssc.xprewards')}</h3>
              <div className="grid grid-cols-3 gap-3">
                {difficultyInfo.map(d => (
                  <div key={d.level} className={`${d.bg} border-2 ${d.border} rounded-xl p-4 text-center shadow-sm`}>
                    <span className="text-2xl">{d.icon}</span>
                    <p className={`font-bold text-lg mt-1 ${d.color}`}>+{d.xp} XP</p>
                    <p className="text-gray-400 text-xs mt-0.5 capitalize">{t('diff.' + d.level)}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'tier2' && (
          <div>
            <div className="bg-amber-50 border border-amber-200 rounded-xl px-4 py-3 mb-5 flex items-center gap-3">
              <span className="text-xl">⚠️</span>
              <p className="text-amber-700 text-sm font-semibold">{t('ssc.tier2.warn')}</p>
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
