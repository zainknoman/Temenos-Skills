#!/usr/bin/env python3
"""Single- vs multi-value flag for every field, read from the T24 record classes.

Each application's Java API is com/temenos/t24/api/records/<pkg>/<Rec>Record.class.
For a field with java alias <Rec>_<Suffix>:

  <Rec>Record.get<Suffix>() returns TField        -> SV        (single value)
  <Rec>Record.get<Suffix>() returns java.util.List -> MV        (multi value)
  no getter on the record, but on a group class
  in the same package (e.g. IcaMainAcctClass)      -> MV-GROUP  (member of a multi-value group)
  no getter anywhere                               -> not stored (unknown)

This is what a template calling rec.get<Field>().getValue() needs to know: that
only works for SV fields. Results go to table field_kinds(release, app,
field_name, kind, getter_class).

  python pipeline/record_parse.py --jars jar --release R23
"""
import argparse
import re
import struct
import zipfile
from collections import defaultdict
from pathlib import Path

from component_parse import _constant_pool, _skip_members
from releases import add_release_args, connect

RECORD_ENTRY = re.compile(r"^com/temenos/t24/api/records/([a-z0-9]+)/([A-Za-z0-9]+)\.class$")
SCHEMA = """CREATE TABLE IF NOT EXISTS field_kinds (
    release TEXT, app TEXT, field_name TEXT, kind TEXT, getter_class TEXT)"""


def no_arg_getters(data):
    """{method name: return descriptor} for every no-argument get* method of a class."""
    pool, off = _constant_pool(data)
    off += 6
    off += 2 + 2 * struct.unpack_from(">H", data, off)[0]  # interfaces
    off = _skip_members(data, off)                          # fields
    getters = {}
    count = struct.unpack_from(">H", data, off)[0]
    off += 2
    for _ in range(count):
        name = pool[struct.unpack_from(">H", data, off + 2)[0]][1]
        desc = pool[struct.unpack_from(">H", data, off + 4)[0]][1]
        attrs = struct.unpack_from(">H", data, off + 6)[0]
        off += 8
        for _ in range(attrs):
            off += 6 + struct.unpack_from(">I", data, off + 2)[0]
        if name.startswith("get") and desc.startswith("()"):
            getters[name] = desc[2:]
    return getters


def index_record_classes(jars_dir):
    """{package: {class name: {getter: return descriptor}}} across every JAR."""
    index = defaultdict(dict)
    for jar in sorted(Path(jars_dir).glob("*.jar")):
        try:
            with zipfile.ZipFile(jar) as z:
                for entry in z.namelist():
                    m = RECORD_ENTRY.match(entry)
                    if m and "$" not in m.group(2):
                        index[m.group(1)][m.group(2)] = no_arg_getters(z.read(entry))
        except (zipfile.BadZipFile, ValueError, IndexError, struct.error):
            continue
    return index


def classify(index, java_alias):
    """(kind, getter class) for one java alias, or None if no getter exists."""
    if not java_alias or "_" not in java_alias:
        return None
    prefix, suffix = java_alias.split("_", 1)
    classes = index.get(prefix.lower(), {})
    getter = f"get{suffix}"
    record = f"{prefix}Record"
    ret = classes.get(record, {}).get(getter)
    if ret is not None:
        return ("MV" if ret == "Ljava/util/List;" else "SV"), record
    for cls, getters in sorted(classes.items()):
        if cls != record and getter in getters:
            return "MV-GROUP", cls
    return None


def build_field_kinds(conn, jars_dir, release):
    index = index_record_classes(jars_dir)
    conn.execute(SCHEMA)
    conn.execute("DELETE FROM field_kinds WHERE release = ?", (release,))
    rows, stats = [], defaultdict(int)
    for app, field_name, alias in conn.execute("SELECT app, field_name, java_alias FROM fields").fetchall():
        hit = classify(index, alias)
        if hit is None:
            stats["unknown"] += 1
            continue
        stats[hit[0]] += 1
        rows.append((release, app, field_name, hit[0], hit[1]))
    conn.executemany("INSERT INTO field_kinds VALUES (?,?,?,?,?)", rows)
    conn.execute("CREATE INDEX IF NOT EXISTS ix_field_kinds ON field_kinds (release, app)")
    conn.commit()
    stats["record_packages"] = len(index)
    return dict(stats)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jars", required=True, help="the release's JAR folder (read only)")
    add_release_args(ap)
    args = ap.parse_args()
    conn = connect(args)
    stats = build_field_kinds(conn, args.jars, args.release)
    conn.close()
    print(f"{args.release}: " + ", ".join(f"{k} {v:,}" for k, v in sorted(stats.items())))


if __name__ == "__main__":
    main()
