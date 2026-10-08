#!/usr/bin/env python3
"""t24skills -- one command line for Temenos-Skills.

Every command takes --json: the result is then one JSON object on stdout,
{"schemaVersion": 1, "command": ..., "ok": true|false, ...}, which is the
contract for other programs (Temenos-Engineering-Platform, CI). Exit codes:
0 = ok, 1 = the check failed (a field is missing, a verify or golden case
FAILs, a stage step fails), 2 = cannot run (no knowledge DB, no vectordb,
unknown release, application, topic, template or file). Full guide: CLI.md.

  t24skills status                                   what is built, per release
  t24skills fields ACCOUNT [--check AC.CUSTOMER,AC.CATEGORY] [--release R25]
  t24skills rules "what controls dormancy?" [--topic ACCOUNT] [-n 5]
  t24skills topics                                   the topics rules --topic accepts
  t24skills samples [FILTER] [--language jbc]        the artefact samples (one golden case per type)
  t24skills sample jbc/local-table [--file F] [--out DIR]   one sample's requirement, inputs and files
  t24skills template jbc/validation                  a template's inputs + a generate command that works
  t24skills generate jbc/validation --set APP=CUSTOMER --set FIELD=EB.CUS.SECTOR ... [--out DIR]
  t24skills verify out/V.CUS.CHECK.b --app CUSTOMER [--release R25] [--no-compile]   (--no-app: a new local table)
  t24skills golden [--case NAME] [--release R25]
  t24skills diff [R23 R25] [--full]
  t24skills stages                                   the pipeline stages, in execution order
  t24skills run STAGE [--release R25] [--dry-run]    run one stage (r23, docs, refs, sepa, r25, golden, export, help)

Commands run from the repository root, wherever they are started; a file path
is resolved against the directory you start in. Launchers: t24skills.cmd
(Windows) and ./t24skills (sh) in the repository root, or
python pipeline/t24skills.py.
"""
import argparse
import json
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from releases import DEFAULT_RELEASE, RELEASES, db_path, open_release_db  # noqa: E402

SCHEMA_VERSION = 1

# Pipeline stages in execution order (the help page's "Execution order" lists the same tools).
# Each step is a pipeline script and its arguments; {release} is the --release of `run`.
STAGES = {
    "r23": ("Extract from the JARs (R23): classes, field schemas, JavaDoc metadata, jBC names, SV/MV flags", [
        ["extract.py", "--jars", "jar", "--cache", "cache", "--workers", "8"],
        ["insert_parse.py", "--jars", "jar", "--db", "temenos_knowledge.db", "--out", "skills/temenos-dev/references/table-schema"],
        ["html_parse.py", "--html", "T24.javadoc/T24.javadoc", "--db", "temenos_knowledge.db", "--out", "skills/temenos-dev/references/table-schema"],
        ["component_parse.py", "--jars", "jar", "--release", "R23"],
        ["record_parse.py", "--jars", "jar", "--release", "R23"],
    ]),
    "docs": ("Business-rule docs (Layer B): chunk and embed the PDFs", [
        ["pdf_extract.py", "--pdfs", "docs", "--vectordb", "vectordb", "--cache", "cache/pdf_extracts"],
    ]),
    "refs": ("Reference files: class index, $USING packages, Java API, hooks", [
        ["aggregate.py", "--cache", "cache", "--out", "skills/temenos-dev/references"],
    ]),
    "sepa": ("Payments / SEPA knowledge (optional) under knowledge/sepa/", [
        ["sepa_extract.py", "--cache", "cache", "--db", "temenos_knowledge.db", "--out", "knowledge/sepa"],
        ["sepa_javap.py", "--jars", "jar", "--out", "knowledge/sepa"],
        ["sepa_hookmap.py", "--schema", "skills/temenos-dev/references/table-schema", "--out", "knowledge/sepa"],
    ]),
    "r25": ("Second release (R25), read-only from C:\\R25, and the R23 -> R25 change report", [
        ["build_release.py", "--release", "R25", "--javadoc-jar", r"C:\R25\bnk\Transact_L3_Javadoc\T24.javadoc.jar"],
        ["release_diff.py", "--old", "R23", "--new", "R25"],
    ]),
    "golden": ("Every golden case: field check + compile", [
        ["run_golden.py", "--release", "{release}"],
    ]),
    "export": ("Gated T24Tools export: golden cases, then fields.json, classes.json, templates.json", [
        ["release_t24tools.py", "--release", "{release}"],
    ]),
    "help": ("Rebuild Temenos-Skills-HelpText.html", [
        ["build_help.py"],
    ]),
}


class CannotRun(Exception):
    """The command cannot run here (exit 2): missing DB, vectordb, file or unknown release."""


