from compile_check import CompileResult
from verify_artefact import verify

OK = lambda src, out: CompileResult("OK", "")
FAIL = lambda src, out: CompileResult("FAIL", "boom")


def test_pass_when_fields_ok_and_compiles(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    report = verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=OK)
    assert report["passed"] is True
    assert report["fields"][0]["missing"] == []


def test_fail_on_missing_field_even_if_compiles(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.NOPE)\n")
    assert verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=OK)["passed"] is False


def test_fail_on_compile_error(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    report = verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=FAIL)
    assert report["passed"] is False
    assert report["compile"]["output"] == "boom"


def test_skipped_compile_is_not_a_pass(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    skip = lambda s, o: CompileResult("SKIPPED", "no R25")
    assert verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=skip)["passed"] is False


def test_unknown_app_fails_cleanly(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("RETURN\n")
    report = verify(f, ["ACCOUT"], db, tmp_path / "out", compile_fn=OK)
    assert report["passed"] is False
    assert "ACCOUT" in report["fields"][0]["error"]


def test_jbc_without_app_is_not_a_pass(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    report = verify(f, [], db, tmp_path / "out", compile_fn=OK)
    assert report["passed"] is False
    assert "--app" in report["fields"][0]["error"]


def test_report_lists_componentised_refs_for_the_compiler(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = EB.SystemTables.getRNew(ST.Customer.Customer.EbCusMnemonic)\n")
    report = verify(f, ["CUSTOMER"], db, tmp_path / "out", compile_fn=OK)
    assert report["fields"][0]["compiler_checked"] == ["Customer.EbCusMnemonic"]
