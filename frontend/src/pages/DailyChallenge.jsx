import { useState, useEffect, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Layout from '../components/Layout';
import api from '../utils/api';

const SECONDS_PER_QUESTION = 60;
const XP_MAP = { easy: 5, medium: 10, hard: 20 };

const diffStyle = {
  easy:   { bg: 'bg-green-500/10',  border: 'border-green-500/30',  text: 'text-green-400'  },
  medium: { bg: 'bg-amber-500/10',  border: 'border-amber-500/30',  text: 'text-amber-400'  },
  hard:   { bg: 'bg-rose-500/10',   border: 'border-rose-500/30',   text: 'text-rose-400'   },
};

const subjectStyle = {
  quant:     'text-indigo-400 bg-indigo-500/10 border-indigo-500/30',
  reasoning: 'text-purple-400 bg-purple-500/10 border-purple-500/30',
  english:   'text-blue-400   bg-blue-500/10   border-blue-500/30',
  ga:        'text-cyan-400   bg-cyan-500/10   border-cyan-500/30',
};

function transformQuestion(q) {
  return {
    id:          q.id,
    question:    q.question_text,
    subject:     q.subject,
    subjectCode: q.subject_code,
    difficulty:  q.difficulty,
    xp:          XP_MAP[q.difficulty] || 5,
    options:     { A: q.option_a, B: q.option_b, C: q.option_c, D: q.option_d },
  };
}

export default function DailyChallenge() {
  const { refreshUser } = useAuth();

  const [questions, setQuestions]       = useState([]);
  const [fetchError, setFetchError]     = useState('');
  const [fetchLoading, setFetchLoading] = useState(true);

  const [idx, setIdx]             = useState(0);
  const [selected, setSelected]   = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [timeLeft, setTimeLeft]   = useState(SECONDS_PER_QUESTION);
  const [timeTaken, setTimeTaken] = useState(0);
  const [results, setResults]     = useState([]);
  const [currentResult, setCurrentResult] = useState(null);
  const [done, setDone]           = useState(false);

  useEffect(() => {
    api.get('/questions/daily')
      .then(res => setQuestions(res.data.map(transformQuestion)))
      .catch(err => {
        const msg = err?.response?.data?.detail
          || err?.message
          || 'Could not load today\'s questions.';
        setFetchError(msg);
      })
      .finally(() => setFetchLoading(false));
  }, []);

  useEffect(() => {
    setTimeLeft(SECONDS_PER_QUESTION);
    setTimeTaken(0);
    setCurrentResult(null);
  }, [idx]);

  const submitAnswer = useCallback(async (selectedAns) => {
    if (submitted || submitting || questions.length === 0) return;
    setSubmitted(true);
    setSubmitting(true);
    const current = questions[idx];
    try {
      const res = await api.post('/questions/submit', {
        question_id:     current.id,
        selected_answer: selectedAns,
        time_taken:      timeTaken,
      });
      setCurrentResult(res.data);
      setResults(prev => [...prev, {
        questionId:    current.id,
        correct:       res.data.is_correct,
        xpEarned:      res.data.xp_earned,
        timeTaken,
        selectedAnswer: selectedAns,
        subject:       current.subject,
      }]);
    } catch {
      setCurrentResult({ is_correct: false, xp_earned: 0, correct_answer: '?', explanation: 'Unable to load explanation.' });
      setResults(prev => [...prev, {
        questionId:    current.id,
        correct:       false,
        xpEarned:      0,
        timeTaken,
        selectedAnswer: selectedAns,
        subject:       current.subject,
      }]);
    } finally {
      setSubmitting(false);
    }
  }, [submitted, submitting, questions, idx, timeTaken]);

  useEffect(() => {
    if (submitted || done || fetchLoading) return;
    if (timeLeft <= 0) { submitAnswer(null); return; }
    const id = setInterval(() => {
      setTimeLeft(t => t - 1);
      setTimeTaken(t => t + 1);
    }, 1000);
    return () => clearInterval(id);
  }, [timeLeft, submitted, done, fetchLoading]);

  const handleNext = () => {
    if (idx + 1 >= questions.length) {
      refreshUser();
      setDone(true);
    } else {
      setIdx(idx + 1);
      setSelected(null);
      setSubmitted(false);
      setCurrentResult(null);
    }
  };

  // LOADING / ERROR STATE
  if (fetchLoading) {
    return (
      <Layout>
        <div className="max-w-2xl mx-auto pt-8 text-center">
          <div className="text-4xl mb-4 animate-pulse">⚡</div>
          <p className="text-gray-400">Loading today's challenge...</p>
        </div>
      </Layout>
    );
  }

  if (fetchError) {
    return (
      <Layout>
        <div className="max-w-2xl mx-auto pt-8 text-center">
          <div className="text-4xl mb-4">😞</div>
          <p className="text-red-400 mb-4">{fetchError}</p>
          <Link to="/home" className="text-rose-400 hover:text-rose-300 text-sm">← Back to Home</Link>
        </div>
      </Layout>
    );
  }

  const totalXP    = results.reduce((s, r) => s + r.xpEarned, 0);
  const correctCnt = results.filter(r => r.correct).length;
  const accuracy   = results.length ? Math.round((correctCnt / results.length) * 100) : 0;
  const finalStreak = currentResult?.current_streak ?? 0;

  // COMPLETED SCREEN
  if (done) {
    const perfect = correctCnt === questions.length;
    return (
      <Layout>
        <div className="max-w-xl mx-auto pt-4 fade-in">
          <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-8 text-center">
            <div className="text-6xl mb-4">{perfect ? '🏆' : correctCnt >= 3 ? '🎉' : '💪'}</div>
            <h2 className="text-2xl font-bold text-white mb-1">
              {perfect ? 'Perfect Score!' : 'Challenge Complete!'}
            </h2>
            <p className="text-gray-500 text-sm mb-6">
              {perfect ? 'Absolutely flawless! You nailed every question.' : 'Good effort! Keep practising to improve.'}
            </p>

            <div className="grid grid-cols-3 gap-3 mb-6">
              <div className="bg-yellow-500/10 border border-yellow-500/25 rounded-xl p-4">
                <p className="text-yellow-400 text-2xl font-bold">+{totalXP}</p>
                <p className="text-gray-500 text-xs mt-1">XP Earned</p>
              </div>
              <div className="bg-green-500/10 border border-green-500/25 rounded-xl p-4">
                <p className="text-green-400 text-2xl font-bold">{correctCnt}/{questions.length}</p>
                <p className="text-gray-500 text-xs mt-1">Correct</p>
              </div>
              <div className="bg-rose-500/10 border border-rose-500/25 rounded-xl p-4">
                <p className="text-rose-400 text-2xl font-bold">{accuracy}%</p>
                <p className="text-gray-500 text-xs mt-1">Accuracy</p>
              </div>
            </div>

            {finalStreak > 0 && (
              <div className="bg-orange-500/10 border border-orange-500/25 rounded-xl px-4 py-3 mb-6 flex items-center gap-3">
                <span className="text-2xl streak-pulse">🔥</span>
                <div className="text-left">
                  <p className="text-orange-400 font-semibold text-sm">Streak Active!</p>
                  <p className="text-gray-500 text-xs">You're on a {finalStreak}-day streak</p>
                </div>
              </div>
            )}

            <div className="text-left space-y-2 mb-6">
              {results.map((r, i) => (
                <div key={i} className={`flex items-center gap-3 p-3 rounded-xl border
                  ${r.correct ? 'bg-green-500/5 border-green-500/20' : 'bg-red-500/5 border-red-500/20'}`}>
                  <span className="text-lg">{r.correct ? '✅' : '❌'}</span>
                  <span className="text-gray-300 text-sm flex-1 truncate">{r.subject}</span>
                  <span className={`text-xs font-semibold ${r.correct ? 'text-yellow-400' : 'text-gray-700'}`}>
                    {r.correct ? `+${r.xpEarned} XP` : '0 XP'}
                  </span>
                </div>
              ))}
            </div>

            <div className="flex gap-3">
              <Link to="/home" className="flex-1 py-3 rounded-xl border border-purple-800/40 text-gray-400 hover:text-white hover:border-purple-700 text-sm font-medium transition-colors text-center">
                ← Home
              </Link>
              <Link to="/leaderboard" className="flex-1 py-3 rounded-xl bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 text-white text-sm font-semibold transition-all text-center">
                View Leaderboard 🏆
              </Link>
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  // QUESTION SCREEN
  const current   = questions[idx];
  const ds        = diffStyle[current.difficulty];
  const ss        = subjectStyle[current.subjectCode];
  const pct       = (timeLeft / SECONDS_PER_QUESTION) * 100;
  const timerColor = timeLeft > 30 ? 'bg-linear-to-r from-green-500 to-emerald-400' : timeLeft > 10 ? 'bg-amber-500' : 'bg-rose-500';

  return (
    <Layout>
      <div className="max-w-2xl mx-auto pt-2 fade-in">
        {/* Progress dots */}
        <div className="flex items-center gap-2 mb-6">
          {questions.map((_, i) => (
            <div key={i} className={`flex-1 h-1.5 rounded-full transition-all duration-300
              ${i < idx ? 'bg-linear-to-r from-rose-500 to-violet-500' :
                i === idx ? 'bg-rose-400' : 'bg-[#1e0030]'}`} />
          ))}
        </div>

        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <div className="flex items-center gap-2">
            <span className={`text-xs font-medium px-2.5 py-1 rounded-full border ${ss}`}>
              {current.subject}
            </span>
            <span className={`text-xs font-medium px-2.5 py-1 rounded-full border ${ds.bg} ${ds.border} ${ds.text} capitalize`}>
              {current.difficulty}
            </span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-yellow-400 text-xs font-semibold">+{current.xp} XP</span>
            <span className="text-gray-600 text-xs">Q {idx + 1}/{questions.length}</span>
          </div>
        </div>

        {/* Timer */}
        <div className="mb-5">
          <div className="flex items-center justify-between mb-1.5">
            <span className="text-gray-600 text-xs">Time remaining</span>
            <span className={`text-sm font-bold ${timeLeft <= 10 ? 'text-rose-400' : 'text-white'}`}>
              {String(Math.floor(timeLeft / 60)).padStart(2, '0')}:{String(timeLeft % 60).padStart(2, '0')}
            </span>
          </div>
          <div className="w-full bg-[#1e0030] rounded-full h-2">
            <div className={`h-2 rounded-full transition-all duration-1000 ${timerColor}`} style={{ width: `${pct}%` }} />
          </div>
        </div>

        {/* Question card */}
        <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-6 mb-5">
          <p className="text-white text-base font-medium leading-relaxed">{current.question}</p>
        </div>

        {/* Options */}
        <div className="space-y-3 mb-6">
          {Object.entries(current.options).map(([key, val]) => {
            let base = 'w-full flex items-center gap-4 px-5 py-4 rounded-xl border text-left transition-all duration-150 cursor-pointer ';

            if (!submitted) {
              base += selected === key
                ? 'bg-rose-500/15 border-rose-500 text-white'
                : 'bg-[#130022] border-purple-800/30 text-gray-300 hover:border-purple-600/50 hover:text-white';
            } else if (!currentResult) {
              // waiting for API response
              base += 'bg-[#130022] border-purple-900/20 text-gray-500 cursor-default';
            } else {
              if (key === currentResult.correct_answer) {
                base += 'bg-green-500/15 border-green-500 text-green-300';
              } else if (key === selected && selected !== currentResult.correct_answer) {
                base += 'bg-red-500/15 border-red-500 text-red-300';
              } else {
                base += 'bg-[#130022] border-purple-900/20 text-gray-700 cursor-default';
              }
            }

            return (
              <button key={key} className={base} onClick={() => !submitted && setSelected(key)} disabled={submitted}>
                <span className={`w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold shrink-0
                  ${!submitted && selected === key
                    ? 'bg-rose-600 text-white'
                    : submitted && currentResult?.correct_answer === key ? 'bg-green-600 text-white'
                    : submitted && key === selected && currentResult ? 'bg-red-600 text-white'
                    : 'bg-white/5 text-gray-500'}`}>
                  {key}
                </span>
                <span className="text-sm">{val}</span>
                {currentResult && key === currentResult.correct_answer && <span className="ml-auto text-green-400 text-sm">✓</span>}
                {currentResult && key === selected && selected !== currentResult.correct_answer && <span className="ml-auto text-red-400 text-sm">✗</span>}
              </button>
            );
          })}
        </div>

        {/* Explanation */}
        {submitted && (
          <div className={`rounded-2xl border p-5 mb-5 fade-in
            ${!currentResult
              ? 'bg-white/3 border-purple-900/30'
              : currentResult.is_correct
                ? 'bg-green-500/10 border-green-500/30'
                : 'bg-red-500/10 border-red-500/30'}`}>
            {!currentResult ? (
              <p className="text-gray-500 text-sm text-center animate-pulse">Checking answer...</p>
            ) : (
              <>
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-lg">{currentResult.is_correct ? '✅' : '❌'}</span>
                  <span className={`font-semibold text-sm ${currentResult.is_correct ? 'text-green-400' : 'text-red-400'}`}>
                    {currentResult.is_correct
                      ? `Correct! +${currentResult.xp_earned} XP earned`
                      : `Incorrect. Correct answer: ${currentResult.correct_answer}`}
                  </span>
                </div>
                <p className="text-gray-300 text-sm leading-relaxed">{currentResult.explanation}</p>
              </>
            )}
          </div>
        )}

        {/* Action button */}
        {!submitted ? (
          <button
            onClick={() => submitAnswer(selected)}
            disabled={!selected || submitting}
            className="w-full bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 disabled:opacity-30 disabled:cursor-not-allowed text-white font-semibold py-3.5 rounded-xl transition-all duration-200 shadow-lg"
          >
            Submit Answer
          </button>
        ) : (
          <button
            onClick={handleNext}
            disabled={!currentResult}
            className="w-full bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 disabled:opacity-40 text-white font-semibold py-3.5 rounded-xl transition-all duration-200 shadow-lg"
          >
            {idx + 1 < questions.length ? 'Next Question →' : 'See Results 🎉'}
          </button>
        )}
      </div>
    </Layout>
  );
}
