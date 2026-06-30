import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useLang } from "../context/LanguageContext";
import api from "../utils/api";

function LangToggle() {
  const { lang, switchLang } = useLang();
  return (
    <div className="flex items-center gap-1 bg-gray-100 rounded-lg p-0.5 border border-gray-200">
      <button
        onClick={() => switchLang("en")}
        className={`px-3 py-1.5 rounded-md text-xs font-bold transition-all duration-150
          ${lang === "en" ? "bg-teal-700 text-white shadow-sm" : "text-gray-500 hover:text-gray-700"}`}
      >
        EN
      </button>
      <button
        onClick={() => switchLang("hi")}
        className={`px-3 py-1.5 rounded-md text-xs font-bold transition-all duration-150
          ${lang === "hi" ? "bg-teal-700 text-white shadow-sm" : "text-gray-500 hover:text-gray-700"}`}
      >
        हिं
      </button>
    </div>
  );
}

const CAT_STYLE = {
  Government: "bg-teal-50 border-teal-200 text-teal-700",
  Economy: "bg-amber-50 border-amber-200 text-amber-700",
  National: "bg-blue-50 border-blue-200 text-blue-700",
  International: "bg-purple-50 border-purple-200 text-purple-700",
  Sports: "bg-emerald-50 border-emerald-200 text-emerald-700",
  "Science & Tech": "bg-blue-50 border-blue-200 text-blue-700",
  Defence: "bg-red-50 border-red-200 text-red-700",
  Awards: "bg-purple-50 border-purple-200 text-purple-700",
};
const DEFAULT_CAT_STYLE = "bg-gray-50 border-gray-200 text-gray-600";

function formatDate(dateStr) {
  if (!dateStr) return "";
  const d = new Date(dateStr);
  return d.toLocaleDateString("en-IN", { day: "numeric", month: "short" });
}

