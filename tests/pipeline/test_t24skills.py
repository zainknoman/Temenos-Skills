import json
import sqlite3
import sys

import pytest

import t24skills
from tests.conftest import COMPONENT_ROWS, KIND_ROWS, ROWS, SCHEMA


def _make_db(path, rows=ROWS):
    conn = sqlite3.connect(path)
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO fields VALUES (?,?,?,?,?,?,?,?)", rows)
    conn.execute("CREATE TABLE component_fields (release TEXT, app TEXT, component TEXT, record TEXT,"
                 " comp_field TEXT, position INTEGER, field_name TEXT)")
    conn.executemany("INSERT INTO component_fields VALUES (?,?,?,?,?,?,?)", COMPONENT_ROWS)
    conn.execute("CREATE TABLE field_kinds (release TEXT, app TEXT, field_name TEXT, kind TEXT, getter_class TEXT)")
    conn.executemany("INSERT INTO field_kinds VALUES (?,?,?,?,?)", KIND_ROWS)
    conn.commit()
    conn.close()


@pytest.fixture
def cli(tmp_path, monkeypatch, capsys):
    """Run t24skills.main against temporary knowledge DBs; returns (exit code, stdout, parsed JSON or None)."""
    dbs = {"R23": tmp_path / "r23.db", "R25": tmp_path / "r25.db"}
    _make_db(dbs["R23"])
    _make_db(dbs["R25"], ROWS + [("CUSTOMER", "EB.CUS.NEW.FIELD", 3, "Customer_NewField", "ST_Customer.jar",
                                  None, None, None)])
    monkeypatch.setattr(t24skills, "_connect", lambda release: sqlite3.connect(dbs[release]))
    monkeypatch.chdir(tmp_path)  # main() changes directory; this puts it back after the test

    def run(*argv):
        code = t24skills.main(list(argv))
        out = capsys.readouterr().out
        return code, out, json.loads(out) if "--json" in argv else None
    return run


def test_fields_lists_application_in_position_order(cli):
    code, _, doc = cli("fields", "customer", "--json")
    assert code == 0 and doc["ok"] and doc["schemaVersion"] == 1 and doc["command"] == "fields"
    assert [f["field"] for f in doc["fields"]] == ["EB.CUS.MNEMONIC", "EB.CUS.SHORT.NAME"]
    first = doc["fields"][0]
    assert first["kind"] == "SV" and first["jbc"] == ["ST.Customer.Customer.EbCusMnemonic"]


def test_fields_follows_release(cli):
    _, _, doc = cli("fields", "CUSTOMER", "--release", "R25", "--json")
    assert doc["release"] == "R25" and doc["count"] == 3


def test_fields_check_missing_field_exits_1(cli):
    code, _, doc = cli("fields", "CUSTOMER", "--check", "EB.CUS.MNEMONIC, eb.cus.nope", "--json")
    assert code == 1 and doc["ok"] is False
    assert [f["field"] for f in doc["verified"]] == ["EB.CUS.MNEMONIC"]
    assert doc["missing"] == ["EB.CUS.NOPE"]


def test_fields_check_all_present_exits_0_with_text(cli):
    code, out, _ = cli("fields", "CUSTOMER", "--check", "EB.CUS.MNEMONIC")
    assert code == 0 and "VERIFIED   EB.CUS.MNEMONIC" in out


def test_unknown_application_cannot_run(cli):
    code, _, doc = cli("fields", "NOSUCHAPP", "--json")
    assert code == 2 and doc["error"]["type"] == "CANNOT_RUN"


def test_unknown_release_is_a_usage_error(cli):
    with pytest.raises(SystemExit) as exc:
        cli("fields", "CUSTOMER", "--release", "R99")
    assert exc.value.code == 2


