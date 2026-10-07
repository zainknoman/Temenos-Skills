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
field_name, kind, getter_class, group_getter).

How Java reaches a multi-value field (`group_getter`, read from the record class's methods, never
guessed from a class name -- AltIdTypeClass is returned by getAltAcctType):

  MV, list of TField:  rec.get<Suffix>(int) returns TField and rec.set<Suffix>(CharSequence, int)
                       exists                                         -> group_getter ''
  MV, list of a group (the group's first field, e.g. EB.CUS.RELATION.CODE):
                       rec.get<Suffix>(int) returns <Group>Class, which has get<Suffix>() -> TField
                                                                      -> MV-GROUP, group_getter <Suffix>
  MV-GROUP member:     a record method get<G>(int) returns the member's group class, the record
                       has set<G>(<Group>Class, int), and the member's getter returns TField
                                                                      -> group_getter <G>
Anything else -- a group nested in a group, a member holding sub-values -- keeps group_getter
NULL: the generators treat it as not reachable from a one-field template.

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
    release TEXT, app TEXT, field_name TEXT, kind TEXT, getter_class TEXT, group_getter TEXT)"""
TFIELD = "Lcom/temenos/api/TField;"
LIST = "Ljava/util/List;"


def class_methods(data):
    """{method name: {descriptor, ...}} for every method of a class."""
    pool, off = _constant_pool(data)
    off += 6
    off += 2 + 2 * struct.unpack_from(">H", data, off)[0]  # interfaces
    off = _skip_members(data, off)                          # fields
    methods = defaultdict(set)
    count = struct.unpack_from(">H", data, off)[0]
    off += 2
    for _ in range(count):
        name = pool[struct.unpack_from(">H", data, off + 2)[0]][1]
        desc = pool[struct.unpack_from(">H", data, off + 4)[0]][1]
        attrs = struct.unpack_from(">H", data, off + 6)[0]
        off += 8
        for _ in range(attrs):
            off += 6 + struct.unpack_from(">I", data, off + 2)[0]
        methods[name].add(desc)
    return dict(methods)


def no_arg_getters(data):
    """{method name: return descriptor} for every no-argument get* method of a class."""
    getters = {}
    for name, descs in class_methods(data).items():
        for desc in descs:
            if name.startswith("get") and desc.startswith("()"):
                getters[name] = desc[2:]
    return getters


def index_record_classes(jars_dir):
    """{package: {class name: {method: {descriptor, ...}}}} across every JAR."""
    index = defaultdict(dict)
    for jar in sorted(Path(jars_dir).glob("*.jar")):
        try:
            with zipfile.ZipFile(jar) as z:
                for entry in z.namelist():
                    m = RECORD_ENTRY.match(entry)
                    if m and "$" not in m.group(2):
                        index[m.group(1)][m.group(2)] = class_methods(z.read(entry))
        except (zipfile.BadZipFile, ValueError, IndexError, struct.error):
            continue
    return index


def _no_arg_return(methods, getter):
    for desc in methods.get(getter, ()):
        if desc.startswith("()"):
            return desc[2:]
    return None


def _indexed_return(methods, getter):
    """Return descriptor of get<X>(int), or None."""
    for desc in methods.get(getter, ()):
        if desc.startswith("(I)"):
            return desc[3:]
    return None


def _group_accessor(package, classes, record, group_class):
    """The record method suffix <G> with get<G>(int) -> group_class and set<G>(group_class, int)."""
    target = f"Lcom/temenos/t24/api/records/{package}/{group_class};"
    methods = classes.get(record, {})
    for name, descs in sorted(methods.items()):
        if name.startswith("get") and f"(I){target}" in descs:
            suffix = name[3:]
            if f"({target}I)V" in methods.get(f"set{suffix}", ()):
                return suffix
    return None


def classify(index, java_alias, package_hint=None):
    """(kind, getter class, group getter) for one java alias, or None if no getter exists.

    group getter: '' for a list of TField reached as get<Suffix>(int); the record-level group
    accessor for a group member; None when Java cannot reach it in one indexed step."""
    if not java_alias or "_" not in java_alias:
        return None
    prefix, suffix = java_alias.split("_", 1)
    package = package_hint or prefix.lower()
    classes = index.get(package, {})
    getter = f"get{suffix}"
    record = f"{prefix}Record"
    rec_methods = classes.get(record, {})
    ret = _no_arg_return(rec_methods, getter)
    if ret is not None:
        if ret != LIST:
            return "SV", record, ""
        item = _indexed_return(rec_methods, getter)
        if item == TFIELD and f"(Ljava/lang/CharSequence;I)V" in rec_methods.get(f"set{suffix}", ()):
            return "MV", record, ""
        group = re.fullmatch(r"Lcom/temenos/t24/api/records/[a-z0-9]+/(\w+);", item or "")
        if group and _no_arg_return(classes.get(group.group(1), {}), getter) == TFIELD:
            # The group's first field: the record list holds the group class, not TField.
            return "MV-GROUP", group.group(1), _group_accessor(package, classes, record, group.group(1))
        return "MV", record, None
    for cls, methods in sorted(classes.items()):
        if cls != record and _no_arg_return(methods, getter) is not None:
            member_ok = _no_arg_return(methods, getter) == TFIELD
            accessor = _group_accessor(package, classes, record, cls) if member_ok else None
            return "MV-GROUP", cls, accessor
    return None


def _ensure_schema(conn):
    conn.execute(SCHEMA)
    columns = {row[1] for row in conn.execute("PRAGMA table_info(field_kinds)")}
    if "group_getter" not in columns:
        conn.execute("ALTER TABLE field_kinds ADD COLUMN group_getter TEXT")


def build_field_kinds(conn, jars_dir, release):
    index = index_record_classes(jars_dir)
    _ensure_schema(conn)
    conn.execute("DELETE FROM field_kinds WHERE release = ?", (release,))
    rows, stats = [], defaultdict(int)
    for app, field_name, alias in conn.execute("SELECT app, field_name, java_alias FROM fields").fetchall():
        hit = classify(index, alias)
        if hit is None:
            stats["unknown"] += 1
            continue
        stats[hit[0]] += 1
        if hit[0] != "SV":
            stats[f"{hit[0]} reachable" if hit[2] is not None else f"{hit[0]} not reachable"] += 1
        rows.append((release, app, field_name, *hit))
    conn.executemany("INSERT INTO field_kinds VALUES (?,?,?,?,?,?)", rows)
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
