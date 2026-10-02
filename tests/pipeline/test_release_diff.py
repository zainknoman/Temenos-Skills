import sqlite3

from tests.conftest import SCHEMA

from release_diff import diff_releases, render_markdown

COMP = ("CREATE TABLE component_fields (release TEXT, app TEXT, component TEXT, record TEXT,"
        " comp_field TEXT, position INTEGER, field_name TEXT)")


def _db(fields, comps=()):
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO fields VALUES (?,?,?,?,?,?,?,?)",
                     [(a, f, p, None, None, None, None, None) for a, f, p in fields])
    conn.execute(COMP)
    conn.executemany("INSERT INTO component_fields VALUES (?,?,?,?,?,?,?)", comps)
    return conn


OLD = _db(
    [("ACCOUNT", "AC.CUSTOMER", 1), ("ACCOUNT", "AC.CATEGORY", 2), ("ACCOUNT", "AC.OLD.FIELD", 3),
     ("GONE.APP", "GA.X", 1)],
    [("R23", "ACCOUNT", "AC.AccountOpening", "Account", "Category", 2, "AC.CATEGORY")])
NEW = _db(
    [("ACCOUNT", "AC.CUSTOMER", 1), ("ACCOUNT", "AC.CATEGORY", 5), ("ACCOUNT", "AC.NEW.FIELD", 3),
     ("NEW.APP", "NA.X", 1)],
    [("R25", "ACCOUNT", "AC.AccountOpening", "Account", "AcCategory", 5, "AC.CATEGORY")])


def test_app_level_changes():
    d = diff_releases(OLD, NEW)
    assert d["apps_added"] == ["NEW.APP"]
    assert d["apps_removed"] == ["GONE.APP"]


def test_field_level_changes():
    acc = diff_releases(OLD, NEW)["apps"]["ACCOUNT"]
    assert acc["fields_added"] == ["AC.NEW.FIELD"]
    assert acc["fields_removed"] == ["AC.OLD.FIELD"]
    assert acc["fields_moved"] == [["AC.CATEGORY", 2, 5]]
    assert acc["jbc_renamed"] == [["AC.CATEGORY", "AC.AccountOpening.Account.Category",
                                   "AC.AccountOpening.Account.AcCategory"]]


def test_unchanged_apps_are_omitted_and_summary_counts():
    d = diff_releases(OLD, NEW)
    assert list(d["apps"]) == ["ACCOUNT"]
    assert d["summary"] == {"apps_added": 1, "apps_removed": 1, "apps_changed": 1, "fields_added": 1,
                            "fields_removed": 1, "fields_moved": 1, "jbc_renamed": 1}


def test_markdown_has_summary_then_per_app_sections():
    md = render_markdown(diff_releases(OLD, NEW), "R23", "R25")
    assert md.index("## Summary") < md.index("### ACCOUNT")
    assert "AC.CATEGORY" in md and "2 → 5" in md