# ---------------------------------------------------------------- helpers

def _mtime(path):
    path = Path(path)
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if path.exists() else None


def _connect(release):
    if release not in RELEASES:
        raise CannotRun(f"unknown release '{release}' -- known: {', '.join(sorted(RELEASES))}")
    try:
        return open_release_db(release)
    except SystemExit as exc:  # MissingReleaseDB
        raise CannotRun(str(exc)) from None


def _use_install(install):
    from compile_check import find_install, install_present, install_release, INSTALL_ENV
    if install:
        os.environ[INSTALL_ENV] = str(install)
    root = find_install()
    return {"path": str(root), "present": install_present(root), "release": install_release(root)}


def _step_command(step, release):
    return [sys.executable, str(HERE / step[0])] + [a.replace("{release}", release) for a in step[1:]]


# ---------------------------------------------------------------- commands

def cmd_status(args):
    releases = []
    for release in sorted(RELEASES):
        path = ROOT / db_path(release)
        entry = {"release": release, "db": db_path(release).as_posix(), "built": path.is_file(), "modified": _mtime(path)}
        if path.is_file():
            conn = sqlite3.connect(path)
            q = lambda sql: conn.execute(sql).fetchone()[0]
            entry["apps"] = q("SELECT COUNT(DISTINCT app) FROM fields")
            entry["fields"] = q("SELECT COUNT(*) FROM fields")
            has = lambda t: conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (t,)).fetchone()
            entry["jbcNames"] = q("SELECT COUNT(*) FROM component_fields") if has("component_fields") else 0
            entry["fieldKinds"] = q("SELECT COUNT(*) FROM field_kinds") if has("field_kinds") else 0
            conn.close()
        export = ROOT / "build" / "t24tools" / release / "fields.json"
        entry["t24toolsExport"] = {"fieldsJson": export.is_file(), "modified": _mtime(export)}
        releases.append(entry)

    catalogue = json.loads((ROOT / "templates" / "catalogue.json").read_text(encoding="utf-8"))
    help_page = ROOT / "Temenos-Skills-HelpText.html"
    sources = [p for d in ("skills", "templates") for p in (ROOT / d).rglob("*")
               if p.is_file() and "table-schema" not in p.parts] + list((ROOT / "pipeline").glob("*.py")) + [p for p in (ROOT / "README.md", ROOT / "CLI.md", HERE / "help_template.html") if p.is_file()]
    newest = max((p.stat().st_mtime for p in sources), default=0)
    vector = ROOT / "vectordb" / "tfidf_vectorizer.joblib"
    return True, {
        "root": str(ROOT),
        "defaultRelease": DEFAULT_RELEASE,
        "releases": releases,
        "vectordb": {"built": vector.is_file(), "modified": _mtime(vector)},
        "templates": {"types": sum(len(lang["types"]) for lang in catalogue["languages"]),
                      "goldenCases": len(list((ROOT / "tests" / "golden").glob("*/case.json"))),
                      "templatesJson": (ROOT / "build" / "t24tools" / "templates.json").is_file()},
        "compileInstall": _use_install(None),
        "helpPage": {"built": help_page.is_file(), "modified": _mtime(help_page),
                     "stale": not help_page.is_file() or help_page.stat().st_mtime < newest},
    }


def show_status(r):
    print(f"Temenos-Skills at {r['root']} (default release {r['defaultRelease']})")
    for e in r["releases"]:
        if e["built"]:
            print(f"  {e['release']}: {e['apps']:,} apps, {e['fields']:,} fields, {e['jbcNames']:,} jBC names "
                  f"({e['db']}, {e['modified']})")
        else:
            print(f"  {e['release']}: not built ({e['db']})")
        print(f"       T24Tools fields.json: {e['t24toolsExport']['modified'] or 'not exported'}")
    print(f"  Business-rule docs (vectordb): {'built ' + r['vectordb']['modified'] if r['vectordb']['built'] else 'not built'}")
    t = r["templates"]
    print(f"  Templates: {t['types']} types, {t['goldenCases']} golden cases, templates.json "
          f"{'exported' if t['templatesJson'] else 'not exported'}")
    c = r["compileInstall"]
    print(f"  Compile install: {c['path']} ({c['release'] or 'release unknown'})" if c["present"]
          else f"  Compile install: none found -- compiles SKIP")
    h = r["helpPage"]
    print(f"  Help page: {'not built' if not h['built'] else h['modified']}"
          f"{' -- STALE, run: t24skills run help' if h['stale'] else ''}")


