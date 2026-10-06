import os
import time
from pathlib import Path

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


# --- choosing the install (R25 machine vs R23 machine, no code change) ------------------------

def _fake_install(root, layout="r25", release="R23"):
    import zipfile
    bnk = root / "bnk" if layout == "r25" else root / "T24" / "bnk"
    (bnk / "t24lib").mkdir(parents=True)
    with zipfile.ZipFile(bnk / "t24lib" / "A.jar", "w") as z:
        z.writestr("META-INF/MANIFEST.MF", f"Manifest-Version: 1.0\nImplementation-Version: {release}_AMR.0 java 11\n")
    (root / "TAFJ" / "bin").mkdir(parents=True)
    (root / "TAFJ" / "bin" / "tCompile.bat").write_text("")
    return root


def test_r25_stays_first_choice(tmp_path):
    from compile_check import find_install
    r25 = _fake_install(tmp_path / "r25", release="R25")
    other = _fake_install(tmp_path / "other", layout="tafj")
    assert find_install(env={}, known=(r25, other)) == r25


def test_falls_back_to_first_present_install(tmp_path):
    from compile_check import find_install
    other = _fake_install(tmp_path / "other", layout="tafj")
    assert find_install(env={}, known=(tmp_path / "absent", other)) == other


def test_explicit_install_and_env_win(tmp_path):
    from compile_check import INSTALL_ENV, find_install
    r25 = _fake_install(tmp_path / "r25")
    assert find_install(explicit=tmp_path / "x", env={}, known=(r25,)) == tmp_path / "x"
    assert find_install(env={INSTALL_ENV: str(tmp_path / "y")}, known=(r25,)) == tmp_path / "y"


def test_bnk_under_t24_layout_and_release_from_manifest(tmp_path):
    from compile_check import bnk_dir, install_release, java_classpath
    root = _fake_install(tmp_path / "e", layout="tafj", release="R23")
    assert bnk_dir(root) == root / "T24" / "bnk"
    assert install_release(root) == "R23"
    assert str(root / "T24" / "bnk" / "t24lib") in java_classpath(root)


def test_java_home_untouched_for_r25_bundled_jdk_elsewhere(tmp_path):
    from compile_check import JAVA_HOME_ENV, R25, install_java_home
    root = tmp_path / "e"
    (root / "3rdParty" / "JDK" / "jdk-11" / "bin").mkdir(parents=True)
    assert install_java_home(R25, env={}) is None
    assert install_java_home(root, env={}) == root / "3rdParty" / "JDK" / "jdk-11"
    assert install_java_home(root, env={JAVA_HOME_ENV: "J"}) == Path("J")


def test_moved_install_homes_repointed_in_scratch_only(tmp_path):
    from compile_check import _scratch_properties
    root = _fake_install(tmp_path / "e", layout="tafj")
    (root / "TAFJ" / "conf").mkdir()
    original = "tafj.home=Z:\gone\TAFJ\nt24.home=Z:\gone\bnk\nx=1\n"
    (root / "TAFJ" / "conf" / "tafj.properties").write_text(original, encoding="latin-1")
    src = tmp_path / "src" / "A.b"
    src.parent.mkdir()
    src.write_text("")
    props = _scratch_properties(src, tmp_path / "out", root).read_text(encoding="latin-1")
    assert f"tafj.home={root / 'TAFJ'}" in props and f"t24.home={root / 'T24' / 'bnk'}" in props
    assert (root / "TAFJ" / "conf" / "tafj.properties").read_text(encoding="latin-1") == original


def test_existing_homes_are_kept(tmp_path):
    from compile_check import _scratch_properties
    root = _fake_install(tmp_path / "r", layout="r25")
    (root / "TAFJ" / "conf").mkdir()
    (root / "TAFJ" / "conf" / "tafj.properties").write_text(f"tafj.home={root / 'TAFJ'}\n", encoding="latin-1")
    src = tmp_path / "A.b"
    src.write_text("")
    props = _scratch_properties(src, tmp_path / "out", root).read_text(encoding="latin-1")
    assert props.count("tafj.home=") == 1


def test_write_guard_skips_unreadable_entries(tmp_path, monkeypatch):
    import compile_check
    root = tmp_path / "inst"
    root.mkdir()
    (root / "ok.txt").write_text("x")
    (root / "broken").write_text("x")
    marker = tmp_path / "m"
    marker.write_text("")
    real_stat = Path.stat

    def flaky(self, *a, **k):
        if self.name == "broken":
            raise FileNotFoundError(self)
        return real_stat(self, *a, **k)

    monkeypatch.setattr(Path, "stat", flaky)
    assert compile_check.r25_writes_since(marker, r25=root) in ([], [root / "ok.txt"])
