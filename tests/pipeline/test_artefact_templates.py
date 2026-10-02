from pathlib import Path

import pytest

from artefact_templates import FieldNotAvailable, MissingInputs, load_templates, render, resolve

JBC = {
    "id": "jbc/validation", "language": "jbc",
    "inputs": [{"id": "APP", "kind": "app"}, {"id": "FIELD", "kind": "field", "of": "APP"},
               {"id": "ROUTINE_NAME", "kind": "routineName"}],
    "files": {"{{ROUTINE_NAME}}.b": "SUBROUTINE {{ROUTINE_NAME}}\n$USING {{APP_COMPONENT}}\n"
                                    "x = EB.SystemTables.getRNew({{FIELD}})\n* {{TODAY}}\n"},
}
JAVA = {
    "id": "java/x", "language": "java",
    "inputs": [{"id": "APP", "kind": "app"}, {"id": "FIELD", "kind": "field", "of": "APP"}],
    "files": {"X.java": "import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;\n"
                        "rec.get{{FIELD}}();\n"},
}


def test_jbc_field_resolves_to_componentised_name(db_with_components):
    values = resolve(JBC, {"APP": "CUSTOMER", "FIELD": "EB.CUS.MNEMONIC", "ROUTINE_NAME": "V.X"},
                     db_with_components, today="2026-10-02")
    out = render(JBC, values)
    assert out == {"V.X.b": "SUBROUTINE V.X\n$USING ST.Customer\n"
                            "x = EB.SystemTables.getRNew(ST.Customer.Customer.EbCusMnemonic)\n* 2026-10-02\n"}


def test_java_field_resolves_to_getter_suffix_and_record_package(db):
    values = resolve(JAVA, {"APP": "CUSTOMER", "FIELD": "EB.CUS.SHORT.NAME"}, db, today="2026-10-02")
    assert render(JAVA, values)["X.java"] == (
        "import com.temenos.t24.api.records.customer.CustomerRecord;\nrec.getShortName();\n")


def test_jbc_field_without_componentised_name_is_refused(db_with_components):
    # ACCOUNT.TITLE.1 has no component_fields row in the fixture
    with pytest.raises(FieldNotAvailable, match="AC.ACCOUNT.TITLE.1"):
        resolve(JBC, {"APP": "ACCOUNT", "FIELD": "AC.ACCOUNT.TITLE.1", "ROUTINE_NAME": "V.X"},
                db_with_components, today="2026-10-02")


def test_unknown_field_is_refused(db):
    with pytest.raises(FieldNotAvailable, match="EB.CUS.NOPE"):
        resolve(JAVA, {"APP": "CUSTOMER", "FIELD": "EB.CUS.NOPE"}, db, today="2026-10-02")


def test_unfilled_placeholder_refuses_to_render():
    with pytest.raises(MissingInputs) as exc:
        render(JBC, {"ROUTINE_NAME": "V.X"})
    assert set(exc.value.missing) == {"APP_COMPONENT", "FIELD", "TODAY"}


def test_shipped_templates_load_with_their_files():
    ids = {t["id"]: t for t in load_templates()}
    assert {"jbc/validation", "java/record-lifecycle-validate"} <= set(ids)
    assert "{{ROUTINE_NAME}}.b" in ids["jbc/validation"]["files"]
    assert "{{PACKAGE}}.component" in ids["jbc/validation"]["files"]


REAL_R23 = Path("temenos_knowledge.db")


@pytest.mark.skipif(not REAL_R23.exists(), reason="R23 knowledge DB not built")
def test_shipped_templates_are_proven_against_their_golden_cases():
    import sqlite3
    from artefact_templates import prove
    conn = sqlite3.connect(REAL_R23)
    for template in load_templates():
        ok, reason = prove(template, conn)
        assert ok, (template["id"], reason)


@pytest.mark.skipif(not REAL_R23.exists(), reason="R23 knowledge DB not built")
def test_one_changed_character_breaks_the_proof(tmp_path):
    import shutil
    import sqlite3
    from artefact_templates import prove
    shutil.copytree("tests/golden", tmp_path / "golden")
    golden = tmp_path / "golden" / "jbc-customer-mnemonic-vvr" / "V.CUS.MNEMONIC.CHECK.b"
    golden.write_text(golden.read_text(encoding="utf-8").replace("lvValue EQ", "lvValue NE", 1), encoding="utf-8")
    template = next(t for t in load_templates() if t["id"] == "jbc/validation")
    ok, reason = prove(template, sqlite3.connect(REAL_R23), golden_root=tmp_path / "golden")
    assert not ok and "differs" in reason