def cmd_fields(args):
    from validate_fields import app_fields, check
    conn = _connect(args.release)
    try:
        if args.check:
            result = check(conn, args.app, args.check.split(","))
            if not result["known"]:
                raise CannotRun(f"no schema for application '{result['app']}' in {args.release}")
            return not result["missing"], {"release": args.release, **result}
        fields = app_fields(conn, args.app)
        if not fields:
            raise CannotRun(f"no schema for application '{args.app.upper()}' in {args.release}")
        return True, {"release": args.release, "app": args.app.upper(), "count": len(fields), "fields": fields}
    finally:
        conn.close()


def show_fields(r):
    if "verified" in r:
        for f in r["verified"]:
            jbc = f"  jBC {' | '.join(f['jbc'])}" if f["jbc"] else ""
            print(f"VERIFIED   {f['field']}  (pos {f['position']}, {f['kind'] or '?'}){jbc}")
        for m in r["missing"]:
            print(f"NOT FOUND  {m}  -- never guess a field name; ask the developer")
        return
    print(f"{r['app']} in {r['release']}: {r['count']} fields")
    for f in r["fields"]:
        print(f"  {f['position']:>4}  {f['field']:<40} {f['kind'] or '':<8} {f['type'] or '':<12} "
              f"{(f['jbc'] or [''])[0]}")


def _vectordb():
    vectordb = ROOT / "vectordb"
    if not (vectordb / "tfidf_vectorizer.joblib").is_file():
        raise CannotRun("no business-rule vectordb -- build it with: t24skills run docs")
    return str(vectordb)


def cmd_rules(args):
    from query_docs import resolve_topic, search, topics
    vectordb = _vectordb()
    topic = args.topic
    hits = search(args.query, topic, args.n, vectordb)
    if topic and not hits:  # an exact topic always has chunks: check the name (any case is accepted)
        try:
            resolved = resolve_topic(topic, [t["topic"] for t in topics(vectordb)])
        except ValueError as exc:
            raise CannotRun(str(exc)) from None
        if resolved != topic:
            topic, hits = resolved, search(args.query, resolved, args.n, vectordb)
    return True, {"query": args.query, "topic": topic, "results": hits}


def show_rules(r):
    if not r["results"]:
        print("No results.")
    for h in r["results"]:
        print(f"--- {h['source']} (page {h['page']}, score {h['score']:.3f}) ---\n{h['text']}\n")


def cmd_topics(args):
    from query_docs import topics
    found = topics(_vectordb(), examples=3)
    return True, {"count": len(found), "chunks": sum(t["chunks"] for t in found), "topics": found}


def show_topics(r):
    print(f"{r['count']} topics for rules --topic. Names are not case-sensitive; quote names with spaces.")
    print(f"  {'TOPIC':<44} {'PDFS':>5} {'CHUNKS':>6}  LARGEST PDF")
    for t in r["topics"]:
        name = t["topic"] if len(t["topic"]) <= 44 else t["topic"][:41] + "..."
        example = (t.get("examples") or [""])[0]
        print(f"  {name:<44} {t['files']:>5} {t['chunks']:>6}  {example[:60]}")


def _samples():
    """Every golden case (one per artefact type) with its template's language, type label and group."""
    catalogue = json.loads((ROOT / "templates" / "catalogue.json").read_text(encoding="utf-8"))
    types, order = {}, {}
    for li, lang in enumerate(catalogue["languages"]):
        groups = lang.get("groups", [])
        for ti, t in enumerate(lang["types"]):
            tid, group = f"{lang['id']}/{t['id']}", t.get("group", "Other")
            types[tid] = (lang["label"], t["label"], group)
            # catalogue order: language, then its group order, then the type's place in the catalogue
            order[tid] = (li, groups.index(group) if group in groups else len(groups), ti)
    out = []
    for case_json in sorted((ROOT / "tests" / "golden").glob("*/case.json")):
        case = json.loads(case_json.read_text(encoding="utf-8"))
        template = case.get("template", "")
        lang_label, type_label, group = types.get(template, ("", case.get("artefact", ""), "Other"))
        out.append({"case": case["name"], "template": template, "language": template.split("/")[0] if template else "",
                    "languageLabel": lang_label, "type": type_label, "group": group, "skill": case.get("skill", ""),
                    "requirement": case.get("requirement", ""), "apps": case.get("apps", []),
                    "compiled": case.get("compiled", True), "dir": case_json.parent, "data": case})
    return sorted(out, key=lambda s: (order.get(s["template"], (99, 0, 0)), s["case"]))


def _public(sample):
    return {k: v for k, v in sample.items() if k not in ("dir", "data")}


