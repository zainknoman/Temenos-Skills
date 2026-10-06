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
    assert report["fields"][0]["compiler_checked"] == ["ST.Customer.Customer.EbCusMnemonic"]


def test_each_run_starts_from_an_empty_build_dir(db, tmp_path):
    # Stale classes (e.g. a .component compiled on an earlier run and since deleted)
    # must not let a later compile pass.
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    stale = tmp_path / "out" / "V" / "classes" / "component_OLD_cl.class"
    stale.parent.mkdir(parents=True)
    stale.write_text("old")
    seen = {}

    def spy(src, out):
        seen["stale_present"] = stale.exists()
        return CompileResult("OK", "")

    verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=spy)
    assert seen["stale_present"] is False


def test_artefact_that_reads_no_application_skips_the_field_check(db, tmp_path):
    f = tmp_path / "SAMPLE.PARAMETER.b"
    f.write_text("    Table.name = 'SAMPLE.PARAMETER'\n")
    report = verify(f, [], db, tmp_path / "out", compile_fn=OK, no_app_ok=True)
    assert report["passed"] is True
    assert report["fields"] == []
