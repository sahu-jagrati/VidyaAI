import { useState, useEffect, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useLang } from '../context/LanguageContext';
import Layout from '../components/Layout';
import api from '../utils/api';


const SECONDS_PER_QUESTION = 60;
const XP_MAP = { easy: 5, medium: 10, hard: 20 };

const diffStyle = {
  easy:   { bg: 'bg-emerald-50', border: 'border-emerald-200', text: 'text-emerald-700' },
  medium: { bg: 'bg-amber-50',   border: 'border-amber-200',   text: 'text-amber-700'   },
  hard:   { bg: 'bg-red-50',     border: 'border-red-200',     text: 'text-red-700'     },
};

const subjectStyle = {
  quant:     'text-indigo-700 bg-indigo-50 border-indigo-200',
  reasoning: 'text-purple-700 bg-purple-50 border-purple-200',
  english:   'text-blue-700   bg-blue-50   border-blue-200',
  ga:        'text-teal-700   bg-teal-50   border-teal-200',
};

function transformQuestion(q) {
  const difficulty = q.difficulty || null;
  return {
    id:          q.id,
    question:    q.question_text,
    imageUrl:    q.image_url || null,
    subject:     q.subject,
    subjectCode: (q.subject || '').toLowerCase(),
    difficulty,
    xp:          XP_MAP[difficulty] || 5,
    options:     { A: q.option_a, B: q.option_b, C: q.option_c, D: q.option_d },
  };
}

