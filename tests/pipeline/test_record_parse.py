import shutil
import sqlite3
import subprocess
import zipfile

import pytest

from tests.conftest import SCHEMA

SOURCES = {
    "com/temenos/api/TField.java": "package com.temenos.api; public class TField {}",
    "com/temenos/t24/api/records/demo/DemoRecord.java": """
        package com.temenos.t24.api.records.demo;
        import com.temenos.api.TField; import java.util.List;
        public class DemoRecord {
            public TField getSingle() { return null; }
            public List<TField> getMulti() { return null; }
            public List<GroupHeadClass> getGroupHead() { return null; }
            public TField getMulti(int i) { return null; }
            public void setSingle(CharSequence v) {}
        }""",
    "com/temenos/t24/api/records/demo/GroupHeadClass.java": """
        package com.temenos.t24.api.records.demo;
        import com.temenos.api.TField;
        public class GroupHeadClass { public TField getMember() { return null; } }""",
}


@pytest.fixture(scope="module")
def demo_jar(tmp_path_factory):
    javac = shutil.which("javac")
    if not javac:
        pytest.skip("javac not available")
    root = tmp_path_factory.mktemp("rec")
    src, out = root / "src", root / "out"
    for rel, text in SOURCES.items():
        (src / rel).parent.mkdir(parents=True, exist_ok=True)
        (src / rel).write_text(text)
    subprocess.run([javac, "-d", str(out)] + [str(src / r) for r in SOURCES], check=True)
    jars = root / "jars"
    jars.mkdir()
    with zipfile.ZipFile(jars / "DEMO.jar", "w") as z:
        for cls in out.rglob("*.class"):
            z.write(cls, cls.relative_to(out).as_posix())
    return jars


def _db():
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    rows = [("DEMO", "DM.SINGLE", 1, "Demo_Single"), ("DEMO", "DM.MULTI", 2, "Demo_Multi"),
            ("DEMO", "DM.GROUP.HEAD", 3, "Demo_GroupHead"), ("DEMO", "DM.MEMBER", 4, "Demo_Member"),
            ("DEMO", "DM.UNKNOWN", 5, "Demo_Unknown")]
    conn.executemany("INSERT INTO fields (app, field_name, position, java_alias) VALUES (?,?,?,?)", rows)
    return conn


def test_no_arg_getters_with_return_types(demo_jar):
    from record_parse import no_arg_getters
    data = zipfile.ZipFile(demo_jar / "DEMO.jar").read("com/temenos/t24/api/records/demo/DemoRecord.class")
    getters = no_arg_getters(data)
    assert getters["getSingle"] == "Lcom/temenos/api/TField;"
    assert getters["getMulti"] == "Ljava/util/List;"          # the no-arg overload, not getMulti(int)
    assert "setSingle" not in getters


def test_build_field_kinds(demo_jar):
    from record_parse import build_field_kinds
    conn = _db()
    stats = build_field_kinds(conn, demo_jar, release="R99")
    kinds = dict(conn.execute("SELECT field_name, kind FROM field_kinds WHERE release='R99'").fetchall())
    assert kinds == {"DM.SINGLE": "SV", "DM.MULTI": "MV", "DM.GROUP.HEAD": "MV", "DM.MEMBER": "MV-GROUP"}
    assert stats["unknown"] == 1                                # DM.UNKNOWN has no getter anywhere
