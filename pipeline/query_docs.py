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

import chromadb
import joblib


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--vectordb", default="vectordb")
    ap.add_argument("-n", "--n-results", type=int, default=5)
    ap.add_argument("--topic", default=None, help="filter by top-level docs/ folder, e.g. ACCOUNT")
    args = ap.parse_args()

    vectordb_dir = Path(args.vectordb)
    vectorizer = joblib.load(vectordb_dir / "tfidf_vectorizer.joblib")
    client = chromadb.PersistentClient(path=str(vectordb_dir))
    collection = client.get_collection("t24_docs")

    query_vec = vectorizer.transform([args.query]).toarray().astype("float32").tolist()
    where = {"topic": args.topic} if args.topic else None
    results = collection.query(query_embeddings=query_vec, n_results=args.n_results, where=where)

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]
    if not docs:
        print("No results.")
        return

    for doc, meta, dist in zip(docs, metas, dists):
        score = 1 - dist
        print(f"--- {meta['source']} (page {meta['page']}, score {score:.3f}) ---")
        print(doc.strip())
        print()


if __name__ == "__main__":
    main()