export default function Landing() {
  const { t, lang } = useLang();
  const [news, setNews] = useState([]);
  const [newsLoading, setNewsLoading] = useState(true);

  useEffect(() => {
    setNewsLoading(true);
    api
      .get(`/news?limit=6&lang=${lang}`)
      .then((r) => setNews(r.data))
      .catch(() => setNews([]))
      .finally(() => setNewsLoading(false));
  }, [lang]);

  const features = [
    { icon: "⚡", title: t("feat.1.t"), desc: t("feat.1.d") },
    { icon: "🔥", title: t("feat.2.t"), desc: t("feat.2.d") },
    { icon: "🏆", title: t("feat.3.t"), desc: t("feat.3.d") },
    { icon: "🎯", title: t("feat.4.t"), desc: t("feat.4.d") },
    { icon: "📄", title: t("feat.5.t"), desc: t("feat.5.d") },
    { icon: "🧠", title: t("feat.6.t"), desc: t("feat.6.d") },
  ];

  const sscTier1 = [
    {
      icon: "🔢",
      label: t("subj.quant"),
      color: "bg-indigo-50 border-indigo-200 text-indigo-700",
    },
    {
      icon: "🧩",
      label: t("subj.reasoning"),
      color: "bg-purple-50 border-purple-200 text-purple-700",
    },
    {
      icon: "📝",
      label: t("subj.english"),
      color: "bg-blue-50 border-blue-200 text-blue-700",
    },
    {
      icon: "🌍",
      label: t("subj.ga"),
      color: "bg-teal-50 border-teal-200 text-teal-700",
    },
  ];

  const stats = [
    { value: "10,000+", label: t("stats.q") },
    { value: "15 Years", label: t("stats.pyq") },
    { value: "4", label: t("stats.sub") },
    { value: "100% Free", label: t("stats.free") },
  ];

  const footerLinks = {
    company: [
      { label: t("link.about"), to: "/about" },
      { label: t("link.contact"), to: "/contact" },
      { label: t("link.board"), to: "/leaderboard" },
    ],
    resources: [
      { label: t("link.tier1"), to: "/ssc-cgl" },
      { label: t("link.tier2"), to: "/ssc-cgl" },
      { label: t("link.pyqm"), to: "/pyq/mains" },
      { label: t("link.pyqa"), to: "/pyq/advanced" },
      { label: t("link.daily"), to: "/daily-challenge" },
    ],
  };

  return (
    <div className="min-h-screen" style={{ backgroundColor: "#F5F7F8" }}>
      {/* ── Simple Navbar ── */}
      <nav className="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          <Link to="/" className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-teal-700 flex items-center justify-center text-white font-bold text-base shadow-md shadow-teal-200">
              V
            </div>
            <span className="font-bold text-xl gradient-text">VidyaAi</span>
          </Link>

          <div className="flex items-center gap-3">
            <LangToggle />
            <Link
              to="/login"
              className="bg-teal-700 hover:bg-teal-800 text-white font-semibold px-5 py-2 rounded-lg text-sm transition-colors shadow-sm shadow-teal-200"
            >
              {t("nav.signup")}
            </Link>
          </div>
        </div>
      </nav>

      {/* ── Hero ── */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 pt-16 pb-14 text-center">
        <span className="inline-block bg-teal-50 border border-teal-200 text-teal-700 text-xs font-bold px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
          {t("hero.badge")}
        </span>
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-5">
          {t("hero.h1.1")}
          <br />
          <span className="gradient-text">{t("hero.h1.2")}</span>
        </h1>
        <p className="text-gray-500 text-lg sm:text-xl max-w-2xl mx-auto mb-8 leading-relaxed whitespace-pre-line">
          {t("hero.sub")}
        </p>
        <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
          <Link
            to="/login"
            className="w-full sm:w-auto bg-teal-700 hover:bg-teal-800 text-white font-bold px-8 py-3.5 rounded-xl transition-all shadow-lg shadow-teal-200 text-base"
          >
            {t("hero.cta")}
          </Link>
          <Link
            to="/login"
            className="w-full sm:w-auto bg-white hover:bg-gray-50 text-gray-700 font-semibold px-8 py-3.5 rounded-xl border-2 border-gray-200 hover:border-teal-300 transition-all text-base"
          >
            {t("hero.login")}
          </Link>
        </div>
        <p className="text-gray-400 text-xs mt-4">{t("hero.free")}</p>
      </section>

      {/* ── Stats bar ── */}
      <section className="bg-teal-700 py-8">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-6 text-center">
            {stats.map((s) => (
              <div key={s.label}>
                <p className="text-white text-2xl sm:text-3xl font-bold">
                  {s.value}
                </p>
                <p className="text-teal-100 text-sm mt-0.5">{s.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── About SSC CGL ── */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 py-14">
        <div className="text-center mb-10">
          <span className="text-xs font-bold text-amber-600 bg-amber-50 border border-amber-200 rounded-full px-3 py-1 uppercase tracking-wider">
            {t("about.badge")}
          </span>
          <h2 className="text-3xl font-bold text-gray-900 mt-4 mb-3">
            {t("about.h2")}
          </h2>
          <p className="text-gray-500 max-w-2xl mx-auto text-base leading-relaxed">
            {t("about.desc")}
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          <div className="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
            <div className="flex items-center gap-3 mb-5">
              <span className="text-2xl">📖</span>
              <h3 className="font-bold text-gray-900 text-lg">
                {t("about.tier1")}
              </h3>
            </div>
            <div className="grid grid-cols-2 gap-3">
              {sscTier1.map((s) => (
                <div
                  key={s.label}
                  className={`flex items-center gap-2.5 p-3 rounded-xl border ${s.color}`}
                >
                  <span className="text-xl">{s.icon}</span>
                  <p className="font-semibold text-xs">{s.label}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
            <h3 className="font-bold text-gray-900 text-lg mb-5">
              {t("about.keyfacts")}
            </h3>
            <div className="space-y-3">
              {[
                { icon: "👥", label: t("about.applicants"), val: "25–30 Lakh" },
                {
                  icon: "💼",
                  label: t("about.vacancies"),
                  val: "15,000–20,000",
                },
                {
                  icon: "💰",
                  label: t("about.salary"),
                  val: "₹25,500 – ₹1,51,100",
                },
                {
                  icon: "🎓",
                  label: t("about.eligibility"),
                  val: t("about.elig.val"),
                },
                {
                  icon: "📅",
                  label: t("about.freq"),
                  val: t("about.freq.val"),
                },
                { icon: "🏛️", label: t("about.by"), val: t("about.by.val") },
              ].map((f) => (
                <div
                  key={f.label}
                  className="flex items-center gap-3 py-2 border-b border-gray-50 last:border-0"
                >
                  <span className="text-lg w-7">{f.icon}</span>
                  <span className="text-gray-500 text-sm flex-1">
                    {f.label}
                  </span>
                  <span className="text-gray-800 text-sm font-semibold">
                    {f.val}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="bg-amber-50 border border-amber-200 rounded-2xl p-5 flex items-start gap-4">
          <span className="text-2xl shrink-0">🚀</span>
          <div>
            <h4 className="font-bold text-amber-800 mb-1">
              {t("about.tier2.h")}
            </h4>
            <p className="text-amber-700 text-sm leading-relaxed">
              {t("about.tier2.desc")}
            </p>
          </div>
        </div>
      </section>

      {/* ── Daily News Affairs ── */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 py-14 border-t border-gray-200">
        <div className="flex items-center justify-between mb-8">
          <div>
            <span className="text-xs font-bold text-teal-700 bg-teal-50 border border-teal-200 rounded-full px-3 py-1 uppercase tracking-wider">
              {t("news.badge")}
            </span>
            <h2 className="text-3xl font-bold text-gray-900 mt-3 mb-1">
              {t("news.h2")}
            </h2>
            <p className="text-gray-500 text-sm">{t("news.sub")}</p>
          </div>
          <Link
            to="/login"
            className="hidden sm:block text-teal-700 hover:text-teal-800 text-sm font-semibold border border-teal-200 bg-teal-50 hover:bg-teal-100 px-4 py-2 rounded-lg transition-colors shrink-0"
          >
            {t("news.viewall")}
          </Link>
        </div>
        {newsLoading ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {Array.from({ length: 6 }).map((_, i) => (
              <div
                key={i}
                className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm animate-pulse"
              >
                <div className="flex gap-2 mb-3">
                  <div className="h-5 w-20 bg-gray-100 rounded-full" />
                  <div className="h-5 w-12 bg-gray-100 rounded-full" />
                </div>
                <div className="space-y-2">
                  <div className="h-4 bg-gray-100 rounded w-full" />
                  <div className="h-4 bg-gray-100 rounded w-4/5" />
                </div>
              </div>
            ))}
          </div>
        ) : news.length === 0 ? (
          <div className="text-center py-10 text-gray-400 text-sm">
            News loading in background — check back in a moment.
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {news.map((item) => (
              <div
                key={item.id}
                className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm hover:border-teal-200 hover:shadow-md transition-all flex flex-col"
              >
                <div className="flex items-center gap-2 mb-3">
                  <span
                    className={`text-xs font-semibold px-2.5 py-0.5 rounded-full border ${CAT_STYLE[item.category] || DEFAULT_CAT_STYLE}`}
                  >
                    {item.category}
                  </span>
                  <span className="text-gray-300 text-xs">
                    {formatDate(item.published_at || item.created_at)}
                  </span>
                </div>
                <p className="text-gray-900 font-semibold text-sm leading-snug flex-1">
                  {item.title}
                </p>
                {item.url && (
                  <a
                    href={item.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="mt-3 text-xs text-teal-600 hover:text-teal-700 font-medium transition-colors self-start"
                  >
                    {t("dn.source")}
                  </a>
                )}
              </div>
            ))}
          </div>
        )}
        <div className="text-center mt-6">
          <Link
            to="/login"
            className="inline-block text-teal-700 hover:text-teal-800 text-sm font-semibold border border-teal-200 bg-white hover:bg-teal-50 px-6 py-2.5 rounded-xl transition-colors shadow-sm"
          >
            {t("news.viewbtn")}
          </Link>
        </div>
      </section>

      {/* ── Features ── */}
      <section
        style={{ backgroundColor: "#F5F7F8" }}
        className="py-14 border-t border-gray-200"
      >
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="text-center mb-10">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">
              {t("feat.h2")}
            </h2>
            <p className="text-gray-500 max-w-xl mx-auto">{t("feat.sub")}</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {features.map((f) => (
              <div
                key={f.title}
                className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm card-hover"
              >
                <span className="text-3xl mb-3 block">{f.icon}</span>
                <h3 className="font-bold text-gray-900 mb-2">{f.title}</h3>
                <p className="text-gray-500 text-sm leading-relaxed">
                  {f.desc}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── CTA Banner ── */}
      <section className="bg-teal-700 py-14">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 text-center">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            {t("cta.h2")}
          </h2>
          <p className="text-teal-100 text-lg mb-8">{t("cta.sub")}</p>
          <Link
            to="/login"
            className="inline-block bg-amber-400 hover:bg-amber-500 text-gray-900 font-bold px-10 py-3.5 rounded-xl transition-all shadow-lg text-base"
          >
            {t("cta.btn")}
          </Link>
        </div>
      </section>

      {/* ── Footer ── */}
      <footer className="bg-white border-t border-gray-200">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 py-12">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10">
            <div className="sm:col-span-2 lg:col-span-1">
              <Link to="/" className="flex items-center gap-2.5 mb-4">
                <div className="w-9 h-9 rounded-xl bg-teal-700 flex items-center justify-center text-white font-bold text-base shadow-md shadow-teal-200">
                  V
                </div>
                <span className="font-bold text-xl gradient-text">VidyaAi</span>
              </Link>
              <p className="text-gray-500 text-sm leading-relaxed mb-5">
                {t("footer.tagline")}
              </p>
              <p className="text-gray-400 text-xs font-medium uppercase tracking-wider mb-3">
                {t("footer.follow")}
              </p>
              <div className="flex items-center gap-3">
                {[
                  { icon: "▶", label: "YouTube" },
                  { icon: "📸", label: "Instagram" },
                  { icon: "𝕏", label: "X/Twitter" },
                  { icon: "f", label: "Facebook" },
                ].map((s) => (
                  <button
                    key={s.label}
                    title={s.label}
                    className="w-8 h-8 rounded-lg bg-gray-100 hover:bg-teal-50 hover:text-teal-700 flex items-center justify-center text-gray-500 text-sm transition-colors border border-gray-200"
                  >
                    {s.icon}
                  </button>
                ))}
              </div>
            </div>

            <div>
              <p className="text-gray-900 font-bold text-sm uppercase tracking-wider mb-4">
                {t("footer.company")}
              </p>
              <ul className="space-y-2.5">
                {footerLinks.company.map((l) => (
                  <li key={l.label}>
                    <Link
                      to={l.to}
                      className="text-gray-500 hover:text-teal-700 text-sm transition-colors"
                    >
                      {l.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>

            <div>
              <p className="text-gray-900 font-bold text-sm uppercase tracking-wider mb-4">
                {t("footer.resources")}
              </p>
              <ul className="space-y-2.5">
                {footerLinks.resources.map((l) => (
                  <li key={l.label}>
                    <Link
                      to={l.to}
                      className="text-gray-500 hover:text-teal-700 text-sm transition-colors"
                    >
                      {l.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>

            <div>
              <p className="text-gray-900 font-bold text-sm uppercase tracking-wider mb-4">
                {t("footer.contact")}
              </p>
              <div className="space-y-3">
                <div>
                  <p className="text-gray-400 text-xs mb-0.5">
                    {t("footer.student")}
                  </p>
                  <a
                    href="mailto:help@vidyaai.in"
                    className="text-teal-700 hover:text-teal-800 text-sm font-medium transition-colors"
                  >
                    help@vidyaai.in
                  </a>
                </div>
                <div>
                  <p className="text-gray-400 text-xs mb-0.5">
                    {t("footer.general")}
                  </p>
                  <a
                    href="mailto:hello@vidyaai.in"
                    className="text-teal-700 hover:text-teal-800 text-sm font-medium transition-colors"
                  >
                    hello@vidyaai.in
                  </a>
                </div>
                <div className="bg-teal-50 border border-teal-200 rounded-xl px-4 py-3 mt-3">
                  <p className="text-teal-700 text-xs font-semibold">
                    {t("footer.free")}
                  </p>
                  <p className="text-teal-600 text-xs mt-0.5">
                    {t("footer.free.sub")}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-100 py-4">
          <div className="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-2">
            <p className="text-gray-400 text-xs">{t("footer.copy")}</p>
            <div className="flex items-center gap-4">
              <a
                href="#"
                className="text-gray-400 hover:text-gray-600 text-xs transition-colors"
              >
                {t("footer.terms")}
              </a>
              <a
                href="#"
                className="text-gray-400 hover:text-gray-600 text-xs transition-colors"
              >
                {t("footer.privacy")}
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