export default function DailyChallenge() {
  const { refreshUser } = useAuth();
  const { t, lang } = useLang();

  const [questions, setQuestions]         = useState([]);
  const [fetchError, setFetchError]       = useState('');
  const [fetchLoading, setFetchLoading]   = useState(true);
  const [idx, setIdx]                     = useState(0);
  const [selected, setSelected]           = useState(null);
  const [submitted, setSubmitted]         = useState(false);
  const [submitting, setSubmitting]       = useState(false);
  const [timeLeft, setTimeLeft]           = useState(SECONDS_PER_QUESTION);
  const [timeTaken, setTimeTaken]         = useState(0);
  const [results, setResults]             = useState([]);
  const [currentResult, setCurrentResult] = useState(null);
  const [done, setDone]                   = useState(false);

  useEffect(() => {
    setFetchLoading(true);
    setFetchError('');
    setIdx(0);
    setSelected(null);
    setSubmitted(false);
    setCurrentResult(null);
    setResults([]);
    setDone(false);
    api.get(`/questions/daily?lang=${lang}`)
      .then(res => setQuestions(res.data.map(transformQuestion)))
      .catch(err => {
        const msg = err?.response?.data?.detail || err?.message || 'Could not load today\'s questions.';
        setFetchError(msg);
      })
      .finally(() => setFetchLoading(false));
  }, [lang]);

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
        lang,
      });
      setCurrentResult({ ...res.data, correct_answer: res.data.correct_answer?.toUpperCase() });
      setResults(prev => [...prev, {
        questionId: current.id, correct: res.data.is_correct,
        xpEarned: res.data.xp_earned, timeTaken, selectedAnswer: selectedAns, subject: current.subject,
      }]);
    } catch {
      setCurrentResult({ is_correct: false, xp_earned: 0, correct_answer: '?', explanation: 'Unable to load explanation.' });
      setResults(prev => [...prev, { questionId: current.id, correct: false, xpEarned: 0, timeTaken, selectedAnswer: selectedAns, subject: current.subject }]);
    } finally {
      setSubmitting(false);
    }
  }, [submitted, submitting, questions, idx, timeTaken]);

  useEffect(() => {
    if (submitted || done || fetchLoading) return;
    if (timeLeft <= 0) { submitAnswer(null); return; }
    const id = setInterval(() => {
      setTimeLeft(prev => prev - 1);
      setTimeTaken(prev => prev + 1);
    }, 1000);
    return () => clearInterval(id);
  }, [timeLeft, submitted, done, fetchLoading]);

  const handleNext = () => {
    if (idx + 1 >= questions.length) { refreshUser(); setDone(true); }
    else { setIdx(idx + 1); setSelected(null); setSubmitted(false); setCurrentResult(null); }
  };

  if (fetchLoading) return (
    <Layout>
      <div className="max-w-2xl mx-auto pt-8 text-center">
        <div className="text-4xl mb-4 animate-pulse">⚡</div>
        <p className="text-gray-500">{t('dc.loading')}</p>
      </div>
    </Layout>
  );

  if (fetchError) return (
    <Layout>
      <div className="max-w-2xl mx-auto pt-8 text-center">
        <p className="text-red-500 mb-4">{fetchError}</p>
        <Link to="/home" className="text-teal-700 hover:text-teal-800 text-sm font-medium">{t('dc.back')}</Link>
      </div>
    </Layout>
  );

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
          <div className="bg-white border border-gray-200 rounded-2xl p-8 text-center shadow-sm">
            <div className="text-6xl mb-4">{perfect ? '🏆' : correctCnt >= 3 ? '🎉' : '💪'}</div>
            <h2 className="text-2xl font-bold text-gray-900 mb-1">
              {perfect ? t('dc.perfect') : t('dc.complete')}
            </h2>
            <p className="text-gray-500 text-sm mb-6">
              {perfect ? t('dc.perfect.sub') : t('dc.complete.sub')}
            </p>
            <div className="grid grid-cols-3 gap-3 mb-6">
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-4">
                <p className="text-amber-600 text-2xl font-bold">+{totalXP}</p>
                <p className="text-gray-400 text-xs mt-1">{t('dc.xp.earned')}</p>
              </div>
              <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-4">
                <p className="text-emerald-600 text-2xl font-bold">{correctCnt}/{questions.length}</p>
                <p className="text-gray-400 text-xs mt-1">{t('dc.correct.label')}</p>
              </div>
              <div className="bg-teal-50 border border-teal-200 rounded-xl p-4">
                <p className="text-teal-700 text-2xl font-bold">{accuracy}%</p>
                <p className="text-gray-400 text-xs mt-1">{t('dc.accuracy')}</p>
              </div>
            </div>
            {finalStreak > 0 && (
              <div className="bg-orange-50 border border-orange-200 rounded-xl px-4 py-3 mb-6 flex items-center gap-3">
                <span className="text-2xl streak-pulse">🔥</span>
                <div className="text-left">
                  <p className="text-orange-600 font-semibold text-sm">{t('dc.streak.active')}</p>
                  <p className="text-gray-400 text-xs">{t('dc.streak.sub').replace('{n}', finalStreak)}</p>
                </div>
              </div>
            )}
            <div className="text-left space-y-2 mb-6">
              {results.map((r, i) => (
                <div key={i} className={`flex items-center gap-3 p-3 rounded-xl border
                  ${r.correct ? 'bg-emerald-50 border-emerald-200' : 'bg-red-50 border-red-200'}`}>
                  <span className="text-lg">{r.correct ? '✅' : '❌'}</span>
                  <span className="text-gray-600 text-sm flex-1 truncate">{r.subject}</span>
                  <span className={`text-xs font-bold ${r.correct ? 'text-amber-600' : 'text-gray-400'}`}>
                    {r.correct ? `+${r.xpEarned} XP` : '0 XP'}
                  </span>
                </div>
              ))}
            </div>
            <div className="flex gap-3">
              <Link to="/home" className="flex-1 py-3 rounded-xl border-2 border-gray-200 text-gray-500 hover:text-gray-800 hover:border-gray-300 text-sm font-semibold transition-colors text-center">
                {t('dc.home.btn')}
              </Link>
              <Link to="/leaderboard" className="flex-1 py-3 rounded-xl bg-teal-700 hover:bg-teal-800 text-white text-sm font-semibold transition-colors text-center shadow-md shadow-teal-200">
                {t('dc.leaderboard.btn')}
              </Link>
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  // QUESTION SCREEN
  const current    = questions[idx];
  const ds         = diffStyle[current.difficulty] || { bg: 'bg-gray-50', border: 'border-gray-200', text: 'text-gray-500' };
  const ss         = subjectStyle[current.subjectCode] || 'text-gray-700 bg-gray-50 border-gray-200';
  const pct        = (timeLeft / SECONDS_PER_QUESTION) * 100;
  const timerColor = timeLeft > 30 ? 'bg-teal-500' : timeLeft > 10 ? 'bg-amber-500' : 'bg-red-500';

  return (
    <Layout>
      <div className="max-w-2xl mx-auto pt-2 fade-in">
        {/* Progress dots */}
        <div className="flex items-center gap-2 mb-6">
          {questions.map((_, i) => (
            <div key={i} className={`flex-1 h-1.5 rounded-full transition-all duration-300
              ${i < idx ? 'bg-teal-600' : i === idx ? 'bg-teal-400' : 'bg-gray-200'}`} />
          ))}
        </div>

        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <div className="flex items-center gap-2">
            <span className={`text-xs font-semibold px-2.5 py-1 rounded-full border ${ss}`}>{current.subject}</span>
            <span className={`text-xs font-semibold px-2.5 py-1 rounded-full border ${ds.bg} ${ds.border} ${ds.text} capitalize`}>{current.difficulty || 'unrated'}</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-amber-600 text-xs font-bold">+{current.xp} XP</span>
            <span className="text-gray-400 text-xs">Q {idx + 1}/{questions.length}</span>
          </div>
        </div>

        {/* Timer */}
        <div className="mb-5">
          <div className="flex items-center justify-between mb-1.5">
            <span className="text-gray-400 text-xs">{t('dc.timer')}</span>
            <span className={`text-sm font-bold ${timeLeft <= 10 ? 'text-red-500' : 'text-gray-700'}`}>
              {String(Math.floor(timeLeft / 60)).padStart(2,'0')}:{String(timeLeft % 60).padStart(2,'0')}
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div className={`h-2 rounded-full transition-all duration-1000 ${timerColor}`} style={{ width: `${pct}%` }} />
          </div>
        </div>

        {/* Question card */}
        <div className="bg-white border border-gray-200 rounded-2xl p-6 mb-5 shadow-sm">
          {current.imageUrl && (
            <img
              src={current.imageUrl}
              alt="Question diagram"
              className="w-full max-h-64 object-contain rounded-xl mb-4 border border-gray-100"
            />
          )}
          <p className="text-gray-800 text-base font-medium leading-relaxed whitespace-pre-line">{current.question}</p>
        </div>

        {/* Options */}
        <div className="space-y-3 mb-6">
          {Object.entries(current.options).map(([key, val]) => {
            let base = 'w-full flex items-center gap-4 px-5 py-4 rounded-xl border-2 text-left transition-all duration-150 cursor-pointer ';
            if (!submitted) {
              base += selected === key
                ? 'bg-teal-50 border-teal-400 text-gray-800'
                : 'bg-white border-gray-200 text-gray-600 hover:border-teal-300 hover:text-gray-800';
            } else if (!currentResult) {
              base += 'bg-white border-gray-100 text-gray-400 cursor-default';
            } else {
              if (key === currentResult.correct_answer) base += 'bg-emerald-50 border-emerald-400 text-emerald-800';
              else if (key === selected && selected !== currentResult.correct_answer) base += 'bg-red-50 border-red-400 text-red-700';
              else base += 'bg-white border-gray-100 text-gray-400 cursor-default';
            }
            return (
              <button key={key} className={base} onClick={() => !submitted && setSelected(key)} disabled={submitted}>
                <span className={`w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold shrink-0
                  ${!submitted && selected === key ? 'bg-teal-700 text-white'
                  : submitted && currentResult?.correct_answer === key ? 'bg-emerald-500 text-white'
                  : submitted && key === selected && currentResult ? 'bg-red-500 text-white'
                  : 'bg-gray-100 text-gray-500'}`}>
                  {key}
                </span>
                <span className="text-sm">{val}</span>
                {currentResult && key === currentResult.correct_answer && <span className="ml-auto text-emerald-600 text-sm font-bold">✓</span>}
                {currentResult && key === selected && selected !== currentResult.correct_answer && <span className="ml-auto text-red-500 text-sm font-bold">✗</span>}
              </button>
            );
          })}
        </div>

        {/* Explanation */}
        {submitted && (
          <div className={`rounded-2xl border-2 p-5 mb-5 fade-in
            ${!currentResult ? 'bg-gray-50 border-gray-200'
              : currentResult.is_correct ? 'bg-emerald-50 border-emerald-300'
              : 'bg-red-50 border-red-300'}`}>
            {!currentResult ? (
              <p className="text-gray-400 text-sm text-center animate-pulse">{t('dc.checking')}</p>
            ) : (
              <>
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-lg">{currentResult.is_correct ? '✅' : '❌'}</span>
                  <span className={`font-bold text-sm ${currentResult.is_correct ? 'text-emerald-700' : 'text-red-600'}`}>
                    {currentResult.is_correct
                      ? t('dc.correct.msg').replace('{xp}', currentResult.xp_earned)
                      : t('dc.wrong.msg').replace('{ans}', currentResult.correct_answer)}
                  </span>
                </div>
                <p className="text-gray-600 text-sm leading-relaxed">{currentResult.explanation}</p>
              </>
            )}
          </div>
        )}

        {/* Action button */}
        {!submitted ? (
          <button onClick={() => submitAnswer(selected)} disabled={!selected || submitting}
            className="w-full bg-teal-700 hover:bg-teal-800 disabled:opacity-30 disabled:cursor-not-allowed text-white font-bold py-3.5 rounded-xl transition-colors shadow-md shadow-teal-200">
            {t('dc.submit')}
          </button>
        ) : (
          <button onClick={handleNext} disabled={!currentResult}
            className="w-full bg-teal-700 hover:bg-teal-800 disabled:opacity-40 text-white font-bold py-3.5 rounded-xl transition-colors shadow-md shadow-teal-200">
            {idx + 1 < questions.length ? t('dc.next') : t('dc.see.results')}
          </button>
        )}
      </div>
    </Layout>
  );
}
