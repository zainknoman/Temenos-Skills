#!/usr/bin/env python3
"""Chunk and embed T24 PDF documentation into a Chroma vector DB (Layer B).

Two phases, both resumable via cache/pdf_extracts/manifest.json (SHA-256
keyed, same incremental-cache pattern as extract.py):

  1. Extract  -- pdfplumber pulls page text from each PDF under --pdfs,
     chunked (~1200 chars, 150 overlap for pages that run long) and cached
     as JSON so a rerun after adding/removing PDFs doesn't re-read unchanged
     files.
  2. Embed    -- TF-IDF (scikit-learn, fully offline -- no model download)
     vectorizes every cached chunk and upserts into a persistent Chroma
     collection at --vectordb. TF-IDF needs the whole corpus to fit its
     vocabulary/IDF weights, so this phase always rebuilds the full
     collection from every cached chunk, not just newly-changed PDFs.
     The fitted vectorizer is persisted to <vectordb>/tfidf_vectorizer.joblib
     so query_docs.py can transform queries into the same vector space.

This is business-rule / documentation search, NOT field-name lookup --
never use this for field names (see CLAUDE.md "Key decisions" #1).

Output:
  - cache/pdf_extracts/<sha256>.json : per-PDF page->chunks cache
  - cache/pdf_extracts/manifest.json : relpath -> {sha256, embedded}
  - <vectordb>/ : persistent Chroma collection "t24_docs" + tfidf_vectorizer.joblib
"""
import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import pdfplumber

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 150
MIN_CHUNK_LEN = 20
WS_RE = re.compile(r"\s+")
LP_PREFIX = "\\\\?\\"


def lp(path) -> str:
    """Windows extended-length path prefix -- bypasses the 260-char MAX_PATH
    limit that some of the deeply-nested source PDF trees exceed."""
    ap = os.path.abspath(str(path))
    if not ap.startswith(LP_PREFIX):
        ap = LP_PREFIX + ap
    return ap


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(lp(path), "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def chunk_page(text: str):
    text = WS_RE.sub(" ", text).strip()
    if len(text) < MIN_CHUNK_LEN:
        return []
    if len(text) <= CHUNK_SIZE:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = end - CHUNK_OVERLAP
    return chunks


def extract_pdf(pdf_path: Path):
    """Return list of {page, chunk_idx, text} for one PDF."""
    entries = []
    with pdfplumber.open(lp(pdf_path)) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            try:
                text = page.extract_text() or ""
            except Exception:
                continue
            for chunk_idx, chunk in enumerate(chunk_page(text)):
                entries.append({"page": page_num, "chunk_idx": chunk_idx, "text": chunk})
    return entries


def load_manifest(cache_dir: Path):
    manifest_path = cache_dir / "manifest.json"
    if manifest_path.exists():
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    return {}


def save_manifest(cache_dir: Path, manifest: dict):
    (cache_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def phase_extract(pdfs_dir: Path, cache_dir: Path):
    cache_dir.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(cache_dir)
    pdf_paths = sorted(pdfs_dir.rglob("*.pdf"))
    print(f"Found {len(pdf_paths)} PDFs under {pdfs_dir}")

    changed = 0
    for i, pdf_path in enumerate(pdf_paths, start=1):
        rel = pdf_path.relative_to(pdfs_dir).as_posix()
        sha = sha256_of(pdf_path)
        entry = manifest.get(rel)
        if entry and entry.get("sha256") == sha:
            continue
        try:
            chunks = extract_pdf(pdf_path)
        except Exception as e:
            print(f"  [extract-fail] {rel}: {e}")
            continue
        (cache_dir / f"{sha}.json").write_text(
            json.dumps({"rel": rel, "chunks": chunks}), encoding="utf-8"
        )
        manifest[rel] = {"sha256": sha, "embedded": False}
        changed += 1
        if changed % 100 == 0:
            print(f"  extracted {changed} changed/new PDFs ({i}/{len(pdf_paths)} scanned)")
            save_manifest(cache_dir, manifest)

    save_manifest(cache_dir, manifest)
    print(f"Extraction done: {changed} PDFs (re)extracted, {len(manifest)} total tracked")
    return manifest


def phase_embed(cache_dir: Path, vectordb_dir: Path, manifest: dict, batch_size: int, max_features: int):
    import chromadb
    import joblib
    from sklearn.feature_extraction.text import TfidfVectorizer

    # Multiple relpaths can share identical file content (the same PDF filed
    # under several topic folders in the source archive) -- dedupe by sha256
    # so we don't try to index the same chunk twice under colliding IDs.
    sha_to_rels: dict[str, list[str]] = {}
    for rel, entry in manifest.items():
        sha_to_rels.setdefault(entry["sha256"], []).append(rel)

    all_ids, all_docs, all_metas = [], [], []
    for sha, rels in sha_to_rels.items():
        cache_file = cache_dir / f"{sha}.json"
        if not cache_file.exists():
            continue
        data = json.loads(cache_file.read_text(encoding="utf-8"))
        rel = sorted(rels)[0]
        topic = rel.split("/", 1)[0] if "/" in rel else rel
        for c in data["chunks"]:
            all_ids.append(f"{sha}:{c['page']}:{c['chunk_idx']}")
            all_docs.append(c["text"])
            all_metas.append({"source": rel, "topic": topic, "page": c["page"]})

    print(f"Fitting TF-IDF over {len(all_docs)} chunks from {len(manifest)} PDFs")
    vectorizer = TfidfVectorizer(
        max_features=max_features, ngram_range=(1, 2), stop_words="english", sublinear_tf=True
    )
    matrix = vectorizer.fit_transform(all_docs)

    vectordb_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(vectorizer, vectordb_dir / "tfidf_vectorizer.joblib")

    client = chromadb.PersistentClient(path=str(vectordb_dir))
    try:
        client.delete_collection("t24_docs")
    except Exception:
        pass
    collection = client.create_collection("t24_docs", metadata={"hnsw:space": "cosine"})

    for start in range(0, len(all_docs), batch_size):
        end = min(start + batch_size, len(all_docs))
        emb = matrix[start:end].toarray().astype("float32").tolist()
        collection.add(
            ids=all_ids[start:end],
            documents=all_docs[start:end],
            metadatas=all_metas[start:end],
            embeddings=emb,
        )
        print(f"  upserted {end}/{len(all_docs)} chunks")

    for rel in manifest:
        manifest[rel]["embedded"] = True
    save_manifest(cache_dir, manifest)
    print(f"Embedding done. Collection count: {collection.count()}")


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdfs", default="docs")
    ap.add_argument("--vectordb", default="vectordb")
    ap.add_argument("--cache", default="cache/pdf_extracts")
    ap.add_argument("--batch-size", type=int, default=2000)
    ap.add_argument("--max-features", type=int, default=8192)
    ap.add_argument("--extract-only", action="store_true")
    ap.add_argument("--embed-only", action="store_true")
    args = ap.parse_args()

    cache_dir = Path(args.cache)
    manifest = load_manifest(cache_dir) if args.embed_only else phase_extract(Path(args.pdfs), cache_dir)
    if not args.extract_only:
        phase_embed(cache_dir, Path(args.vectordb), manifest, args.batch_size, args.max_features)


if __name__ == "__main__":
    main()
