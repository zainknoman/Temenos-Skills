#!/usr/bin/env python3
"""Build Temenos-Skills-HelpText.html -- a JavaDoc-style, self-contained help
page for the whole repository.

Like RepoMind, it works in two steps: build an *index* (a structured model of
the repo), then render a viewer over it. The index holds:

  overview   README sections, in reading order (READING_ORDER)
  cli        CLI.md (the t24skills command line) + its stages from t24skills.STAGES
  samples    every sample (golden case) with its t24skills commands, generated
  skills     every skill: SKILL.md frontmatter + every text file under the skill
             (outline of headings + full content), except table-schema/ (4,596
             files, 35 MB) which is summarised as a directory of applications
  templates  the artefact catalogue: language -> group -> type, inputs, template
             sources, golden output, proven status
  golden     the golden cases (requirement, apps, expected fields)
  pipeline   every pipeline/*.py tool with its docstring, in execution order
             (PIPELINE_STAGES: stage, purpose, command)
  releases   per-release counts read from each built knowledge DB
  schemas    application -> field count (and jBC-name count) per release

The HTML embeds the index as JSON and needs no network: open the file in a
browser. Markdown is parsed with marked (inlined from pipeline/vendor/) and
shown as an MDFV-style document sheet (github.com/zainknoman/MDFV); only its
web fonts come from the network, with system-font fallbacks offline. Rebuild after changing skills, templates or pipeline tools.

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
# marked (MIT), the Markdown parser MDFV uses -- vendored and inlined so the page still needs no network.
MARKED_JS = Path(__file__).resolve().parent / "vendor" / "marked.min.js"

# Overview menu: README sections in reading order (a title matches by prefix, so
# "Artefact Templates" still matches "Artefact Templates (59 types)"). A section
# not listed here goes after these, in README order.
READING_ORDER = [
    "Introduction", "Install the Skills", "How to Use After Install", "Skill Architecture",
    "Knowledge Base: Three Layers", "Releases", "Field Verification Gate", "Artefact Templates",
    "T24Tools Artefact Generator", "Accuracy Harness", "Prerequisites", "Command Line", "How to Run", "Pipeline",
    "The Knowledge DB", "What the Reference Files Contain", "Repository Structure", "Component Analyzer",
    "MCP Server", "Component Type Classification", "Incremental Caching", "Re-running After a T24 Upgrade",
]

# Pipeline tools menu: stages in execution order; each tool = (file, what it does, command).
# A tool not listed here goes under "Other" so a new one is never hidden. A stage whose
# tools have no command (the command line, shared modules) is listed but not numbered.
PIPELINE_STAGES = [
    ("Command line", "t24skills runs every stage below (t24skills run <stage>) and the everyday "
     "commands, each with --json: t24skills.cmd on Windows, ./t24skills in sh.", [
        ("t24skills.py", "status, fields, rules, verify, golden, diff, stages, run <stage>", ""),
    ]),
    ("Extract from the JARs (R23)", "Builds Layer A, the field schemas, from jar/.", [
        ("extract.py", "Classes and methods of every JAR into the SHA-256 cache",
         "python pipeline/extract.py --jars jar --cache cache --workers 8"),
        ("insert_parse.py", "Field names and positions from INSERTS/I_F.* (Layer A ground truth)",
         "python pipeline/insert_parse.py --jars jar --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema"),
        ("html_parse.py", "Type, mandatory flag and description from the JavaDoc HTML",
         "python pipeline/html_parse.py --html T24.javadoc/T24.javadoc --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema"),
        ("component_parse.py", "Componentised (jBC) field names",
         "python pipeline/component_parse.py --jars jar --release R23"),
        ("record_parse.py", "Single- vs multi-value flag per field",
         "python pipeline/record_parse.py --jars jar --release R23"),
    ]),
    ("Business-rule docs (Layer B)", "Embeds the PDFs for semantic search.", [
        ("pdf_extract.py", "Chunk the PDFs and embed them into Chroma (TF-IDF, offline)",
         "python pipeline/pdf_extract.py --pdfs docs --vectordb vectordb --cache cache/pdf_extracts"),
        ("query_docs.py", "Search the business rules",
         'python pipeline/query_docs.py "what controls dormancy in ACCOUNT?" --topic ACCOUNT -n 5'),
    ]),
    ("Reference files", "Generates the class and API markdown the skills read.", [
        ("aggregate.py", "Class index, $USING packages, Java API and hook references",
         "python pipeline/aggregate.py --cache cache --out skills/temenos-dev/references"),
    ]),
    ("Payments / SEPA knowledge", "Optional: the payment-domain inventory under knowledge/sepa/.", [
        ("sepa_extract.py", "Payment-domain classes and fields from the cache and the DB",
         "python pipeline/sepa_extract.py --cache cache --db temenos_knowledge.db --out knowledge/sepa"),
        ("sepa_javap.py", "Exact method signatures of the payment hook APIs",
         "python pipeline/sepa_javap.py --jars jar --out knowledge/sepa"),
        ("sepa_hookmap.py", "Configuration field to Java hook wiring",
         "python pipeline/sepa_hookmap.py --schema skills/temenos-dev/references/table-schema --out knowledge/sepa"),
    ]),
    ("Second release (R25)", "Builds the R25 DB read-only from C:\\R25 and reports what changed.", [
        ("build_release.py", "Complete R25 knowledge DB in releases/R25/",
         'python pipeline/build_release.py --release R25 --javadoc-jar "C:\\R25\\bnk\\Transact_L3_Javadoc\\T24.javadoc.jar"'),
        ("release_diff.py", "R23 to R25 change report (build/releases/R23-to-R25.md)",
         "python pipeline/release_diff.py --old R23 --new R25"),
    ]),
    ("Generate and verify artefacts", "Used while writing code, and for every golden case.", [
        ("validate_fields.py", "Field Verification Gate: are these field names real?",
         'python pipeline/validate_fields.py --app ACCOUNT --fields "AC.CUSTOMER,AC.CATEGORY"'),
        ("make_goldens.py", "Render each template into a golden case (new types only)",
         "python pipeline/make_goldens.py --release R25"),
        ("verify_artefact.py", "Accuracy gate for one file: field check + R25 compile",
         "python pipeline/verify_artefact.py --file out/V.CUS.CHECK.b --app CUSTOMER --release R25"),
        ("run_golden.py", "Every golden case must PASS",
         "python pipeline/run_golden.py --release R25"),
    ]),
    ("Export to T24Tools", "Runs only if every golden case passes.", [
        ("release_t24tools.py", "Gate + export in one step (runs the golden cases, then the two below)",
         "python pipeline/release_t24tools.py --release R25"),
        ("export_t24tools.py", "fields.json for the release",
         "python pipeline/export_t24tools.py --release R25"),
        ("class_export.py", "classes.json for the JAR Viewer",
         "python pipeline/class_export.py --release R25"),
    ]),
    ("Documentation", "Rebuild after changing skills, templates or tools.", [
        ("build_help.py", "This help page", "python pipeline/build_help.py"),
    ]),
    ("Shared modules", "Imported by the tools above; not run on their own.", [
        ("releases.py", "Release registry and DB paths", ""),
        ("jar_types.py", "Component type of a JAR from its file name", ""),
        ("jar_classes.py", "Public classes from .class headers (no javatools)", ""),
        ("artefact_templates.py", "Load, resolve, render and prove templates", ""),
        ("artefact_fields.py", "Find and check field references in generated source", ""),
        ("compile_check.py", "Compile gate against the T24 install", ""),
    ]),
]


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
    sections = [s for s in sections if s["content"].strip()]
    rank = lambda s: next((k for k, t in enumerate(READING_ORDER) if s["title"].startswith(t)), len(READING_ORDER))
    return sorted(sections, key=rank)  # stable: unlisted sections keep their README order


def template_index():
    templates = {t["id"]: t for t in load_templates()}
    exported = ROOT / "build" / "t24tools" / "templates.json"
    proven, compiled, golden_out = {}, {}, {}
    if exported.exists():
        doc = json.loads(exported.read_text(encoding="utf-8"))
        for lang in doc["languages"]:
            for typ in lang["types"]:
                proven[f"{lang['id']}/{typ['id']}"] = typ["proven"]
                # proven but "compiled": false = renders and field-checks, never compiled on T24 yet
                compiled[f"{lang['id']}/{typ['id']}"] = typ.get("compiled", typ["proven"])
        golden_out = {tid: t.get("golden", {}) for tid, t in doc["templates"].items()}
    catalogue = json.loads((ROOT / "templates" / "catalogue.json").read_text(encoding="utf-8"))
    langs = []
    for lang in catalogue["languages"]:
        types = []
        for typ in lang["types"]:
            tid = f"{lang['id']}/{typ['id']}"
            t = templates.get(tid, {})
            types.append({
                "id": tid, "label": typ["label"], "group": typ.get("group", "Other"),
                "description": t.get("description", ""),
                "inputs": t.get("inputs", []), "files": t.get("files", {}),
                "proven": proven.get(tid), "compiled": compiled.get(tid), "golden": golden_out.get(tid, {}),
            })
        # listed by group, in the catalogue's group order (as T24Tools' step-3 type cards)
        order = list(dict.fromkeys(lang.get("groups", []) + [t["group"] for t in types]))
        types.sort(key=lambda t: order.index(t["group"]))
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
    # execution order: stage by stage, as listed in PIPELINE_STAGES
    place = {name: (k, j, stage, purpose, cmd) for k, (stage, _, items) in enumerate(PIPELINE_STAGES)
             for j, (name, purpose, cmd) in enumerate(items)}
    for t in tools:
        k, j, stage, purpose, cmd = place.get(t["name"], (len(PIPELINE_STAGES), 0, "Other", "", ""))
        t.update(stage=stage, purpose=purpose, command=cmd, order=(k, j))
    tools.sort(key=lambda t: t.pop("order"))
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


def cli_index():
    """CLI.md plus a stages section generated from t24skills.STAGES, so the page always
    matches what `t24skills run <stage>` does."""
    from t24skills import STAGES
    guide = ROOT / "CLI.md"
    text = guide.read_text(encoding="utf-8", errors="replace") if guide.exists() else "# t24skills\n"
    text += ("\n## Pipeline stages (generated from pipeline/t24skills.py)\n\n"
             "`t24skills run <stage>` runs a stage's steps in this order and stops at the first that fails.\n\n"
             "| # | Stage | What it does |\n|---|---|---|\n")
    text += "".join(f"| {k} | `{name}` | {desc.replace('|', '/')} |\n"
                    for k, (name, (desc, _)) in enumerate(STAGES.items(), 1))
    for name, (desc, steps) in STAGES.items():
        commands = "\n".join(" ".join(["python", f"pipeline/{s[0]}", *s[1:]]) for s in steps)
        text += f"\n### run {name}\n\n{desc}\n\n```\n{commands}\n```\n"
    text += rules_topics_section()
    return {"content": text, "outline": outline(text)}


def rules_topics_section(vectordb=ROOT / "vectordb"):
    """Markdown table of every topic `t24skills rules --topic` accepts, read from the vectordb
    (the same list as `t24skills topics`); empty if the vectordb is not built."""
    if not (vectordb / "chroma.sqlite3").is_file():
        return ""
    from query_docs import topics
    found = topics(vectordb, examples=3)
    cell = lambda s: s.replace("|", "/")
    rows = "".join(f"| `{cell(t['topic'])}` | {t['files']:,} | {t['chunks']:,} | {cell('; '.join(t['examples']))} |\n"
                   for t in found)
    return ("\n## Topics for rules --topic (generated from the vectordb)\n\n"
            f"{len(found)} topics, {sum(t['chunks'] for t in found):,} chunks. A topic is the top-level `docs/` folder a PDF "
            "was indexed under (or the PDF's own name when it sits directly in `docs/`). It is not a T24 application: "
            "there is no `CUSTOMER` topic, and the CUSTOMER user guide is under `Temenos_Applications`. Names are "
            "not case-sensitive. Put a name with spaces in quotes: `--topic \"Basics & Fundamentals\"`. "
            "An unknown topic exits `2` and suggests close names. Leave `--topic` out to search every topic. "
            "The same list: `t24skills topics`.\n\n"
            "| Topic | PDFs | Chunks | Largest PDFs |\n|---|---:|---:|---|\n" + rows)


def _ps(value):
    """A PowerShell / cmd argument: quoted when it has a space or a shell character."""
    value = str(value)
    return f'"{value}"' if re.search(r"[\s&|;'$@(){},<>`]", value) else value


def sample_commands(sample, template, release="R25"):
    """The commands for one sample: show it, its template, generate it two ways, compile it."""
    sid, tid, data = sample["case"], sample["template"], sample["data"]
    out = f".\\work\\{sid}"
    sets = [(i["id"], data["userInputs"][i["id"]]) for i in template["inputs"]
            if not i.get("fixed") and i["id"] in data.get("userInputs", {})]
    main = data["file"]
    apps = " ".join(f"--app {a}" for a in data.get("apps", []))
    app_args = apps or ("" if main.endswith(".java") else "--no-app")
    full = "\n".join([f"t24skills generate {tid} `"] + [f"  --set {k}={_ps(v)} `" for k, v in sets]
                     + [f"  --release {release} --out {out}"])
    return "\n".join([
        f"t24skills sample {sid}",
        f"t24skills template {tid}",
        "",
        "# generate it with the sample's inputs: the sample's code, dated today",
        f"t24skills generate {tid} --from-sample --release {release} --out {out}",
        "",
        "# generate it with every input written out: change the values you need",
        full,
        "",
        "# compile it on R25",
        f"t24skills verify {out}\\{main} {app_args} --release {release}".replace("  ", " "),
    ])


def samples_page():
    """Markdown for the help's Samples page: every sample, grouped as in T24Tools, with the commands
    to show, generate and compile it. Built from the golden cases and templates, so it cannot drift."""
    from t24skills import _samples, _templates
    samples, templates = _samples(), _templates()
    lines = [
        "# Samples: commands for every artefact type", "",
        f"Every artefact type has one sample: a golden case in `tests/golden/<sample>/`, generated from its template "
        f"and compiled on R25. This page lists all {len(samples)} with the commands for each one. They are "
        "PowerShell (a backtick ` continues a line) and assume `t24skills` is on your PATH; without that, use "
        "`.\\t24skills.cmd` in the repository folder.", "",
        "For each sample:", "",
        "- `sample` shows its requirement, inputs and files; `template` shows the inputs the type takes.",
        "- `generate --from-sample` writes the sample's code into `.\\work\\<sample>`, dated today "
        "(add `--today 2026-10-02` and it is byte-identical to the sample).",
        "- The long `generate` form lists every input: copy it and change the values (a field input is the EQU name; "
        "the generator turns it into the jBC name or Java getter for the release).",
        "- `verify` compiles the main file on R25 (field check + compile).", "",
        "Add `--json` to any of them for one JSON object; add `--force` to `generate --out` to overwrite.", "",
        "## All samples", "",
        "| Sample | Type | Template | Main file | Applications |", "|---|---|---|---|---|",
    ]
    lines += [f"| `{s['case']}` | {s['type'].replace('|', '/')} | `{s['template']}` | `{s['data']['file']}` | "
              f"{', '.join(s['apps']) or '-'} |" for s in samples]
    heading = (None, None)
    for s in samples:
        if s["languageLabel"] != heading[0]:
            lines += ["", f"## {s['languageLabel']}"]
        if (s["languageLabel"], s["group"]) != heading:
            lines += ["", f"### {s['group']}"]
            heading = (s["languageLabel"], s["group"])
        t = templates.get(s["template"])
        if not t:
            continue
        lines += ["", f"#### {s['case']}", "",
                  f"**{s['type']}**. {s['requirement']} Applications: {', '.join(s['apps']) or 'none'}. "
                  f"Generates: {', '.join(f'`{n}`' for n in sorted(p.name for p in s['dir'].iterdir() if p.name != 'case.json'))}.",
                  "", "```powershell", sample_commands(s, t), "```"]
    text = "\n".join(lines) + "\n"
    return {"content": text, "outline": outline(text), "count": len(samples)}


def build_index():
    releases, schemas = release_index()
    diff = ROOT / "build" / "releases" / "R23-to-R25.json"
    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "overview": readme_sections(),
        "cli": cli_index(),
        "samples": samples_page(),
        "skills": [skill_index(d) for d in sorted((ROOT / "skills").iterdir()) if d.is_dir()],
        "templates": template_index(),
        "golden": golden_index(),
        "pipeline": pipeline_index(),
        "pipelineStages": [{"title": t, "intro": i} for t, i, _ in PIPELINE_STAGES],
        "releases": releases,
        "releaseDiff": json.loads(diff.read_text(encoding="utf-8"))["summary"] if diff.exists() else None,
        "schemas": schemas,
    }


def script_safe_json(obj):
    """JSON that can sit inside <script>: no '</' sequence can close the tag."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def write_help(out):
    index = build_index()
    marked = MARKED_JS.read_text(encoding="utf-8")
    if "</script" in marked.lower():
        raise ValueError(f"{MARKED_JS} contains '</script' and cannot be inlined")
    html = (HELP_TEMPLATE.read_text(encoding="utf-8")
            .replace("/*__MARKED_JS__*/", marked)
            .replace("/*__HELP_INDEX__*/null", script_safe_json(index)))
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
