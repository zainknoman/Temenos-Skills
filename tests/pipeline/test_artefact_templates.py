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


def _catalogue(tmp_path, types):
    import json
    path = tmp_path / "catalogue.json"
    path.write_text(json.dumps({"languages": [{"id": "jbc", "label": "jBC", "types": types}]}))
    return path


def test_export_marks_proven_and_unproven_types(db_with_components, tmp_path):
    from artefact_templates import export_templates
    cat = _catalogue(tmp_path, [{"id": "validation", "label": "VVR"}, {"id": "get-api", "label": "GET"}])
    doc = export_templates(tmp_path / "templates.json", catalogue=cat, conns={"R23": db_with_components})
    types = {t["id"]: t for t in doc["languages"][0]["types"]}
    assert types["validation"]["proven"] is True and types["validation"]["template"] == "jbc/validation"
    assert types["get-api"] == {"id": "get-api", "label": "GET", "proven": False}
    t = doc["templates"]["jbc/validation"]
    assert "{{ROUTINE_NAME}}.b" in t["files"]
    assert t["golden"]["output"]["V.CUS.MNEMONIC.CHECK.b"].startswith("*---")
    assert t["golden"]["resolved"]["R23"]["FIELD"] == "ST.Customer.Customer.EbCusMnemonic"


def test_template_failing_its_proof_is_exported_unproven(db_with_components, tmp_path, capsys):
    import shutil
    from artefact_templates import export_templates
    shutil.copytree("tests/golden", tmp_path / "golden")
    g = tmp_path / "golden" / "jbc-customer-mnemonic-vvr" / "V.CUS.MNEMONIC.CHECK.b"
    g.write_text(g.read_text(encoding="utf-8").replace("RETURN", "RETURN ", 1), encoding="utf-8")
    cat = _catalogue(tmp_path, [{"id": "validation", "label": "VVR"}])
    doc = export_templates(tmp_path / "t.json", catalogue=cat, conns={"R23": db_with_components},
                           golden_root=tmp_path / "golden")
    assert doc["languages"][0]["types"][0]["proven"] is False
    assert "jbc/validation" in capsys.readouterr().out


def test_java_refuses_multi_value_fields(db_with_kinds):
    with pytest.raises(FieldNotAvailable, match="multi-value"):
        resolve(JAVA, {"APP": "CUSTOMER", "FIELD": "EB.CUS.SHORT.NAME"}, db_with_kinds, today="2026-10-03")


def test_java_refuses_fields_without_a_record_getter(db_with_kinds):
    # AC.ACCOUNT.TITLE.1 is in fields but has no field_kinds row (no getter found)
    with pytest.raises(FieldNotAvailable, match="no single-value getter"):
        resolve(JAVA, {"APP": "ACCOUNT", "FIELD": "AC.ACCOUNT.TITLE.1"}, db_with_kinds, today="2026-10-03")


def test_java_accepts_single_value_and_infobasic_accepts_multi_value(db_with_kinds):
    assert resolve(JAVA, {"APP": "CUSTOMER", "FIELD": "EB.CUS.MNEMONIC"}, db_with_kinds, today="x")["FIELD"] == "Mnemonic"
    basic = {**JAVA, "language": "infobasic"}
    assert resolve(basic, {"APP": "CUSTOMER", "FIELD": "EB.CUS.SHORT.NAME"}, db_with_kinds, today="x")["FIELD"] == "EB.CUS.SHORT.NAME"


def test_export_flags_a_proven_template_that_was_never_compiled(db_with_components, tmp_path):
    import json
    import shutil
    from artefact_templates import export_templates
    shutil.copytree("tests/golden", tmp_path / "golden")
    case = tmp_path / "golden" / "jbc-customer-mnemonic-vvr" / "case.json"
    case.write_text(json.dumps({**json.loads(case.read_text(encoding="utf-8")), "compiled": False}), encoding="utf-8")
    cat = _catalogue(tmp_path, [{"id": "validation", "label": "VVR"}])
    doc = export_templates(tmp_path / "t.json", catalogue=cat, conns={"R23": db_with_components},
                           golden_root=tmp_path / "golden")
    entry = doc["languages"][0]["types"][0]
    assert entry["proven"] is True and entry["compiled"] is False


def test_compiled_golden_cases_export_as_compiled(db_with_components, tmp_path):
    from artefact_templates import export_templates
    cat = _catalogue(tmp_path, [{"id": "validation", "label": "VVR"}])
    doc = export_templates(tmp_path / "t.json", catalogue=cat, conns={"R23": db_with_components})
    assert doc["languages"][0]["types"][0]["compiled"] is True