def cmd_samples(args):
    q = (args.filter or "").lower()
    found = [s for s in _samples()
             if (not args.language or s["language"] == args.language)
             and (not q or q in " ".join([s["case"], s["template"], s["type"], s["group"], s["requirement"]]).lower())]
    return True, {"count": len(found), "samples": [_public(s) for s in found]}


def show_samples(r):
    if not r["samples"]:
        print("No samples match.")
        return
    heading = None
    for s in r["samples"]:
        if (s["languageLabel"], s["group"]) != heading:
            heading = (s["languageLabel"], s["group"])
            print(f"\n{s['languageLabel']} > {s['group']}")
        print(f"  {s['case']:<42} {s['type']}{'' if s['compiled'] else '  (not compiled yet)'}")
    print(f"\n{r['count']} samples. Show one: t24skills sample <name>")


def _find_sample(name):
    samples = _samples()
    key = name.strip().lower().replace("\\", "/")
    for s in samples:
        if key in (s["case"].lower(), s["template"].lower()):
            return s
    import difflib
    names = [s["case"] for s in samples]
    close = [n for n in names if key in n] or difflib.get_close_matches(key, names, n=5, cutoff=0.5)
    hint = f" Did you mean: {', '.join(close[:5])}?" if close else ""
    raise CannotRun(f"no sample '{name}'.{hint} List them with: t24skills samples")


def cmd_sample(args):
    s = _find_sample(args.name)
    main_file = s["data"].get("file")
    paths = sorted((p for p in s["dir"].iterdir() if p.is_file() and p.name != "case.json"),
                   key=lambda p: (p.name != main_file, p.suffix == ".component", p.name))
    files = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in paths}
    result = {**_public(s), "today": s["data"].get("today"), "userInputs": s["data"].get("userInputs", {}),
              "expectedFields": s["data"].get("expected_fields", []), "mainFile": main_file,
              "path": s["dir"].relative_to(ROOT).as_posix(), "files": files}
    if args.pick:
        match = next((n for n in files if n.lower() == args.pick.lower()), None)
        if not match:
            raise CannotRun(f"sample {s['case']} has no file '{args.pick}' -- it has: {', '.join(files)}")
        result["files"] = {match: files[match]}
        result["only"] = match
    if args.out:
        out = Path(args.out)
        clash = [n for n in result["files"] if (out / n).exists()]
        if clash and not args.force:
            raise CannotRun(f"{out} already has {', '.join(clash)} -- use --force to overwrite")
        out.mkdir(parents=True, exist_ok=True)
        for n in result["files"]:
            (out / n).write_bytes((s["dir"] / n).read_bytes())  # byte for byte: keeps the CRLF line ends
        result["copiedTo"] = str(out)
    return True, result


def show_sample(r):
    if r.get("copiedTo"):
        print(f"Copied {', '.join(r['files'])} to {r['copiedTo']}")
        return
    if r.get("only"):
        print(r["files"][r["only"]], end="")
        return
    print(f"{r['case']}: {r['type']}")
    print(f"  Template:     {r['template']}  ({r['languageLabel']} > {r['group']})")
    print(f"  Skill:        {r['skill']}")
    print(f"  Requirement:  {r['requirement']}")
    print(f"  Applications: {', '.join(r['apps']) or '-'}")
    print(f"  Compiled:     {'yes, on R25' if r['compiled'] else 'not yet'}")
    print(f"  Folder:       {r['path']}")
    print("  Inputs:")
    for k, v in r["userInputs"].items():
        print(f"    {k} = {v}")
    for name, text in r["files"].items():
        label = " (main)" if name == r["mainFile"] else ""
        print(f"\n===== {name}{label} =====")
        print(text.rstrip("\n"))


def _templates():
    """{template id: template} from templates/<language>/<type>/, in catalogue order."""
    from artefact_templates import load_templates
    by_id = {t["id"]: t for t in load_templates(ROOT / "templates")}
    order = [s["template"] for s in _samples()]
    return {tid: by_id[tid] for tid in sorted(by_id, key=lambda t: (order.index(t) if t in order else len(order), t))}


def _find_template(name):
    templates = _templates()
    key = name.strip().lower().replace("\\", "/")
    by_case = {s["case"].lower(): s["template"] for s in _samples()}
    tid = key if key in templates else by_case.get(key)
    if tid in templates:
        return templates[tid]
    import difflib
    close = [t for t in templates if key in t] or difflib.get_close_matches(key, list(templates), n=5, cutoff=0.5)
    hint = f" Did you mean: {', '.join(close[:5])}?" if close else ""
    raise CannotRun(f"no template '{name}'.{hint} List them with: t24skills samples")


