"""Step 1: collect news articles for a topic (no API key needed)."""
import re
import feedparser
try:
    import trafilatura
except Exception:      # blocked or missing: fall back to snippets
    trafilatura = None
from urllib.parse import urlparse, parse_qs, quote_plus
from concurrent.futures import ThreadPoolExecutor


def _real_url(link):
    # Bing wraps the real article link inside ?url=...
    q = parse_qs(urlparse(link).query)
    return q.get("url", [link])[0]


def _clean_html(text):
    return re.sub(r"<[^>]+>", " ", text or "").strip()


def _get_full_text(url):
    if trafilatura is None:
        return ""
    try:
        html = trafilatura.fetch_url(url)
        if html:
            return trafilatura.extract(html) or ""
    except Exception:
        pass
    return ""


def fetch_articles(query, limit=15):
    feed = feedparser.parse(
        f"https://www.bing.com/news/search?q={quote_plus(query)}&format=rss"
    )
    items, seen = [], set()
    for e in feed.entries:
        title = e.get("title", "").strip()
        if not title or title in seen:
            continue
        seen.add(title)
        items.append({
            "title": title,
            "url": _real_url(e.get("link", "")),
            "snippet": _clean_html(e.get("summary", "")),
            "source": e.get("news_source", "News"),
            "published": e.get("published", ""),
        })
        if len(items) >= limit:
            break

    # download full article text in parallel (faster)
    with ThreadPoolExecutor(8) as pool:
        texts = list(pool.map(lambda a: _get_full_text(a["url"]), items))

    for a, t in zip(items, texts):
        # if the full text could not be downloaded, use title + snippet
        a["text"] = t if len(t) > 300 else f'{a["title"]}. {a["snippet"]}'
    return items
