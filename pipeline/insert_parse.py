#!/usr/bin/env python3
"""Extract T24 table field schemas from INSERTS/I_F.<APP> entries inside the JARs.

Each JAR may contain INSERTS/I_F.<APP.NAME> files: jBASE copybook-style EQU blocks
mapping a T24 field name and a Java field alias to a shared file position, e.g.

    EQU AA.AC.ACTIVITY TO 1,   AaSimAccount_Activity TO 1,

This is Layer A ground truth for field names (never invent a field name).
Multivalue status is NOT in this file -- cross-reference against
com/temenos/t24/api/records/<app>/ (see "Identifying Multivalue Core Fields
from JAR Structure" in skills/temenos-dev/SKILL.md) for that.

Output:
  - temenos_knowledge.db: table `fields(app, field_name, position, java_alias, source_jar)`
  - skills/temenos-dev/references/table-schema/<APP>.md: one file per T24 application
"""
import argparse
import re
import sqlite3
import zipfile
from pathlib import Path

INSERT_NAME_RE = re.compile(r"^INSERTS/I_F\.(.+)$")
EQU_TOKEN_RE = re.compile(r"([A-Za-z0-9_.]+)\s+TO\s+(\d+)")


def parse_insert_body(text: str):
    """Return list of (field_name, position, java_alias) from an I_F.* body."""
    tokens = EQU_TOKEN_RE.findall(text)
    pairs = []
    i = 0
    while i + 1 < len(tokens):
        (field_name, pos1), (java_alias, pos2) = tokens[i], tokens[i + 1]
        if pos1 == pos2:
            pairs.append((field_name, int(pos1), java_alias))
            i += 2
        else:
            # unexpected shape -- skip one token and resync
            i += 1
    return pairs


def scan_jars(jar_dir: Path):
    """Yield (app, field_name, position, java_alias, source_jar) for every I_F.* found."""
    for jar_path in sorted(jar_dir.glob("*.jar")):
        try:
            with zipfile.ZipFile(jar_path) as zf:
                names = [n for n in zf.namelist() if INSERT_NAME_RE.match(n)]
                for name in names:
                    app = INSERT_NAME_RE.match(name).group(1)
                    try:
                        text = zf.read(name).decode("utf-8", errors="replace")
                    except (KeyError, zipfile.BadZipFile):
                        continue
                    for field_name, position, java_alias in parse_insert_body(text):
                        yield app, field_name, position, java_alias, jar_path.name
        except zipfile.BadZipFile:
            continue


def write_db(db_path: Path, rows):
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS fields (
            app         TEXT NOT NULL,
            field_name  TEXT NOT NULL,
            position    INTEGER NOT NULL,
            java_alias  TEXT,
            source_jar  TEXT NOT NULL,
            PRIMARY KEY (app, field_name)
        )
    """)
    conn.execute("DELETE FROM fields")
    conn.executemany(
        "INSERT OR IGNORE INTO fields (app, field_name, position, java_alias, source_jar) "
        "VALUES (?, ?, ?, ?, ?)",
        [(app, fn, pos, alias, jar) for app, fn, pos, alias, jar in rows],
    )
    conn.commit()
    conn.close()


def write_markdown(out_dir: Path, by_app: dict):
    out_dir.mkdir(parents=True, exist_ok=True)
    for app, entries in sorted(by_app.items()):
        entries = sorted(entries, key=lambda e: e[0])  # by position
        source_jar = entries[0][3]
        lines = [
            f"# {app} — Table Schema",
            "",
            f"> Source: `INSERTS/I_F.{app}` in `{source_jar}` (extracted by `pipeline/insert_parse.py`).",
            "> Multivalue status is NOT captured here — cross-check "
            "`com/temenos/t24/api/records/` per the MV-field-detection rule in "
            "`skills/temenos-dev/SKILL.md` before treating any field as single-value.",
            "",
            "| Position | Field Name | Java Alias |",
            "|----------|------------|------------|",
        ]
        for position, field_name, java_alias, _jar in entries:
            lines.append(f"| {position} | `{field_name}` | `{java_alias}` |")
        (out_dir / f"{app}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jars", default="jar")
    ap.add_argument("--db", default="temenos_knowledge.db")
    ap.add_argument("--out", default="skills/temenos-dev/references/table-schema")
    args = ap.parse_args()

    jar_dir = Path(args.jars)
    rows = list(scan_jars(jar_dir))
    print(f"Parsed {len(rows)} field entries from INSERTS/I_F.* across {jar_dir}")

    by_app = {}
    for app, field_name, position, java_alias, source_jar in rows:
        by_app.setdefault(app, []).append((position, field_name, java_alias, source_jar))

    print(f"Covering {len(by_app)} T24 applications/tables")

    write_db(Path(args.db), rows)
    write_markdown(Path(args.out), by_app)
    print(f"Wrote {args.db} (table `fields`) and {len(by_app)} files under {args.out}/")


if __name__ == "__main__":
    main()