def _example_command(template, inputs):
    """A generate command line that works: the template's sample inputs, ready to edit."""
    quote = lambda v: f'"{v}"' if any(c in str(v) for c in " &|;'") else str(v)
    sets = " ".join(f"--set {k}={quote(v)}" for k, v in inputs.items()
                    if not any(i["id"] == k and i.get("fixed") for i in template["inputs"]))
    return f"t24skills generate {template['id']} {sets} --release R25 --out .\\work"


def cmd_template(args):
    if not args.name:
        return True, {"templates": [{"id": t["id"], "label": t["label"]} for t in _templates().values()]}
    t = _find_template(args.name)
    sample = next((s for s in _samples() if s["template"] == t["id"]), None)
    sample_inputs = sample["data"].get("userInputs", {}) if sample else {}
    inputs = [{**i, "sample": sample_inputs.get(i["id"])} for i in t["inputs"]]
    return True, {"id": t["id"], "language": t["language"], "label": t["label"], "description": t.get("description", ""),
                  "group": sample["group"] if sample else "", "sample": sample["case"] if sample else None,
                  "inputs": inputs, "files": list(t["files"]),
                  "example": _example_command(t, sample_inputs) if sample else None}


def show_template(r):
    if "templates" in r:
        for t in r["templates"]:
            print(f"  {t['id']:<44} {t['label']}")
        print(f"\n{len(r['templates'])} templates. Show one: t24skills template <id>")
        return
    print(f"{r['id']}: {r['label']}  ({r['group']})")
    print(f"  {r['description']}")
    print(f"  Generates: {', '.join(r['files'])}")
    print("\n  INPUT              KIND          SAMPLE VALUE")
    for i in r["inputs"]:
        kind = i["kind"] + (f" of {i['of']}" if i.get("of") else "")
        value = f"(fixed) {i['fixed']}" if i.get("fixed") else (i.get("sample") or i.get("example") or "")
        print(f"  {i['id']:<18} {kind:<13} {value}")
    print("\n  A field input is the EQU name (EB.CUS.SECTOR); the generator turns it into the jBC name or Java"
          "\n  getter for the release. TODAY and the record class / component names are filled in for you.")
    if r["example"]:
        print(f"\nTry it with the sample's inputs (change any --set):\n  {r['example']}")
        print(f"Or start from the sample and set only what differs:\n"
              f"  t24skills generate {r['id']} --from-sample --set KEY=VALUE --release R25 --out .\\work")


def _parse_sets(pairs):
    values = {}
    for pair in pairs or []:
        key, sep, value = pair.partition("=")
        if not sep or not key.strip():
            raise CannotRun(f"--set needs KEY=VALUE, got '{pair}'")
        values[key.strip().upper()] = value
    return values


def cmd_generate(args):
    from artefact_fields import UnknownApp, check_fields
    from artefact_templates import FieldNotAvailable, MissingInputs, render, resolve
    t = _find_template(args.name)
    specs = {i["id"]: i for i in t["inputs"]}
    inputs = {}
    if args.from_sample:
        sample = next((s for s in _samples() if s["template"] == t["id"]), None)
        inputs.update(sample["data"].get("userInputs", {}) if sample else {})
    if args.inputs:
        try:
            inputs.update({k.upper(): str(v) for k, v in json.loads(Path(args.inputs).read_text(encoding="utf-8")).items()})
        except (OSError, ValueError, AttributeError) as exc:
            raise CannotRun(f"cannot read --inputs {args.inputs}: {exc}") from None
    inputs.update(_parse_sets(args.set))
    unknown = sorted(k for k in inputs if k not in specs)
    if unknown:
        raise CannotRun(f"{t['id']} has no input {', '.join(unknown)} -- its inputs: {', '.join(specs)}")
    for i in t["inputs"]:
        if i.get("fixed"):
            inputs[i["id"]] = i["fixed"]
        elif i["kind"] in ("app", "field") and i["id"] in inputs:
            inputs[i["id"]] = inputs[i["id"]].strip().upper()
    missing = [i for i in t["inputs"] if i["id"] not in inputs or not str(inputs[i["id"]]).strip()]
    if missing:
        raise CannotRun("missing inputs: " + ", ".join(f"{i['id']} ({i['kind']})" for i in missing)
                        + f" -- see: t24skills template {t['id']}")

    today = args.today or datetime.now().strftime("%Y-%m-%d")
    conn = _connect(args.release)
    try:
        for i in t["inputs"]:  # an unknown application would otherwise only show up as a missing field
            if i["kind"] == "app" and not conn.execute("SELECT 1 FROM fields WHERE app = ? LIMIT 1", (inputs[i["id"]],)).fetchone():
                raise CannotRun(f"no application '{inputs[i['id']]}' in {args.release} ({i['id']})")
        try:
            files = render(t, resolve(t, inputs, conn, today))
        except FieldNotAvailable as exc:
            return False, {"template": t["id"], "release": args.release, "inputs": inputs,
                           "error": {"type": "FIELD_NOT_AVAILABLE", "message": str(exc)}, "files": {}}
        except MissingInputs as exc:
            raise CannotRun(f"{exc} -- see: t24skills template {t['id']}") from None
        # field check of every generated Infobasic / jBC routine (javac is the gate for Java), as T24Tools does
        apps = [inputs[i["id"]] for i in t["inputs"] if i["kind"] == "app"]
        checks, ok = [], True
        for name, content in files.items():
            if not name.endswith(".b"):
                continue
            for app in dict.fromkeys(apps):
                try:
                    res = check_fields(conn, app, content)
                except UnknownApp as exc:
                    checks.append({"file": name, "app": app, "error": str(exc), "verified": [], "missing": []})
                    ok = False
                    continue
                checks.append({"file": name, "app": app, "verified": res.verified, "missing": res.missing})
                ok &= not res.missing
    finally:
        conn.close()

    result = {"template": t["id"], "release": args.release, "today": today, "inputs": inputs,
              "files": files, "fieldCheck": checks}
    if args.out:
        out = Path(args.out)
        clash = [n for n in files if (out / n).exists()]
        if clash and not args.force:
            raise CannotRun(f"{out} already has {', '.join(clash)} -- use --force to overwrite")
        out.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (out / name).write_text(content, encoding="utf-8")  # same line ends as the golden cases
        result["writtenTo"] = str(out)
        main = next((n for n in files if not n.endswith(".component")), None)
        if main:
            app_args = "".join(f" --app {a}" for a in dict.fromkeys(apps)) or (
                "" if main.endswith(".java") else " --no-app")
            result["next"] = f"t24skills verify {out / main}{app_args} --release {args.release}"
    return ok, result


