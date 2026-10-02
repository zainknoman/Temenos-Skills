#!/usr/bin/env python3
"""Extract componentised field names from the T24 component classes in the JARs.

Each jBC component compiles to com/temenos/t24/component_<Mod>_<Name>_<n>_cl.class,
which declares one `public static int _<Table>_<Field>` per table field and
assigns its field position in <clinit>, e.g.

    _Customer_EbCusMnemonic = 1     ->  ST.Customer.Customer.EbCusMnemonic
    _Account_Category       = 2     ->  AC.AccountOpening.Account.Category

Joining (app, position) to the Layer A `fields` table gives the exact EQU name
(EB.CUS.MNEMONIC, AC.CATEGORY) -- no name guessing. Verified against R25 on
2026-10-02: componentised names are NOT the java alias (Customer_Mnemonic).

  python pipeline/component_parse.py --jars jar --db temenos_knowledge.db
"""
import argparse
import re
import sqlite3
import struct
import zipfile
from pathlib import Path

from artefact_fields import dotted_prefix, record_class

CLASS_RE = re.compile(r"(?:^|/)component_([A-Za-z0-9]+)_([A-Za-z0-9]+)_\d+_cl\.class$")

# JVM instruction lengths (opcode + operands) for the fixed-size opcodes that
# are not 1 byte long; tableswitch (0xaa), lookupswitch (0xab) and wide (0xc4)
# are variable and handled in _walk.
_LEN = {0x10: 2, 0x11: 3, 0x12: 2, 0x13: 3, 0x14: 3, 0xa9: 2, 0xbc: 2, 0x84: 3,
        0xb9: 5, 0xba: 5, 0xc5: 4, 0xc8: 5, 0xc9: 5}
_LEN.update({op: 2 for op in range(0x15, 0x1a)})        # iload..aload <idx>
_LEN.update({op: 2 for op in range(0x36, 0x3b)})        # istore..astore <idx>
_LEN.update({op: 3 for op in range(0x99, 0xa9)})        # if*/goto/jsr
_LEN.update({op: 3 for op in range(0xb2, 0xb9)})        # get/putfield/static, invoke*
_LEN.update({op: 3 for op in (0xbb, 0xbd, 0xc0, 0xc1, 0xc6, 0xc7)})


def component_name(class_path):
    m = CLASS_RE.search(class_path)
    return f"{m.group(1)}.{m.group(2)}" if m else None


def split_constant(name):
    """'_Customer_EbCusMnemonic' -> ('Customer', 'EbCusMnemonic'); None if not _<T>_<F>."""
    parts = name[1:].split("_", 1) if name.startswith("_") else []
    return (parts[0], parts[1]) if len(parts) == 2 and all(parts) else None


def _constant_pool(data):
    count = struct.unpack_from(">H", data, 8)[0]
    pool, i, off = [None] * count, 1, 10
    while i < count:
        tag = data[off]
        if tag == 1:
            n = struct.unpack_from(">H", data, off + 1)[0]
            pool[i] = ("utf8", data[off + 3:off + 3 + n].decode("utf-8", "replace"))
            off += 3 + n
        elif tag == 3:
            pool[i] = ("int", struct.unpack_from(">i", data, off + 1)[0])
            off += 5
        elif tag == 4:
            off += 5
        elif tag in (5, 6):
            off += 9
            i += 1  # 8-byte constants take two slots
        elif tag in (7, 8, 16, 19, 20):
            pool[i] = (tag, struct.unpack_from(">H", data, off + 1)[0])
            off += 3
        elif tag in (9, 10, 11, 12, 17, 18):
            pool[i] = (tag,) + struct.unpack_from(">HH", data, off + 1)
            off += 5
        elif tag == 15:
            off += 4
        else:
            raise ValueError(f"unknown constant pool tag {tag} at {off}")
        i += 1
    return pool, off


def _skip_members(data, off):
    count = struct.unpack_from(">H", data, off)[0]
    off += 2
    for _ in range(count):
        off += 6
        attrs = struct.unpack_from(">H", data, off)[0]
        off += 2
        for _ in range(attrs):
            off += 6 + struct.unpack_from(">I", data, off + 2)[0]
    return off


def _walk(code, pool):
    """Yield (field_name, int) for every `<int push>; putstatic <field>` pair."""
    pc, last_int = 0, None
    while pc < len(code):
        op = code[pc]
        if 0x02 <= op <= 0x08:                       # iconst_m1..iconst_5
            last_int, size = op - 0x03, 1
        elif op == 0x10:                             # bipush
            last_int, size = struct.unpack_from(">b", code, pc + 1)[0], 2
        elif op == 0x11:                             # sipush
            last_int, size = struct.unpack_from(">h", code, pc + 1)[0], 3
        elif op in (0x12, 0x13):                     # ldc / ldc_w
            idx = code[pc + 1] if op == 0x12 else struct.unpack_from(">H", code, pc + 1)[0]
            entry = pool[idx]
            last_int = entry[1] if entry and entry[0] == "int" else None
            size = 2 if op == 0x12 else 3
        elif op == 0xb3:                             # putstatic
            if last_int is not None:
                _, _, nat = pool[struct.unpack_from(">H", code, pc + 1)[0]]
                yield pool[pool[nat][1]][1], last_int
            last_int, size = None, 3
        elif op == 0xaa:                             # tableswitch
            base = pc + 1 + (-(pc + 1) % 4)
            low, high = struct.unpack_from(">ii", code, base + 4)
            last_int, size = None, base + 12 + 4 * (high - low + 1) - pc
        elif op == 0xab:                             # lookupswitch
            base = pc + 1 + (-(pc + 1) % 4)
            npairs = struct.unpack_from(">i", code, base + 4)[0]
            last_int, size = None, base + 8 + 8 * npairs - pc
        elif op == 0xc4:                             # wide
            last_int, size = None, 6 if code[pc + 1] == 0x84 else 4
        else:
            last_int, size = None, _LEN.get(op, 1)
        pc += size


