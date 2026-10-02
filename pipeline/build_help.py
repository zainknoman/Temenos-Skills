#!/usr/bin/env python3
"""Build Temenos-Skills-HelpText.html -- a JavaDoc-style, self-contained help
page for the whole repository.

Like RepoMind, it works in two steps: build an *index* (a structured model of
the repo), then render a viewer over it. The index holds:

  overview   README sections
  skills     every skill: SKILL.md frontmatter + every text file under the skill
             (outline of headings + full content), except table-schema/ (4,596
             files, 35 MB) which is summarised as a directory of applications
  templates  the artefact catalogue: language -> type, inputs, template sources,
             golden output, proven status
  golden     the golden cases (requirement, apps, expected fields)
  pipeline   every pipeline/*.py tool with its docstring
  releases   per-release counts read from each built knowledge DB
  schemas    application -> field count (and jBC-name count) per release

The HTML embeds the index as JSON and needs no network: open the file in a
browser. Rebuild after changing skills, templates or pipeline tools.

  python pipeline/build_help.py [--out Temenos-Skills-HelpText.html]
"""
import argparse
import ast
import json
import re
import sqlite3
import warnings
from datetime import datetime, timezone
from pathlib import Path

from artefact_templates import load_templates
from releases import RELEASES, db_path

ROOT = Path(".")
TEXT_SUFFIXES = {".md", ".b", ".component", ".py", ".json", ".txt", ".java", ".yml", ".yaml"}
SKIP_DIRS = {"table-schema", "__pycache__"}
HELP_TEMPLATE = Path(__file__).resolve().parent / "help_template.html"


