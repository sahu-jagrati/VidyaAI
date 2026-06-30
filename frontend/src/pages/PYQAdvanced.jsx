import { useState } from 'react';
import Layout from '../components/Layout';
import { Link } from 'react-router-dom';

const tier2Papers = [
  { year: 2024, dates: ['Nov 18', 'Nov 19'], shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)', 'Paper III (General Studies)'] },
  { year: 2023, dates: ['Oct 26', 'Oct 27'], shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)', 'Paper III (General Studies)'] },
  { year: 2022, dates: ['Mar 9', 'Mar 10'],  shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English & Reasoning)'] },
  { year: 2021, dates: ['Nov 29'],            shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English & Reasoning)'] },
  { year: 2020, dates: ['Nov 15', 'Nov 16'], shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2019, dates: ['Sep 11', 'Sep 12'], shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2018, dates: ['Feb 17', 'Feb 18'], shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2017, dates: ['Feb 18', 'Feb 19'], shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2016, dates: ['Nov 30', 'Dec 1'],  shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2015, dates: ['Oct 25'],            shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2014, dates: ['Nov 1'],             shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2013, dates: ['Sep 29'],            shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2012, dates: ['Sep 16'],            shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2011, dates: ['Oct 16'],            shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
  { year: 2010, dates: ['Oct 17'],            shifts: 2, papers: ['Paper I (Maths)', 'Paper II (English)'] },
];

const paperColors = [
  { bg: 'bg-indigo-50', border: 'border-indigo-200', text: 'text-indigo-700' },
  { bg: 'bg-blue-50',   border: 'border-blue-200',   text: 'text-blue-700'   },
  { bg: 'bg-purple-50', border: 'border-purple-200', text: 'text-purple-700' },
];

export default function PYQAdvanced() {
  const [expandedYear, setExpandedYear] = useState(2024);

  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in">

        {/* Header */}
        <div className="mb-6">
          <div className="flex items-center gap-2 mb-2">
            <Link to="/ssc-cgl" className="text-gray-400 hover:text-teal-700 text-xs transition-colors">SSC CGL</Link>
            <span className="text-gray-300 text-xs">›</span>
            <span className="text-xs text-amber-600 font-semibold">PYQ Advanced</span>
          </div>
          <div className="flex items-center gap-3 mb-1">
            <span className="w-10 h-10 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-xl shrink-0">🚀</span>
            <div>
              <h1 className="text-2xl font-bold text-gray-900">PYQs — Advanced (Tier 2)</h1>
              <p className="text-gray-400 text-sm">Previous year papers from 2010–2024 · Paper-wise</p>
            </div>
          </div>
        </div>

        {/* Warning */}
        <div className="bg-amber-50 border border-amber-200 rounded-xl px-4 py-3 mb-6 flex items-center gap-3">
          <span className="text-xl shrink-0">⚠️</span>
          <p className="text-amber-700 text-sm font-semibold">Recommended after completing Tier 1 preparation. These are advanced-level papers.</p>
        </div>

        {/* Info bar */}
        <div className="flex flex-wrap gap-3 mb-6">
          {[
            { icon: '📅', val: '15 Years', label: '2010–2024',       bg: 'bg-amber-50',  border: 'border-amber-200',  text: 'text-amber-700'  },
            { icon: '📄', val: '30+',      label: 'Papers',          bg: 'bg-blue-50',   border: 'border-blue-200',   text: 'text-blue-700'   },
            { icon: '📝', val: '3',        label: 'Papers per exam', bg: 'bg-purple-50', border: 'border-purple-200', text: 'text-purple-700' },
            { icon: '⏱️', val: '2 hrs',    label: 'Per paper',       bg: 'bg-teal-50',   border: 'border-teal-200',   text: 'text-teal-700'   },
          ].map(s => (
            <div key={s.label} className={`flex items-center gap-2 ${s.bg} border ${s.border} rounded-xl px-4 py-2 shadow-sm`}>
              <span className="text-base">{s.icon}</span>
              <div>
                <p className={`${s.text} font-bold text-sm leading-tight`}>{s.val}</p>
                <p className="text-gray-400 text-xs">{s.label}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Year-wise accordion */}
        <div className="space-y-2">
          {tier2Papers.map(paper => {
            const isOpen = expandedYear === paper.year;
            const isRecent = paper.year >= 2020;
            return (
              <div key={paper.year} className={`bg-white border rounded-2xl overflow-hidden shadow-sm transition-all ${isOpen ? 'border-amber-300' : 'border-gray-200'}`}>
                <button
                  onClick={() => setExpandedYear(isOpen ? null : paper.year)}
                  className="w-full flex items-center justify-between px-5 py-4 hover:bg-gray-50 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <span className={`text-base font-bold ${isOpen ? 'text-amber-600' : 'text-gray-900'}`}>{paper.year}</span>
                    {isRecent && (
                      <span className="text-xs font-semibold bg-emerald-50 border border-emerald-200 text-emerald-700 px-2 py-0.5 rounded-full">Important</span>
                    )}
                    <span className="text-gray-400 text-xs">{paper.dates.length} exam date{paper.dates.length > 1 ? 's' : ''} · {paper.papers.length} papers</span>
                  </div>
                  <svg className={`w-4 h-4 text-gray-400 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                  </svg>
                </button>

                {isOpen && (
                  <div className="px-5 pb-5 fade-in">
                    <div className="space-y-3">
                      {paper.dates.map(date => (
                        <div key={date} className="border border-gray-100 rounded-xl overflow-hidden">
                          <div className="bg-gray-50 px-4 py-2 border-b border-gray-100">
                            <span className="text-xs font-bold text-gray-500 uppercase tracking-wider">{date}, {paper.year}</span>
                          </div>
                          <div className="divide-y divide-gray-50">
                            {paper.papers.map((p, pi) => {
                              const c = paperColors[pi] || paperColors[0];
                              return (
                                <div key={p} className="bg-white px-4 py-3 flex items-center justify-between">
                                  <div className="flex items-center gap-2">
                                    <span className={`text-xs font-bold px-2 py-0.5 rounded-full border ${c.bg} ${c.border} ${c.text}`}>
                                      {`P${pi + 1}`}
                                    </span>
                                    <div>
                                      <p className="text-gray-700 text-xs font-semibold">{p}</p>
                                      <p className="text-gray-400 text-xs mt-0.5">200 Marks · 2 Hours</p>
                                    </div>
                                  </div>
                                  <button className="text-xs bg-amber-50 hover:bg-amber-100 text-amber-700 border border-amber-200 font-semibold px-3 py-1.5 rounded-lg transition-colors">
                                    Practice
                                  </button>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>

        <p className="text-center text-gray-400 text-xs mt-6 pb-2">
          Papers are for practice · Questions sourced from official SSC CGL exam records
        </p>
      </div>
    </Layout>
  );
}
