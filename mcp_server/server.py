#!/usr/bin/env python3
"""MCP server exposing the T24 knowledge base (CLAUDE.md P4).

Two tools:
  - lookup_fields(app)  : exact field-name lookup for a T24 application (Layer A)
  - search_rules(query) : semantic search over PDF business rules (Layer B)

This supplements, not replaces, the instruction-file skill (CLAUDE.md Key
Decision #5) -- the skill still works with zero setup by reading
skills/temenos-dev/references/table-schema/*.md and running pipeline/query_docs.py
directly. Register this server only if you want faster/structured tool calls
instead of file reads + Bash invocations:

    claude mcp add t24-knowledge -- python mcp_server/server.py

lookup_fields is field-name ground truth -- never invent a field name, always
check here (or table-schema/<APP>.md) first. search_rules is fuzzy semantic
search over business-rule PDFs and must never be used for field names (see
CLAUDE.md "Key decisions" #1).
"""
import sqlite3
from pathlib import Path
from typing import Optional

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "temenos_knowledge.db"
VECTORDB_PATH = ROOT / "vectordb"

mcp = FastMCP("t24-knowledge")


@mcp.tool()
def lookup_fields(app: str) -> list[dict]:
    """Look up every T24 field for a given application: exact field name,
    file position, Java alias, and type/mandatory/description where known.
    Ground truth from JAR INSERTS/I_F.* + JavaDoc HTML (Layer A). Never
    invent a field name -- if a field isn't returned here, it doesn't exist;
    halt and ask the developer rather than guessing.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT field_name, position, java_alias, field_type, mandatory, description "
        "FROM fields WHERE app = ? ORDER BY position",
        (app.upper(),),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@mcp.tool()
def search_rules(query: str, topic: Optional[str] = None, n_results: int = 5) -> list[dict]:
    """Semantic search over T24 PDF business-rule documentation (Layer B,
    TF-IDF -- offline, no embedding model download). Use for questions like
    "what controls dormancy in ACCOUNT?" or "what triggers ACCOUNT.OFFICER
    validation?". Optionally filter by topic (top-level docs/ folder, e.g.
    ACCOUNT, AA, DE, OFS). NOT for field names -- use lookup_fields for that.
    """
    import chromadb
    import joblib

    vectorizer = joblib.load(VECTORDB_PATH / "tfidf_vectorizer.joblib")
    client = chromadb.PersistentClient(path=str(VECTORDB_PATH))
    collection = client.get_collection("t24_docs")

    query_vec = vectorizer.transform([query]).toarray().astype("float32").tolist()
    where = {"topic": topic} if topic else None
    results = collection.query(query_embeddings=query_vec, n_results=n_results, where=where)

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]
    return [
        {"source": m["source"], "page": m["page"], "score": round(1 - d, 3), "text": doc.strip()}
        for doc, m, d in zip(docs, metas, dists)
    ]


if __name__ == "__main__":
    mcp.run()
