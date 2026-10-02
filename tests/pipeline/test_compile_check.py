import os
import time

from compile_check import (LOG_ENV_VARS, TCOMPILE_OVERRIDES, compile_java, compile_jbc,
                           jbc_status, r25_writes_since, scratch_env)

OK_OUT = ("Compiling...         0 error |      1 compiled |     0 remaining  [100%]\n"
          "Compilation completed for 1 file(s). \nFiles With Error : \n")
FAIL_OUT = ("[ERROR] (line 3) SPIKE.BAD, unexpected token: CALL\n"
            "Compilation completed for 1 file(s). 4 errors\nFiles With Error : \nSPIKE.BAD\n")


def test_missing_r25_is_skipped_not_passed(tmp_path):
    src = tmp_path / "A.java"
    src.write_text("class A {}")
    result = compile_java(src, tmp_path / "out", r25=tmp_path / "no-such-r25")
    assert result.status == "SKIPPED"
    assert "no-such-r25" in result.output


def test_jbc_missing_r25_is_skipped(tmp_path):
    src = tmp_path / "X.b"
    src.write_text("PROGRAM X\nEND\n")
    assert compile_jbc(src, tmp_path / "out", r25=tmp_path / "nope").status == "SKIPPED"


def test_write_guard_finds_newer_files(tmp_path):
    marker = tmp_path / "marker"
    marker.write_text("")
    fake_r25 = tmp_path / "r25"
    fake_r25.mkdir()
    newer = fake_r25 / "touched.log"
    newer.write_text("x")
    old = time.time() - 60
    os.utime(marker, (old, old))
    assert r25_writes_since(marker, r25=fake_r25) == [newer]


def test_write_guard_skips_third_party(tmp_path):
    marker = tmp_path / "marker"
    marker.write_text("")
    old = time.time() - 60
    os.utime(marker, (old, old))
    skipped = tmp_path / "r25" / "TAFJ" / "3rdParty"
    skipped.mkdir(parents=True)
    (skipped / "db.bak").write_text("x")
    assert r25_writes_since(marker, r25=tmp_path / "r25") == []


def test_jbc_status_reads_real_tcompile_output():
    assert jbc_status(0, OK_OUT) == "OK"  # contains "error" twice, still OK
    assert jbc_status(1, FAIL_OUT) == "FAIL"
    assert jbc_status(0, FAIL_OUT) == "FAIL"  # [ERROR] line wins over exit code
    assert jbc_status(0, "Config file not found") == "FAIL"  # no completion line


def test_logs_and_dirs_redirected_into_out_dir(tmp_path):
    env = scratch_env(tmp_path)
    for var in LOG_ENV_VARS:
        assert env[var].startswith(str(tmp_path))
    assert "temn.tafj.directory.classes" in TCOMPILE_OVERRIDES
    assert "temn.tafj.runtime.directory.current" in TCOMPILE_OVERRIDES


def test_javac_ignores_stub_sources_inside_r25_jars(tmp_path):
    # R25 JARs ship .java doc stubs next to .class files; javac must not compile them.
    from compile_check import javac_command
    cmd = javac_command("javac", tmp_path / "A.java", tmp_path / "out", "cp")
    assert cmd[cmd.index("-sourcepath") + 1] == ""


def test_java_classpath_includes_tafj_ext(tmp_path):
    # AccountRecord(JSONObject) needs org.json from TAFJ/ext/json.jar.
    from compile_check import java_classpath
    cp = java_classpath(tmp_path)
    for part in ("t24lib", "lib", "ext"):
        assert any(p.rstrip("\*").endswith(part) for p in cp.split(";")), part


def test_component_stub_dir_redirected():
    # Compiling a .component writes TAFC stubs to temn.tafj.compiler.tafc.component.dir,
    # which in R25 points at C:\R25\TAFJ\tafc_components (caught by the write guard 2026-10-02).
    assert "temn.tafj.compiler.tafc.component.dir" in TCOMPILE_OVERRIDES


def test_component_files_beside_a_routine_compile_first(tmp_path):
    from compile_check import compile_order
    (tmp_path / "PKG.Comp.component").write_text("component PKG.Comp\n")
    routine = tmp_path / "V.X.b"
    routine.write_text("SUBROUTINE V.X\n")
    assert compile_order(routine) == [tmp_path / "PKG.Comp.component", routine]
    assert compile_order(tmp_path / "PKG.Comp.component") == [tmp_path / "PKG.Comp.component"]
