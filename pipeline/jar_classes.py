#!/usr/bin/env python3
"""Public classes of a JAR folder without javatools: each .class header is read
with the standard library (constant pool -> this / super / interfaces + access
flags), and public method signatures come from JavaDoc HTML pages
(<div class="signature">). Used for R25 by class_export.py; output has the
extract.py cache shape: [(jar_name, [class dicts])]. Read-only on the JARs."""
import html
import re
import struct
import zipfile
from pathlib import Path

from jar_types import classify_component

ACC_PUBLIC, ACC_INTERFACE, ACC_ABSTRACT = 0x0001, 0x0200, 0x0400
METHOD_TYPES = {"hook", "public-api", "batch", "service", "integration"}
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


_SIG = re.compile(r"^((?:(?:public|protected|private|static|final|abstract|synchronized|default|native)\s+)*)"
                  r"(.+?)\s+(\w+)\((.*)\)(?:\s+throws\s+.*)?$")


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
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", raw)).replace("\xa0", " ")).strip()
    m = _SIG.match(text)
    if not m or "public" not in m.group(1).split():
        return None
    return [m.group(3), m.group(2), _split_params(m.group(4))]


def javadoc_methods(javadoc_root, qualified):
    page = Path(javadoc_root) / (qualified.replace("$", ".").replace(".", "/") + ".html")
    if not javadoc_root or not page.is_file():
        return []
    sigs = re.findall(r'<div class="signature">(.*?)</div>', page.read_text(encoding="utf-8", errors="replace"), re.S)
    return [m for m in (parse_signature(s) for s in sigs) if m]


def load_jars(jars_dir, javadoc_root=None):
    out = []
    for jar in sorted(Path(jars_dir).rglob("*.jar")):
        jtype = classify_component(jar.name)
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
