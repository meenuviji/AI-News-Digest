# src/fetcher.py
import re
import time
import feedparser
from datetime import datetime, timezone, timedelta
from config.feeds import RSS_FEEDS


def fetch_articles(hours_lookback: int = 24, max_per_category: int = 8) -> dict:
    """Fetch recent articles from all RSS feeds, grouped by category."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours_lookback)
    all_articles = {}

    for category, feeds in RSS_FEEDS.items():
        articles = []
        for source_name, url in feeds:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:10]:
                    pub = _parse_date(entry)
                    if pub and pub < cutoff:
                        continue

                    summary = re.sub(
                        r"<[^>]+>", "",
                        getattr(entry, "summary", "") or ""
                    )[:500]

                    articles.append({
                        "source":    source_name,
                        "title":     getattr(entry, "title", "Untitled"),
                        "link":      getattr(entry, "link", "#"),
                        "summary":   summary.strip(),
                        "published": pub.strftime("%b %d, %Y %H:%M UTC") if pub else "Recent",
                    })
            except Exception as e:
                print(f"  ⚠️  Could not fetch {source_name}: {e}")

        if articles:
            all_articles[category] = articles[:max_per_category]

    return all_articles


def _parse_date(entry):
    """Extract and normalize the published date from a feed entry."""
    for field in ["published_parsed", "updated_parsed"]:
        val = getattr(entry, field, None)
        if val:
            try:
                return datetime.fromtimestamp(time.mktime(val), tz=timezone.utc)
            except Exception:
                pass
    return None