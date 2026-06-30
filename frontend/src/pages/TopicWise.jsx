import { useState, useEffect, useCallback } from "react";
import Layout from "../components/Layout";
import { useLang } from "../context/LanguageContext";
import { useAuth } from "../context/AuthContext";
import api from "../utils/api";

// ── constants ──────────────────────────────────────────────
const XP_MAP = { easy: 5, medium: 10, hard: 20 };
const SECONDS = 60;

const diffBadge = {
  easy: "bg-emerald-50 border-emerald-200 text-emerald-700",
  medium: "bg-amber-50   border-amber-200   text-amber-700",
  hard: "bg-red-50     border-red-200     text-red-700",
};
const diffDot = { easy: "🟢", medium: "🟡", hard: "🔴" };

const subjectStyle = {
  quant: "text-indigo-700 bg-indigo-50 border-indigo-200",
  reasoning: "text-purple-700 bg-purple-50 border-purple-200",
  english: "text-blue-700   bg-blue-50   border-blue-200",
  ga: "text-teal-700   bg-teal-50   border-teal-200",
};

function transformQuestion(q) {
  return {
    id: q.id,
    question: q.question_text,
    imageUrl: q.image_url || null,
    subject: q.subject,
    subjectCode: (q.subject || '').toLowerCase(),
    topic: q.topic,
    difficulty: q.difficulty,
    xp: XP_MAP[q.difficulty] || 5,
    options: { A: q.option_a, B: q.option_b, C: q.option_c, D: q.option_d },
  };
}