def test_missing_release_db_cannot_run(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(t24skills, "ROOT", tmp_path)  # no knowledge DB under this root
    code = t24skills.main(["fields", "CUSTOMER", "--json"])
    doc = json.loads(capsys.readouterr().out)
    assert code == 2 and "no knowledge DB" in doc["error"]["message"]


def test_verify_resolves_relative_path_and_checks_fields(cli, tmp_path, monkeypatch):
    work = tmp_path / "work"
    work.mkdir()
    (work / "V.TEST.b").write_text("Y = R.NEW(EB.CUS.MNEMONIC)\nZ = R.NEW(EB.CUS.NOPE)\n")
    monkeypatch.chdir(work)
    code, _, doc = cli("verify", "V.TEST.b", "--app", "customer", "--no-compile", "--json")
    assert code == 1 and doc["file"] == str(work / "V.TEST.b")
    assert doc["fields"][0]["verified"] == ["EB.CUS.MNEMONIC"] and doc["fields"][0]["missing"] == ["EB.CUS.NOPE"]
    assert doc["compile"]["status"] == "NOT_RUN" and doc["compileInstall"] is None


def test_verify_missing_file_cannot_run(cli):
    code, _, doc = cli("verify", "nope.b", "--app", "CUSTOMER", "--no-compile", "--json")
    assert code == 2 and "no such file" in doc["error"]["message"]


def test_diff_summary_and_full(cli):
    code, _, doc = cli("diff", "--json")
    assert code == 0 and doc["old"] == "R23" and doc["new"] == "R25"
    assert doc["summary"]["fields_added"] == 1 and "apps" not in doc
    _, _, full = cli("diff", "R23", "R25", "--full", "--json")
    assert full["apps"]["CUSTOMER"]["fields_added"] == ["EB.CUS.NEW.FIELD"]


def test_rules_without_vectordb_cannot_run(cli, monkeypatch, tmp_path):
    monkeypatch.setattr(t24skills, "ROOT", tmp_path)
    code, _, doc = cli("rules", "dormancy", "--json")
    assert code == 2 and "t24skills run docs" in doc["error"]["message"]


def test_stages_are_in_execution_order_and_scripts_exist(cli):
    _, _, doc = cli("stages", "--json")
    assert [s["stage"] for s in doc["stages"]] == ["r23", "docs", "refs", "sepa", "r25", "golden", "export", "help"]
    for _, steps in t24skills.STAGES.values():
        for step in steps:
            assert (t24skills.HERE / step[0]).is_file(), step[0]


def test_run_dry_run_substitutes_release(cli):
    code, _, doc = cli("run", "export", "--release", "R25", "--dry-run", "--json")
    assert code == 0 and doc["dryRun"]
    assert doc["steps"][0]["command"][1:] == [str(t24skills.HERE / "release_t24tools.py"), "--release", "R25"]


def test_run_stops_at_first_failing_step(cli, monkeypatch, tmp_path):
    calls = []

    class Done:
        def __init__(self, code):
            self.returncode = code

    def fake_run(cmd, cwd, stdout):
        calls.append(cmd)
        return Done(1 if len(calls) == 2 else 0)
    monkeypatch.setattr(t24skills.subprocess, "run", fake_run)
    code, out, _ = cli("run", "r23")
    assert code == 1 and len(calls) == 2
    assert "Stage r23 stopped: step exited 1" in out


def test_run_json_keeps_stdout_one_object(cli, monkeypatch):
    seen = {}

    def fake_run(cmd, cwd, stdout):
        seen["stdout"] = stdout
        return type("Done", (), {"returncode": 0})()
    monkeypatch.setattr(t24skills.subprocess, "run", fake_run)
    code, _, doc = cli("run", "help", "--json")
    assert code == 0 and doc["ok"] and seen["stdout"] is sys.stderr


def test_golden_counts_results(cli, monkeypatch):
    import run_golden

    def fake_cases(conn, only=None, root=None):
        yield {"case": "a", "result": "PASS", "lost": [], "compiled": True,
               "report": {"compile": {"status": "OK", "output": ""}, "fields": [], "passed": True}}
        yield {"case": "b", "result": "FAIL", "lost": [], "compiled": True,
               "report": {"compile": {"status": "FAILED", "output": "boom"}, "fields": [], "passed": False}}
    monkeypatch.setattr(run_golden, "run_cases", fake_cases)
    monkeypatch.setattr(t24skills, "_use_install", lambda install: {"path": "X", "present": False, "release": None})
    code, _, doc = cli("golden", "--json")
    assert code == 1 and doc["counts"] == {"PASS": 1, "FAIL": 1, "PEND": 0}
    assert doc["cases"][1]["compileOutput"] == "boom" and "report" not in doc["cases"][0]


def test_validate_fields_check_reports_known_and_missing(db_with_kinds):
    from validate_fields import check
    res = check(db_with_kinds, "customer", ["EB.CUS.MNEMONIC", " ", "X.Y"])
    assert res["known"] and res["missing"] == ["X.Y"]
    assert res["verified"][0]["kind"] == "SV" and res["verified"][0]["jbc"] == []
    assert check(db_with_kinds, "NOAPP", ["A"])["known"] is False


@pytest.fixture
def docs(cli, monkeypatch, tmp_path):
    """A fake vectordb: search returns hits only for the exact topic 'Temenos_Applications' (or none)."""
    import query_docs
    (tmp_path / "vectordb").mkdir()
    (tmp_path / "vectordb" / "tfidf_vectorizer.joblib").write_text("")
    monkeypatch.setattr(t24skills, "ROOT", tmp_path)
    calls = []

    def fake_search(query, topic, n, vectordb):
        calls.append(topic)
        return [{"source": "Temenos_Applications/Customer.pdf", "page": 9, "score": 0.5, "text": "t"}] \
            if topic in (None, "Temenos_Applications") else []
    monkeypatch.setattr(query_docs, "search", fake_search)
    monkeypatch.setattr(query_docs, "topics", lambda vectordb, examples=0: [
        {"topic": "ACCOUNT", "files": 5, "chunks": 181, **({"examples": ["Accounts_AC.pdf"]} if examples else {})},
        {"topic": "Temenos_Applications", "files": 25, "chunks": 1407, **({"examples": ["Customer.pdf"]} if examples else {})}])
    return calls


def test_rules_topic_any_case_is_resolved(cli, docs):
    code, _, doc = cli("rules", "customer legal id", "--topic", "temenos_applications", "--json")
    assert code == 0 and doc["topic"] == "Temenos_Applications" and len(doc["results"]) == 1
    assert docs == ["temenos_applications", "Temenos_Applications"]


def test_rules_unknown_topic_cannot_run(cli, docs):
    code, _, doc = cli("rules", "customer legal id", "--topic", "CUSTOMER", "--json")
    assert code == 2 and "unknown topic 'CUSTOMER'" in doc["error"]["message"]


def test_rules_known_topic_without_hits_is_not_an_error(cli, docs):
    code, out, _ = cli("rules", "nothing", "--topic", "ACCOUNT")
    assert code == 0 and "No results." in out


def test_topics_lists_names_and_counts(cli, docs):
    code, _, doc = cli("topics", "--json")
    assert code == 0 and doc["count"] == 2 and doc["chunks"] == 1588
    assert doc["topics"][1]["examples"] == ["Customer.pdf"]
    _, out, _ = cli("topics")
    assert "Temenos_Applications" in out and "Customer.pdf" in out


@pytest.fixture
def repo(cli, monkeypatch, tmp_path):
    """A repository root with a catalogue and two golden cases (listed out of catalogue order on disk)."""
    root = tmp_path / "repo"
    (root / "templates").mkdir(parents=True)
    (root / "templates" / "catalogue.json").write_text(json.dumps({"languages": [
        {"id": "jbc", "label": "jBC (componentised)", "groups": ["Version routines", "Tables"], "types": [
            {"id": "validation", "label": "Validation routine (VVR)", "group": "Version routines"},
            {"id": "local-table", "label": "Local table", "group": "Tables"}]}]}))
    for name, template, files in [
        ("a-table", "jbc/local-table", {"T.b": "* table\r\n", "P.component": "component\r\n"}),
        ("z-vvr", "jbc/validation", {"V.b": "* vvr\r\n"}),
    ]:
        d = root / "tests" / "golden" / name
        d.mkdir(parents=True)
        main = next(iter(files))
        (d / "case.json").write_text(json.dumps({"name": name, "template": template, "skill": "temenos-jbc",
            "requirement": f"req {name}", "apps": [], "file": main, "expected_fields": [], "today": "2026-10-02",
            "userInputs": {"PACKAGE": "GOLDEN.Api"}}))
        for fname, text in files.items():
            (d / fname).write_bytes(text.encode())
    monkeypatch.setattr(t24skills, "ROOT", root)
    return root


def test_samples_listed_in_catalogue_order_and_filtered(cli, repo):
    _, _, doc = cli("samples", "--json")
    assert [s["case"] for s in doc["samples"]] == ["z-vvr", "a-table"]  # Version routines before Tables
    assert doc["samples"][1]["group"] == "Tables" and "dir" not in doc["samples"][1]
    _, _, doc = cli("samples", "TABLE", "--json")
    assert [s["case"] for s in doc["samples"]] == ["a-table"]
    _, out, _ = cli("samples")
    assert "jBC (componentised) > Tables" in out and "2 samples" in out


def test_sample_by_case_or_template_id(cli, repo):
    _, _, by_case = cli("sample", "a-table", "--json")
    _, _, by_template = cli("sample", "JBC/Local-Table", "--json")
    assert by_case["case"] == by_template["case"] == "a-table"
    assert list(by_case["files"]) == ["T.b", "P.component"] and by_case["mainFile"] == "T.b"
    _, out, _ = cli("sample", "a-table")
    assert "===== T.b (main) =====" in out and "PACKAGE = GOLDEN.Api" in out


def test_sample_unknown_suggests(cli, repo):
    code, _, doc = cli("sample", "table", "--json")
    assert code == 2 and "Did you mean: a-table" in doc["error"]["message"]


def test_sample_file_prints_only_that_file(cli, repo):
    code, out, _ = cli("sample", "a-table", "--file", "p.component")
    assert code == 0 and out.strip() == "component"
    code, _, doc = cli("sample", "a-table", "--file", "nope.b", "--json")
    assert code == 2 and "has no file 'nope.b'" in doc["error"]["message"]


def test_sample_out_copies_bytes_and_refuses_overwrite(cli, repo, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    code, _, _ = cli("sample", "a-table", "--out", "work")
    assert code == 0 and (tmp_path / "work" / "T.b").read_bytes() == b"* table\r\n"  # relative to where it started
    monkeypatch.chdir(tmp_path)  # main() moved to the repository root; a real run is a new process
    code, _, doc = cli("sample", "a-table", "--out", "work", "--json")
    assert code == 2 and "--force" in doc["error"]["message"]
    monkeypatch.chdir(tmp_path)
    assert cli("sample", "a-table", "--out", "work", "--force")[0] == 0


@pytest.fixture
def tpl(repo):
    """repo + a jbc/validation template whose sample is z-vvr."""
    d = repo / "templates" / "jbc" / "validation"
    d.mkdir(parents=True)
    (d / "template.json").write_text(json.dumps({
        "id": "jbc/validation", "language": "jbc", "type": "validation", "label": "Validation routine (VVR)",
        "description": "Reject an empty field.", "inputs": [
            {"id": "ROUTINE_NAME", "label": "Routine name", "kind": "routineName", "example": "V.SAMPLE"},
            {"id": "APP", "label": "Application", "kind": "app"},
            {"id": "FIELD", "label": "Field", "kind": "field", "of": "APP"},
            {"id": "PRODUCT", "label": "Product", "kind": "text", "fixed": "EB"}]}))
    (d / "{{ROUTINE_NAME}}.b").write_text("* {{ROUTINE_NAME}} {{TODAY}} {{PRODUCT}}\nY = {{FIELD}}\n")
    case = repo / "tests" / "golden" / "z-vvr" / "case.json"
    data = json.loads(case.read_text())
    data["userInputs"] = {"ROUTINE_NAME": "V.CUS.CHECK", "APP": "CUSTOMER", "FIELD": "EB.CUS.MNEMONIC", "PRODUCT": "EB"}
    case.write_text(json.dumps(data))
    return repo


def test_template_lists_inputs_and_a_working_example(cli, tpl):
    _, _, doc = cli("template", "z-vvr", "--json")  # a sample name works too
    assert doc["id"] == "jbc/validation" and doc["sample"] == "z-vvr"
    assert [i["id"] for i in doc["inputs"]] == ["ROUTINE_NAME", "APP", "FIELD", "PRODUCT"]
    assert doc["inputs"][2]["sample"] == "EB.CUS.MNEMONIC"
    assert "--set FIELD=EB.CUS.MNEMONIC" in doc["example"] and "PRODUCT" not in doc["example"]  # fixed: not asked
    _, _, listing = cli("template", "--json")
    assert [t["id"] for t in listing["templates"]] == ["jbc/validation"]


def test_generate_resolves_field_per_release_and_checks_it(cli, tpl):
    code, _, doc = cli("generate", "jbc/validation", "--set", "ROUTINE_NAME=V.CUS.CHECK", "--set", "app=customer",
                       "--set", "FIELD=eb.cus.mnemonic", "--today", "2026-10-08", "--json")
    assert code == 0 and doc["ok"]
    assert doc["files"] == {"V.CUS.CHECK.b": "* V.CUS.CHECK 2026-10-08 EB\nY = ST.Customer.Customer.EbCusMnemonic\n"}
    assert doc["fieldCheck"][0]["verified"] == ["ST.Customer.Customer.EbCusMnemonic"]


def test_generate_from_sample_with_override_writes_files(cli, tpl, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    code, out, _ = cli("generate", "z-vvr", "--from-sample", "--set", "ROUTINE_NAME=V.OTHER", "--out", "gen")
    assert code == 0 and (tmp_path / "gen" / "V.OTHER.b").is_file()
    assert "Compile it: t24skills verify" in out and "--app CUSTOMER" in out
    monkeypatch.chdir(tmp_path)
    code, _, doc = cli("generate", "z-vvr", "--from-sample", "--set", "ROUTINE_NAME=V.OTHER", "--out", "gen", "--json")
    assert code == 2 and "--force" in doc["error"]["message"]


def test_generate_inputs_file(cli, tpl, tmp_path, monkeypatch):
    (tmp_path / "in.json").write_text(json.dumps({"ROUTINE_NAME": "V.X", "APP": "CUSTOMER", "FIELD": "EB.CUS.MNEMONIC"}))
    monkeypatch.chdir(tmp_path)
    code, _, doc = cli("generate", "jbc/validation", "--inputs", "in.json", "--json")
    assert code == 0 and list(doc["files"]) == ["V.X.b"]


@pytest.mark.parametrize("argv, code, text", [
    (["--set", "APP=CUSTOMER"], 2, "missing inputs: ROUTINE_NAME (routineName), FIELD (field)"),
    (["--from-sample", "--set", "COLOUR=red"], 2, "has no input COLOUR"),
    (["--from-sample", "--set", "APP=NOAPP"], 2, "no application 'NOAPP'"),
    (["--from-sample", "--set", "FIELD=EB.CUS.NOPE"], 1, "EB.CUS.NOPE is not a field of CUSTOMER"),
    (["--set", "BROKEN"], 2, "--set needs KEY=VALUE"),
])
def test_generate_errors(cli, tpl, argv, code, text):
    got, _, doc = cli("generate", "jbc/validation", *argv, "--json")
    assert got == code and text in doc["error"]["message"]


def test_generate_unknown_template(cli, tpl):
    code, _, doc = cli("generate", "jbc/valid", "--json")
    assert code == 2 and "Did you mean: jbc/validation" in doc["error"]["message"]


def test_verify_no_app_skips_the_field_check(cli, tmp_path):
    (tmp_path / "T.b").write_text("* a new local table\n")
    code, _, doc = cli("verify", str(tmp_path / "T.b"), "--no-app", "--no-compile", "--json")
    assert code == 0 and doc["fields"] == []
    code, _, doc = cli("verify", str(tmp_path / "T.b"), "--no-compile", "--json")
    assert code == 1 and "no --app given" in doc["fields"][0]["error"]
