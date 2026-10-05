import struct
import zipfile

from jar_classes import javadoc_methods, load_jars, parse_signature, read_class_header
from jar_types import classify_component

PUBLIC, INTERFACE, ABSTRACT = 0x0001, 0x0200, 0x0400


def class_bytes(this, sup="java.lang.Object", ifaces=(), access=PUBLIC | 0x0020):
    """Minimal valid .class header: magic, version, constant pool (Utf8 + Class), flags, this, super, interfaces."""
    pool = []

    def utf8(s):
        pool.append(b"\x01" + struct.pack(">H", len(s)) + s.encode())
        return len(pool)

    def cls(name):
        i = utf8(name.replace(".", "/"))
        pool.append(b"\x07" + struct.pack(">H", i))
        return len(pool)

    pool.append(b"\x03" + struct.pack(">i", 42))  # an Integer constant, to exercise skipping
    t = cls(this)
    s = cls(sup) if sup else 0
    ii = [cls(x) for x in ifaces]
    head = b"\xca\xfe\xba\xbe" + struct.pack(">HHH", 0, 52, len(pool) + 1) + b"".join(pool)
    return head + struct.pack(">HHHH", access, t, s, len(ii)) + b"".join(struct.pack(">H", x) for x in ii) + b"\0" * 6


def test_header_gives_name_superclass_interfaces_and_flags():
    data = class_bytes("com.x.hook.Lifecycle", "com.x.core.Context", ["com.x.api.Hook"])
    assert read_class_header(data) == (PUBLIC | 0x0020, "com.x.hook.Lifecycle", "com.x.core.Context", ["com.x.api.Hook"])


def test_header_object_superclass_is_blank_and_garbage_is_none():
    assert read_class_header(class_bytes("com.x.A"))[2] == ""
    assert read_class_header(b"not a class") is None


def test_classify_component_is_importable_without_javatools():
    assert classify_component("EB_TemplateHook.jar") == "hook"
    assert classify_component("AA_Something.jar") == "internal"


def test_parse_signature_reads_public_methods_and_skips_constructors():
    assert parse_signature("public&nbsp;String&nbsp;checkId(String currentRecordId, "
                           '<a href="x.html">TransactionContext</a> transactionContext)') == \
        ["checkId", "String", ["String", "TransactionContext"]]
    assert parse_signature("public&nbsp;void&nbsp;post(List&lt;TransactionData&gt; data, Map&lt;String, String&gt; m)") == \
        ["post", "void", ["List<TransactionData>", "Map<String, String>"]]
    assert parse_signature("public&nbsp;Lifecycle()") is None
    assert parse_signature("protected&nbsp;void&nbsp;hidden()") is None


def test_javadoc_methods_and_load_jars(tmp_path):
    doc = tmp_path / "javadoc" / "com" / "x" / "hook"
    doc.mkdir(parents=True)
    (doc / "Lifecycle.html").write_text(
        '<h2 title="Class Lifecycle">Class Lifecycle</h2><div class="signature">public&nbsp;Lifecycle()</div>'
        '<div class="signature">public&nbsp;String&nbsp;checkId(String id)</div>', encoding="utf-8")
    assert javadoc_methods(tmp_path / "javadoc", "com.x.hook.Lifecycle") == [["checkId", "String", ["String"]]]
    assert javadoc_methods(tmp_path / "javadoc", "com.x.hook.Missing") == []

    jars = tmp_path / "jars"
    (jars / "sub").mkdir(parents=True)
    with zipfile.ZipFile(jars / "EB_TemplateHook.jar", "w") as z:
        z.writestr("com/x/hook/Lifecycle.class", class_bytes("com.x.hook.Lifecycle", "com.x.core.Context"))
        z.writestr("com/x/hook/Secret.class", class_bytes("com.x.hook.Secret", access=0x0020))
        z.writestr("module-info.class", b"skip")
        z.writestr("META-INF/MANIFEST.MF", "x")
    with zipfile.ZipFile(jars / "sub" / "AA_Core.jar", "w") as z:
        z.writestr("com/x/core/Iface.class", class_bytes("com.x.core.Iface", ifaces=[], access=PUBLIC | INTERFACE | ABSTRACT))
    (jars / "broken.jar").write_bytes(b"not a zip")

    out = dict(load_jars(jars, tmp_path / "javadoc"))
    assert sorted(out) == ["AA_Core.jar", "EB_TemplateHook.jar"]
    [life] = out["EB_TemplateHook.jar"]
    assert life == {"name": "Lifecycle", "package": "com.x.hook", "qualified": "com.x.hook.Lifecycle",
                    "superclass": "com.x.core.Context", "interfaces": [], "is_interface": False,
                    "is_abstract": False, "is_public": True, "component_type": "hook",
                    "methods": [{"name": "checkId", "return_type": "String", "params": ["String"], "is_public": True}]}
    [iface] = out["AA_Core.jar"]
    assert iface["is_interface"] and iface["is_abstract"] and iface["methods"] == []
