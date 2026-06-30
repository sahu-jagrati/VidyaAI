import { useState, useEffect } from 'react';
import Layout from '../components/Layout';
import { useLang } from '../context/LanguageContext';
import api from '../utils/api';

const CATEGORIES = ['All', 'Government', 'National', 'Economy', 'Science & Tech', 'Sports', 'Defence', 'International'];

const categoryStyle = {
  'Government':     { bg: 'bg-teal-50',    border: 'border-teal-200',   text: 'text-teal-700'   },
  'National':       { bg: 'bg-cyan-50',    border: 'border-cyan-200',   text: 'text-cyan-700'   },
  'Economy':        { bg: 'bg-amber-50',   border: 'border-amber-200',  text: 'text-amber-700'  },
  'Science & Tech': { bg: 'bg-blue-50',    border: 'border-blue-200',   text: 'text-blue-700'   },
  'Sports':         { bg: 'bg-emerald-50', border: 'border-emerald-200',text: 'text-emerald-700'},
  'Awards':         { bg: 'bg-purple-50',  border: 'border-purple-200', text: 'text-purple-700' },
  'Defence':        { bg: 'bg-red-50',     border: 'border-red-200',    text: 'text-red-700'    },
  'International':  { bg: 'bg-indigo-50',  border: 'border-indigo-200', text: 'text-indigo-700' },
};

const examTagMap = {
  Government:       'SSC Relevant: Government Schemes',
  National:         'SSC Relevant: National Affairs',
  Economy:          'SSC Relevant: Economy & Finance',
  'Science & Tech': 'SSC Relevant: Science & Technology',
  Sports:           'SSC Relevant: Sports',
  Awards:           'SSC Relevant: Awards & Honours',
  Defence:          'SSC Relevant: Defence',
  International:    'SSC Relevant: International Affairs',
};

function formatDate(dateStr) {
  if (!dateStr) return '';
  try {
    return new Date(dateStr).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
  } catch { return ''; }
}

export default function DailyNews() {
  const { lang, t } = useLang();
  const [activeCategory, setActiveCategory] = useState('All');
  const [expanded,  setExpanded]  = useState(null);
  const [articles,  setArticles]  = useState([]);
  const [loading,   setLoading]   = useState(true);

  useEffect(() => {
    setLoading(true);
    setExpanded(null);
    const langParam = `lang=${lang}`;
    const params = activeCategory !== 'All'
      ? `?${langParam}&category=${encodeURIComponent(activeCategory)}&limit=40`
      : `?${langParam}&limit=40`;
    api.get(`/news${params}`)
      .then(r => setArticles(r.data))
      .catch(() => setArticles([]))
      .finally(() => setLoading(false));
  }, [activeCategory, lang]);

  return (
    <Layout>
      <div className="max-w-3xl mx-auto fade-in">

        {/* Header */}
        <div className="mb-6">
          <div className="flex items-center gap-2 mb-2">
            <span className="text-xs font-bold text-teal-700 bg-teal-50 border border-teal-200 rounded-full px-2.5 py-1">{t('dn.badge')}</span>
          </div>
          <h1 className="text-2xl font-bold text-gray-900">{t('dn.title')}</h1>
          <p className="text-gray-400 text-sm mt-1">{t('dn.desc')}</p>
        </div>

        {/* Category filter */}
        <div className="flex gap-2 flex-wrap mb-6">
          {CATEGORIES.map(cat => (
            <button key={cat} onClick={() => setActiveCategory(cat)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 border
                ${activeCategory === cat
                  ? 'bg-teal-700 text-white border-teal-700 shadow-sm'
                  : 'bg-white text-gray-500 border-gray-200 hover:border-teal-300 hover:text-teal-700'}`}>
              {cat === 'All' ? t('dn.all') : cat}
            </button>
          ))}
        </div>

        {/* Loading skeletons */}
        {loading && (
          <div className="space-y-3">
            {[1,2,3,4,5].map(i => (
              <div key={i} className="bg-white border border-gray-100 rounded-2xl p-5 animate-pulse">
                <div className="flex gap-2 mb-3">
                  <div className="h-5 w-20 bg-gray-100 rounded-full" />
                  <div className="h-5 w-16 bg-gray-100 rounded-full" />
                </div>
                <div className="h-4 bg-gray-100 rounded w-3/4 mb-2" />
                <div className="h-3 bg-gray-100 rounded w-1/2" />
              </div>
            ))}
          </div>
        )}

        {/* Empty state */}
        {!loading && articles.length === 0 && (
          <div className="text-center py-16 text-gray-400">
            <p className="text-4xl mb-3">📰</p>
            <p className="font-semibold text-gray-600 text-sm">{t('dn.empty.title')}</p>
            <p className="text-xs mt-1 text-gray-400">{t('dn.empty.sub')}</p>
          </div>
        )}

        {/* News cards */}
        {!loading && articles.length > 0 && (
          <div className="space-y-3">
            {articles.map(item => {
              const c   = categoryStyle[item.category] || { bg: 'bg-gray-50', border: 'border-gray-200', text: 'text-gray-600' };
              const isOpen = expanded === item.id;
              const tag = examTagMap[item.category] || `SSC Relevant: ${item.category}`;
              return (
                <div key={item.id}
                  className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm hover:border-teal-200 transition-all cursor-pointer"
                  onClick={() => setExpanded(isOpen ? null : item.id)}
                >
                  <div className="flex items-center gap-2 flex-wrap mb-2">
                    <span className={`text-xs font-semibold px-2.5 py-0.5 rounded-full border ${c.bg} ${c.border} ${c.text}`}>
                      {item.category}
                    </span>
                    <span className="text-gray-300 text-xs">{formatDate(item.published_at || item.created_at)}</span>
                    {item.source && <span className="text-gray-300 text-xs">· {item.source}</span>}
                  </div>

                  <h3 className="text-gray-900 font-bold text-sm leading-snug mb-2">{item.title}</h3>

                  {isOpen && item.summary && (
                    <p className="text-gray-500 text-sm leading-relaxed mb-3 fade-in">{item.summary}</p>
                  )}

                  <div className="flex items-center justify-between flex-wrap gap-2 mt-1">
                    <span className="text-xs text-teal-700 bg-teal-50 border border-teal-100 rounded-full px-2.5 py-0.5 font-medium">
                      📌 {tag}
                    </span>
                    <div className="flex items-center gap-3">
                      {item.url && (
                        <a href={item.url} target="_blank" rel="noopener noreferrer"
                          onClick={e => e.stopPropagation()}
                          className="text-xs text-gray-400 hover:text-teal-700 font-medium transition-colors">
                          {t('dn.source')}
                        </a>
                      )}
                      {item.summary && (
                        <span className="text-xs text-gray-400 font-semibold">
                          {isOpen ? t('dn.showless') : t('dn.readmore')}
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}

        <p className="text-center text-gray-400 text-xs mt-6 pb-2">
          {t('dn.footer')}
        </p>
      </div>
    </Layout>
  );
}
