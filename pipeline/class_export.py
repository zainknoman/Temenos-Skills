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
