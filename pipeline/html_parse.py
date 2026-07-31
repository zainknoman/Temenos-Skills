#!/usr/bin/env python3
"""Enrich T24 field schemas with type/mandatory/description from JavaDoc HTML.

Walks com/temenos/t24/api/records/**/*Record.html and extracts each getter's
javadoc block. Every getter is matched to `fields.java_alias` (set by
insert_parse.py, format "<ClassName>_<Suffix>") -- this is an exact key match,
not a fuzzy one, since the HTML file stem (minus "Record") is the ClassName
and the getter name (minus "get") is the Suffix. Layer A enrichment
(Phase 1c) -- see CLAUDE.md.

Output:
  - temenos_knowledge.db: adds field_type/mandatory/description columns to `fields`
  - skills/temenos-dev/references/table-schema/<APP>.md: regenerated with enrichment columns
"""
import argparse
import re
import sqlite3
from pathlib import Path

GETTER_RE = re.compile(
    r'<a name="get([A-Za-z0-9]+)--">.*?'
    r'<div class="signature">public&nbsp;([\w.\[\]]+)&nbsp;get\1\(\)</div>'
    r'<div class="block">(.*?)</div><dl>',
    re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
T24_TYPE_RE = re.compile(r"type\s+([A-Z])\s*\(([a-z]+)\)", re.IGNORECASE)


def clean_text(raw: str) -> str:
    text = TAG_RE.sub(" ", raw)
    text = WS_RE.sub(" ", text).strip()
    text = re.sub(r"^Returns the \w+\s*", "", text)
    return text.replace("Field description:", "").strip()


def infer_mandatory(text: str) -> str:
    lower = text.lower()
    has_mandatory = "mandatory" in lower
    has_optional = "optional" in lower
    if has_mandatory and not has_optional:
        return "Yes"
    if has_optional and not has_mandatory:
        return "No"
    if has_mandatory and has_optional:
        return "Conditional"
    return ""


def infer_type(text: str, java_type: str) -> str:
    m = T24_TYPE_RE.search(text)
    if m:
        return f"{m.group(1).upper()} ({m.group(2)})"
    return java_type


def parse_record_html(html_path: Path, class_name: str):
    text = html_path.read_text(encoding="utf-8", errors="replace")
    for m in GETTER_RE.finditer(text):
        suffix, java_type, block = m.group(1), m.group(2), m.group(3)
        description = clean_text(block)
        yield (
            infer_type(description, java_type),
            infer_mandatory(description),
            description,
            f"{class_name}_{suffix}",
        )


def scan_html(html_dir: Path):
    records_dir = html_dir / "com" / "temenos" / "t24" / "api" / "records"
    for record_file in sorted(records_dir.rglob("*Record.html")):
        stem = record_file.stem
        class_name = stem[: -len("Record")] if stem.endswith("Record") else stem
        yield from parse_record_html(record_file, class_name)


def ensure_columns(conn: sqlite3.Connection):
    cols = {r[1] for r in conn.execute("PRAGMA table_info(fields)")}
    for col in ("field_type", "mandatory", "description"):
        if col not in cols:
            conn.execute(f"ALTER TABLE fields ADD COLUMN {col} TEXT")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_fields_java_alias ON fields(java_alias)")
    conn.commit()


def apply_enrichment(conn: sqlite3.Connection, rows):
    updated = conn.executemany(
        "UPDATE fields SET field_type=?, mandatory=?, description=? WHERE java_alias=?",
        rows,
    ).rowcount
    conn.commit()
    return updated


def write_markdown(conn: sqlite3.Connection, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    apps = [r[0] for r in conn.execute("SELECT DISTINCT app FROM fields ORDER BY app")]
    for app in apps:
        rows = conn.execute(
            "SELECT position, field_name, java_alias, field_type, mandatory, description "
            "FROM fields WHERE app=? ORDER BY position",
            (app,),
        ).fetchall()
        source_jar = conn.execute(
            "SELECT source_jar FROM fields WHERE app=? LIMIT 1", (app,)
        ).fetchone()[0]
        lines = [
            f"# {app} — Table Schema",
            "",
            f"> Source: `INSERTS/I_F.{app}` in `{source_jar}` (positions/aliases via "
            "`pipeline/insert_parse.py`); type/mandatory/description via "
            "`pipeline/html_parse.py` from JavaDoc HTML.",
            "> Multivalue status is NOT captured here — cross-check "
            "`com/temenos/t24/api/records/` per the MV-field-detection rule in "
            "`skills/temenos-dev/SKILL.md` before treating any field as single-value.",
            "> Type/mandatory are inferred from JavaDoc free text and may be blank "
            "where the HTML gave no clear signal — do not treat a blank as \"optional\".",
            "",
            "| Position | Field Name | Java Alias | Type | Mandatory | Description |",
            "|----------|------------|------------|------|-----------|--------------|",
        ]
        for position, field_name, java_alias, field_type, mandatory, description in rows:
            desc = (description or "").replace("|", "\\|")
            lines.append(
                f"| {position} | `{field_name}` | `{java_alias}` | {field_type or ''} "
                f"| {mandatory or ''} | {desc} |"
            )
        (out_dir / f"{app}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(apps)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", default="T24.javadoc/T24.javadoc")
    ap.add_argument("--db", default="temenos_knowledge.db")
    ap.add_argument("--out", default="skills/temenos-dev/references/table-schema")
    args = ap.parse_args()

    rows = list(scan_html(Path(args.html)))
    print(f"Parsed {len(rows)} getter javadoc blocks from {args.html}")

    conn = sqlite3.connect(args.db)
    ensure_columns(conn)
    updated = apply_enrichment(conn, rows)
    print(f"Updated {updated} field rows with type/mandatory/description")

    app_count = write_markdown(conn, Path(args.out))
    print(f"Regenerated {app_count} files under {args.out}/")
    conn.close()


if __name__ == "__main__":
    main()
