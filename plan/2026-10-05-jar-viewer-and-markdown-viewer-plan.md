# JAR Viewer, Markdown Viewer and Application Viewer — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Look up the JAR and package of any T24 class (R23/R25) in a new T24Tools JAR Viewer, add a Markdown Viewer, and rename the JSON Viewer to Application Viewer.

**Architecture:** Temenos-Skills turns its JAR extraction cache into a compact `classes.json` per release (string tables + tuples, ~7 MB). T24Tools publishes that file with the site like `fields.json` and reads it in a new tab built on a pure `classIndex.js`. The Markdown Viewer is RepoMind's renderer (marked → DOMPurify, lazy mermaid) with MDFV's upload list and manuscript styling.

**Tech Stack:** Python 3.13 + pytest (Temenos-Skills); React 19, Vite, Vitest 5, Playwright (T24Tools); marked, dompurify, mermaid.

**Spec:** `plan/2026-10-05-jar-viewer-and-markdown-viewer-design.md` (Temenos-Skills).

**Repos:** Temenos-Skills = `D:\Personal\Projects\Temenos-Skills` (Python is `py`). T24Tools = `D:\Personal\Projects\T24Tools` (branch `master`, same commit as GitHub).

## Global Constraints

- Never write under `C:\R25`; it is read-only. R25 classes are read from the JARs in memory; nothing is cached or written there.
- `classes.json`: `"kind": "t24-classes"`, `"schemaVersion": 1`; class tuple `[name, packageIdx, jarIdx, typeIdx, flags, superclass, interfaces, methods?]`; flags bit 1 interface, 2 abstract. Public classes only; `java.lang.Object` superclass stored as `""`.
- Methods (public only, `[name, returnType, [paramTypes]]`) only for types `hook`, `public-api`, `batch`, `service`, `integration`.
- T24Tools tab ids are permanent: `json` (label "Application Viewer"), new `jar` ("JAR Viewer"), new `md` ("Markdown Viewer").
- No knowledge download links in the T24Tools header.
- README disclaimer: the only Temenos-derived data used is application field names and Java class and JAR names.
- T24Tools dependencies are pinned to exact versions: `marked` 18.0.14, `dompurify` 3.4.15, `mermaid` 12.0.0, dev `jsdom` 30.1.1 (versions RepoMind already ships).
- CSP is unchanged: no external fonts or scripts; mermaid is bundled and lazy-loaded.
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. A class that exists in two JARs (split package) — must show both JARs, not just the first. Pinned in Task 1 and Task 5 tests.
2. Searching with lowercase or a fully-qualified name (`com.temenos.t24.api.hook.system.recordlifecycle`) — must find the class. Pinned in Task 5.
3. Dropping `fields.json` (or any JSON) into the JAR Viewer — must say it's not a classes.json and point to Application Viewer, not crash. Pinned in Task 5 (`decodeClassIndex`) and Task 7 E2E.
4. Only one release loaded — no release badges, no errors; badges appear once both are loaded. Pinned in Task 5 (`compareReleases`) and Task 7.
5. A markdown file with a broken mermaid block or `<script>` — rest of the page renders, script never runs. Pinned in Task 8.

---

## Part 1 — Temenos-Skills

### Task 1: `class_export.py` — compact class index + manifest entry

**Files:**
- Create: `pipeline/class_export.py`
- Create: `tests/pipeline/test_class_export.py`
- Modify: `pipeline/release_t24tools.py`
- Modify: `tests/pipeline/test_release_t24tools.py`

**Interfaces:**
- Produces: `load_cache(cache_dir) -> [(jar_name, [class dicts])]`, `build_class_index(jar_classes, release, now) -> dict`, `write_class_index(jar_classes, out_dir, release, now=None) -> dict` (the manifest entry), `METHOD_TYPES`, CLI `py pipeline/class_export.py --release R23 [--out DIR]` (Task 2 adds R25). `release(golden_cmd, export_cmd, templates_cmd=None, class_cmd=None)`.

- [ ] **Step 1: Write the failing tests** — `tests/pipeline/test_class_export.py`

```python
import json

from class_export import METHOD_TYPES, build_class_index, load_cache, write_class_index


def _cls(name, package, jar_type, *, superclass="", interfaces=(), is_interface=0, is_abstract=0,
         is_public=True, methods=()):
    return {"name": name, "package": package, "qualified": f"{package}.{name}", "superclass": superclass,
            "interfaces": list(interfaces), "is_interface": is_interface, "is_abstract": is_abstract,
            "is_public": is_public, "component_type": jar_type, "domain": "x",
            "methods": [{"name": m, "return_type": "java.lang.String", "params": ["java.lang.String"],
                         "is_public": pub, "is_static": 0, "is_abstract": 0} for m, pub in methods]}


HOOK = _cls("RecordLifecycle", "com.temenos.t24.api.hook.system", "hook",
            superclass="com.temenos.tafj.api.client.impl.T24Context",
            methods=[("checkId", True), ("secret", False)])
INTERNAL = _cls("Helper", "com.temenos.t24.internal", "internal", is_abstract=4,
                methods=[("run", True)])
IFACE = _cls("Dup", "com.temenos.shared", "internal", is_interface=512)


def _jars():
    return [("EB_TemplateHook.jar", [HOOK]), ("ZZ_Internal.jar", [INTERNAL, IFACE]), ("AA_Other.jar", [IFACE])]


def _decode(doc):
    out = {}
    for t in doc["classes"]:
        q = f"{doc['packages'][t[1]]}.{t[0]}"
        out.setdefault(q, []).append({"jar": doc["jars"][t[2]], "type": doc["types"][t[3]], "flags": t[4],
                                      "superclass": t[5], "interfaces": t[6],
                                      "methods": t[7] if len(t) > 7 else None})
    return out


def test_header_and_string_tables_are_sorted():
    doc = build_class_index(_jars(), "R23", "2026-10-05T00:00:00Z")
    assert doc["kind"] == "t24-classes" and doc["schemaVersion"] == 1 and doc["release"] == "R23"
    assert doc["jars"] == sorted(doc["jars"])
    assert doc["packages"] == sorted(doc["packages"])
    assert doc["types"] == sorted(doc["types"])


def test_record_lifecycle_round_trips_to_its_jar_and_superclass():
    entry = _decode(build_class_index(_jars(), "R23", "t"))["com.temenos.t24.api.hook.system.RecordLifecycle"]
    assert entry == [{"jar": "EB_TemplateHook.jar", "type": "hook", "flags": 0,
                      "superclass": "com.temenos.tafj.api.client.impl.T24Context", "interfaces": [],
                      "methods": [["checkId", "java.lang.String", ["java.lang.String"]]]}]


def test_methods_only_for_method_types_and_only_public():
    assert {"hook", "public-api", "batch", "service", "integration"} == METHOD_TYPES
    decoded = _decode(build_class_index(_jars(), "R23", "t"))
    assert decoded["com.temenos.t24.internal.Helper"][0]["methods"] is None


def test_flags_interface_and_abstract():
    decoded = _decode(build_class_index(_jars(), "R23", "t"))
    assert decoded["com.temenos.t24.internal.Helper"][0]["flags"] == 2
    assert all(e["flags"] == 1 for e in decoded["com.temenos.shared.Dup"])


def test_class_in_two_jars_is_listed_once_per_jar_in_jar_order():
    decoded = _decode(build_class_index(_jars(), "R23", "t"))
    assert [e["jar"] for e in decoded["com.temenos.shared.Dup"]] == ["AA_Other.jar", "ZZ_Internal.jar"]


def test_output_is_deterministic():
    a = json.dumps(build_class_index(_jars(), "R23", "t"))
    b = json.dumps(build_class_index(list(reversed(_jars())), "R23", "t"))
    assert a == b


def test_write_adds_classes_json_to_existing_manifest(tmp_path):
    cache = tmp_path / "cache"; cache.mkdir()
    for jar, classes in _jars():
        (cache / jar.replace(".jar", ".json")).write_text(json.dumps({"jar": jar, "sha256": "x", "classes": classes}))
    (cache / "broken.json").write_text("{not json")
    out = tmp_path / "out"; out.mkdir()
    (out / "manifest.json").write_text(json.dumps({"release": "R23", "files": {"fields.json": {"bytes": 1, "sha256": "a"}}}))
    entry = write_class_index(load_cache(cache), out, "R23", now="2026-10-05T00:00:00Z")
    manifest = json.loads((out / "manifest.json").read_text())
    data = (out / "classes.json").read_bytes()
    import hashlib
    assert manifest["files"]["fields.json"] == {"bytes": 1, "sha256": "a"}
    assert manifest["files"]["classes.json"] == entry == {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    assert manifest["classes"] == 4 and manifest["jars"] == 3
```

- [ ] **Step 2: Run to verify it fails**

Run: `py -m pytest tests/pipeline/test_class_export.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'class_export'`

- [ ] **Step 3: Implement `pipeline/class_export.py`**

