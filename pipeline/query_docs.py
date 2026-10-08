#!/usr/bin/env python3
"""Query Layer B -- the PDF business-rule vector DB built by pdf_extract.py.

TF-IDF based (fully offline, no embedding model download -- see CLAUDE.md
Layer B). This is for business-rule / documentation search only, e.g.
"what controls dormancy in ACCOUNT?" -- NEVER use this for T24 field names.
Field names come only from skills/temenos-dev/references/table-schema/ (Layer A);
see CLAUDE.md "Key decisions" #1.
"""
import argparse
import sys
from pathlib import Path


def search(query, topic=None, n_results=5, vectordb="vectordb"):
    """[{"source", "page", "score", "text"}] for the best-matching chunks, best first."""
    import chromadb
    import joblib

    vectordb_dir = Path(vectordb)
    vectorizer = joblib.load(vectordb_dir / "tfidf_vectorizer.joblib")
    client = chromadb.PersistentClient(path=str(vectordb_dir))
    collection = client.get_collection("t24_docs")

    query_vec = vectorizer.transform([query]).toarray().astype("float32").tolist()
    where = {"topic": topic} if topic else None
    results = collection.query(query_embeddings=query_vec, n_results=n_results, where=where)
    return [{"source": meta["source"], "page": meta["page"], "score": round(1 - dist, 3), "text": doc.strip()}
            for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0])]


TOPICS_SQL = """
    SELECT t.string_value, s.string_value, COUNT(*)
    FROM embedding_metadata t
    JOIN embedding_metadata s ON s.id = t.id AND s.key = 'source'
    JOIN embeddings e ON e.id = t.id
    JOIN segments g ON g.id = e.segment_id
    JOIN collections c ON c.id = g.collection AND c.name = 't24_docs'
    WHERE t.key = 'topic'
    GROUP BY t.string_value, s.string_value"""


def _source_chunks(vectordb, batch):
    """{(topic, source): chunk count}, from Chroma's own SQLite file (read-only, under a second), or
    through the Chroma API (about 30 s for 30,000 chunks) only if that file cannot be read."""
    import sqlite3

    try:
        conn = sqlite3.connect(f"file:{(Path(vectordb) / 'chroma.sqlite3').resolve().as_posix()}?mode=ro", uri=True)
        try:
            rows = conn.execute(TOPICS_SQL).fetchall()
        finally:
            conn.close()
        if rows:
            return {(t or "", src or ""): n for t, src, n in rows}
    except sqlite3.Error:
        pass
    import chromadb

    collection = chromadb.PersistentClient(path=str(Path(vectordb))).get_collection("t24_docs")
    counts = {}
    for offset in range(0, collection.count(), batch):
        for meta in collection.get(include=["metadatas"], limit=batch, offset=offset)["metadatas"]:
            key = (meta.get("topic") or "", meta.get("source") or "")
            counts[key] = counts.get(key, 0) + 1
    return counts


def topics(vectordb="vectordb", examples=0, batch=5000):
    """Every topic in the vectordb (the top-level docs/ folder, or the file name of a PDF stored
    directly in docs/), sorted by name: [{"topic", "files", "chunks"}], plus "examples" (up to
    `examples` PDF names, largest first) when asked. --topic must be one of these names."""
    by_topic = {}
    for (topic, source), n in _source_chunks(vectordb, batch).items():
        by_topic.setdefault(topic, []).append((n, source))
    out = []
    for topic in sorted(by_topic, key=str.lower):
        sources = sorted(by_topic[topic], key=lambda x: (-x[0], x[1]))
        entry = {"topic": topic, "files": len(sources), "chunks": sum(n for n, _ in sources)}
        if examples:
            entry["examples"] = [Path(src).name for _, src in sources[:examples]]
        out.append(entry)
    return out


def resolve_topic(topic, known):
    """The exact topic name for `topic` (any case), or raise ValueError naming close matches."""
    if topic in known:
        return topic
    by_lower = {k.lower(): k for k in known}
    if topic.lower() in by_lower:
        return by_lower[topic.lower()]
    import difflib
    close = [k for k in known if topic.lower() in k.lower()] or difflib.get_close_matches(topic, known, n=5, cutoff=0.5)
    hint = (f" Did you mean: {', '.join(close[:5])}?" if close else
            " A topic is a documentation folder, not a T24 application; leave --topic out to search everything.")
    raise ValueError(f"unknown topic '{topic}'.{hint} List them with: t24skills topics")


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--vectordb", default="vectordb")
    ap.add_argument("-n", "--n-results", type=int, default=5)
    ap.add_argument("--topic", default=None, help="filter by top-level docs/ folder, e.g. ACCOUNT")
    args = ap.parse_args()

    hits = search(args.query, args.topic, args.n_results, args.vectordb)
    if not hits:
        print("No results.")
        return

    for hit in hits:
        print(f"--- {hit['source']} (page {hit['page']}, score {hit['score']:.3f}) ---")
        print(hit["text"])
        print()


if __name__ == "__main__":
    main()