// ── subject / topic data ───────────────────────────────────
const SUBJECTS = [
  {
    icon: "🔢",
    label: "Quantitative",
    code: "quant",
    color: {
      bg: "bg-indigo-50",
      border: "border-indigo-200",
      text: "text-indigo-700",
      tag: "border-indigo-200 bg-indigo-50 text-indigo-700",
    },
    topics: [
      { name: "Number System", icon: "🔢" },
      { name: "LCM & HCF", icon: "🔣" },
      { name: "Surds & Indices", icon: "🔬" },
      { name: "Simplification", icon: "🧮" },
      { name: "Percentage", icon: "📊" },
      { name: "Ratio & Proportion", icon: "⚖️" },
      { name: "Average", icon: "📉" },
      { name: "Profit & Loss", icon: "💰" },
      { name: "Discount", icon: "🏷️" },
      { name: "Discount Sheet", icon: "🎫" },
      { name: "Dishonest Shopkeeper", icon: "🎭" },
      { name: "Simple Interest", icon: "🏦" },
      { name: "Compound Interest", icon: "📈" },
      { name: "Time & Work", icon: "⏱️" },
      { name: "Pipe & Cistern", icon: "🚰" },
      { name: "Speed, Time & Distance", icon: "🚀" },
      { name: "Train Sheet", icon: "🚆" },
      { name: "Boat & Stream", icon: "🚣" },
      { name: "Mixture & Alligation", icon: "⚗️" },
      { name: "Partnership", icon: "🤝" },
      { name: "Algebra", icon: "📐" },
      { name: "Coordinate Geometry", icon: "📍" },
      { name: "Geometry", icon: "📏" },
      { name: "Mensuration 2D", icon: "🔷" },
      { name: "Mensuration 3D", icon: "📦" },
      { name: "Trigonometry", icon: "📐" },
      { name: "Data Interpretation", icon: "📊" },
      { name: "Permutation & Combination", icon: "🔀" },
      { name: "Probability", icon: "🎲" },
    ],
  },
  {
    icon: "🧩",
    label: "Reasoning",
    code: "reasoning",
    color: {
      bg: "bg-purple-50",
      border: "border-purple-200",
      text: "text-purple-700",
      tag: "border-purple-200 bg-purple-50 text-purple-700",
    },
    topics: [
      { name: "Series", icon: "🔗" },
      { name: "Analogy", icon: "🔄" },
      { name: "Coding-Decoding", icon: "🔐" },
      { name: "Blood Relation", icon: "👨‍👩‍👧" },
      { name: "Direction & Distance", icon: "🧭" },
      { name: "Syllogism", icon: "💭" },
      { name: "Matrix", icon: "🔲" },
      { name: "Venn Diagram", icon: "⭕" },
      { name: "Puzzle", icon: "🧩" },
      { name: "Statement & Conclusion", icon: "📋" },
      { name: "Classification", icon: "📂" },
      { name: "Mirror & Water Image", icon: "🪞" },
    ],
  },
  {
    icon: "📝",
    label: "English",
    code: "english",
    color: {
      bg: "bg-blue-50",
      border: "border-blue-200",
      text: "text-blue-700",
      tag: "border-blue-200 bg-blue-50 text-blue-700",
    },
    topics: [
      { name: "Verb (Basic)", icon: "📝" },
      { name: "Tense", icon: "⏰" },
      { name: "Passive Voice", icon: "↔️" },
      { name: "Narration", icon: "💬" },
      { name: "Question Tag", icon: "❓" },
      { name: "Subject Verb Agreement", icon: "🤝" },
      { name: "Conditional Sentences", icon: "🔀" },
      { name: "Verb (Advance)", icon: "📝" },
      { name: "Verb as Noun & Gerund", icon: "🔤" },
      { name: "Infinitive", icon: "🔁" },
      { name: "Participle", icon: "🔡" },
      { name: "Inversion", icon: "🔃" },
      { name: "Mood", icon: "🎭" },
      { name: "Noun", icon: "📦" },
      { name: "Pronoun", icon: "👤" },
      { name: "Adjective", icon: "✨" },
      { name: "Conjunction", icon: "🔗" },
      { name: "Article", icon: "📄" },
      { name: "Preposition", icon: "📍" },
      { name: "Adverb", icon: "⚡" },
      { name: "Parallelism", icon: "⚖️" },
      { name: "Superfluous Expressions", icon: "✂️" },
      { name: "Phrasal Verb", icon: "🔧" },
      { name: "Sentence Improvement", icon: "✍️" },
      { name: "Word Often Confused & Misused", icon: "🤔" },
      { name: "Vocabularies", icon: "📚" },
      { name: "Synonyms", icon: "📖" },
      { name: "Antonyms", icon: "🔃" },
      {
        name: "One Word Substitution",
        icon: "💬",
        subtopics: ["Meanings", "Practice Set"],
      },
      {
        name: "Idioms & Phrases",
        icon: "🗣️",
        subtopics: ["Meanings", "In Sentences", "Practice Set"],
      },
      { name: "Spellings", icon: "🔠" },
    ],
  },
  {
    icon: "🌍",
    label: "General Awareness",
    code: "ga",
    color: {
      bg: "bg-teal-50",
      border: "border-teal-200",
      text: "text-teal-700",
      tag: "border-teal-200 bg-teal-50 text-teal-700",
    },
    topics: [
      { name: "History", icon: "🏛️" },
      { name: "Geography", icon: "🗺️" },
      { name: "Indian Polity", icon: "⚖️" },
      { name: "Economy", icon: "📈" },
      { name: "Science & Tech", icon: "🔬" },
      { name: "Current Affairs", icon: "📰" },
      { name: "Sports", icon: "🏆" },
      { name: "Awards & Honours", icon: "🎖️" },
      { name: "Books & Authors", icon: "📚" },
      { name: "Important Days", icon: "📅" },
      { name: "Inventions & Discoveries", icon: "💡" },
      { name: "Indian Constitution", icon: "📜" },
    ],
  },
];

