import json

from run_golden import load_cases


def test_load_cases_reads_case_json(tmp_path):
    case_dir = tmp_path / "c1"
    case_dir.mkdir()
    (case_dir / "case.json").write_text(json.dumps({"name": "c1", "apps": ["ACCOUNT"], "file": "A.b"}))
    (tmp_path / "not-a-case").mkdir()
    cases = load_cases(tmp_path)
    assert [c["name"] for c in cases] == ["c1"]
    assert cases[0]["dir"] == case_dir


def _report(compile_status, missing=(), passed=False):
    return {"passed": passed, "compile": {"status": compile_status, "output": ""},
            "fields": [{"app": "CUSTOMER", "verified": [], "missing": list(missing)}]}


def test_uncompiled_case_without_r25_is_pending_not_failed():
    from run_golden import outcome
    assert outcome({"compiled": False}, _report("SKIPPED"), set()) == "PEND"


def test_compiled_case_without_r25_still_fails():
    from run_golden import outcome
    assert outcome({}, _report("SKIPPED"), set()) == "FAIL"


def test_uncompiled_case_fails_on_a_missing_field_or_a_compile_error():
    from run_golden import outcome
    assert outcome({"compiled": False}, _report("SKIPPED", ["EB.CUS.X"]), set()) == "FAIL"
    assert outcome({"compiled": False}, _report("FAIL"), set()) == "FAIL"
    assert outcome({"compiled": False}, _report("SKIPPED"), {"EB.CUS.SECTOR"}) == "FAIL"


def test_passing_case_passes():
    from run_golden import outcome
    assert outcome({"compiled": False}, _report("OK", passed=True), set()) == "PASS"
