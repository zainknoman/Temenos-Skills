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


# The shapes of the real R23 / R25 record classes (javap of AccountRecord, CustomerRecord):
# a list of TField with indexed get/set, a group reached from the record, the group's first field
# (whose record list holds the group class), and a group nested in another group.
SHAPES = {
    "com/temenos/api/TField.java": "package com.temenos.api; public class TField {}",
    "com/temenos/t24/api/records/shape/ShapeRecord.java": """
        package com.temenos.t24.api.records.shape;
        import com.temenos.api.TField; import java.util.List;
        public class ShapeRecord {
            public TField getSingle() { return null; }
            public List<TField> getTitle() { return null; }
            public TField getTitle(int i) { return null; }
            public void setTitle(CharSequence v, int i) {}
            public List<RelationCodeClass> getRelationCode() { return null; }
            public RelationCodeClass getRelationCode(int i) { return null; }
            public void setRelationCode(RelationCodeClass g, int i) {}
        }""",
    "com/temenos/t24/api/records/shape/RelationCodeClass.java": """
        package com.temenos.t24.api.records.shape;
        import com.temenos.api.TField; import java.util.List;
        public class RelationCodeClass {
            public TField getRelationCode() { return null; }
            public TField getRelCustomer() { return null; }
            public List<RelDelivOptClass> getRelDelivOpt() { return null; }
            public RelDelivOptClass getRelDelivOpt(int i) { return null; }
        }""",
    "com/temenos/t24/api/records/shape/RelDelivOptClass.java": """
        package com.temenos.t24.api.records.shape;
        import com.temenos.api.TField;
        public class RelDelivOptClass { public TField getRole() { return null; } }""",
}


@pytest.fixture(scope="module")
def shape_index(tmp_path_factory):
    javac = shutil.which("javac")
    if not javac:
        pytest.skip("javac not available")
    root = tmp_path_factory.mktemp("shape")
    src, out = root / "src", root / "out"
    for rel, text in SHAPES.items():
        (src / rel).parent.mkdir(parents=True, exist_ok=True)
        (src / rel).write_text(text)
    subprocess.run([javac, "-d", str(out)] + [str(src / r) for r in SHAPES], check=True)
    (root / "jars").mkdir()
    with zipfile.ZipFile(root / "jars" / "SHAPE.jar", "w") as z:
        for cls in out.rglob("*.class"):
            z.write(cls, cls.relative_to(out).as_posix())
    from record_parse import index_record_classes
    return index_record_classes(root / "jars")


def test_how_java_reaches_each_kind_of_field(shape_index):
    from record_parse import classify
    assert classify(shape_index, "Shape_Single") == ("SV", "ShapeRecord", "")
    # A list of TField: rec.getTitle(0), rec.setTitle(value, 0).
    assert classify(shape_index, "Shape_Title") == ("MV", "ShapeRecord", "")
    # The group's first field: the record list holds RelationCodeClass, reached as
    # rec.getRelationCode(0).getRelationCode().
    assert classify(shape_index, "Shape_RelationCode") == ("MV-GROUP", "RelationCodeClass", "RelationCode")
    # A member: rec.getRelationCode(0).getRelCustomer().
    assert classify(shape_index, "Shape_RelCustomer") == ("MV-GROUP", "RelationCodeClass", "RelationCode")
    # Nested in a group: no record method returns RelDelivOptClass, so not reachable in one step.
    assert classify(shape_index, "Shape_Role") == ("MV-GROUP", "RelDelivOptClass", None)
