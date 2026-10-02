import sqlite3
import subprocess
import sys

from tests.conftest import COMPONENT_ROWS, ROOT, ROWS, SCHEMA


def _run(tmp_path, fields, with_components=True):
    db = tmp_path / "k.db"
    conn = sqlite3.connect(db)
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO fields VALUES (?,?,?,?,?,?,?,?)", ROWS)
    if with_components:
        conn.execute("CREATE TABLE component_fields (release TEXT, app TEXT, component TEXT, record TEXT,"
                     " comp_field TEXT, position INTEGER, field_name TEXT)")
        conn.executemany("INSERT INTO component_fields VALUES (?,?,?,?,?,?,?)", COMPONENT_ROWS)
    conn.commit()
    conn.close()
    return subprocess.run([sys.executable, str(ROOT / "pipeline" / "validate_fields.py"), "--db", str(db),
                           "--app", "CUSTOMER", "--fields", fields], capture_output=True, text=True)


def test_prints_componentised_name(tmp_path):
    out = _run(tmp_path, "EB.CUS.MNEMONIC").stdout
    assert "jBC ST.Customer.Customer.EbCusMnemonic" in out


def test_works_without_component_table(tmp_path):
    proc = _run(tmp_path, "EB.CUS.MNEMONIC", with_components=False)
    assert proc.returncode == 0
    assert "jBC" not in proc.stdout
