import Layout from '../components/Layout';
import { Link } from 'react-router-dom';

const values = [
  { icon: '⚡', title: 'Daily Consistency',  desc: 'Just 5 questions a day compounds into exam-cracking skill over months. Small daily actions beat occasional long sessions every time.' },
  { icon: '🏆', title: 'Competitive Drive',   desc: 'Live leaderboards and streaks make preparation feel like a game you genuinely want to win — not a chore you keep postponing.' },
  { icon: '🎯', title: 'Focused Practice',    desc: 'No long videos, no fluff. Pure active practice with real SSC CGL questions and explanations that actually build retention.' },
  { icon: '💰', title: 'Free Forever',         desc: 'Quality exam preparation should be accessible to every aspirant regardless of financial background. No paywalls, ever.' },
];

const roadmap = [
  {
    phase: 'Phase 1 · Now', badge: 'bg-emerald-50 border-emerald-200 text-emerald-700',
    dot: 'bg-emerald-500',
    items: ['SSC CGL Tier 1 & 2 practice', 'Daily challenge with streak system', 'XP rewards & live leaderboard', 'Subject-wise performance analytics', 'Previous Year Papers (2010–2024)'],
  },
  {
    phase: 'Phase 2 · Coming Soon', badge: 'bg-amber-50 border-amber-200 text-amber-700',
    dot: 'bg-amber-400',
    items: ['Full-length mock tests', 'Live contests & tournaments', 'Mobile app (Android & iOS)', 'Discussion community & doubt solving'],
  },
  {
    phase: 'Phase 3 · Future', badge: 'bg-blue-50 border-blue-200 text-blue-700',
    dot: 'bg-blue-400',
    items: ['UPSC · Banking · GATE · CAT support', 'AI-powered personalised study plans', 'Offline downloads for low-connectivity areas', 'Premium leaderboard battles'],
  },
];

const team = [
  { initials: 'JS', name: 'Jagrati Sahu', role: 'Founder & Developer', bg: 'bg-teal-700' },
];

export default function About() {
  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in space-y-7">

        {/* Hero */}
        <div className="accent-card p-8 text-center">
          <div className="w-16 h-16 rounded-2xl bg-teal-700 flex items-center justify-center text-white text-3xl font-bold mx-auto mb-4 shadow-lg shadow-teal-200">
            V
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-3">About <span className="gradient-text">VidyaAi</span></h1>
          <p className="text-gray-500 text-base leading-relaxed max-w-xl mx-auto">
            A <span className="text-teal-700 font-semibold">gamified exam preparation platform</span> built to help every SSC CGL aspirant build
            daily consistency, practise smarter, and crack the exam — without expensive coaching.
          </p>
        </div>

        {/* Our Story */}
        <div className="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
          <h2 className="text-gray-900 font-bold text-lg mb-3">Our Story</h2>
          <p className="text-gray-500 text-sm leading-relaxed mb-3">
            VidyaAi was born from a simple frustration — most SSC CGL aspirants start with high motivation but lose consistency within two weeks.
            Existing platforms push long video lectures that feel like school all over again. Students watch passively, never practise actively,
            and eventually give up.
          </p>
          <p className="text-gray-700 text-sm leading-relaxed font-medium">
            We took inspiration from apps like Duolingo and built VidyaAi to make exam preparation feel like a game —
            <span className="text-teal-700"> daily streaks, XP rewards, live leaderboards, real PYQs</span>.
            The goal isn't 8-hour study sessions. It's 10 focused minutes every single day.
          </p>
        </div>

        {/* Problem → Solution */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="bg-red-50 border border-red-200 rounded-2xl p-5">
            <p className="text-red-600 text-xs font-bold uppercase tracking-wider mb-3">❌ The Problem</p>
            <ul className="space-y-2">
              {[
                'Passive video lectures don\'t build recall',
                'No consistency tracking or accountability',
                'Expensive coaching out of reach for many',
                'No feedback on weak subjects until it\'s too late',
              ].map(p => (
                <li key={p} className="text-gray-600 text-sm flex items-start gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-red-400 shrink-0 mt-1.5" />
                  {p}
                </li>
              ))}
            </ul>
          </div>
          <div className="bg-teal-50 border border-teal-200 rounded-2xl p-5">
            <p className="text-teal-700 text-xs font-bold uppercase tracking-wider mb-3">✅ Our Solution</p>
            <ul className="space-y-2">
              {[
                'Active MCQ practice with real SSC questions',
                'Daily streaks and XP to enforce consistency',
                'Free forever — no paywalls on core features',
                'Instant feedback with subject-wise accuracy tracking',
              ].map(s => (
                <li key={s} className="text-gray-600 text-sm flex items-start gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-teal-500 shrink-0 mt-1.5" />
                  {s}
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Core Values */}
        <div>
          <h2 className="text-gray-900 font-bold text-lg mb-4">Our Core Principles</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {values.map(v => (
              <div key={v.title} className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm card-hover">
                <span className="text-3xl">{v.icon}</span>
                <h3 className="text-gray-900 font-semibold mt-3 mb-1">{v.title}</h3>
                <p className="text-gray-500 text-sm leading-relaxed">{v.desc}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Team */}
        <div className="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
          <h2 className="text-gray-900 font-bold text-lg mb-5">The Team</h2>
          <div className="flex flex-wrap gap-4">
            {team.map(t => (
              <div key={t.name} className="flex items-center gap-3 bg-gray-50 border border-gray-200 rounded-xl px-4 py-3">
                <div className={`w-10 h-10 rounded-xl ${t.bg} flex items-center justify-center text-white font-bold text-sm shadow-sm`}>
                  {t.initials}
                </div>
                <div>
                  <p className="text-gray-900 font-semibold text-sm">{t.name}</p>
                  <p className="text-gray-400 text-xs">{t.role}</p>
                </div>
              </div>
            ))}
          </div>
          <p className="text-gray-400 text-xs mt-4">
            VidyaAi is an independent project built with passion for making quality exam prep accessible to every aspirant in India.
          </p>
        </div>

        {/* Roadmap */}
        <div>
          <h2 className="text-gray-900 font-bold text-lg mb-4">Roadmap</h2>
          <div className="space-y-3">
            {roadmap.map(r => (
              <div key={r.phase} className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
                <span className={`text-xs font-bold px-2.5 py-1 rounded-full border ${r.badge}`}>{r.phase}</span>
                <ul className="mt-3 space-y-1.5">
                  {r.items.map(item => (
                    <li key={item} className="text-gray-500 text-sm flex items-center gap-2">
                      <span className={`w-1.5 h-1.5 rounded-full shrink-0 ${r.dot}`} />
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>

        {/* CTA */}
        <div className="bg-teal-700 rounded-2xl p-8 text-center shadow-lg shadow-teal-200">
          <h3 className="text-white font-bold text-xl mb-2">Ready to start your streak?</h3>
          <p className="text-teal-100 text-sm mb-5">Join thousands of SSC CGL aspirants practising daily on VidyaAi.</p>
          <Link to="/daily-challenge"
            className="inline-block bg-amber-400 hover:bg-amber-500 text-gray-900 font-bold px-8 py-3 rounded-xl transition-all shadow-md text-sm">
            Start Today's Challenge ⚡
          </Link>
        </div>

      </div>
    </Layout>
  );
}
