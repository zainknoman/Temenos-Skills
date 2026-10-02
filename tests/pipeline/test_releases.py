import pytest

from releases import RELEASES, db_path


def test_r23_keeps_the_existing_db_location():
    assert str(db_path("R23")) == "temenos_knowledge.db"


def test_other_releases_live_under_releases_dir():
    assert db_path("R25").as_posix() == "releases/R25/temenos_knowledge.db"


def test_unknown_release_is_an_error():
    with pytest.raises(ValueError, match="R23"):
        db_path("R99")


def test_registry_points_r25_at_the_installed_model_bank():
    assert RELEASES["R25"].as_posix().endswith("R25/bnk/t24lib")


def test_missing_release_db_is_a_clear_error_not_an_empty_db(tmp_path):
    from releases import MissingReleaseDB, open_release_db
    missing = tmp_path / "nope.db"
    with pytest.raises(MissingReleaseDB, match="build_release.py"):
        open_release_db("R25", db=str(missing))
    assert not missing.exists()


def test_open_release_db_uses_explicit_db(tmp_path):
    import sqlite3
    from releases import open_release_db
    path = tmp_path / "k.db"
    sqlite3.connect(path).close()
    conn = open_release_db("R23", db=str(path))
    conn.close()


def test_cli_rejects_unknown_release():
    import subprocess
    import sys
    from tests.conftest import ROOT
    proc = subprocess.run([sys.executable, str(ROOT / "pipeline" / "validate_fields.py"), "--release", "R99",
                           "--app", "CUSTOMER", "--fields", "X"], capture_output=True, text=True)
    assert proc.returncode != 0
    assert "unknown release 'R99'" in proc.stdout + proc.stderr
