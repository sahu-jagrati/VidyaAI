import re
import time
import feedparser
import httpx
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.news_model import NewsArticle
from app.services.translation_service import translate_hi

RSS_FEEDS = [
    {"url": "https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3",              "category": "Government"},
    {"url": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",           "category": "National"},
    {"url": "https://www.thehindu.com/news/national/feeder/default.rss",            "category": "National"},
    {"url": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",           "category": "International"},
    {"url": "https://www.thehindu.com/news/international/feeder/default.rss",       "category": "International"},
    {"url": "https://economictimes.indiatimes.com/rssfeeds/1977021501.cms",         "category": "Economy"},
    {"url": "https://economictimes.indiatimes.com/rssfeeds/2647163.cms",            "category": "Economy"},
    {"url": "https://feeds.feedburner.com/ndtvsports-latest",                       "category": "Sports"},
    {"url": "https://timesofindia.indiatimes.com/rssfeeds/4719161.cms",             "category": "Sports"},
    {"url": "https://www.thehindu.com/sci-tech/science/feeder/default.rss",         "category": "Science & Tech"},
    {"url": "https://www.thehindu.com/sci-tech/technology/feeder/default.rss",      "category": "Science & Tech"},
    {"url": "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",             "category": "Defence"},
]

DEFENCE_KEYWORDS = {"army", "navy", "airforce", "air force", "military", "missile", "defence", "defense", "armed forces", "isro", "drdo", "ins ", "iac", "warship", "soldier", "regiment"}

AGENT   = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
TIMEOUT = 20




def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "").strip()


def _parse_date(entry) -> datetime | None:
    for attr in ("published_parsed", "updated_parsed"):
        val = getattr(entry, attr, None)
        if val:
            try:
                return datetime.fromtimestamp(time.mktime(val), tz=timezone.utc)
            except Exception:
                pass
    return None


def _fetch_feed(url: str):
    """Fetch RSS via httpx (handles SSL issues) then parse with feedparser."""
    try:
        with httpx.Client(verify=False, timeout=TIMEOUT, follow_redirects=True) as client:
            resp = client.get(url, headers={"User-Agent": AGENT})
            resp.raise_for_status()
            return feedparser.parse(resp.content)
    except Exception as exc:
        print(f"[news] fetch error {url}: {exc}")
        return None


def fetch_and_store_news(db: Session) -> int:
    count = 0
    for feed_info in RSS_FEEDS:
        feed = _fetch_feed(feed_info["url"])
        if not feed or not feed.entries:
            continue

        source_name = getattr(feed.feed, "title", feed_info["category"])[:140]

        for entry in feed.entries[:20]:
            title = _strip_html(entry.get("title", "")).strip()
            if not title:
                continue

            url = entry.get("link", "").strip() or None

            # De-duplicate by URL, fall back to title
            if url:
                exists = db.query(NewsArticle).filter(NewsArticle.url == url).first()
            else:
                exists = db.query(NewsArticle).filter(NewsArticle.title == title[:490]).first()
            if exists:
                continue

            summary = _strip_html(
                entry.get("summary") or entry.get("description", "")
            )[:800] or None

            # Promote to Defence if keywords found in title
            category = feed_info["category"]
            if category != "Defence":
                title_lower = title.lower()
                if any(kw in title_lower for kw in DEFENCE_KEYWORDS):
                    category = "Defence"

            db.add(NewsArticle(
                title        = title[:490],
                title_hi     = translate_hi(title[:490]),
                summary      = summary,
                summary_hi   = translate_hi(summary) if summary else None,
                source       = source_name,
                url          = url,
                category     = category,
                published_at = _parse_date(entry),
            ))
            count += 1

    if count:
        db.commit()
        print(f"[news] Stored {count} new articles")
    return count


def translate_missing(db: Session) -> int:
    """Back-fill Hindi translations for articles that don't have them yet."""
    articles = db.query(NewsArticle).filter(NewsArticle.title_hi.is_(None)).all()
    updated = 0
    for article in articles:
        article.title_hi   = translate_hi(article.title)
        article.summary_hi = translate_hi(article.summary) if article.summary else None
        updated += 1
    if updated:
        db.commit()
        print(f"[news] Translated {updated} existing articles to Hindi")
    return updated