// ════════════════════════════════════════════════════════════
export default function TopicWise() {
  const { t, lang } = useLang();
  const { refreshUser } = useAuth();

  // ── mode: 'select' | 'list' | 'question' ────────────────
  const [mode, setMode] = useState("select");

  // ── selection ────────────────────────────────────────────
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [selectedSubtopic, setSelectedSubtopic] = useState(null);

  // ── question list ────────────────────────────────────────
  const [questions, setQuestions] = useState([]);
  const [loadingList, setLoadingList] = useState(false);
  const [loadError, setLoadError] = useState("");
  const [attempted, setAttempted] = useState({}); // {id: 'correct'|'wrong'}

  // ── single question state ────────────────────────────────
  const [activeQ, setActiveQ] = useState(null); // question object
  const [activeIdx, setActiveIdx] = useState(null); // index in questions[]
  const [selected, setSelected] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [timeLeft, setTimeLeft] = useState(SECONDS);
  const [timeTaken, setTimeTaken] = useState(0);
  const [currentResult, setCurrentResult] = useState(null);

  // ── derived ──────────────────────────────────────────────
  const subject = SUBJECTS.find((s) => s.code === selectedSubject);
  const topic = subject?.topics.find((tp) => tp.name === selectedTopic);
  const hasSubtopics = !!topic?.subtopics;

  const topicLabel = selectedSubtopic
    ? `${selectedTopic} — ${selectedSubtopic}`
    : selectedTopic;

  // ── fetch question list ──────────────────────────────────
  const fetchList = useCallback(
    async (subjectCode, topicName) => {
      setLoadingList(true);
      setLoadError("");
      try {
        const res = await api.get(
          `/questions/topic?subject=${encodeURIComponent(subjectCode)}&topic=${encodeURIComponent(topicName)}&lang=${lang}&limit=500`,
        );
        setQuestions(res.data.map(transformQuestion));
        setMode("list");
      } catch (err) {
        setLoadError(
          err?.response?.data?.detail ||
            "Could not load questions for this topic.",
        );
      } finally {
        setLoadingList(false);
      }
    },
    [lang],
  );

  // topic / subtopic click
  const handleTopicClick = (name) => {
    const tp = subject?.topics.find((t) => t.name === name);
    setSelectedTopic(name);
    setSelectedSubtopic(null);
    if (!tp?.subtopics) fetchList(selectedSubject, name);
  };
  const handleSubtopicClick = (st) => {
    setSelectedSubtopic(st);
    fetchList(selectedSubject, `${selectedTopic} — ${st}`);
  };

  // open a question from the list
  const openQuestion = (q, idx) => {
    setActiveQ(q);
    setActiveIdx(idx);
    setSelected(null);
    setSubmitted(false);
    setCurrentResult(null);
    setTimeLeft(SECONDS);
    setTimeTaken(0);
    setMode("question");
  };

  // reset to list
  const backToList = () => {
    setMode("list");
    setActiveQ(null);
  };

  // reset to topic selector
  const resetToSelect = () => {
    setMode("select");
    setSelectedTopic(null);
    setSelectedSubtopic(null);
    setQuestions([]);
    setAttempted({});
    setLoadError("");
  };

  // ── timer ────────────────────────────────────────────────
  useEffect(() => {
    if (mode !== "question" || submitted) return;
    if (timeLeft <= 0) {
      submitAnswer(null);
      return;
    }
    const id = setInterval(() => {
      setTimeLeft((p) => p - 1);
      setTimeTaken((p) => p + 1);
    }, 1000);
    return () => clearInterval(id);
  }, [timeLeft, mode, submitted]);

  useEffect(() => {
    if (mode === "question") {
      setTimeLeft(SECONDS);
      setTimeTaken(0);
    }
  }, [activeQ]);

  // ── submit ───────────────────────────────────────────────
  const submitAnswer = useCallback(
    async (ans) => {
      if (submitted || submitting || !activeQ) return;
      setSubmitted(true);
      setSubmitting(true);
      try {
        const res = await api.post("/questions/submit", {
          question_id: activeQ.id,
          selected_answer: ans,
          time_taken: timeTaken,
          lang,
        });
        const result = {
          ...res.data,
          correct_answer: res.data.correct_answer?.toUpperCase(),
        };
        setCurrentResult(result);
        setAttempted((prev) => ({
          ...prev,
          [activeQ.id]: result.is_correct ? "correct" : "wrong",
        }));
        refreshUser();
      } catch {
        setCurrentResult({
          is_correct: false,
          xp_earned: 0,
          correct_answer: "?",
          explanation: "Unable to load explanation.",
        });
      } finally {
        setSubmitting(false);
      }
    },
    [submitted, submitting, activeQ, timeTaken, lang],
  );

  const goNext = () => {
    const next = activeIdx + 1;
    if (next < questions.length) openQuestion(questions[next], next);
    else backToList();
  };
  const goPrev = () => {
    const prev = activeIdx - 1;
    if (prev >= 0) openQuestion(questions[prev], prev);
  };

  // ════════════════════════════════════════════════════════════
  // LOADING
  // ════════════════════════════════════════════════════════════
  if (loadingList)
    return (
      <Layout>
        <div className="max-w-2xl mx-auto pt-16 text-center">
          <div className="text-4xl mb-4 animate-pulse">📚</div>
          <p className="text-gray-500 text-sm">Loading questions…</p>
        </div>
      </Layout>
    );

  if (loadError)
    return (
      <Layout>
        <div className="max-w-2xl mx-auto pt-16 text-center">
          <p className="text-4xl mb-4">😔</p>
          <p className="text-red-500 mb-4 text-sm">{loadError}</p>
          <button
            onClick={resetToSelect}
            className="text-teal-700 hover:text-teal-800 text-sm font-medium"
          >
            ← Back to topics
          </button>
        </div>
      </Layout>
    );

  // ════════════════════════════════════════════════════════════
  // QUESTION VIEW
  // ════════════════════════════════════════════════════════════
  if (mode === "question" && activeQ) {
    const ss = subjectStyle[activeQ.subjectCode] || "";
    const db = diffBadge[activeQ.difficulty] || "";
    const pct = (timeLeft / SECONDS) * 100;
    const timerColor =
      timeLeft > 30
        ? "bg-teal-500"
        : timeLeft > 10
          ? "bg-amber-500"
          : "bg-red-500";

    return (
      <Layout>
        <div className="max-w-2xl mx-auto pt-2 fade-in">
          {/* Top nav */}
          <div className="flex items-center gap-2 mb-5 flex-wrap">
            <button
              onClick={backToList}
              className="text-gray-400 hover:text-gray-700 text-sm flex items-center gap-1 transition-colors"
            >
              ← Question List
            </button>
            <span className="text-gray-300">·</span>
            <span
              className={`text-xs font-semibold px-2.5 py-1 rounded-full border ${ss}`}
            >
              {activeQ.subject}
            </span>
            <span
              className={`text-xs font-semibold px-2.5 py-1 rounded-full border ${db}`}
            >
              {activeQ.difficulty}
            </span>
          </div>

          {/* Timer */}
          <div className="mb-5">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-gray-400 text-xs">{t("dc.timer")}</span>
              <span
                className={`text-sm font-bold ${timeLeft <= 10 ? "text-red-500" : "text-gray-700"}`}
              >
                {String(Math.floor(timeLeft / 60)).padStart(2, "0")}:
                {String(timeLeft % 60).padStart(2, "0")}
              </span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className={`h-2 rounded-full transition-all duration-1000 ${timerColor}`}
                style={{ width: `${pct}%` }}
              />
            </div>
          </div>

          {/* Question */}
          <div className="bg-white border border-gray-200 rounded-2xl p-6 mb-5 shadow-sm">
            {activeQ.imageUrl && (
              <img
                src={activeQ.imageUrl}
                alt="Question diagram"
                className="w-full max-h-64 object-contain rounded-xl mb-4 border border-gray-100"
              />
            )}
            <p className="text-gray-800 text-base font-medium leading-relaxed whitespace-pre-line">
              {activeQ.question}
            </p>
          </div>

          {/* Options */}
          <div className="space-y-3 mb-6">
            {Object.entries(activeQ.options).map(([key, val]) => {
              let base =
                "w-full flex items-center gap-4 px-5 py-4 rounded-xl border-2 text-left transition-all duration-150 cursor-pointer ";
              if (!submitted) {
                base +=
                  selected === key
                    ? "bg-teal-50 border-teal-400 text-gray-800"
                    : "bg-white border-gray-200 text-gray-600 hover:border-teal-300 hover:text-gray-800";
              } else if (!currentResult) {
                base += "bg-white border-gray-100 text-gray-400 cursor-default";
              } else {
                if (key === currentResult.correct_answer)
                  base += "bg-emerald-50 border-emerald-400 text-emerald-800";
                else if (
                  key === selected &&
                  selected !== currentResult.correct_answer
                )
                  base += "bg-red-50 border-red-400 text-red-700";
                else
                  base +=
                    "bg-white border-gray-100 text-gray-400 cursor-default";
              }
              return (
                <button
                  key={key}
                  className={base}
                  onClick={() => !submitted && setSelected(key)}
                  disabled={submitted}
                >
                  <span
                    className={`w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold shrink-0
                    ${
                      !submitted && selected === key
                        ? "bg-teal-700 text-white"
                        : submitted && currentResult?.correct_answer === key
                          ? "bg-emerald-500 text-white"
                          : submitted && key === selected && currentResult
                            ? "bg-red-500 text-white"
                            : "bg-gray-100 text-gray-500"
                    }`}
                  >
                    {key}
                  </span>
                  <span className="text-sm">{val}</span>
                  {currentResult && key === currentResult.correct_answer && (
                    <span className="ml-auto text-emerald-600 text-sm font-bold">
                      ✓
                    </span>
                  )}
                  {currentResult &&
                    key === selected &&
                    selected !== currentResult.correct_answer && (
                      <span className="ml-auto text-red-500 text-sm font-bold">
                        ✗
                      </span>
                    )}
                </button>
              );
            })}
          </div>

          {/* Explanation */}
          {submitted && (
            <div
              className={`rounded-2xl border-2 p-5 mb-5 fade-in
              ${
                !currentResult
                  ? "bg-gray-50 border-gray-200"
                  : currentResult.is_correct
                    ? "bg-emerald-50 border-emerald-300"
                    : "bg-red-50 border-red-300"
              }`}
            >
              {!currentResult ? (
                <p className="text-gray-400 text-sm text-center animate-pulse">
                  {t("dc.checking")}
                </p>
              ) : (
                <>
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-lg">
                      {currentResult.is_correct ? "✅" : "❌"}
                    </span>
                    <span
                      className={`font-bold text-sm ${currentResult.is_correct ? "text-emerald-700" : "text-red-600"}`}
                    >
                      {currentResult.is_correct
                        ? t("dc.correct.msg").replace(
                            "{xp}",
                            currentResult.xp_earned,
                          )
                        : t("dc.wrong.msg").replace(
                            "{ans}",
                            currentResult.correct_answer,
                          )}
                    </span>
                  </div>
                  <p className="text-gray-600 text-sm leading-relaxed">
                    {currentResult.explanation}
                  </p>
                </>
              )}
            </div>
          )}

          {/* Action buttons */}
          {!submitted ? (
            <button
              onClick={() => submitAnswer(selected)}
              disabled={!selected || submitting}
              className="w-full bg-teal-700 hover:bg-teal-800 disabled:opacity-30 disabled:cursor-not-allowed text-white font-bold py-3.5 rounded-xl transition-colors shadow-md shadow-teal-200"
            >
              {t("dc.submit")}
            </button>
          ) : (
            <div className="flex gap-3">
              {activeIdx > 0 && (
                <button
                  onClick={goPrev}
                  className="flex-1 py-3.5 rounded-xl border-2 border-gray-200 text-gray-600 hover:border-gray-300 font-semibold text-sm transition-colors"
                >
                  ← Prev
                </button>
              )}
              <button
                onClick={activeIdx + 1 < questions.length ? goNext : backToList}
                className="flex-1 bg-teal-700 hover:bg-teal-800 text-white font-bold py-3.5 rounded-xl transition-colors shadow-md shadow-teal-200 text-sm"
              >
                {activeIdx + 1 < questions.length ? "Next →" : "← Back to List"}
              </button>
            </div>
          )}
        </div>
      </Layout>
    );
  }

  // ════════════════════════════════════════════════════════════
  // QUESTION LIST VIEW
  // ════════════════════════════════════════════════════════════
  if (mode === "list") {
    const ss = subjectStyle[selectedSubject] || "";
    const solved = Object.values(attempted).filter(
      (v) => v === "correct",
    ).length;
    const wrongCnt = Object.values(attempted).filter(
      (v) => v === "wrong",
    ).length;

    return (
      <Layout>
        <div className="max-w-3xl mx-auto fade-in">
          {/* Header */}
          <div className="flex items-center gap-3 mb-5">
            <button
              onClick={resetToSelect}
              className="text-gray-400 hover:text-gray-700 text-sm flex items-center gap-1 transition-colors"
            >
              ← Topics
            </button>
            <span className="text-gray-300">·</span>
            <span
              className={`text-xs font-semibold px-2.5 py-1 rounded-full border ${ss}`}
            >
              {topicLabel}
            </span>
          </div>

          {/* Stats bar */}
          <div className="bg-white border border-gray-200 rounded-2xl p-4 shadow-sm mb-4 flex items-center gap-6">
            <div className="text-center">
              <p className="text-2xl font-bold text-gray-900">
                {questions.length}
              </p>
              <p className="text-xs text-gray-400 mt-0.5">Total</p>
            </div>
            <div className="w-px h-8 bg-gray-200" />
            <div className="text-center">
              <p className="text-2xl font-bold text-emerald-600">{solved}</p>
              <p className="text-xs text-gray-400 mt-0.5">Solved</p>
            </div>
            <div className="w-px h-8 bg-gray-200" />
            <div className="text-center">
              <p className="text-2xl font-bold text-red-500">{wrongCnt}</p>
              <p className="text-xs text-gray-400 mt-0.5">Wrong</p>
            </div>
            <div className="w-px h-8 bg-gray-200" />
            <div className="text-center">
              <p className="text-2xl font-bold text-gray-400">
                {questions.length - solved - wrongCnt}
              </p>
              <p className="text-xs text-gray-400 mt-0.5">Todo</p>
            </div>
            {Object.keys(attempted).length > 0 && (
              <>
                <div className="w-px h-8 bg-gray-200" />
                <div className="flex-1 text-right">
                  <button
                    onClick={() => setAttempted({})}
                    className="text-xs text-gray-400 hover:text-gray-600 underline transition-colors"
                  >
                    Reset progress
                  </button>
                </div>
              </>
            )}
          </div>

          {/* Question list */}
          <div className="bg-white border border-gray-200 rounded-2xl shadow-sm overflow-hidden">
            {/* Table header */}
            <div className="grid grid-cols-[2.5rem_1fr_5rem] gap-3 px-5 py-3 bg-gray-50 border-b border-gray-200">
              <span className="text-xs font-bold text-gray-400 uppercase tracking-wider">
                #
              </span>
              <span className="text-xs font-bold text-gray-400 uppercase tracking-wider">
                Question
              </span>
              <span className="text-xs font-bold text-gray-400 uppercase tracking-wider text-center">
                Difficulty
              </span>
            </div>

            {/* Rows */}
            <div className="divide-y divide-gray-100">
              {questions.map((q, i) => {
                const status = attempted[q.id];
                const rowBg =
                  status === "correct"
                    ? "bg-emerald-50 hover:bg-emerald-100"
                    : status === "wrong"
                      ? "bg-red-50 hover:bg-red-100"
                      : "bg-white hover:bg-gray-50";

                return (
                  <button
                    key={q.id}
                    onClick={() => openQuestion(q, i)}
                    className={`w-full grid grid-cols-[2.5rem_1fr_5rem] gap-3 px-5 py-4 text-left transition-colors ${rowBg}`}
                  >
                    {/* Index / status icon */}
                    <span className="flex items-center justify-center">
                      {status === "correct" ? (
                        <span className="w-6 h-6 rounded-full bg-emerald-500 flex items-center justify-center text-white text-xs font-bold">
                          ✓
                        </span>
                      ) : status === "wrong" ? (
                        <span className="w-6 h-6 rounded-full bg-red-400 flex items-center justify-center text-white text-xs font-bold">
                          ✗
                        </span>
                      ) : (
                        <span className="text-gray-400 text-sm font-medium">
                          {i + 1}
                        </span>
                      )}
                    </span>

                    {/* Question text */}
                    <span
                      className={`text-sm leading-snug line-clamp-2 ${
                        status === "correct"
                          ? "text-emerald-800 font-medium"
                          : status === "wrong"
                            ? "text-red-700"
                            : "text-gray-700"
                      }`}
                    >
                      {q.question}
                    </span>

                    {/* Difficulty */}
                    <span className="flex items-center justify-center">
                      <span
                        className={`text-xs font-semibold px-2 py-0.5 rounded-full border capitalize ${diffBadge[q.difficulty]}`}
                      >
                        {diffDot[q.difficulty]} {q.difficulty}
                      </span>
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  // ════════════════════════════════════════════════════════════
  // SELECT MODE (subject → topic)
  // ════════════════════════════════════════════════════════════
  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in">
        {/* Header */}
        <div className="mb-6">
          <span className="text-xs font-bold text-teal-700 bg-teal-50 border border-teal-200 rounded-full px-2.5 py-1">
            {t("tw.badge")}
          </span>
          <h1 className="text-2xl font-bold text-gray-900 mt-2">
            {t("tw.title")}
          </h1>
          <p className="text-gray-400 text-sm mt-1">{t("tw.sub")}</p>
        </div>

        {/* Step 1 — Subject */}
        <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm mb-4">
          <p className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">
            {t("tw.step1")}
          </p>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            {SUBJECTS.map((s) => (
              <button
                key={s.code}
                onClick={() => {
                  setSelectedSubject(s.code);
                  setSelectedTopic(null);
                  setSelectedSubtopic(null);
                }}
                className={`flex flex-col items-center gap-2 p-4 rounded-xl border-2 transition-all font-semibold text-sm
                  ${
                    selectedSubject === s.code
                      ? `${s.color.bg} ${s.color.border} ${s.color.text} shadow-sm`
                      : "bg-gray-50 border-gray-200 text-gray-500 hover:border-gray-300"
                  }`}
              >
                <span className="text-2xl">{s.icon}</span>
                <span className="text-xs text-center leading-tight">
                  {s.label}
                </span>
              </button>
            ))}
          </div>
        </div>

        {/* Step 2 — Topic */}
        {subject && (
          <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm mb-4 fade-in">
            <div className="flex items-center justify-between mb-4">
              <p className="text-xs font-bold text-gray-400 uppercase tracking-wider">
                {t("tw.step2")}
              </p>
              <span
                className={`text-xs font-semibold px-2.5 py-0.5 rounded-full border ${subject.color.tag}`}
              >
                {subject.label}
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {subject.topics.map((tp) => (
                <button
                  key={tp.name}
                  onClick={() => handleTopicClick(tp.name)}
                  className={`flex items-center gap-2 px-4 py-3 rounded-xl border-2 transition-all text-left
                    ${
                      selectedTopic === tp.name
                        ? `${subject.color.bg} ${subject.color.border} ${subject.color.text}`
                        : "bg-gray-50 border-gray-100 text-gray-600 hover:border-gray-200"
                    }`}
                >
                  <span className="text-base">{tp.icon}</span>
                  <span className="text-sm font-semibold">{tp.name}</span>
                  {tp.subtopics && (
                    <span className="ml-auto text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded-full">
                      {tp.subtopics.length} sections
                    </span>
                  )}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Step 2b — Sub-topic */}
        {selectedTopic && hasSubtopics && (
          <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm mb-4 fade-in">
            <div className="flex items-center justify-between mb-4">
              <p className="text-xs font-bold text-gray-400 uppercase tracking-wider">
                Choose Section
              </p>
              <span
                className={`text-xs font-semibold px-2.5 py-0.5 rounded-full border ${subject.color.tag}`}
              >
                {topic.icon} {topic.name}
              </span>
            </div>
            <div className="flex flex-wrap gap-2">
              {topic.subtopics.map((st, i) => (
                <button
                  key={st}
                  onClick={() => handleSubtopicClick(st)}
                  className="flex items-center gap-2 px-4 py-2.5 rounded-xl border-2 transition-all text-sm font-semibold bg-gray-50 border-gray-100 text-gray-600 hover:border-gray-200"
                >
                  <span className="text-gray-400 text-xs font-bold">
                    {["i", "ii", "iii"][i]})
                  </span>
                  {st}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Empty state */}
        {!selectedSubject && (
          <div className="text-center py-10 text-gray-400">
            <p className="text-4xl mb-3">🎯</p>
            <p className="text-sm">{t("tw.empty")}</p>
          </div>
        )} 
      </div>
    </Layout>
  );
}