def parse_static_ints(data):
    """{static field name: int} assigned by constant in the class's <clinit>."""
    pool, off = _constant_pool(data)
    off += 6
    off += 2 + 2 * struct.unpack_from(">H", data, off)[0]  # interfaces
    off = _skip_members(data, off)                          # fields
    values = {}
    methods = struct.unpack_from(">H", data, off)[0]
    off += 2
    for _ in range(methods):
        name = pool[struct.unpack_from(">H", data, off + 2)[0]][1]
        attrs = struct.unpack_from(">H", data, off + 6)[0]
        off += 8
        for _ in range(attrs):
            attr_name = pool[struct.unpack_from(">H", data, off)[0]][1]
            length = struct.unpack_from(">I", data, off + 2)[0]
            if name == "<clinit>" and attr_name == "Code":
                code_len = struct.unpack_from(">I", data, off + 10)[0]
                values.update(_walk(data[off + 14:off + 14 + code_len], pool))
            off += 6 + length
    return values


_NUMBER_WORDS = {w: str(i) for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen twenty".split())}


def _camel_tokens(name):
    tokens = re.findall(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+|[0-9]+", name)
    return [_NUMBER_WORDS.get(t.lower(), t.lower()) for t in tokens]


def _equ_tokens(name):
    return [t.lower() for t in name.split(".") if t]


def names_match(comp_field, field_name, prefix):
    """True if the componentised name spells the EQU name, with or without the
    app prefix: EbCusMnemonic ~ EB.CUS.MNEMONIC, Category ~ AC.CATEGORY,
    EbCusNameOne ~ EB.CUS.NAME.1. Rejects another component's same-named table
    at the same position (CusActivity vs EB.CUS.MNEMONIC)."""
    camel = "".join(_camel_tokens(comp_field))
    full = "".join(_equ_tokens(field_name))
    short = "".join(_equ_tokens(field_name[len(prefix):])) if prefix and field_name.startswith(prefix) else None
    return camel == full or (short is not None and camel == short)


SCHEMA = """CREATE TABLE IF NOT EXISTS component_fields (
    release TEXT, app TEXT, component TEXT, record TEXT, comp_field TEXT,
    position INTEGER, field_name TEXT)"""


def iter_component_classes(jars_dir):
    """Yield (component name, class bytes) for every component class in every JAR."""
    for jar in sorted(Path(jars_dir).glob("*.jar")):
        try:
            with zipfile.ZipFile(jar) as z:
                for entry in z.namelist():
                    comp = component_name(entry)
                    if comp:
                        yield comp, z.read(entry)
        except zipfile.BadZipFile:
            continue


def build_component_fields(conn, jars_dir, release):
    """Rebuild component_fields for one release: every _<Record>_<Field> = <pos>
    constant whose <Record> is an app's record class and whose position has a
    row in `fields` (the same release's Layer A schema)."""
    by_record = {}
    for (app,) in conn.execute("SELECT DISTINCT app FROM fields"):
        by_record.setdefault(record_class(app), []).append(app)
    names = {(a, p): f for a, p, f in conn.execute("SELECT app, position, field_name FROM fields")}
    prefixes = {}
    for a, f in conn.execute("SELECT app, field_name FROM fields"):
        prefixes.setdefault(a, []).append(f)
    prefixes = {a: dotted_prefix(fs) for a, fs in prefixes.items()}

    conn.execute(SCHEMA)
    conn.execute("DELETE FROM component_fields WHERE release = ?", (release,))
    rows, stats = set(), {"classes": 0, "constants": 0, "joined": 0, "unjoined": 0}
    for comp, data in iter_component_classes(jars_dir):
        stats["classes"] += 1
        for const, pos in parse_static_ints(data).items():
            split = split_constant(const)
            if not split:
                continue
            stats["constants"] += 1
            record, field = split
            apps = by_record.get(record, [])
            hits = [(a, names[(a, pos)]) for a in apps
                    if (a, pos) in names and names_match(field, names[(a, pos)], prefixes[a])]
            if len(hits) == 1:
                rows.add((release, hits[0][0], comp, record, field, pos, hits[0][1]))
            else:
                stats["unjoined"] += 1
    conn.executemany("INSERT INTO component_fields VALUES (?,?,?,?,?,?,?)", sorted(rows))
    conn.execute("CREATE INDEX IF NOT EXISTS ix_component_fields ON component_fields (release, app)")
    conn.commit()
    stats["joined"] = len(rows)
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jars", default="jar")
    ap.add_argument("--db", default="temenos_knowledge.db")
    ap.add_argument("--release", required=True, help="release of --jars AND of the fields table, e.g. R23")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    stats = build_component_fields(conn, args.jars, args.release)
    conn.close()
    print(f"{args.release}: {stats['classes']} component classes, {stats['constants']} table constants, "
          f"{stats['joined']} joined to fields, {stats['unjoined']} not joined")


if __name__ == "__main__":
    main()
