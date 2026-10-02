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