```python
#!/usr/bin/env python3
"""Export a release's Java class index for T24Tools' JAR Viewer:
build/t24tools/<release>/classes.json, plus its entry in that folder's manifest.json.

Source is the extract.py cache (R23) or the JARs + JavaDoc themselves (R25, see
jar_classes.py). Every public class is listed with its
JAR, package, type (from the JAR name), flags, superclass and interfaces; public
method signatures are kept only for the types a developer codes against
(METHOD_TYPES) -- for all classes they would be ~190 MB.

  python pipeline/class_export.py --release R23
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1
METHOD_TYPES = {"hook", "public-api", "batch", "service", "integration"}  # Task 2 moves this to jar_classes.py
CLASS_CACHE = Path("cache")  # R23; Task 2 replaces this with CLASS_SOURCE
INTERFACE, ABSTRACT = 1, 2


def load_cache(cache_dir):
    """[(jar_name, [class dicts])] for every readable extract.py cache file."""
    out = []
    for path in sorted(Path(cache_dir).glob("*.json")):
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(doc, dict) and "jar" in doc and "classes" in doc:
            out.append((doc["jar"], doc["classes"]))
    return out


def _flags(c):
    return (INTERFACE if c.get("is_interface") else 0) | (ABSTRACT if c.get("is_abstract") else 0)


def build_class_index(jar_classes, release, now):
    rows = [(c, jar) for jar, classes in jar_classes for c in classes]
    jars = sorted({jar for _, jar in rows})
    packages = sorted({c["package"] for c, _ in rows})
    types = sorted({c.get("component_type") or "" for c, _ in rows})
    j, p, t = ({v: i for i, v in enumerate(xs)} for xs in (jars, packages, types))
    classes = []
    for c, jar in sorted(rows, key=lambda r: (r[0]["name"], r[0]["package"], r[1])):
        ctype = c.get("component_type") or ""
        row = [c["name"], p[c["package"]], j[jar], t[ctype], _flags(c), c.get("superclass") or "",
               list(c.get("interfaces") or [])]
        if ctype in METHOD_TYPES:
            row.append([[m["name"], m.get("return_type", ""), list(m.get("params") or [])]
                        for m in c.get("methods") or [] if m.get("is_public")])
        classes.append(row)
    return {"kind": "t24-classes", "schemaVersion": SCHEMA_VERSION, "release": release, "generated": now,
            "jars": jars, "packages": packages, "types": types, "classes": classes}


def write_class_index(jar_classes, out_dir, release, now=None):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = build_class_index(jar_classes, release,
                            now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    data = json.dumps(doc, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    (out_dir / "classes.json").write_bytes(data)
    entry = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    mpath = out_dir / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {"release": release, "files": {}}
    manifest.setdefault("files", {})["classes.json"] = entry
    manifest["classes"] = len(doc["classes"])
    manifest["jars"] = len(doc["jars"])
    mpath.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return entry


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", required=True, choices=["R23"])
    ap.add_argument("--out", help="default: build/t24tools/<release>")
    args = ap.parse_args()
    if not any(CLASS_CACHE.glob("*.json")):
        raise SystemExit(f"no class cache at {CLASS_CACHE} -- run pipeline/extract.py first")
    out = Path(args.out or f"build/t24tools/{args.release}")
    entry = write_class_index(load_cache(CLASS_CACHE), out, args.release)
    print(f"Wrote {out / 'classes.json'} ({entry['bytes'] / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run to verify it passes**

Run: `py -m pytest tests/pipeline/test_class_export.py -q`
Expected: 7 passed

- [ ] **Step 5: Wire into `release_t24tools.py` — failing test first.** Append to `tests/pipeline/test_release_t24tools.py`:

```python
def test_classes_are_exported_after_the_fields_and_not_when_golden_fails(tmp_path):
    marker = tmp_path / "classes"
    classes = [sys.executable, "-c", f"open(r'{marker}', 'w').close()"]
    assert release(golden_cmd=FAIL, export_cmd=OK, class_cmd=classes) == 1
    assert not marker.exists()
    assert release(golden_cmd=OK, export_cmd=OK, class_cmd=classes) == 0
    assert marker.exists()
```

Run: `py -m pytest tests/pipeline/test_release_t24tools.py -q` → FAIL (`unexpected keyword argument 'class_cmd'`).

- [ ] **Step 6: Implement.** In `pipeline/release_t24tools.py` replace `release()` and the `release(...)` call in `main()`:

```python
def release(golden_cmd, export_cmd, templates_cmd=None, class_cmd=None):
    if subprocess.run(golden_cmd).returncode != 0:
        print("Golden suite failed -- export NOT written.")
        return 1
    rc = subprocess.run(export_cmd).returncode
    for cmd in (class_cmd, templates_cmd):
        if rc == 0 and cmd:
            rc = subprocess.run(cmd).returncode
    return rc
```

```python
    sys.exit(release(
        golden_cmd=[sys.executable, str(HERE / "run_golden.py"), "--release", args.release],
        export_cmd=[sys.executable, str(HERE / "export_t24tools.py"), "--release", args.release,
                    "--db", str(_db(args.release)), "--out", f"build/t24tools/{args.release}"],
        class_cmd=[sys.executable, str(HERE / "class_export.py"), "--release", args.release,
                   "--out", f"build/t24tools/{args.release}"],
        templates_cmd=[sys.executable, "-c", TEMPLATES_SNIPPET, str(HERE), "build/t24tools/templates.json"],
    ))
```

Also extend the module docstring's first sentence: "...write that release's T24Tools knowledge export (build/t24tools/<release>/: fields.json, descriptions.json, classes.json)".

- [ ] **Step 7: Run all pipeline tests**

Run: `py -m pytest tests/pipeline -q`
Expected: all pass (88 before + 8 new)

- [ ] **Step 8: Commit**

```bash
git add pipeline/class_export.py pipeline/release_t24tools.py tests/pipeline/test_class_export.py tests/pipeline/test_release_t24tools.py
git commit -m "feat(export): classes.json class -> JAR index for the T24Tools JAR Viewer"
```

### Task 2: R25 classes straight from the JARs + JavaDoc (no `javatools`)

R25 has no class data in Temenos-Skills, and no R25 JAR is byte-identical to its R23 version, so the R23 cache can't be reused. Instead of the ~90-minute `extract.py` run, read each `.class` header (superclass, interfaces, flags) with the standard library (~35 s for 2,135 JARs, measured) and take methods from the R25 JavaDoc that `build_release.py` already generated.

**Files:**
- Create: `pipeline/jar_types.py` (component rules moved out of `extract.py`, which exits on import without `javatools`)
- Create: `pipeline/jar_classes.py`
- Create: `tests/pipeline/test_jar_classes.py`
- Modify: `pipeline/extract.py:138-177` (rules → import), `pipeline/class_export.py` (`main()` source switch)

**Interfaces:**
- Consumes: Task 1 `build_class_index`, `write_class_index(jar_classes, out_dir, release, now=None)`, `load_cache`, `METHOD_TYPES`.
- Produces: `jar_types.classify_component(jar_name) -> str`; `jar_classes.read_class_header(data: bytes) -> (access_flags, qualified, superclass, [interfaces]) | None`; `jar_classes.parse_signature(text) -> [name, returnType, [paramTypes]] | None`; `jar_classes.javadoc_methods(javadoc_root, qualified) -> list`; `jar_classes.load_jars(jars_dir, javadoc_root=None) -> [(jar_name, [class dicts])]` in the extract.py cache shape.

- [ ] **Step 1: Move the component rules.** Create `pipeline/jar_types.py` containing, verbatim, the `_COMPONENT_RULES` list and `classify_component()` from `pipeline/extract.py:138-177` under the docstring `"""Component type of a T24 JAR from its file name (shared by extract.py and jar_classes.py; no javatools needed)."""`. In `extract.py` delete those lines and add `from jar_types import classify_component` next to the other imports (above the `javatools` try-block). Run `py -m pytest tests/pipeline -q` → still all pass.

- [ ] **Step 2: Write the failing tests** — `tests/pipeline/test_jar_classes.py`

```python
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
```

- [ ] **Step 3: Run to verify it fails**

Run: `py -m pytest tests/pipeline/test_jar_classes.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jar_classes'`

- [ ] **Step 4: Implement `pipeline/jar_classes.py`**

```python
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
```

In `pipeline/class_export.py` import `METHOD_TYPES` from `jar_classes` instead of defining it (one definition), keep it re-exported for the Task 1 test.

- [ ] **Step 5: Run to verify it passes**

Run: `py -m pytest tests/pipeline/test_jar_classes.py tests/pipeline/test_class_export.py -q`
Expected: all pass

- [ ] **Step 6: Source switch in `class_export.py`.** Delete the local `METHOD_TYPES` and `CLASS_CACHE`, and replace `main()` (the Task 1 version accepts only R23):