def frontmatter(text):
    """Minimal YAML frontmatter reader (name/description/version) for SKILL.md."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    meta, key = {}, None
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            meta[key] = "" if val in (">", "|", ">-", "|-") else val.strip('"')
        elif key and line.startswith(" "):
            stripped = line.strip()
            sub = re.match(r"^([A-Za-z_]+):\s*(.*)$", stripped)
            if sub and key == "metadata":
                meta[sub.group(1)] = sub.group(2).strip('"')
            else:
                meta[key] = (meta[key] + " " + stripped).strip()
    return meta, text[m.end():]


def outline(text):
    return [{"level": len(h), "title": t.strip()}
            for h, t in re.findall(r"^(#{1,4})\s+(.+)$", text, re.M)]


def skill_index(skill_dir):
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8", errors="replace") if skill_md.exists() else ""
    meta, _ = frontmatter(text)
    files = []
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if SKIP_DIRS & set(path.relative_to(skill_dir).parts):
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        files.append({
            "path": path.relative_to(skill_dir).as_posix(),
            "kind": path.suffix.lower().lstrip("."),
            "bytes": len(content.encode("utf-8")),
            "lines": content.count("\n") + 1,
            "outline": outline(content) if path.suffix.lower() == ".md" else [],
            "content": content,
        })
    return {
        "id": skill_dir.name,
        "name": meta.get("name", skill_dir.name),
        "description": meta.get("description", ""),
        "version": meta.get("version", ""),
        "hasTableSchema": (skill_dir / "references" / "table-schema").is_dir(),
        "files": files,
    }


def readme_sections():
    readme = ROOT / "README.md"
    if not readme.exists():
        return []
    sections, current = [], {"title": "Introduction", "content": ""}
    for line in readme.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True):
        if line.startswith("## "):
            sections.append(current)
            current = {"title": line[3:].strip(), "content": ""}
        current["content"] += line
    sections.append(current)
    return [s for s in sections if s["content"].strip()]


def template_index():
    templates = {t["id"]: t for t in load_templates()}
    exported = ROOT / "build" / "t24tools" / "templates.json"
    proven, golden_out = {}, {}
    if exported.exists():
        doc = json.loads(exported.read_text(encoding="utf-8"))
        for lang in doc["languages"]:
            for typ in lang["types"]:
                proven[f"{lang['id']}/{typ['id']}"] = typ["proven"]
        golden_out = {tid: t.get("golden", {}) for tid, t in doc["templates"].items()}
    catalogue = json.loads((ROOT / "templates" / "catalogue.json").read_text(encoding="utf-8"))
    langs = []
    for lang in catalogue["languages"]:
        types = []
        for typ in lang["types"]:
            tid = f"{lang['id']}/{typ['id']}"
            t = templates.get(tid, {})
            types.append({
                "id": tid, "label": typ["label"], "description": t.get("description", ""),
                "inputs": t.get("inputs", []), "files": t.get("files", {}),
                "proven": proven.get(tid), "golden": golden_out.get(tid, {}),
            })
        langs.append({"id": lang["id"], "label": lang["label"], "types": types})
    return langs


def golden_index():
    cases = []
    for case_json in sorted((ROOT / "tests" / "golden").glob("*/case.json")):
        case = json.loads(case_json.read_text(encoding="utf-8"))
        case["files"] = {p.name: p.read_text(encoding="utf-8", errors="replace")
                         for p in sorted(case_json.parent.iterdir()) if p.name != "case.json"}
        cases.append(case)
    return cases


def pipeline_index():
    tools = []
    for py in sorted((ROOT / "pipeline").glob("*.py")):
        src = py.read_text(encoding="utf-8", errors="replace")
        try:
            with warnings.catch_warnings():  # docstrings with Windows paths ("C:\R25") warn on parse
                warnings.simplefilter("ignore", SyntaxWarning)
                doc = ast.get_docstring(ast.parse(src)) or ""
        except SyntaxError:
            doc = ""
        tools.append({"name": py.name, "doc": doc, "lines": src.count("\n") + 1})
    return tools


def release_index():
    out, schemas = [], {}
    for release in sorted(RELEASES):
        path = db_path(release)
        if not path.is_file():
            out.append({"release": release, "built": False, "source": str(RELEASES[release])})
            continue
        conn = sqlite3.connect(path)
        q = lambda s: conn.execute(s).fetchone()[0]
        has_comp = conn.execute("SELECT 1 FROM sqlite_master WHERE name='component_fields'").fetchone()
        info = {"release": release, "built": True, "source": str(RELEASES[release]), "db": path.as_posix(),
                "apps": q("SELECT COUNT(DISTINCT app) FROM fields"), "fields": q("SELECT COUNT(*) FROM fields"),
                "enriched": q("SELECT COUNT(*) FROM fields WHERE field_type IS NOT NULL AND field_type != ''"),
                "jbcNames": q("SELECT COUNT(*) FROM component_fields") if has_comp else 0}
        out.append(info)
        jbc = dict(conn.execute("SELECT app, COUNT(*) FROM component_fields GROUP BY app").fetchall()) if has_comp else {}
        schemas[release] = [[a, n, jbc.get(a, 0)] for a, n in
                            conn.execute("SELECT app, COUNT(*) FROM fields GROUP BY app ORDER BY app")]
        conn.close()
    return out, schemas


def build_index():
    releases, schemas = release_index()
    diff = ROOT / "build" / "releases" / "R23-to-R25.json"
    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "overview": readme_sections(),
        "skills": [skill_index(d) for d in sorted((ROOT / "skills").iterdir()) if d.is_dir()],
        "templates": template_index(),
        "golden": golden_index(),
        "pipeline": pipeline_index(),
        "releases": releases,
        "releaseDiff": json.loads(diff.read_text(encoding="utf-8"))["summary"] if diff.exists() else None,
        "schemas": schemas,
    }


def script_safe_json(obj):
    """JSON that can sit inside <script>: no '</' sequence can close the tag."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def write_help(out):
    index = build_index()
    html = HELP_TEMPLATE.read_text(encoding="utf-8").replace("/*__HELP_INDEX__*/null", script_safe_json(index))
    Path(out).write_text(html, encoding="utf-8")
    return index, len(html.encode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="Temenos-Skills-HelpText.html")
    args = ap.parse_args()
    index, size = write_help(args.out)
    files = sum(len(s["files"]) for s in index["skills"])
    types = sum(len(l["types"]) for l in index["templates"])
    print(f"Wrote {args.out} ({size / 1e6:.1f} MB): {len(index['skills'])} skills / {files} files, "
          f"{types} artefact types, {len(index['golden'])} golden cases, {len(index['pipeline'])} pipeline tools")


if __name__ == "__main__":
    main()