def show_generate(r):
    if r.get("error"):
        print(f"NOT GENERATED: {r['error']['message']}")
        return
    print(f"Generated {r['template']} for {r['release']}: {', '.join(r['files'])}")
    for c in r["fieldCheck"]:
        if c.get("error"):
            print(f"  HALT {c['file']}: {c['error']}")
        for m in c["missing"]:
            print(f"  NOT FOUND in {c['app']} ({c['file']}): {m}")
        if c["verified"]:
            print(f"  VERIFIED in {c['app']} ({c['file']}): {', '.join(c['verified'])}")
    if not r["fieldCheck"]:
        print("  Field check: none (Java is checked by javac, or the template reads no application)")
    if r.get("writtenTo"):
        n = len(r["files"])
        print(f"Wrote {n} file{'' if n == 1 else 's'} to {r['writtenTo']}")
        if r.get("next"):
            print(f"Compile it: {r['next']}")
        return
    for name, text in r["files"].items():
        print(f"\n===== {name} =====")
        print(text.rstrip("\n"))


def cmd_verify(args):
    path = Path(args.file)
    if not path.is_file():
        raise CannotRun(f"no such file: {path}")
    install = None if args.no_compile else _use_install(args.install)
    from verify_artefact import DEFAULT_OUT, verify
    conn = _connect(args.release)
    try:
        report = verify(path, [a.upper() for a in args.app], conn, ROOT / DEFAULT_OUT, skip_compile=args.no_compile,
                        no_app_ok=args.no_app)
    finally:
        conn.close()
    return report["passed"], {"release": args.release, "compileInstall": install, **report}


def show_verify(r):
    for f in r["fields"]:
        if f.get("error"):
            print(f"HALT: {f['error']}")
        for m in f["missing"]:
            print(f"NOT FOUND in {f['app']}: {m}")
        if f["verified"]:
            print(f"VERIFIED in {f['app']}: {', '.join(f['verified'])}")
        if f.get("compiler_checked"):
            print(f"COMPONENTISED (checked by compiler) in {f['app']}: {', '.join(f['compiler_checked'])}")
    if r["compileInstall"]:
        c = r["compileInstall"]
        print(f"Compile install: {c['path']} ({c['release'] or 'release unknown'})" if c["present"]
              else "Compile install: none found -- compiles SKIP")
    print(f"COMPILE: {r['compile']['status']}")
    if r["compile"]["status"] not in ("OK", "NOT_RUN"):
        print(r["compile"]["output"][-3000:])
    print("PASS" if r["passed"] else "FAIL")


