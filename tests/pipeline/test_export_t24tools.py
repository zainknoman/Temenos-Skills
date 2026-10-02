import json

from export_t24tools import build_export, write_export


def test_fields_doc_shape_and_nulls(db):
    fields, _ = build_export(db, "R25")
    acc = fields["apps"]["ACCOUNT"]
    assert acc["prefix"] == "AC."
    assert acc["recordClass"] == "Account"
    assert acc["fields"][0] == [1, "AC.CUSTOMER", "Account_Customer", "TField", "Yes", None]
    assert acc["fields"][2] == [3, "AC.ACCOUNT.TITLE.1", "Account_AccountTitle1", None, None, None]


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
    assert (m["apps"], m["fields"], m["schemaVersion"]) == (2, 5, 2)
    assert json.loads((tmp_path / "manifest.json").read_text()) == m


def test_blank_strings_export_as_null_not_optional(db, tmp_path):
    db.execute("INSERT INTO fields VALUES ('ACCOUNT','AC.BLANK',4,'Account_Blank','x.jar','','','')")
    fields, desc = build_export(db, "R25")
    assert fields["apps"]["ACCOUNT"]["fields"][3] == [4, "AC.BLANK", "Account_Blank", None, None, None]
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
