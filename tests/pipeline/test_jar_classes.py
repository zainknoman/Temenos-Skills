import struct
import zipfile

from jar_classes import javadoc_methods, load_jars, load_tafj, parse_signature, read_class_header
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


def test_javadoc_methods_read_from_a_javadoc_jar(tmp_path):
    jar = tmp_path / "Client-javadoc.jar"
    with zipfile.ZipFile(jar, "w") as z:
        z.writestr("com/x/core/Context.html",
                   '<div class="signature">public&nbsp;String&nbsp;getId()</div>')
    with zipfile.ZipFile(jar) as z:
        assert javadoc_methods(z, "com.x.core.Context") == [["getId", "String", []]]
        assert javadoc_methods(z, "com.x.core.Missing") == []
    assert javadoc_methods(None, "com.x.core.Context") == []


def test_load_tafj_takes_only_tafj_and_temenos_jars_as_type_tafj(tmp_path):
    lib = tmp_path / "lib"
    lib.mkdir()
    with zipfile.ZipFile(lib / "TAFJClient.jar", "w") as z:
        z.writestr("com/x/core/Context.class", class_bytes("com.x.core.Context"))
    with zipfile.ZipFile(lib / "TemnSecurity.jar", "w") as z:
        z.writestr("com/x/sec/Guard.class", class_bytes("com.x.sec.Guard"))
    with zipfile.ZipFile(lib / "ant.jar", "w") as z:
        z.writestr("org/apache/Ant.class", class_bytes("org.apache.Ant"))
    doc = tmp_path / "TAFJClient-javadoc.jar"
    with zipfile.ZipFile(doc, "w") as z:
        z.writestr("com/x/core/Context.html", '<div class="signature">public&nbsp;String&nbsp;getId()</div>')

    out = dict(load_tafj(lib, doc))
    assert sorted(out) == ["TAFJClient.jar", "TemnSecurity.jar"]
    [ctx] = out["TAFJClient.jar"]
    assert ctx["component_type"] == "tafj"
    assert ctx["methods"] == [{"name": "getId", "return_type": "String", "params": [], "is_public": True}]
    assert out["TemnSecurity.jar"][0]["methods"] == []
    assert dict(load_tafj(lib, tmp_path / "missing-javadoc.jar"))["TAFJClient.jar"][0]["methods"] == []


def test_jdk11_javadoc_method_signatures_are_read():
    assert parse_signature("public&nbsp;&lt;T&gt;&nbsp;T&nbsp;getInstanceOf&#8203;(<a href=\"x\">Class</a>&lt;T&gt;&nbsp;clazz)") == \
        ["getInstanceOf", "T", ["Class<T>"]]


def test_javadoc_methods_reads_jdk11_pre_method_signature(tmp_path):
    jar = tmp_path / "Client-javadoc.jar"
    with zipfile.ZipFile(jar, "w") as z:
        z.writestr("com/x/core/Context.html",
                   '<pre class="methodSignature">public&nbsp;String&nbsp;getId&#8203;()</pre>'
                   '<pre>public class Context extends Object</pre>')
    with zipfile.ZipFile(jar) as z:
        assert javadoc_methods(z, "com.x.core.Context") == [["getId", "String", []]]


def test_annotated_method_signatures_are_kept():
    assert parse_signature('<a href="x">@Deprecated</a>\npublic&nbsp;static&nbsp;void&nbsp;run(String s)') == \
        ["run", "void", ["String"]]
    assert parse_signature('@SuppressWarnings("unchecked") public&nbsp;int&nbsp;size()') == ["size", "int", []]
