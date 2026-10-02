import sqlite3

import pytest

from tests.conftest import ROOT

REAL_DB = ROOT / "temenos_knowledge.db"


def _columns(conn):
    return [row[1] for row in conn.execute("PRAGMA table_info(fields)")]


@pytest.mark.skipif(not REAL_DB.exists(), reason="temenos_knowledge.db not built on this machine")
def test_fixture_matches_real_fields_table(db):
    real = sqlite3.connect(REAL_DB)
    try:
        assert _columns(db) == _columns(real)
    finally:
        real.close()
