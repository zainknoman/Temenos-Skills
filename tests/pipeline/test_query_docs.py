import sqlite3

import pytest

from query_docs import resolve_topic, topics

KNOWN = ["AA", "ACCOUNT", "Temenos_Applications", "TPH - Copy", "TPH-Clearing", "TPH-R21"]


def _fake_chroma(dirpath, chunks):
    """The tables of Chroma's SQLite file that topics() reads: chunks = [(collection, topic, source)]."""
    conn = sqlite3.connect(dirpath / "chroma.sqlite3")
    conn.executescript("""
        CREATE TABLE collections (id TEXT, name TEXT);
        CREATE TABLE segments (id TEXT, collection TEXT);
        CREATE TABLE embeddings (id INTEGER, segment_id TEXT);
        CREATE TABLE embedding_metadata (id INTEGER, key TEXT, string_value TEXT);
        INSERT INTO collections VALUES ('c1', 't24_docs'), ('c2', 'other');
        INSERT INTO segments VALUES ('s1', 'c1'), ('s2', 'c2');""")
    for i, (collection, topic, source) in enumerate(chunks):
        conn.execute("INSERT INTO embeddings VALUES (?, ?)", (i, "s1" if collection == "t24_docs" else "s2"))
        conn.executemany("INSERT INTO embedding_metadata VALUES (?, ?, ?)",
                         [(i, "topic", topic), (i, "source", source), (i, "page", None)])
    conn.commit()
    conn.close()


def test_topics_counts_files_and_chunks_per_topic(tmp_path):
    _fake_chroma(tmp_path, [
        ("t24_docs", "ACCOUNT", "ACCOUNT/a.pdf"), ("t24_docs", "ACCOUNT", "ACCOUNT/a.pdf"),
        ("t24_docs", "ACCOUNT", "ACCOUNT/sub/b.pdf"), ("t24_docs", "aa", "aa/c.pdf"),
        ("other", "IGNORED", "x.pdf"),  # another collection is not counted
    ])
    found = topics(tmp_path, examples=2)
    assert [t["topic"] for t in found] == ["aa", "ACCOUNT"]  # sorted case-insensitively
    account = found[1]
    assert (account["files"], account["chunks"]) == (2, 3)
    assert account["examples"] == ["a.pdf", "b.pdf"]  # largest first, file name only
    assert "examples" not in topics(tmp_path)[0]


def test_resolve_topic_exact_and_any_case():
    assert resolve_topic("ACCOUNT", KNOWN) == "ACCOUNT"
    assert resolve_topic("temenos_applications", KNOWN) == "Temenos_Applications"


def test_resolve_topic_suggests_close_names():
    with pytest.raises(ValueError, match="Did you mean: TPH - Copy, TPH-Clearing, TPH-R21"):
        resolve_topic("tph", KNOWN)


def test_resolve_topic_explains_application_is_not_a_topic():
    with pytest.raises(ValueError, match="not a T24 application"):
        resolve_topic("CUSTOMER", KNOWN)