```python
CLASS_SOURCE = {
    "R23": {"cache": Path("cache")},
    "R25": {"jars": Path(r"C:\R25\bnk\t24lib"), "javadoc": Path("build/releases/R25/javadoc/T24.javadoc")},
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", required=True, choices=sorted(CLASS_SOURCE))
    ap.add_argument("--out", help="default: build/t24tools/<release>")
    args = ap.parse_args()
    src = CLASS_SOURCE[args.release]
    if "cache" in src:
        if not any(src["cache"].glob("*.json")):
            raise SystemExit(f"no class cache at {src['cache']} -- run pipeline/extract.py first")
        jar_classes = load_cache(src["cache"])
    else:
        if not src["javadoc"].is_dir():
            print(f"WARNING: no JavaDoc at {src['javadoc']} -- classes without methods (run build_release.py)")
        jar_classes = load_jars(src["jars"], src["javadoc"])
    out = Path(args.out or f"build/t24tools/{args.release}")
    entry = write_class_index(jar_classes, out, args.release)
    print(f"Wrote {out / 'classes.json'} ({entry['bytes'] / 1e6:.1f} MB)")
```
with `from jar_classes import METHOD_TYPES, load_jars` at the top. Update the module docstring's usage line for R25 to `python pipeline/class_export.py --release R25   # reads C:\R25 JARs + build/releases/R25 JavaDoc`.

- [ ] **Step 7: Full suite and commit**

Run: `py -m pytest tests/pipeline -q` → all pass.

```bash
git add pipeline/jar_types.py pipeline/jar_classes.py pipeline/extract.py pipeline/class_export.py tests/pipeline/test_jar_classes.py
git commit -m "feat(export): R25 class index from JAR headers + JavaDoc, no javatools"
```

### Task 3: Generate R23 + R25 `classes.json`, update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`
- Output (git-ignored): `build/t24tools/R23/classes.json`, `build/t24tools/R25/classes.json`

- [ ] **Step 1: Export both releases**

Run: `py pipeline/release_t24tools.py --release R23` then `py pipeline/release_t24tools.py --release R25`
Expected: golden suite passes each time, then `Wrote build\t24tools\<R>\classes.json (… MB)`.

- [ ] **Step 2: Spot-check RecordLifecycle in both**

```bash
py -c "import json
for r in ('R23','R25'):
    d=json.load(open(f'build/t24tools/{r}/classes.json',encoding='utf-8'))
    hits=[(d['jars'][c[2]],d['packages'][c[1]],c[5],len(c[7]) if len(c)>7 else None) for c in d['classes'] if c[0]=='RecordLifecycle']
    print(r,len(d['classes']),'classes',len(d['jars']),'jars',hits)"
```
Expected: both list `('EB_TemplateHook.jar', 'com.temenos.t24.api.hook.system', 'com.temenos.tafj.api.client.impl.T24Context', <method count>)`; R23 ≈ 92,912 classes / 2,050 JARs, R25 ≈ 2,135 JARs. If R25's method count is 0, the JavaDoc path is wrong — stop and report.

- [ ] **Step 3: CLAUDE.md.** Replace the line
`# Temenos-derived data: personal use only, never commit it to the public T24Tools repo.` with
`# Published with T24Tools (docs/t24tools/<R>/: fields.json, classes.json, manifest.json), loadable in-tool; no download link in the T24Tools header.`
and add under the T24Tools export lines:
```
# Class -> JAR index (classes.json) for the T24Tools JAR Viewer; release_t24tools.py runs it after fields.json.
# R23 from the extract.py cache; R25 straight from C:\R25 JAR headers + build/releases/R25 JavaDoc (read-only, ~1 min).
python pipeline/class_export.py --release R23
```

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: classes.json export and T24Tools publishing rule"
```

## Part 2 — T24Tools (`D:\Personal\Projects\T24Tools`)

### Task 4: Application Viewer rename, header links removed, README

**Files:**
- Modify: `src/navigation.js`, `src/navigation.test.js`, `src/App.jsx`, `src/features/jsonViewer/JsonViewer.jsx:566` (eyebrow), `README.md`, `tests/e2e/builder.spec.js:9-17`, `tests/e2e/json.spec.js` (describe name only)

- [ ] **Step 1: Failing unit test.** In `src/navigation.test.js` change the expected last entry to `['json', 'Application Viewer']` and the title to `'has exactly the six T24 tools, in header order'` (unchanged count).

Run: `npm test -- src/navigation.test.js` → FAIL (`'JSON Viewer'` vs `'Application Viewer'`).

- [ ] **Step 2: Implement.** `src/navigation.js`: `['json', 'Application Viewer'],`. `JsonViewer.jsx` eyebrow: `<span className="eyebrow">Application Viewer</span>`.

- [ ] **Step 3: Remove header links.** In `src/App.jsx` delete the whole `<span className="knowledge-links">…</span>` block and the now-unused imports `siteKnowledgeUrl` and `SITE_RELEASES`. Delete `.knowledge-links` rules from `src/styles.css` if present (`grep -n knowledge-links src/styles.css`).

- [ ] **Step 4: E2E.** Replace the test at `tests/e2e/builder.spec.js:10` with:

```js
  test('the header has no knowledge download links', async ({ page }) => {
    await page.goto('./');
    await expect(page.locator('header a[download]')).toHaveCount(0);
    await expect(page.locator('header')).not.toContainText('Knowledge files');
  });
