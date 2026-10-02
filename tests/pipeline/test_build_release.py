from pathlib import Path, PurePath

import pytest

from build_release import plan_steps

JAVADOC = Path(r"C:\R25\bnk\Transact_L3_Javadoc\T24.javadoc.jar")


def test_r25_build_steps_in_order():
    names = [s.name for s in plan_steps("R25", javadoc_jar=JAVADOC)]
    assert names == ["copy-javadoc", "generate-javadoc", "insert_parse", "html_parse", "component_parse"]


def test_r25_build_writes_only_to_releases_and_build():
    for step in plan_steps("R25", javadoc_jar=JAVADOC):
        for out in step.writes:
            assert PurePath(out).parts[0] in ("releases", "build"), (step.name, out)
        assert step.cwd is None or PurePath(step.cwd).parts[0] == "build", step.name


def test_javadoc_is_generated_from_a_copy_not_in_place():
    copy, generate = plan_steps("R25", javadoc_jar=JAVADOC)[:2]
    assert str(JAVADOC) in copy.cmd                      # read from C:\R25
    assert str(JAVADOC) not in generate.cmd              # run on the copy, inside build/
    assert generate.cwd.as_posix() == "build/releases/R25/javadoc"


def test_r23_rebuild_is_refused():
    with pytest.raises(ValueError, match="R23"):
        plan_steps("R23", javadoc_jar=None)


def test_without_javadoc_the_html_steps_are_skipped():
    names = [s.name for s in plan_steps("R25", javadoc_jar=None)]
    assert names == ["insert_parse", "component_parse"]
