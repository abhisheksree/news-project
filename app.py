"""Step 4: the website."""
import time
import threading      
import webbrowser 
from flask import Flask, render_template, abort, request
from news import fetch_articles
from nlp import summarize, cluster_articles

app = Flask(__name__)

TOPICS = {
    "t20":     {"title": "T20 Cricket World Cup", "query": "T20 Cricket World Cup", "icon": "🏏"},
    "trade":   {"title": "American Trade Wars",   "query": "US tariffs trade war",  "icon": "📦"},
    "quantum": {"title": "Quantum Computing",     "query": "quantum computing",     "icon": "⚛️"},
    "space":   {"title": "Space News",            "query": "ISRO NASA space mission", "icon": "🚀"},
    "nobel":   {"title": "Nobel Prizes",          "query": "Nobel Prize",           "icon": "🏅"},
}

CACHE = {}            # remembers results so pages open fast
CACHE_SECONDS = 1800  # 30 minutes


def build_topic(key):
    articles = fetch_articles(TOPICS[key]["query"])
    for a in articles:
        a["summary"] = summarize(a["text"], n=2)
    overall = summarize(" ".join(a["summary"] for a in articles), n=4) if articles else ""
    return {"articles": articles, "overall": overall,
            "clusters": cluster_articles(articles), "time": time.time()}


@app.route("/")
def index():
    return render_template("index.html", topics=TOPICS)


@app.route("/topic/<key>")
def topic(key):
    if key not in TOPICS:
        abort(404)
    cached = CACHE.get(key)
    if request.args.get("refresh") or not cached or time.time() - cached["time"] > CACHE_SECONDS:
        cached = CACHE[key] = build_topic(key)
    return render_template("topic.html", t=TOPICS[key], key=key, data=cached)


if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    # open the browser 1 second after the server starts
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(debug=False, port=5000)