def cmd_golden(args):
    install = _use_install(args.install)
    from run_golden import run_cases
    conn = _connect(args.release)
    results = []
    try:
        for r in run_cases(conn, args.case, root=ROOT / "tests" / "golden"):
            report = r.pop("report")
            r["compile"] = report["compile"]["status"]
            if r["result"] == "FAIL":
                r["fields"] = report["fields"]
                r["compileOutput"] = report["compile"]["output"][-2000:]
            results.append(r)
            if not args.json:
                print(f"{r['result']}  {r['case']:<40} {r['compile']}"
                      + (f" expected-fields-not-seen={r['lost']}" if r["lost"] else ""), flush=True)
    finally:
        conn.close()
    if args.case and not results:
        raise CannotRun(f"no golden case named '{args.case}'")
    counts = {k: sum(r["result"] == k for r in results) for k in ("PASS", "FAIL", "PEND")}
    return counts["FAIL"] == 0, {"release": args.release, "compileInstall": install, "counts": counts, "cases": results}


def show_golden(r):
    c = r["counts"]
    print(f"{c['PASS']} PASS, {c['FAIL']} FAIL, {c['PEND']} PEND on {r['release']}")


def cmd_diff(args):
    from release_diff import diff_releases
    old, new = _connect(args.old), _connect(args.new)
    try:
        diff = diff_releases(old, new)
    finally:
        old.close()
        new.close()
    if not args.full:
        diff = {"summary": diff["summary"], "apps_added": diff["apps_added"], "apps_removed": diff["apps_removed"]}
    return True, {"old": args.old, "new": args.new, **diff}


def show_diff(r):
    print(f"{r['old']} -> {r['new']}")
    for k, v in r["summary"].items():
        print(f"  {k:<16} {v:,}")
    print("Full report: --full --json, or build/releases/<old>-to-<new>.md (t24skills run r25)")


def cmd_stages(args):
    return True, {"stages": [{"stage": name, "description": desc,
                              "commands": [" ".join(["python", f"pipeline/{s[0]}", *s[1:]]) for s in steps]}
                             for name, (desc, steps) in STAGES.items()]}


def show_stages(r):
    for k, s in enumerate(r["stages"], 1):
        print(f"{k}. {s['stage']:<7} {s['description']}")
        for c in s["commands"]:
            print(f"     {c}")


def cmd_run(args):
    desc, steps = STAGES[args.stage]
    commands = [_step_command(s, args.release) for s in steps]
    out = {"stage": args.stage, "description": desc, "release": args.release, "dryRun": args.dry_run, "steps": []}
    if args.dry_run:
        out["steps"] = [{"command": c} for c in commands]
        return True, out
    for c in commands:
        if not args.json:
            print(f">>> {' '.join(c[1:])}", flush=True)
        start = time.monotonic()
        # in --json mode the step's own output goes to stderr, so stdout stays one JSON object
        proc = subprocess.run(c, cwd=ROOT, stdout=sys.stderr if args.json else None)
        out["steps"].append({"command": c, "exitCode": proc.returncode, "seconds": round(time.monotonic() - start, 1)})
        if proc.returncode != 0:
            return False, out
    return True, out


def show_run(r):
    if r["dryRun"]:
        for s in r["steps"]:
            print(" ".join(s["command"]))
        return
    last = r["steps"][-1] if r["steps"] else None
    if last and last["exitCode"]:
        print(f"Stage {r['stage']} stopped: step exited {last['exitCode']}")
    else:
        print(f"Stage {r['stage']} done ({sum(s['seconds'] for s in r['steps'])} s)")


COMMANDS = {
    "status": (cmd_status, show_status), "fields": (cmd_fields, show_fields), "rules": (cmd_rules, show_rules),
    "topics": (cmd_topics, show_topics),
    "samples": (cmd_samples, show_samples), "sample": (cmd_sample, show_sample),
    "template": (cmd_template, show_template), "generate": (cmd_generate, show_generate),
    "verify": (cmd_verify, show_verify), "golden": (cmd_golden, show_golden), "diff": (cmd_diff, show_diff),
    "stages": (cmd_stages, show_stages), "run": (cmd_run, show_run),
}


def parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", help="print one JSON object (the machine contract)")
    rel = argparse.ArgumentParser(add_help=False)
    rel.add_argument("--release", default=DEFAULT_RELEASE, choices=sorted(RELEASES),
                     help=f"T24 release (default {DEFAULT_RELEASE})")
    inst = argparse.ArgumentParser(add_help=False)
    inst.add_argument("--install", help="T24 install to compile against (default: $T24_INSTALL, else C:\\R25 ...)")

    ap = argparse.ArgumentParser(prog="t24skills", description="Temenos-Skills command line.",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog="Every command takes --json. Exit: 0 ok, 1 check failed, 2 cannot run.")
    sub = ap.add_subparsers(dest="command", required=True, metavar="COMMAND")
    sub.add_parser("status", parents=[common], help="what is built, per release")
    p = sub.add_parser("fields", parents=[common, rel], help="an application's fields, or check field names")
    p.add_argument("app")
    p.add_argument("--check", metavar="F1,F2", help="verify these field names (exit 1 if any is missing)")
    p = sub.add_parser("rules", parents=[common], help="search the business-rule PDFs (never for field names)")
    p.add_argument("query")
    p.add_argument("--topic", help="limit to one topic, e.g. ACCOUNT (any case; list them with: t24skills topics)")
    p.add_argument("-n", type=int, default=5, help="number of results (default 5)")
    sub.add_parser("topics", parents=[common], help="the topics rules --topic accepts, with PDF and chunk counts")
    p = sub.add_parser("samples", parents=[common], help="list the artefact samples (one golden case per type)")
    p.add_argument("filter", nargs="?", help="only samples whose name, type, group or requirement contains this")
    p.add_argument("--language", choices=["infobasic", "jbc", "java"])
    p = sub.add_parser("sample", parents=[common], help="show one sample: requirement, inputs and generated files")
    p.add_argument("name", help="case name (jbc-local-table) or template id (jbc/local-table)")
    p.add_argument("--file", dest="pick", metavar="FILE", help="print only this file's content")
    p.add_argument("--out", metavar="DIR", help="copy the sample's files into DIR")
    p.add_argument("--force", action="store_true", help="with --out: overwrite files that already exist")
    p = sub.add_parser("template", parents=[common], help="a template's inputs and a ready-to-run generate command")
    p.add_argument("name", nargs="?", help="template id (jbc/validation) or sample name; omit to list them")
    p = sub.add_parser("generate", parents=[common, rel], help="generate an artefact from a template, with a field check")
    p.add_argument("name", help="template id (jbc/validation) or sample name")
    p.add_argument("--set", action="append", metavar="KEY=VALUE", help="an input value (repeatable), e.g. --set APP=CUSTOMER")
    p.add_argument("--inputs", metavar="FILE", help="input values from a JSON file {\"APP\": \"CUSTOMER\", ...}")
    p.add_argument("--from-sample", action="store_true", help="start from the sample's inputs; --set overrides them")
    p.add_argument("--today", metavar="YYYY-MM-DD", help="the date in the file header (default today)")
    p.add_argument("--out", metavar="DIR", help="write the files into DIR (default: print them)")
    p.add_argument("--force", action="store_true", help="with --out: overwrite files that already exist")
    p = sub.add_parser("verify", parents=[common, rel, inst], help="accuracy gate for a generated file")
    p.add_argument("file")
    p.add_argument("--app", action="append", default=[], help="application whose fields it uses (repeatable)")
    p.add_argument("--no-compile", action="store_true", help="field check only")
    p.add_argument("--no-app", action="store_true",
                   help="the file reads no T24 application (a new local table): no fields to check, compile only")
    p = sub.add_parser("golden", parents=[common, rel, inst], help="run the golden cases")
    p.add_argument("--case", help="only this case")
    p = sub.add_parser("diff", parents=[common], help="what changed between two releases")
    p.add_argument("old", nargs="?", default="R23")
    p.add_argument("new", nargs="?", default="R25")
    p.add_argument("--full", action="store_true", help="every changed application, not just the summary")
    sub.add_parser("stages", parents=[common], help="the pipeline stages, in execution order")
    p = sub.add_parser("run", parents=[common, rel], help="run one pipeline stage")
    p.add_argument("stage", choices=list(STAGES))
    p.add_argument("--dry-run", action="store_true", help="print the commands only")
    return ap


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):  # not on a test's captured stream
            stream.reconfigure(encoding="utf-8", errors="replace")
    args = parser().parse_args(argv)
    if getattr(args, "file", None):
        args.file = str(Path(args.file).resolve())  # relative to where the user started, before chdir
    for name in ("out", "inputs"):  # paths are relative to where the user started
        if getattr(args, name, None):
            setattr(args, name, str(Path(getattr(args, name)).resolve()))
    os.chdir(ROOT)
    run, show = COMMANDS[args.command]
    try:
        ok, result = run(args)
        code = 0 if ok else 1
    except CannotRun as exc:
        ok, result, code = False, {"error": {"type": "CANNOT_RUN", "message": str(exc)}}, 2
    if args.json:
        print(json.dumps({"schemaVersion": SCHEMA_VERSION, "command": args.command, "ok": ok, **result},
                         ensure_ascii=False, indent=1))
    elif code == 2:
        print(f"t24skills: {result['error']['message']}", file=sys.stderr)
    else:
        show(result)
    return code


if __name__ == "__main__":
    sys.exit(main())
