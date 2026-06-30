import { useState } from 'react';
import Layout from '../components/Layout';
import { Link } from 'react-router-dom';

const shifts = ['Shift 1 (Morning)', 'Shift 2 (Afternoon)', 'Shift 3 (Evening)'];

const papers = [
  { year: 2024, dates: ['Sep 9', 'Sep 10', 'Sep 11', 'Sep 12', 'Sep 13'], shifts: 3 },
  { year: 2023, dates: ['Jul 14', 'Jul 17', 'Jul 18', 'Jul 19', 'Jul 20', 'Jul 21', 'Jul 24', 'Jul 25', 'Jul 26'], shifts: 3 },
  { year: 2022, dates: ['Dec 1', 'Dec 2', 'Dec 5', 'Dec 6', 'Dec 8', 'Dec 9', 'Dec 12', 'Dec 13'], shifts: 3 },
  { year: 2021, dates: ['Apr 13', 'Apr 14', 'Apr 15', 'Apr 16', 'Apr 17', 'Apr 20'], shifts: 3 },
  { year: 2020, dates: ['Mar 3', 'Mar 4', 'Mar 5', 'Mar 6', 'Mar 7', 'Mar 9'], shifts: 3 },
  { year: 2019, dates: ['Jun 3', 'Jun 4', 'Jun 5', 'Jun 6', 'Jun 7'], shifts: 3 },
  { year: 2018, dates: ['Jun 4', 'Jun 5', 'Jun 6', 'Jun 7', 'Jun 8', 'Jun 9', 'Jun 12'], shifts: 3 },
  { year: 2017, dates: ['Aug 5', 'Aug 8', 'Aug 9', 'Aug 11', 'Aug 12', 'Aug 16'], shifts: 3 },
  { year: 2016, dates: ['Aug 27', 'Aug 28', 'Aug 29', 'Aug 30', 'Aug 31', 'Sep 1', 'Sep 2'], shifts: 2 },
  { year: 2015, dates: ['Aug 9', 'Aug 16'], shifts: 2 },
  { year: 2014, dates: ['Oct 19', 'Oct 26'], shifts: 2 },
  { year: 2013, dates: ['Apr 21', 'Apr 28'], shifts: 2 },
  { year: 2012, dates: ['May 1', 'May 8'], shifts: 2 },
  { year: 2011, dates: ['Jun 19', 'Jun 26'], shifts: 2 },
  { year: 2010, dates: ['Jul 4', 'Jul 11'], shifts: 2 },
];

export default function PYQMains() {
  const [expandedYear, setExpandedYear] = useState(2024);

  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in">

        {/* Header */}
        <div className="mb-6">
          <div className="flex items-center gap-2 mb-2">
            <Link to="/ssc-cgl" className="text-gray-400 hover:text-teal-700 text-xs transition-colors">SSC CGL</Link>
            <span className="text-gray-300 text-xs">›</span>
            <span className="text-xs text-teal-700 font-semibold">PYQ Mains</span>
          </div>
          <div className="flex items-center gap-3 mb-1">
            <span className="w-10 h-10 rounded-xl bg-teal-50 border border-teal-200 flex items-center justify-center text-xl shrink-0">📖</span>
            <div>
              <h1 className="text-2xl font-bold text-gray-900">PYQs — Mains (Tier 1)</h1>
              <p className="text-gray-400 text-sm">Previous year papers from 2010–2024 · Shift-wise</p>
            </div>
          </div>
        </div>

        {/* Info bar */}
        <div className="flex flex-wrap gap-3 mb-6">
          {[
            { icon: '📅', val: '15 Years', label: '2010–2024',        bg: 'bg-teal-50',   border: 'border-teal-200',   text: 'text-teal-700'   },
            { icon: '📄', val: '100+',     label: 'Papers',           bg: 'bg-blue-50',   border: 'border-blue-200',   text: 'text-blue-700'   },
            { icon: '🕐', val: '3',        label: 'Shifts per day',   bg: 'bg-purple-50', border: 'border-purple-200', text: 'text-purple-700' },
            { icon: '❓', val: '100 Qs',   label: 'Per paper',        bg: 'bg-amber-50',  border: 'border-amber-200',  text: 'text-amber-700'  },
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
          {papers.map(paper => {
            const isOpen = expandedYear === paper.year;
            const isRecent = paper.year >= 2020;
            return (
              <div key={paper.year} className={`bg-white border rounded-2xl overflow-hidden shadow-sm transition-all ${isOpen ? 'border-teal-300' : 'border-gray-200'}`}>
                <button
                  onClick={() => setExpandedYear(isOpen ? null : paper.year)}
                  className="w-full flex items-center justify-between px-5 py-4 hover:bg-gray-50 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <span className={`text-base font-bold ${isOpen ? 'text-teal-700' : 'text-gray-900'}`}>{paper.year}</span>
                    {isRecent && (
                      <span className="text-xs font-semibold bg-emerald-50 border border-emerald-200 text-emerald-700 px-2 py-0.5 rounded-full">Important</span>
                    )}
                    <span className="text-gray-400 text-xs">{paper.dates.length} exam dates · {paper.shifts} shifts</span>
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
                          <div className="grid grid-cols-1 sm:grid-cols-3 gap-px bg-gray-100">
                            {shifts.slice(0, paper.shifts).map((shift, si) => (
                              <div key={shift} className="bg-white px-4 py-3 flex items-center justify-between">
                                <div>
                                  <p className="text-gray-700 text-xs font-semibold">{shift}</p>
                                  <p className="text-gray-400 text-xs mt-0.5">100 Qs · 200 Marks</p>
                                </div>
                                <button className="text-xs bg-teal-50 hover:bg-teal-100 text-teal-700 border border-teal-200 font-semibold px-3 py-1.5 rounded-lg transition-colors">
                                  Practice
                                </button>
                              </div>
                            ))}
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
