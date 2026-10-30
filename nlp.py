"""Summarization + clustering in plain Python (no scikit-learn, no numpy)."""
import re
import math
import random
from collections import Counter

STOP = set("""the and for that with this from are was were has have had not but you your they their them his her its
will would can could should may might also into than then there here about after before over under more most some such
only other which when where while what who whom why how all any both each few many much own same too very just said says
say new one two been being out off our ours she him who's per via get got use used""".split())


def tokenize(text):
    return [w for w in re.findall(r"[a-z]{3,}", text.lower()) if w not in STOP]


def tfidf_vectors(docs, normalize=True):
    """Turn each text into a {word: weight} dictionary using TF-IDF."""
    tokens = [tokenize(d) for d in docs]
    n = len(docs)
    df = Counter()
    for t in tokens:
        df.update(set(t))
    idf = {w: math.log((1 + n) / (1 + c)) + 1 for w, c in df.items()}
    vectors = []
    for t in tokens:
        v = {w: c * idf[w] for w, c in Counter(t).items()}
        if normalize:
            norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
            v = {w: x / norm for w, x in v.items()}
        vectors.append(v)
    return vectors


def cosine(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(w, 0.0) for w, x in a.items())


# ---------------- Summarization ----------------
def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
    return [p.strip() for p in parts if 40 <= len(p.strip()) <= 400]


def summarize(text, n=3):
    """Pick the n most important sentences (TF-IDF score)."""
    sents = split_sentences(text)
    if not sents:
        return text[:300]
    if len(sents) <= n:
        return " ".join(sents)
    vectors = tfidf_vectors(sents, normalize=False)
    scores = [sum(v.values()) / math.sqrt(max(len(v), 1)) for v in vectors]
    best = sorted(sorted(range(len(sents)), key=lambda i: scores[i])[-n:])
    return " ".join(sents[i] for i in best)


# ---------------- Clustering ----------------
def _centroid(members):
    total = Counter()
    for v in members:
        for w, x in v.items():
            total[w] += x
    norm = math.sqrt(sum(x * x for x in total.values())) or 1.0
    return {w: x / norm for w, x in total.items()}


def _kmeans(vectors, k, iterations=20):
    random.seed(42)
    centers = [random.choice(vectors)]
    while len(centers) < k:                      # pick far-apart starting points
        far = min(vectors, key=lambda v: max(cosine(v, c) for c in centers))
        centers.append(far)
    labels = [0] * len(vectors)
    for _ in range(iterations):
        new = [max(range(k), key=lambda c: cosine(v, centers[c])) for v in vectors]
        if new == labels:
            break
        labels = new
        for c in range(k):
            members = [vectors[i] for i in range(len(vectors)) if labels[i] == c]
            if members:
                centers[c] = _centroid(members)
    return labels, centers


def cluster_articles(articles, k=3):
    if len(articles) < 4:
        return [{"label": "All articles", "articles": articles}]
    texts = [a["title"] + " " + a["text"] for a in articles]
    vectors = tfidf_vectors(texts)
    k = max(2, min(k, len(texts) // 2))
    labels, centers = _kmeans(vectors, k)

    groups = []
    for c in range(k):
        members = [articles[i] for i in range(len(articles)) if labels[i] == c]
        if not members:
            continue
        top = sorted(centers[c], key=centers[c].get, reverse=True)[:3]
        groups.append({"label": ", ".join(top), "articles": members})
    return sorted(groups, key=lambda g: -len(g["articles"]))
