import json

from export_t24tools import build_export, write_export


def test_fields_doc_shape_and_nulls(db):
    fields, _ = build_export(db, "R25")
    acc = fields["apps"]["ACCOUNT"]
    assert acc["prefix"] == "AC."
    assert acc["recordClass"] == "Account"
    assert acc["fields"][0] == [1, "AC.CUSTOMER", "Account_Customer", "TField", "Yes", None, None]
    assert acc["fields"][2] == [3, "AC.ACCOUNT.TITLE.1", "Account_AccountTitle1", None, None, None, None]


def test_descriptions_skip_empty(db):
    _, desc = build_export(db, "R25")
    assert desc["apps"]["ACCOUNT"] == {"AC.CUSTOMER": "Customer id", "AC.CATEGORY": "Category"}


def test_output_is_deterministic(db, tmp_path):
    m1 = write_export(db, tmp_path / "a", "R25", now="2026-10-02T00:00:00Z")
    m2 = write_export(db, tmp_path / "b", "R25", now="2026-10-02T00:00:00Z")
    assert m1 == m2
    assert (tmp_path / "a" / "fields.json").read_bytes() == (tmp_path / "b" / "fields.json").read_bytes()


def test_manifest_counts(db, tmp_path):
    m = write_export(db, tmp_path, "R25", now="2026-10-02T00:00:00Z")
    assert (m["apps"], m["fields"], m["schemaVersion"]) == (2, 5, 3)
    assert json.loads((tmp_path / "manifest.json").read_text()) == m


def test_blank_strings_export_as_null_not_optional(db, tmp_path):
    db.execute("INSERT INTO fields VALUES ('ACCOUNT','AC.BLANK',4,'Account_Blank','x.jar','','','')")
    fields, desc = build_export(db, "R25")
    assert fields["apps"]["ACCOUNT"]["fields"][3] == [4, "AC.BLANK", "Account_Blank", None, None, None, None]
    assert "AC.BLANK" not in desc["apps"]["ACCOUNT"]


def test_componentised_names_from_the_primary_component(db_with_components):
    db_with_components.execute("INSERT INTO component_fields VALUES "
                               "('R23','ACCOUNT','AZ.Contract','Account','Category',2,'AC.CATEGORY')")
    db_with_components.execute("INSERT INTO component_fields VALUES "
                               "('R23','ACCOUNT','AC.AccountOpening','Account','Customer',1,'AC.CUSTOMER')")
    fields, _ = build_export(db_with_components, "R23")
    acc = fields["apps"]["ACCOUNT"]
    assert acc["components"] == ["AC.AccountOpening", "AZ.Contract"]   # most fields first
    assert acc["fields"][1][5] == "AC.AccountOpening.Account.Category"
    cus = fields["apps"]["CUSTOMER"]
    assert cus["fields"][0][5] == "ST.Customer.Customer.EbCusMnemonic"


def test_release_must_be_given(db, tmp_path):
    import pytest
    with pytest.raises(ValueError):
        write_export(db, tmp_path, "", now="2026-10-02T00:00:00Z")


def test_cli_reads_the_selected_releases_db_not_r23(tmp_path):
    # Run where only an R23 DB exists: asking for R25 must fail, never export R23 data labelled R25.
    import shutil
    import sqlite3
    import subprocess
    import sys
    from tests.conftest import ROOT, ROWS, SCHEMA
    conn = sqlite3.connect(tmp_path / "temenos_knowledge.db")
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO fields VALUES (?,?,?,?,?,?,?,?)", ROWS)
    conn.commit()
    conn.close()
    proc = subprocess.run([sys.executable, str(ROOT / "pipeline" / "export_t24tools.py"), "--release", "R25"],
                          cwd=tmp_path, capture_output=True, text=True)
    assert proc.returncode != 0
    assert "no knowledge DB for R25" in proc.stdout + proc.stderr
    assert not (tmp_path / "build").exists()


def test_export_v3_carries_value_kind(db_with_kinds):
    fields, _ = build_export(db_with_kinds, "R23")
    cus = {f[1]: f for f in fields["apps"]["CUSTOMER"]["fields"]}
    assert cus["EB.CUS.MNEMONIC"][6] == "SV"
    assert cus["EB.CUS.SHORT.NAME"][6] == "MV"
    acc = {f[1]: f for f in fields["apps"]["ACCOUNT"]["fields"]}
    assert acc["AC.ACCOUNT.TITLE.1"][6] is None      # unknown, never guessed


def test_every_export_file_states_its_schema_version_and_release(db, tmp_path):
    # T24Tools validates fields.json on its own (the manifest is not loaded), so the file must
    # carry schemaVersion itself -- without it the browser rejects the file.
    write_export(db, tmp_path, "R23", now="2026-10-03T00:00:00Z")
    for name in ("fields.json", "descriptions.json"):
        doc = json.loads((tmp_path / name).read_text(encoding="utf-8"))
        assert doc["schemaVersion"] == 3 and doc["release"] == "R23", name