```
In `tests/e2e/json.spec.js` rename `test.describe('JSON Viewer'` to `test.describe('Application Viewer'`.

- [ ] **Step 5: README.** Tool table: rename the row to `**Application Viewer**` (same text). Knowledge files bullet becomes: "**Knowledge files**: **Load R23 / R25 from this site** (Routine Builder, Artefact Generator, Application Viewer, JAR Viewer) loads a published release; you can also open your own file." Replace the disclaimer's "T24Tools contains no Temenos data: field data is loaded by each user from their own knowledge file and never leaves their browser." with "The only Temenos-derived data T24Tools uses is application field names (`fields.json`) and Java class and JAR names (`classes.json`), generated from T24 product JARs. Files you open stay in your browser."

- [ ] **Step 6: Verify and commit**

Run: `npm run check` → format, lint, tests, build all pass. Run: `npm run test:e2e -- tests/e2e/builder.spec.js tests/e2e/json.spec.js` → pass.

```bash
git add -A src tests README.md
git commit -m "feat: rename JSON Viewer to Application Viewer, drop header download links"
```

### Task 5: `classIndex.js` — decode, search, JAR listing, release comparison

**Files:**
- Create: `src/features/jarViewer/classIndex.js`
- Create: `src/features/jarViewer/classIndex.test.js`

**Interfaces:**
- Produces:
  - `decodeClassIndex(doc) -> { release, generated, jars: string[], types: string[], classes: ClassEntry[], byQualified: Map<string, ClassEntry[]> }`; throws `Error` with a user-facing message on a wrong `kind` or `schemaVersion`.
  - `ClassEntry = { name, package, qualified, jar, type, isInterface, isAbstract, superclass, interfaces: string[], methods: [name, returnType, string[]][] | null }`
  - `searchClasses(index, query, { types = null, limit = 200 }) -> { results: ClassEntry[], total }` (`types`: Set of allowed types or null for all).
  - `classesInJar(index, jar) -> Map<package, ClassEntry[]>` (case-insensitive jar match, packages sorted).
  - `isJarQuery(index, query) -> string | null` (the matching JAR name).
  - `compareReleases(a, b) -> Map<qualified, { status: 'same'|'moved'|'onlyA'|'onlyB', a: string[], b: string[] }>`
  - `DEFAULT_HIDDEN_TYPES = ['internal', 'test']`

- [ ] **Step 1: Write the failing tests** — `src/features/jarViewer/classIndex.test.js`

```js
import { describe, expect, it } from 'vitest';
import {
  DEFAULT_HIDDEN_TYPES,
  classesInJar,
  compareReleases,
  decodeClassIndex,
  isJarQuery,
  searchClasses,
} from './classIndex';

// Synthetic index in the classes.json format (no Temenos data).
const doc = (release, rows, jars = ['A_Hook.jar', 'B_Core.jar', 'C_Dup.jar']) => ({
  kind: 't24-classes',
  schemaVersion: 1,
  release,
  generated: '2026-10-05T00:00:00Z',
  jars,
  packages: ['com.x.hook', 'com.x.core'],
  types: ['hook', 'internal', 'public-api'],
  classes: rows,
});
const R23 = doc('R23', [
  ['Lifecycle', 0, 0, 0, 0, 'com.x.core.Context', [], [['checkId', 'java.lang.String', ['java.lang.String']]]],
  ['LifecycleHelper', 1, 1, 1, 2, '', ['com.x.hook.Lifecycle']],
  ['Context', 1, 1, 2, 0, '', [], []],
  ['Shared', 1, 1, 1, 1, '', []],
  ['Shared', 1, 2, 1, 1, '', []],
  ['MyLifecycleUtil', 1, 1, 2, 0, '', [], []],
]);

describe('decodeClassIndex', () => {
  it('expands tuples into entries with flags and methods', () => {
    const index = decodeClassIndex(R23);
    const [hook] = index.byQualified.get('com.x.hook.Lifecycle');
    expect(hook).toMatchObject({
      name: 'Lifecycle',
      package: 'com.x.hook',
      jar: 'A_Hook.jar',
      type: 'hook',
      isInterface: false,
      isAbstract: false,
      superclass: 'com.x.core.Context',
      methods: [['checkId', 'java.lang.String', ['java.lang.String']]],
    });
    const [helper] = index.byQualified.get('com.x.core.LifecycleHelper');
    expect(helper).toMatchObject({ isAbstract: true, methods: null });
  });

  it('keeps a class found in two JARs as two entries', () => {
    const shared = decodeClassIndex(R23).byQualified.get('com.x.core.Shared');
    expect(shared.map((c) => c.jar)).toEqual(['B_Core.jar', 'C_Dup.jar']);
  });

  it('rejects a fields.json and an unknown schema version with a readable message', () => {
    expect(() => decodeClassIndex({ release: 'R23', apps: {} })).toThrow(
      /isn't a classes\.json.*Application Viewer/,
    );
    expect(() => decodeClassIndex({ ...R23, schemaVersion: 9 })).toThrow(/version 9.*version 1/);
  });
});

describe('searchClasses', () => {
  const index = decodeClassIndex(R23);
  it('ranks exact name, then prefix, then contains — case-insensitive', () => {
    const names = searchClasses(index, 'lifecycle').results.map((c) => c.name);
    expect(names).toEqual(['Lifecycle', 'LifecycleHelper', 'MyLifecycleUtil']);
  });
  it('matches a fully-qualified name and a JAR name', () => {
    expect(searchClasses(index, 'COM.X.HOOK.LIFECYCLE').results[0].qualified).toBe(
      'com.x.hook.Lifecycle',
    );
    expect(searchClasses(index, 'c_dup').results.map((c) => c.jar)).toEqual(['C_Dup.jar']);
  });
  it('filters by type and caps the list but reports the total', () => {
    const shown = new Set(['hook', 'public-api']);
    expect(searchClasses(index, 'life', { types: shown }).results.map((c) => c.name)).toEqual([
      'Lifecycle',
      'MyLifecycleUtil',
    ]);
    const capped = searchClasses(index, 'l', { limit: 2 });
    expect(capped.results).toHaveLength(2);
    expect(capped.total).toBeGreaterThan(2);
    expect(DEFAULT_HIDDEN_TYPES).toEqual(['internal', 'test']);
  });
  it('needs at least two characters', () => {
    expect(searchClasses(index, ' x ')).toEqual({ results: [], total: 0 });
  });
});

describe('JAR mode', () => {
  const index = decodeClassIndex(R23);
  it('recognises a JAR name with or without .jar, any case', () => {
    expect(isJarQuery(index, 'b_core.jar')).toBe('B_Core.jar');
    expect(isJarQuery(index, 'B_CORE')).toBe('B_Core.jar');
    expect(isJarQuery(index, 'Lifecycle')).toBeNull();
  });
  it('lists the classes of a JAR grouped by package', () => {
    const groups = classesInJar(index, 'A_Hook.jar');
    expect([...groups.keys()]).toEqual(['com.x.hook']);
    expect(groups.get('com.x.hook').map((c) => c.name)).toEqual(['Lifecycle']);
  });
});

describe('compareReleases', () => {
  it('marks same, moved, and one-release-only classes', () => {
    const a = decodeClassIndex(R23);
    const b = decodeClassIndex(
      doc(
        'R25',
        [
          ['Lifecycle', 0, 0, 0, 0, '', []],
          ['Context', 1, 2, 2, 0, '', []],
          ['NewOne', 1, 1, 2, 0, '', []],
        ],
        ['A_Hook.jar', 'B_Core.jar', 'D_New.jar'],
      ),
    );
    const diff = compareReleases(a, b);
    expect(diff.get('com.x.hook.Lifecycle')).toEqual({
      status: 'same',
      a: ['A_Hook.jar'],
      b: ['A_Hook.jar'],
    });
    expect(diff.get('com.x.core.Context')).toEqual({
      status: 'moved',
      a: ['B_Core.jar'],
      b: ['D_New.jar'],
    });
    expect(diff.get('com.x.core.NewOne').status).toBe('onlyB');
    expect(diff.get('com.x.core.Shared').status).toBe('onlyA');
  });
});
```

- [ ] **Step 2: Run to verify it fails**

Run: `npm test -- src/features/jarViewer/classIndex.test.js`
Expected: FAIL — cannot resolve `./classIndex`

- [ ] **Step 3: Implement `src/features/jarViewer/classIndex.js`**

```js
// Reading of a classes.json class index (exported by Temenos-Skills pipeline/class_export.py):
// string tables + one tuple per class, [name, packageIdx, jarIdx, typeIdx, flags, superclass,
// interfaces, methods?]. Flags: 1 interface, 2 abstract. Public classes only.

export const SUPPORTED_SCHEMA = 1;
export const DEFAULT_HIDDEN_TYPES = ['internal', 'test'];

export function decodeClassIndex(doc) {
  if (doc?.kind !== 't24-classes')
    throw new Error(
      "This isn't a classes.json (expected kind t24-classes). Open fields.json and other JSON in the Application Viewer.",
    );
  if (doc.schemaVersion !== SUPPORTED_SCHEMA)
    throw new Error(
      `classes.json format version ${doc.schemaVersion} is not supported; this JAR Viewer reads version ${SUPPORTED_SCHEMA}.`,
    );
  const byQualified = new Map();
  const classes = doc.classes.map(([name, p, j, t, flags, superclass, interfaces, methods]) => {
    const pkg = doc.packages[p];
    const entry = {
      name,
      package: pkg,
      qualified: pkg ? `${pkg}.${name}` : name,
      jar: doc.jars[j],
      type: doc.types[t],
      isInterface: (flags & 1) !== 0,
      isAbstract: (flags & 2) !== 0,
      superclass: superclass || '',
      interfaces: interfaces || [],
      methods: methods || null,
    };
    if (!byQualified.has(entry.qualified)) byQualified.set(entry.qualified, []);
    byQualified.get(entry.qualified).push(entry);
    return entry;
  });
  return {
    release: doc.release,
    generated: doc.generated,
    jars: doc.jars,
    types: doc.types,
    classes,
    byQualified,
  };
}

function rank(entry, q) {
  const name = entry.name.toLowerCase();
  if (name === q || entry.qualified.toLowerCase() === q) return 0;
  if (name.startsWith(q)) return 1;
  if (name.includes(q)) return 2;
  if (entry.qualified.toLowerCase().includes(q) || entry.jar.toLowerCase().includes(q)) return 3;
  return -1;
}

export function searchClasses(index, query, { types = null, limit = 200 } = {}) {
  const q = query.trim().toLowerCase();
  if (q.length < 2) return { results: [], total: 0 };
  const hits = [];
  for (const entry of index.classes) {
    if (types && !types.has(entry.type)) continue;
    const r = rank(entry, q);
    if (r >= 0) hits.push([r, entry]);
  }
  hits.sort(
    (x, y) =>
      x[0] - y[0] ||
      x[1].name.length - y[1].name.length ||
      x[1].qualified.localeCompare(y[1].qualified),
  );
  return { results: hits.slice(0, limit).map(([, e]) => e), total: hits.length };
}

export function isJarQuery(index, query) {
  const q = query.trim().toLowerCase().replace(/\.jar$/, '');
  if (!q) return null;
  return index.jars.find((jar) => jar.toLowerCase().replace(/\.jar$/, '') === q) || null;
}

export function classesInJar(index, jar) {
  const groups = new Map();
  for (const entry of index.classes) {
    if (entry.jar.toLowerCase() !== jar.toLowerCase()) continue;
    if (!groups.has(entry.package)) groups.set(entry.package, []);
    groups.get(entry.package).push(entry);
  }
  return new Map([...groups.entries()].sort(([a], [b]) => a.localeCompare(b)));
}

export function compareReleases(a, b) {
  const jarsOf = (index, q) => (index.byQualified.get(q) || []).map((e) => e.jar).sort();
  const out = new Map();
  for (const q of new Set([...a.byQualified.keys(), ...b.byQualified.keys()])) {
    const ja = jarsOf(a, q);
    const jb = jarsOf(b, q);
    const status = !jb.length
      ? 'onlyA'
      : !ja.length
        ? 'onlyB'
        : ja.join('\n') === jb.join('\n')
          ? 'same'
          : 'moved';
    out.set(q, { status, a: ja, b: jb });
  }
  return out;
}
```

- [ ] **Step 4: Run to verify it passes**

Run: `npm test -- src/features/jarViewer/classIndex.test.js`
Expected: PASS (all tests)

- [ ] **Step 5: Commit**

```bash
git add src/features/jarViewer
git commit -m "feat(jar): class index decoding, ranked search, JAR listing, release comparison"
```

### Task 6: Publish `classes.json` with the site

**Files:**
- Modify: `src/build/knowledgeFiles.js:11-17`, `src/build/knowledgeFiles.test.js`
- Add: `docs/t24tools/R23/classes.json`, `docs/t24tools/R25/classes.json`; update both `manifest.json`

- [ ] **Step 1: Failing test.** In `src/build/knowledgeFiles.test.js`, change the first test's expectation to:

```js
    expect(files.map((f) => f.target)).toEqual(
      SITE_RELEASES.flatMap((r) => [
        siteKnowledgePath(r),
        siteKnowledgePath(r, 'classes.json'),
        siteKnowledgePath(r, 'manifest.json'),
      ]),
    );
```
and turn the checksum test into one over both files:

```js
  it.each(SITE_RELEASES.flatMap((r) => [[r, 'fields.json'], [r, 'classes.json']]))(
    '%s %s matches the SHA-256 in its manifest',
    (release, file) => {
      const dir = new URL(`docs/t24tools/${release}/`, root);
      const manifest = JSON.parse(readFileSync(new URL('manifest.json', dir), 'utf8'));
      const bytes = readFileSync(new URL(file, dir));
      expect(manifest.release).toBe(release);
      expect(bytes.length).toBe(manifest.files[file].bytes);
      expect(createHash('sha256').update(bytes).digest('hex')).toBe(manifest.files[file].sha256);
    },
  );
```

Run: `npm test -- src/build/knowledgeFiles.test.js` → FAIL.

- [ ] **Step 2: Implement.** In `knowledgeFiles()` change `['fields.json', 'manifest.json']` to `['fields.json', 'classes.json', 'manifest.json']`; update the header comment to "publish the R23 / R25 knowledge files (fields.json, classes.json) kept in docs/t24tools/".

- [ ] **Step 3: Copy the export.** For R23 and R25 copy `classes.json` and `manifest.json` from `D:\Personal\Projects\Temenos-Skills\build\t24tools\<R>\` into `docs/t24tools/<R>/` (overwrite the manifest — its `fields.json` entry is unchanged because Task 3 re-exported fields from the same DB; verify with `git diff docs/t24tools/R23/manifest.json` that only `generated`, `classes`, `jars` and `files.classes.json` changed. If the `fields.json` sha256 changed, copy that `fields.json` too.)

- [ ] **Step 4: Verify and commit**

Run: `npm test -- src/build/knowledgeFiles.test.js` → PASS.

```bash
git add src/build docs/t24tools
git commit -m "feat(knowledge): publish R23/R25 classes.json with the site"
```

### Task 7: JAR Viewer tab

**Files:**
- Create: `src/features/jarViewer/JarViewer.jsx`
- Create: `tests/e2e/jar.spec.js`, `tests/e2e/fixtures/classes-RTEST.json`
- Modify: `src/navigation.js`, `src/navigation.test.js`, `src/App.jsx`, `src/styles.css`, `README.md`

**Interfaces:**
- Consumes: Task 5 `decodeClassIndex`, `searchClasses`, `classesInJar`, `isJarQuery`, `compareReleases`, `DEFAULT_HIDDEN_TYPES`; `siteKnowledgeUrl(release, file)` from `src/lib/knowledge.js`; `SITE_RELEASES` from `src/lib/siteKnowledge.js`; `formatBytes` from `src/features/jsonViewer/jsonTree.js`; `toast` from `src/lib/toast.js` (check its export name with `grep -n export src/lib/toast.js` and use it for the Copy confirmation).
- Produces: `export function JarViewer()`.

- [ ] **Step 1: Navigation test first.** In `src/navigation.test.js` expect seven tabs, the new last entry `['jar', 'JAR Viewer']`, rename the title to `'has exactly the seven T24 tools, in header order'`, and add `expect(initialTab('?tool=jar')).toBe('jar');`. Run `npm test -- src/navigation.test.js` → FAIL. Add `['jar', 'JAR Viewer'],` after `json` in `NAV_TABS` → PASS.

- [ ] **Step 2: E2E fixture** — `tests/e2e/fixtures/classes-RTEST.json` (synthetic, no Temenos data):

```json
{"kind":"t24-classes","schemaVersion":1,"release":"RTEST","generated":"2026-10-05T00:00:00Z",
 "jars":["SAMPLE_Hooks.jar","SAMPLE_Core.jar"],"packages":["com.sample.core","com.sample.hook"],
 "types":["hook","internal"],
 "classes":[["BaseContext",0,1,1,2,"",[]],
  ["SampleLifecycle",1,0,0,0,"com.sample.core.BaseContext",[],[["checkId","java.lang.String",["java.lang.String"]]]]]}
```

- [ ] **Step 3: Failing E2E** — `tests/e2e/jar.spec.js`

```js
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { expect, test } from '@playwright/test';

const FIXTURE = fileURLToPath(new URL('./fixtures/classes-RTEST.json', import.meta.url));
const upload = (page, name, buffer) =>
  page
    .locator('input[type=file][aria-label="classes.json file"]')
    .setInputFiles({ name, mimeType: 'application/json', buffer });

test.describe('JAR Viewer', () => {
  test('finds a class, shows its JAR, follows the superclass', async ({ page }) => {
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.goto('./?tool=jar');
    await upload(page, 'classes-RTEST.json', readFileSync(FIXTURE));
    await expect(page.getByText(/RTEST · 2 classes · 2 JARs/)).toBeVisible();
    await page.getByLabel('Search classes, packages or JARs').fill('samplelife');
    await page.getByRole('button', { name: /SampleLifecycle/ }).click();
    const detail = page.getByRole('region', { name: 'Class detail' });
    await expect(detail).toContainText('SAMPLE_Hooks.jar');
    await expect(detail).toContainText('checkId(java.lang.String)');
    await detail.getByRole('button', { name: 'com.sample.core.BaseContext' }).click();
    await expect(detail).toContainText('SAMPLE_Core.jar');
    expect(errors).toEqual([]);
  });

  test('a JAR name lists its classes', async ({ page }) => {
    await page.goto('./?tool=jar');
    await upload(page, 'classes-RTEST.json', readFileSync(FIXTURE));
    await page.getByLabel('Show types').getByLabel('internal').check();
    await page.getByLabel('Search classes, packages or JARs').fill('sample_core.jar');
    await expect(page.getByRole('heading', { name: 'SAMPLE_Core.jar' })).toBeVisible();
    await expect(page.getByText('BaseContext')).toBeVisible();
  });

  test('a fields.json is refused with a pointer to the Application Viewer', async ({ page }) => {
    await page.goto('./?tool=jar');
    await upload(page, 'fields.json', Buffer.from('{"release":"R23","apps":{}}'));
    await expect(page.getByRole('alert')).toContainText('Application Viewer');
  });

  test('loads the published R23 index and finds RecordLifecycle', async ({ page }) => {
    await page.goto('./?tool=jar');
    await page.getByRole('button', { name: 'Load R23 from this site' }).click();
    await expect(page.getByText(/R23 · [\d,]+ classes/)).toBeVisible({ timeout: 30_000 });
    await page.getByLabel('Search classes, packages or JARs').fill('RecordLifecycle');
    await page.getByRole('button', { name: /^RecordLifecycle com\.temenos\.t24\.api\.hook\.system/ }).click();
    await expect(page.getByRole('region', { name: 'Class detail' })).toContainText('EB_TemplateHook.jar');
  });
});
```

Run: `npm run test:e2e -- tests/e2e/jar.spec.js` → FAIL (no tab content).

- [ ] **Step 4: Implement `src/features/jarViewer/JarViewer.jsx`**

```jsx
import { useMemo, useRef, useState } from 'react';
import { siteKnowledgeUrl } from '../../lib/knowledge';
import { SITE_RELEASES } from '../../lib/siteKnowledge';
import { formatBytes } from '../jsonViewer/jsonTree';
import {
  DEFAULT_HIDDEN_TYPES,
  classesInJar,
  compareReleases,
  decodeClassIndex,
  isJarQuery,
  searchClasses,
} from './classIndex';

const BADGE = {
  same: (d) => `same JAR in both`,
  moved: (d) => `moved: ${d.a.join(', ')} → ${d.b.join(', ')}`,
  onlyA: () => 'only in the first release',
  onlyB: () => 'only in the second release',
};

function Kind({ c }) {
  const bits = [c.type, c.isInterface && 'interface', c.isAbstract && 'abstract'];
  return <small className="muted">{bits.filter(Boolean).join(' · ')}</small>;
}

function ClassDetail({ entries, index, diff, releases, onOpen }) {
  const c = entries[0];
  const known = (q) => index.byQualified.has(q);
  const link = (q) =>
    known(q) ? (
      <button type="button" className="link-button" onClick={() => onOpen(q)}>
        {q}
      </button>
    ) : (
      <code>{q}</code>
    );
  const d = diff?.get(c.qualified);
  return (
    <section className="routine-card jar-detail" aria-label="Class detail">
      <h2>{c.name}</h2>
      <p className="muted">
        <code>{c.package}</code> <Kind c={c} />
      </p>
      <table>
        <tbody>
          <tr>
            <th>JAR</th>
            <td>
              {entries.map((e) => (
                <code key={e.jar} className="jar-name">
                  {e.jar}
                </code>
              ))}
              {entries.length > 1 && <small className="muted"> (in {entries.length} JARs)</small>}
            </td>
          </tr>
          {c.superclass && (
            <tr>
              <th>Extends</th>
              <td>{link(c.superclass)}</td>
            </tr>
          )}
          {c.interfaces.length > 0 && (
            <tr>
              <th>Implements</th>
              <td>{c.interfaces.map((q) => <div key={q}>{link(q)}</div>)}</td>
            </tr>
          )}
          {d && (
            <tr>
              <th>{releases.join(' → ')}</th>
              <td>{BADGE[d.status](d)}</td>
            </tr>
          )}
        </tbody>
      </table>
      <p>
        <button
          type="button"
          onClick={() => navigator.clipboard?.writeText(`import ${c.qualified};`)}
        >
          Copy import
        </button>{' '}
        <code>import {c.qualified};</code>
      </p>
      {c.methods && (
        <>
          <h3>Public methods ({c.methods.length})</h3>
          <ul className="jar-methods">
            {c.methods.map(([name, ret, params], i) => (
              <li key={i}>
                <code>
                  {ret} {name}({params.join(', ')})
                </code>
              </li>
            ))}
          </ul>
        </>
      )}
    </section>
  );
}

export function JarViewer() {
  const fileInput = useRef(null);
  const [indexes, setIndexes] = useState({}); // release -> decoded index (session only)
  const [active, setActive] = useState('');
  const [query, setQuery] = useState('');
  const [shown, setShown] = useState(null); // Set of visible types; null until an index loads
  const [selected, setSelected] = useState('');
  const [error, setError] = useState('');
  const [busy, setBusy] = useState('');

  const index = indexes[active];
  const releases = Object.keys(indexes).sort();
  const diff = useMemo(
    () => (releases.length === 2 ? compareReleases(indexes[releases[0]], indexes[releases[1]]) : null),
    [indexes], // eslint-disable-line react-hooks/exhaustive-deps
  );

  function add(doc, label) {
    const decoded = decodeClassIndex(doc);
    setIndexes((cur) => ({ ...cur, [decoded.release]: decoded }));
    setActive(decoded.release);
    setShown((cur) => cur || new Set(decoded.types.filter((t) => !DEFAULT_HIDDEN_TYPES.includes(t))));
    setError('');
    return `${label}`;
  }

  async function run(label, load) {
    setBusy(label);
    setError('');
    try {
      add(await load(), label);
    } catch (e) {
      setError(`${label}: ${e.message}`);
    } finally {
      setBusy('');
    }
  }

  const loadSite = (r) =>
    run(`Load ${r}`, async () => {
      const res = await fetch(siteKnowledgeUrl(r, 'classes.json'));
      if (!res.ok) throw new Error(`HTTP ${res.status} — upload a classes.json instead`);
      return res.json();
    });

  const loadFile = (file) =>
    file && run(`${file.name} (${formatBytes(file.size)})`, async () => JSON.parse(await file.text()));

  const jar = index ? isJarQuery(index, query) : null;
  const found = index && !jar ? searchClasses(index, query, { types: shown }) : null;
  const detail = index && selected ? index.byQualified.get(selected) : null;
  const badge = (q) => diff?.get(q)?.status;

  return (
    <div className="routine-creator jar-viewer">
      <div className="routine-creator-hero">
        <div>
          <span className="eyebrow">JAR Viewer</span>
          <h1>Which JAR holds a T24 class?</h1>
          <p className="muted">
            Load a release's <code>classes.json</code> and search a class, package or JAR name.
            Load R23 and R25 to see which classes moved between JARs.
          </p>
        </div>
      </div>

      <section className="routine-card" aria-label="Class index">
        <div className="routine-creator-actions">
          {SITE_RELEASES.map((r) => (
            <button key={r} type="button" disabled={!!busy} onClick={() => loadSite(r)}>
              {busy === `Load ${r}` ? `Loading ${r}…` : `Load ${r} from this site`}
            </button>
          ))}
          <button type="button" className="primary" onClick={() => fileInput.current?.click()}>
            Open classes.json…
          </button>
          <input
            ref={fileInput}
            type="file"
            accept=".json,application/json"
            hidden
            aria-label="classes.json file"
            onChange={(e) => {
              loadFile(e.target.files?.[0]);
              e.target.value = '';
            }}
          />
        </div>
        {error && (
          <p className="routine-validation" role="alert">
            {error}
          </p>
        )}
        {releases.length > 0 && (
          <div className="jar-releases" role="status">
            {releases.map((r) => (
              <button
                key={r}
                type="button"
                className={r === active ? 'active' : undefined}
                aria-pressed={r === active}
                onClick={() => setActive(r)}
              >
                {r} · {indexes[r].classes.length.toLocaleString()} classes ·{' '}
                {indexes[r].jars.length.toLocaleString()} JARs
              </button>
            ))}
          </div>
        )}
      </section>

      {index && (
        <section className="routine-card" aria-label="Search">
          <input
            className="jar-search"
            aria-label="Search classes, packages or JARs"
            placeholder="Class, package or JAR name — e.g. RecordLifecycle or EB_TemplateHook.jar"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <fieldset className="jar-types" aria-label="Show types">
            {index.types.map((t) => (
              <label key={t}>
                <input
                  type="checkbox"
                  aria-label={t}
                  checked={shown.has(t)}
                  onChange={() =>
                    setShown((cur) => {
                      const next = new Set(cur);
                      next.has(t) ? next.delete(t) : next.add(t);
                      return next;
                    })
                  }
                />{' '}
                {t}
              </label>
            ))}
          </fieldset>

          {jar && (
            <div className="jar-list">
              <h2>{jar}</h2>
              {[...classesInJar(index, jar)].map(([pkg, list]) => (
                <div key={pkg}>
                  <h3>
                    <code>{pkg}</code> <small className="muted">{list.length}</small>
                  </h3>
                  {list.map((c) => (
                    <button key={c.qualified} type="button" className="jar-hit" onClick={() => setSelected(c.qualified)}>
                      {c.name}
                    </button>
                  ))}
                </div>
              ))}
            </div>
          )}

          {found && query.trim().length >= 2 && (
            <div className="jar-list">
              <p className="muted">
                {found.total.toLocaleString()} match{found.total === 1 ? '' : 'es'}
                {found.total > found.results.length && ` — showing the best ${found.results.length}, refine to narrow`}
              </p>
              {found.results.map((c) => (
                <button
                  key={c.qualified + c.jar}
                  type="button"
                  className="jar-hit"
                  aria-current={c.qualified === selected ? 'true' : undefined}
                  onClick={() => setSelected(c.qualified)}
                >
                  <b>{c.name}</b> <code>{c.package}</code> <span className="jar-name">{c.jar}</span>
                  {badge(c.qualified) && <span className={`jar-badge ${badge(c.qualified)}`}>{badge(c.qualified)}</span>}
                </button>
              ))}
            </div>
          )}
        </section>
      )}

      {detail && (
        <ClassDetail entries={detail} index={index} diff={diff} releases={releases} onOpen={setSelected} />
      )}
    </div>
  );
}
```

Remove the unused `d` parameter from `BADGE.same` if lint flags it (`same: () => 'same JAR in both'`). Run `npx prettier --write src/features/jarViewer` before linting.

- [ ] **Step 5: Wire up.** `src/App.jsx`: add
`const JarViewer = named(() => import('./features/jarViewer/JarViewer'), 'JarViewer');` and `{tab === 'jar' && <JarViewer />}` after the `json` line.
`src/styles.css` (append):

```css
.jar-search { width: 100%; padding: 9px 12px; font: inherit; }
.jar-types { display: flex; flex-wrap: wrap; gap: 4px 14px; border: 0; padding: 8px 0; margin: 0; }
.jar-releases { display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap; }
.jar-releases button.active { font-weight: 600; }
.jar-list { margin-top: 10px; }
.jar-hit { display: flex; flex-wrap: wrap; gap: 4px 10px; align-items: baseline; width: 100%;
  text-align: left; background: none; border: 0; border-bottom: 1px solid var(--line, #ddd); padding: 6px 4px;
  cursor: pointer; font: inherit; color: inherit; }
.jar-hit[aria-current='true'] { background: var(--accent-soft, #e3eef6); }
.jar-name { font-family: ui-monospace, Consolas, monospace; font-size: 0.85em; }
.jar-badge { font-size: 0.75em; padding: 1px 6px; border-radius: 8px; border: 1px solid currentColor; }
.jar-badge.moved { color: #b26a00; } .jar-badge.onlyA, .jar-badge.onlyB { color: #8a3ffc; }
.jar-detail table { border-collapse: collapse; margin: 8px 0; }
.jar-detail th { text-align: left; padding: 4px 12px 4px 0; vertical-align: top; }
.jar-detail .jar-name + .jar-name { margin-left: 8px; }
.jar-methods { font-size: 0.9em; padding-left: 18px; }
.link-button { background: none; border: 0; padding: 0; color: var(--accent, #1f5f8b);
  text-decoration: underline; cursor: pointer; font-family: ui-monospace, Consolas, monospace; }
```
Before appending, check `src/styles.css` for the variable names actually used for line/accent colours (`grep -n "^\s*--" src/styles.css | head -30`) and use those names.

README: add a tool-table row — `| **JAR Viewer** | Finds the JAR and package of any T24 Java class (R23/R25): load a published class index or your own classes.json, search a class, package or JAR, follow superclasses, see public methods of hook and API classes, and which classes moved JAR between releases. |` and add `?tool=jar` to the deep-link list.

- [ ] **Step 6: Verify and commit**

Run: `npm run check` → pass. Run: `npm run test:e2e -- tests/e2e/jar.spec.js` → 4 passed.

```bash
git add src tests README.md
git commit -m "feat(jar): JAR Viewer tab — class -> JAR search for R23/R25"
```

### Task 8: Markdown Viewer tab

**Files:**
- Create: `src/lib/markdown.js`, `src/lib/markdown.test.js`, `src/services/diagram.js`, `src/features/markdownViewer/MarkdownViewer.jsx`, `tests/e2e/markdown.spec.js`
- Modify: `package.json` (+lock), `src/navigation.js`, `src/navigation.test.js`, `src/App.jsx`, `src/styles.css`, `README.md`

**Interfaces:**
- Produces: `renderMarkdown(value: string) -> string` (sanitised HTML), `renderMermaidBlocks(root: Element) -> Promise<void>`, `export function MarkdownViewer()`.
- Consumes: `escapeHtml` — T24Tools' `src/lib/text.js` has no `escapeHtml`; add it there (copy from RepoMind, below).

- [ ] **Step 1: Dependencies**

Run: `npm install --save-exact marked@18.0.14 dompurify@3.4.15 mermaid@12.0.0 && npm install --save-exact --save-dev jsdom@30.1.1`

- [ ] **Step 2: Failing tests** — `src/lib/markdown.test.js`

```js
// @vitest-environment jsdom
import { describe, expect, it } from 'vitest';
import { renderMarkdown } from './markdown';

describe('renderMarkdown', () => {
  it('keeps code blocks as text and marks mermaid blocks', () => {
    const html = renderMarkdown('```js\n<b>x</b>\n```\n\n```mermaid\ngraph TD; A-->B\n```');
    expect(html).toContain('&lt;b&gt;x&lt;/b&gt;');
    expect(html).toContain('class="mermaid"');
  });
  it('renders GFM tables and nested lists with code', () => {
    const html = renderMarkdown('| a | b |\n|---|---|\n| 1 | 2 |\n\n1. step\n   ```\n   run\n   ```');
    expect(html).toContain('<table>');
    expect(html).toMatch(/<li>[\s\S]*<pre><code/);
  });
  it('strips scripts and event handlers', () => {
    const html = renderMarkdown('<script>alert(1)</script><img src="x" onerror="alert(2)">\n\nok');
    expect(html).not.toContain('<script');
    expect(html).not.toContain('onerror');
    expect(html).toContain('ok');
  });
});
```

Run: `npm test -- src/lib/markdown.test.js` → FAIL (cannot resolve `./markdown`).

- [ ] **Step 3: Implement.** Append to `src/lib/text.js`:

```js
export function escapeHtml(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
```
(Before adding, compare with RepoMind's `src/lib/text.js:42-50` and copy its exact body.)

`src/lib/markdown.js`:

```js
// Markdown → safe HTML, as RepoMind's Markdown viewer does it: marked parses, DOMPurify sanitises,
// ```mermaid fences become <div class="mermaid"> for renderMermaidBlocks (services/diagram.js).
import { marked } from 'marked';
import DOMPurify from 'dompurify';
import { escapeHtml } from './text';

export function renderMarkdown(value) {
  const renderer = new marked.Renderer();
  renderer.code = function ({ text, lang }) {
    if (lang && lang.toLowerCase() === 'mermaid')
      return '<div class="mermaid">' + escapeHtml(text) + '</div>';
    return (
      '<pre><code class="language-' +
      escapeHtml(lang || '') +
      '">' +
      escapeHtml(text) +
      '</code></pre>'
    );
  };
  return DOMPurify.sanitize(marked.parse(value || '', { renderer, gfm: true }), {
    ADD_TAGS: ['div'],
    ADD_ATTR: ['class'],
  });
}
```

`src/services/diagram.js`:

```js
// Mermaid is bundled from npm and loaded on first use, so it adds nothing to the initial page load
// and never reaches out to a CDN (the CSP allows only this site).
import { STALE_BUILD_MESSAGE, isStaleBuildError } from '../lib/staleBuild';

let mermaidPromise = null;

export function loadMermaid() {
  if (!mermaidPromise) {
    mermaidPromise = import('mermaid')
      .then(({ default: mermaid }) => {
        mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: 'default' });
        return mermaid;
      })
      .catch((error) => {
        mermaidPromise = null;
        throw new Error(
          isStaleBuildError(error)
            ? STALE_BUILD_MESSAGE
            : 'Unable to load the Mermaid renderer: ' + error.message,
        );
      });
  }
  return mermaidPromise;
}

/** Renders every `.mermaid` block inside `root` in place; a broken block shows its own error. */
export async function renderMermaidBlocks(root) {
  const nodes = root ? [...root.querySelectorAll('.mermaid:not([data-processed])')] : [];
  if (!nodes.length) return;
  const mermaid = await loadMermaid();
  await mermaid.run({ nodes, suppressErrors: true });
}
```

Run: `npm test -- src/lib/markdown.test.js` → PASS.

- [ ] **Step 4: Navigation.** `src/navigation.test.js`: eight tabs, last `['md', 'Markdown Viewer']`, title `'has exactly the eight T24 tools, in header order'`, add `expect(initialTab('?tool=md')).toBe('md');`. Run → FAIL; add `['md', 'Markdown Viewer'],` to `NAV_TABS` → PASS.

- [ ] **Step 5: Failing E2E** — `tests/e2e/markdown.spec.js`

```js
import { expect, test } from '@playwright/test';

test.describe('Markdown Viewer', () => {
  test('renders pasted markdown, a mermaid diagram, and never runs scripts', async ({ page }) => {
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    page.on('dialog', (d) => errors.push('dialog: ' + d.message()));
    await page.goto('./?tool=md');
    await page
      .getByLabel('Markdown source')
      .fill(
        '# Title\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n```mermaid\ngraph TD; A-->B\n```\n\n```mermaid\nnot a diagram ((\n```\n\n<img src=x onerror="alert(1)">',
      );
    const sheet = page.getByRole('article', { name: 'Rendered markdown' });
    await expect(sheet.getByRole('heading', { name: 'Title' })).toBeVisible();
    await expect(sheet.locator('table')).toBeVisible();
    await expect(sheet.locator('.mermaid svg').first()).toBeVisible({ timeout: 20_000 });
    await expect(page.locator('.md-tab')).toHaveText('pasted.md');
    expect(errors).toEqual([]);
  });

  test('uploaded .md files are listed and switchable', async ({ page }) => {
    await page.goto('./?tool=md');
    await page.locator('input[type=file][aria-label="Markdown file"]').setInputFiles([
      { name: 'one.md', mimeType: 'text/markdown', buffer: Buffer.from('# One') },
      { name: 'two.md', mimeType: 'text/markdown', buffer: Buffer.from('# Two') },
    ]);
    const list = page.getByRole('list', { name: 'Markdown files' });
    await expect(list.getByRole('listitem')).toHaveCount(2);
    await expect(page.getByRole('heading', { name: 'One' })).toBeVisible();
    await list.getByRole('button', { name: /^two\.md/ }).click();
    await expect(page.getByRole('heading', { name: 'Two' })).toBeVisible();
    await expect(page.locator('.md-tab')).toHaveText('two.md');
  });
});
```

Run: `npm run test:e2e -- tests/e2e/markdown.spec.js` → FAIL.

- [ ] **Step 6: Implement `src/features/markdownViewer/MarkdownViewer.jsx`**

```jsx
import { useEffect, useMemo, useRef, useState } from 'react';
import { renderMarkdown } from '../../lib/markdown';
import { renderMermaidBlocks } from '../../services/diagram';

// RepoMind's Markdown viewer (paste, sanitised, mermaid) with MDFV's file upload and manuscript sheet.
export function MarkdownViewer() {
  const fileInput = useRef(null);
  const sheet = useRef(null);
  const seq = useRef(0);
  const [pasted, setPasted] = useState('');
  const [files, setFiles] = useState([]); // [{ id, name, text }] for this session only
  const [active, setActive] = useState(''); // '' = pasted text, else a file id
  const [diagramError, setDiagramError] = useState('');
  const [dragging, setDragging] = useState(false);

  const current = files.find((f) => f.id === active);
  const text = current ? current.text : pasted;
  const html = useMemo(() => renderMarkdown(text), [text]);

  useEffect(() => {
    let live = true;
    renderMermaidBlocks(sheet.current)
      .then(() => live && setDiagramError(''))
      .catch((e) => live && setDiagramError(e.message));
    return () => {
      live = false;
    };
  }, [html]);

  async function add(list) {
    const picked = [...(list || [])];
    if (!picked.length) return;
    const read = await Promise.all(
      picked.map(async (file) => ({ id: `m${++seq.current}`, name: file.name, text: await file.text() })),
    );
    setFiles((cur) => [...cur, ...read]);
    setActive(read[0].id);
  }

  function remove(id) {
    setFiles((cur) => cur.filter((f) => f.id !== id));
    if (id === active) setActive('');
  }

  const drop = {
    onDragOver: (e) => {
      e.preventDefault();
      setDragging(true);
    },
    onDragLeave: () => setDragging(false),
    onDrop: (e) => {
      e.preventDefault();
      setDragging(false);
      add(e.dataTransfer.files);
    },
  };

  return (
    <div className="routine-creator md-viewer-tool">
      <div className="routine-creator-hero">
        <div>
          <span className="eyebrow">Markdown Viewer</span>
          <h1>Read Markdown, including Mermaid diagrams</h1>
          <p className="muted">
            Paste Markdown or open <code>.md</code> files. Everything stays in this browser.
          </p>
        </div>
      </div>

      <section className={`routine-card md-intake${dragging ? ' dragging' : ''}`} aria-label="Input" {...drop}>
        <textarea
          aria-label="Markdown source"
          className="md-input"
          spellCheck={false}
          value={pasted}
          onChange={(e) => {
            setPasted(e.target.value);
            setActive('');
          }}
          placeholder="Paste Markdown here, or drop .md files…"
        />
        <div className="routine-creator-actions">
          <button type="button" className="primary" onClick={() => fileInput.current?.click()}>
            Open .md files…
          </button>
          <button
            type="button"
            onClick={() => {
              setPasted('');
              setActive('');
            }}
          >
            Clear
          </button>
          <input
            ref={fileInput}
            type="file"
            accept=".md,.markdown,text/markdown,text/plain"
            multiple
            hidden
            aria-label="Markdown file"
            onChange={(e) => {
              add(e.target.files);
              e.target.value = '';
            }}
          />
        </div>
        {files.length > 0 && (
          <ul className="json-uploads" aria-label="Markdown files">
            {files.map((f) => (
              <li key={f.id} className={f.id === active ? 'on' : undefined}>
                <button
                  type="button"
                  className="json-upload-open"
                  aria-current={f.id === active ? 'true' : undefined}
                  onClick={() => setActive(f.id)}
                >
                  <b>{f.name}</b>
                </button>
                <button
                  type="button"
                  className="json-upload-remove"
                  aria-label={`Remove ${f.name}`}
                  onClick={() => remove(f.id)}
                >
                  ×
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>

      {diagramError && (
        <p className="routine-validation" role="alert">
          {diagramError}
        </p>
      )}
      {text.trim() && (
        <div className="md-frame">
          <span className="md-tab">{current ? current.name : 'pasted.md'}</span>
          <article
            ref={sheet}
            className="md-sheet"
            aria-label="Rendered markdown"
            dangerouslySetInnerHTML={{ __html: html }}
          />
        </div>
      )}
    </div>
  );
}
```

- [ ] **Step 7: Wire up and style.** `src/App.jsx`: `const MarkdownViewer = named(() => import('./features/markdownViewer/MarkdownViewer'), 'MarkdownViewer');` and `{tab === 'md' && <MarkdownViewer />}`. Append to `src/styles.css` (MDFV sheet; local font stacks — the CSP blocks Google Fonts):

```css
:root { --md-paper: #faf7f0; --md-canvas: #fff; --md-ink: #23211d; --md-soft: #5b5648;
  --md-spine: #445f5a; --md-spine-dark: #324644; --md-line: #dedacd; --md-rust: #a6462e; --md-tab-ink: #faf7f0; }
@media (prefers-color-scheme: dark) { :root:not([data-theme='light']) { --md-paper: #1f1e1b; --md-canvas: #262521;
  --md-ink: #ece8de; --md-soft: #b5ae9e; --md-spine: #7fa59d; --md-spine-dark: #a9cbc3; --md-line: #3a3832;
  --md-rust: #d9805f; --md-tab-ink: #161716; } }
:root[data-theme='dark'] { --md-paper: #1f1e1b; --md-canvas: #262521; --md-ink: #ece8de; --md-soft: #b5ae9e;
  --md-spine: #7fa59d; --md-spine-dark: #a9cbc3; --md-line: #3a3832; --md-rust: #d9805f; --md-tab-ink: #161716; }
.md-input { width: 100%; min-height: 160px; font-family: ui-monospace, Consolas, monospace; font-size: 13px; }
.md-intake.dragging { outline: 2px dashed var(--md-spine); }
.md-frame { position: relative; margin-top: 28px; }
.md-tab { position: absolute; top: -15px; left: 28px; background: var(--md-spine); color: var(--md-tab-ink);
  font: 11px/1 ui-monospace, Consolas, monospace; letter-spacing: .06em; padding: 7px 12px 5px;
  border-radius: 2px 2px 0 0; z-index: 2; }
.md-sheet { background: var(--md-canvas); color: var(--md-ink); border: 1px solid var(--md-line);
  border-top: 3px solid var(--md-spine); border-radius: 2px; padding: 40px 48px;
  font: 17px/1.7 'Iowan Old Style', 'Palatino Linotype', Georgia, serif; overflow-wrap: break-word;
  box-shadow: 0 2px 0 var(--md-line), 0 14px 30px -18px rgba(35,33,29,.25); }
.md-sheet > :first-child { margin-top: 0; }
.md-sheet h1, .md-sheet h2, .md-sheet h3 { font-weight: 600; letter-spacing: -.01em; line-height: 1.3; }
.md-sheet h1 { font-size: 30px; border-bottom: 2px solid var(--md-ink); padding-bottom: 10px; }
.md-sheet h2 { font-size: 23px; margin-top: 2em; }
.md-sheet a { color: var(--md-spine-dark); }
.md-sheet code { font-family: ui-monospace, Consolas, monospace; font-size: .82em; background: var(--md-paper);
  border: 1px solid var(--md-line); border-radius: 2px; padding: 1px 5px; }
.md-sheet pre { background: var(--md-paper); border: 1px solid var(--md-line); border-left: 3px solid var(--md-spine);
  border-radius: 2px; padding: 16px 18px; overflow-x: auto; line-height: 1.5; }
.md-sheet pre code { border: 0; padding: 0; background: none; font-size: 13px; }
.md-sheet blockquote { margin: 1.4em 0; padding: 4px 20px; border-left: 3px solid var(--md-rust);
  color: var(--md-soft); font-style: italic; }
.md-sheet table { border-collapse: collapse; display: block; overflow-x: auto; max-width: 100%;
  font: 14px/1.5 system-ui, sans-serif; }
.md-sheet th, .md-sheet td { border: 1px solid var(--md-line); padding: 8px 12px; }
.md-sheet th { background: var(--md-paper); font: 11px ui-monospace, Consolas, monospace; letter-spacing: .05em;
  text-transform: uppercase; }
.md-sheet img { max-width: 100%; }
.md-sheet hr { border: 0; border-top: 1px solid var(--md-line); margin: 2.2em 0; }
.md-sheet .mermaid { text-align: center; margin: 1.2em 0; }
@media (max-width: 800px) { .md-sheet { padding: 28px 18px; font-size: 16px; } .md-tab { left: 14px; } }
```

README: tool-table row `| **Markdown Viewer** | Paste Markdown or open .md files and read them rendered: tables, code, nested lists and Mermaid diagrams. Scripts in the Markdown never run, and files stay in this browser. |`, and `?tool=md` in the deep-link list.

- [ ] **Step 8: Verify and commit**

Run: `npm run check` → pass. Run: `npm run test:e2e` (full suite) → all pass. Check the build output for a separate mermaid chunk: `ls dist/assets | grep -i mermaid` shows it is not in the main `index-*.js`.

```bash
git add package.json package-lock.json src tests README.md
git commit -m "feat(md): Markdown Viewer tab — marked + DOMPurify, lazy Mermaid, MDFV sheet"
```

### Task 9: Browser verification and CHANGELOG

**Files:**
- Modify: `CHANGELOG.md` (T24Tools)

- [ ] **Step 1:** `npm run build && npm run preview` (port 4791). In a browser at `http://127.0.0.1:4791/T24Tools/`: header shows no download links; tabs read Application Viewer / JAR Viewer / Markdown Viewer; JAR Viewer → Load R23 and R25 → search `RecordLifecycle` → `EB_TemplateHook.jar`, superclass link opens `T24Context`, release badge shows; Markdown Viewer renders a paste with a mermaid block in light and dark theme. No console errors.
- [ ] **Step 2:** Add a CHANGELOG entry at the top in the file's existing style: Application Viewer rename, JAR Viewer, Markdown Viewer, header download links removed, classes.json published.
- [ ] **Step 3:** Commit `docs: changelog for JAR Viewer and Markdown Viewer`. Do not push — ask the developer first.
