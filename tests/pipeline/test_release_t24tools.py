import sys

from release_t24tools import release

OK = [sys.executable, "-c", "raise SystemExit(0)"]
FAIL = [sys.executable, "-c", "raise SystemExit(1)"]


def test_failed_golden_suite_blocks_the_export(tmp_path):
    marker = tmp_path / "exported"
    export = [sys.executable, "-c", f"open(r'{marker}', 'w').close()"]
    assert release(golden_cmd=FAIL, export_cmd=export) == 1
    assert not marker.exists()


def test_passing_golden_suite_runs_the_export(tmp_path):
    marker = tmp_path / "exported"
    export = [sys.executable, "-c", f"open(r'{marker}', 'w').close()"]
    assert release(golden_cmd=OK, export_cmd=export) == 0
    assert marker.exists()


def test_templates_are_exported_after_the_fields_and_not_when_golden_fails(tmp_path):
    marker = tmp_path / "templates"
    templates = [sys.executable, "-c", f"open(r'{marker}', 'w').close()"]
    assert release(golden_cmd=FAIL, export_cmd=OK, templates_cmd=templates) == 1
    assert not marker.exists()
    assert release(golden_cmd=OK, export_cmd=OK, templates_cmd=templates) == 0
    assert marker.exists()


def test_classes_are_exported_after_the_fields_and_not_when_golden_fails(tmp_path):
    marker = tmp_path / "classes"
    classes = [sys.executable, "-c", f"open(r'{marker}', 'w').close()"]
    assert release(golden_cmd=FAIL, export_cmd=OK, class_cmd=classes) == 1
    assert not marker.exists()
    assert release(golden_cmd=OK, export_cmd=OK, class_cmd=classes) == 0
    assert marker.exists()
