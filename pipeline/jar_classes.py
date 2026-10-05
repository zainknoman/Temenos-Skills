#!/usr/bin/env python3
"""Public classes of a JAR folder without javatools: each .class header is read
with the standard library (constant pool -> this / super / interfaces + access
flags), and public method signatures come from JavaDoc HTML pages
(<div class="signature">), from a JavaDoc folder or a -javadoc.jar read in memory.
Used for R25 by class_export.py (the T24 JARs, plus the TAFJ runtime JARs that hold
their superclasses); output has the extract.py cache shape: [(jar_name, [class dicts])].
Read-only on the JARs."""
import html
import re
import struct
import zipfile
from pathlib import Path

from jar_types import classify_component

ACC_PUBLIC, ACC_INTERFACE, ACC_ABSTRACT = 0x0001, 0x0200, 0x0400
METHOD_TYPES = {"hook", "public-api", "batch", "service", "integration", "tafj"}
TAFJ_JARS = ("TAFJ*.jar", "Temn*.jar")  # TAFJ runtime + Temenos platform JARs; skips the third-party ones
_SKIP_TAGS = {3: 4, 4: 4, 9: 4, 10: 4, 11: 4, 12: 4, 17: 4, 18: 4, 8: 2, 16: 2, 19: 2, 20: 2, 15: 3}


def read_class_header(data):
    """(access_flags, qualified, superclass, [interfaces]) or None if not a readable class file."""
    try:
        if data[:4] != b"\xca\xfe\xba\xbe":
            return None
        count = struct.unpack_from(">H", data, 8)[0]
        pos, i, utf8, classes = 10, 1, {}, {}
        while i < count:
            tag = data[pos]
            if tag == 1:
                length = struct.unpack_from(">H", data, pos + 1)[0]
                utf8[i] = data[pos + 3:pos + 3 + length].decode("utf-8", "replace")
                pos += 3 + length
            elif tag == 7:
                classes[i] = struct.unpack_from(">H", data, pos + 1)[0]
                pos += 3
            elif tag in (5, 6):  # long / double take two slots
                pos += 9
                i += 1
            elif tag in _SKIP_TAGS:
                pos += 1 + _SKIP_TAGS[tag]
            else:
                return None
            i += 1
        access, this, sup, n = struct.unpack_from(">HHHH", data, pos)
        name = lambda k: utf8[classes[k]].replace("/", ".") if k else ""
        interfaces = [name(struct.unpack_from(">H", data, pos + 8 + 2 * k)[0]) for k in range(n)]
        superclass = name(sup)
        return access, name(this), "" if superclass == "java.lang.Object" else superclass, interfaces
    except (IndexError, KeyError, struct.error):
        return None


_SIG = re.compile(r"^(?:@[\w.]+(?:\([^)]*\))?\s+)*"  # annotations, e.g. @Deprecated
                  r"((?:(?:public|protected|private|static|final|abstract|synchronized|default|native)\s+)*)"
                  r"(?:<.*?>\s+)?"  # a generic method's type parameters, e.g. <T>
                  r"(.+?)\s+(\w+)\((.*)\)(?:\s+throws\s+.*)?$")
# Method signatures as JavaDoc writes them: <div class="signature"> (JDK 17+) or
# <pre class="methodSignature"> (JDK 11, e.g. the TAFJ JavaDoc).
_SIGNATURE_HTML = re.compile(r'<div class="signature">(.*?)</div>|<pre class="methodSignature">(.*?)</pre>', re.S)


def _split_params(text):
    out, depth, cur = [], 0, ""
    for ch in text:
        depth += ch == "<"
        depth -= ch == ">"
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return [p.rsplit(" ", 1)[0] if " " in p else p for p in out]


def parse_signature(raw):
    """[name, returnType, [paramTypes]] for a public method signature div, else None."""
    text = html.unescape(re.sub(r"<[^>]+>", "", raw)).replace("\xa0", " ").replace("\u200b", "")
    text = re.sub(r"\s+", " ", text).strip()
    m = _SIG.match(text)
    if not m or "public" not in m.group(1).split():
        return None
    return [m.group(3), m.group(2), _split_params(m.group(4))]


def javadoc_methods(javadoc, qualified):
    """Public methods from a class's JavaDoc page; `javadoc` is a folder, an open -javadoc.jar
    (zipfile.ZipFile) or None."""
    if not javadoc:
        return []
    rel = qualified.replace("$", ".").replace(".", "/") + ".html"
    if isinstance(javadoc, zipfile.ZipFile):
        try:
            text = javadoc.read(rel).decode("utf-8", "replace")
        except KeyError:
            return []
    else:
        page = Path(javadoc) / rel
        if not page.is_file():
            return []
        text = page.read_text(encoding="utf-8", errors="replace")
    sigs = [div or pre for div, pre in _SIGNATURE_HTML.findall(text)]
    return [m for m in (parse_signature(s) for s in sigs) if m]


def load_jars(jars_dir, javadoc_root=None, *, jars=None, jar_type=None):
    """`jars` overrides the recursive *.jar scan; `jar_type` overrides the type from the JAR name."""
    out = []
    for jar in sorted(jars if jars is not None else Path(jars_dir).rglob("*.jar")):
        jtype = jar_type or classify_component(jar.name)
        classes = []
        try:
            with zipfile.ZipFile(jar) as z:
                for entry in z.namelist():
                    if not entry.endswith(".class") or entry.rsplit("/", 1)[-1] in ("module-info.class", "package-info.class"):
                        continue
                    head = read_class_header(z.read(entry))
                    if not head or not head[0] & ACC_PUBLIC:
                        continue
                    access, qualified, superclass, interfaces = head
                    package, _, name = qualified.rpartition(".")
                    methods = javadoc_methods(javadoc_root, qualified) if jtype in METHOD_TYPES else []
                    classes.append({
                        "name": name, "package": package, "qualified": qualified, "superclass": superclass,
                        "interfaces": interfaces, "is_interface": bool(access & ACC_INTERFACE),
                        "is_abstract": bool(access & ACC_ABSTRACT), "is_public": True, "component_type": jtype,
                        "methods": [{"name": n, "return_type": r, "params": p, "is_public": True} for n, r, p in methods],
                    })
        except (zipfile.BadZipFile, OSError) as exc:
            print(f"WARNING: skipped {jar.name}: {exc}")
            continue
        out.append((jar.name, classes))
    return out


def load_tafj(lib_dir, javadoc_jar=None):
    """The TAFJ runtime JARs (TAFJ_JARS in lib_dir, not recursive) as type "tafj"; methods from
    the TAFJ -javadoc.jar, read in memory, when it exists."""
    jars = sorted({j for pattern in TAFJ_JARS for j in Path(lib_dir).glob(pattern)})
    if javadoc_jar and Path(javadoc_jar).is_file():
        with zipfile.ZipFile(javadoc_jar) as doc:
            return load_jars(lib_dir, doc, jars=jars, jar_type="tafj")
    return load_jars(lib_dir, None, jars=jars, jar_type="tafj")
