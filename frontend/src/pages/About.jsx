import Layout from '../components/Layout';
import { Link } from 'react-router-dom';

const values = [
  { icon: '⚡', title: 'Daily Consistency', desc: 'Just 5 questions a day compounds into exam-cracking skill over months.' },
  { icon: '🏆', title: 'Competitive Drive',  desc: 'Leaderboards and streaks make preparation feel like a game you want to win.' },
  { icon: '🎯', title: 'Focused Practice',   desc: 'No videos, no fluff. Pure active practice that actually builds retention.' },
  { icon: '💰', title: 'Free Forever',        desc: 'No paywalls for core practice. Quality preparation should be accessible.' },
];

const roadmap = [
  { phase: 'Phase 1 · Now',   color: 'text-green-400  bg-green-500/10  border-green-500/30',  items: ['SSC CGL Tier 1 & 2 practice', 'Streak system', 'XP & Leaderboard', 'Profile analytics'] },
  { phase: 'Phase 2 · Soon',  color: 'text-yellow-400 bg-yellow-500/10 border-yellow-500/30', items: ['Mock tests', 'Live contests', 'Mobile app', 'Discussion community'] },
  { phase: 'Phase 3 · Later', color: 'text-violet-400  bg-violet-500/10  border-violet-500/30', items: ['UPSC · Banking · GATE · CAT', 'AI doubt solver', 'Personalised study plans', 'Premium leaderboard battles'] },
];

export default function About() {
  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in space-y-8">
        {/* Hero */}
        <div className="relative overflow-hidden rounded-2xl p-8 text-center border border-purple-800/30 bg-[#130022]">
          <div className="absolute -top-16 -right-16 w-48 h-48 bg-rose-500/15 rounded-full blur-3xl pointer-events-none" />
          <div className="absolute -bottom-16 -left-16 w-48 h-48 bg-violet-500/15 rounded-full blur-3xl pointer-events-none" />
          <div className="relative">
            <div className="w-16 h-16 rounded-2xl bg-linear-to-br from-rose-500 to-violet-600 flex items-center justify-center text-white text-3xl font-bold mx-auto mb-4 shadow-lg">V</div>
            <h1 className="text-3xl font-bold text-white mb-3">About <span className="gradient-text">VidyaAi</span></h1>
            <p className="text-gray-300 text-base leading-relaxed max-w-xl mx-auto">
              A <span className="text-rose-400 font-semibold">gamified exam preparation platform</span> built to help students build
              daily consistency while preparing for competitive exams — starting with SSC CGL.
            </p>
          </div>
        </div>

        {/* Mission */}
        <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-6">
          <h2 className="text-white font-bold text-lg mb-2">The Problem We're Solving</h2>
          <p className="text-gray-400 text-sm leading-relaxed mb-4">
            Most SSC aspirants start with high motivation and lose consistency within 2 weeks. Existing platforms focus on long video lectures
            that promote passive consumption. Students don't track progress, feel isolated, and eventually give up.
          </p>
          <p className="text-gray-300 text-sm leading-relaxed font-medium">
            VidyaAi flips this by making preparation feel like a game — <span className="text-rose-400">daily streaks, XP rewards, live leaderboards</span>.
            The goal isn't 8-hour study sessions. It's 10 minutes every single day.
          </p>
        </div>

        {/* Values */}
        <div>
          <h2 className="text-white font-bold text-lg mb-4">Our Core Principles</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {values.map(v => (
              <div key={v.title} className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5 card-hover hover:border-rose-500/30">
                <span className="text-3xl">{v.icon}</span>
                <h3 className="text-white font-semibold mt-3 mb-1">{v.title}</h3>
                <p className="text-gray-400 text-sm">{v.desc}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Roadmap */}
        <div>
          <h2 className="text-white font-bold text-lg mb-4">Roadmap</h2>
          <div className="space-y-3">
            {roadmap.map(r => (
              <div key={r.phase} className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5">
                <span className={`text-xs font-semibold px-2.5 py-1 rounded-full border ${r.color}`}>{r.phase}</span>
                <ul className="mt-3 space-y-1">
                  {r.items.map(item => (
                    <li key={item} className="text-gray-400 text-sm flex items-center gap-2">
                      <span className="w-1.5 h-1.5 rounded-full bg-rose-500/50 shrink-0" />
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>

        {/* CTA */}
        <div className="text-center pb-4">
          <p className="text-gray-500 text-sm mb-4">Ready to build your streak?</p>
          <Link to="/daily-challenge"
            className="inline-block bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 text-white font-semibold px-8 py-3 rounded-xl transition-all duration-200 shadow-lg">
            Start Today's Challenge ⚡
          </Link>
        </div>
      </div>
    </Layout>
  );
}
