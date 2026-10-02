#!/usr/bin/env python3
"""Artefact templates: the user's own source templates with {{PLACEHOLDER}}s.

templates/<language>/<type>/template.json describes the inputs; every other
file in that folder is a source file whose *name* and *content* may contain
placeholders. resolve() turns the developer's inputs into placeholder values
for one release (a `field` input becomes the EQU name for Infobasic, the
componentised name for jBC, the getter suffix for Java; APP_COMPONENT,
RECORD_CLASS, RECORD_PACKAGE and TODAY are derived). render() fills them in
and refuses to leave any {{X}} behind.

A template is *proven* when rendering its golden case's userInputs reproduces
that golden case's files byte-for-byte (prove()); the golden files themselves
are field-checked and compiled by run_golden.py. T24Tools re-implements
resolve/render in JS and must match these rules.
"""
import json
import re
from pathlib import Path

from artefact_fields import record_class

TEMPLATES = Path("templates")
PLACEHOLDER = re.compile(r"{{([A-Z_]+)}}")


class MissingInputs(ValueError):
    def __init__(self, missing):
        self.missing = sorted(set(missing))
        super().__init__("missing inputs: " + ", ".join(self.missing))


class FieldNotAvailable(ValueError):
    pass


def load_templates(root=TEMPLATES):
    templates = []
    for meta in sorted(Path(root).glob("*/*/template.json")):
        t = json.loads(meta.read_text(encoding="utf-8"))
        t["files"] = {p.name: p.read_text(encoding="utf-8")
                      for p in sorted(meta.parent.iterdir()) if p.name != "template.json" and p.is_file()}
        templates.append(t)
    return templates


def _primary_jbc_name(conn, app, field_name):
    rows = conn.execute(
        "SELECT component, record, comp_field FROM component_fields WHERE app = ? AND field_name = ?",
        (app, field_name)).fetchall()
    if not rows:
        return None
    counts = dict(conn.execute(
        "SELECT component, COUNT(*) FROM component_fields WHERE app = ? GROUP BY component", (app,)).fetchall())
    comp, record, field = sorted(rows, key=lambda r: (-counts.get(r[0], 0), r[0]))[0]
    return f"{comp}.{record}.{field}", comp


def _field_value(language, conn, app, field_name):
    row = conn.execute("SELECT java_alias FROM fields WHERE app = ? AND field_name = ?",
                       (app, field_name)).fetchone()
    if not row:
        raise FieldNotAvailable(f"{field_name} is not a field of {app} in this release")
    if language == "infobasic":
        return field_name, None
    if language == "java":
        return row[0].split("_", 1)[1], None
    try:
        hit = _primary_jbc_name(conn, app, field_name)
    except Exception:  # no component_fields table
        hit = None
    if not hit:
        raise FieldNotAvailable(f"{field_name} has no componentised (jBC) name in this release")
    return hit


def resolve(template, user_inputs, conn, today):
    values = {k: str(v) for k, v in user_inputs.items()}
    values["TODAY"] = today
    language = template["language"]
    for spec in template["inputs"]:
        if spec.get("kind") != "field" or spec["id"] not in user_inputs:
            continue
        app = user_inputs[spec["of"]].upper()
        value, component = _field_value(language, conn, app, user_inputs[spec["id"]].upper())
        values[spec["id"]] = value
        if component:
            values.setdefault("APP_COMPONENT", component)
    for spec in template["inputs"]:
        if spec.get("kind") == "app" and spec["id"] in user_inputs:
            cls = record_class(user_inputs[spec["id"]].upper())
            values.setdefault("RECORD_CLASS", cls)
            values.setdefault("RECORD_PACKAGE", cls.lower())
    return values


def _fill(text, values, missing):
    def sub(m):
        if m.group(1) not in values:
            missing.append(m.group(1))
            return m.group(0)
        return values[m.group(1)]
    return PLACEHOLDER.sub(sub, text)


def render(template, values):
    missing, out = [], {}
    for name, content in template["files"].items():
        out[_fill(name, values, missing)] = _fill(content, values, missing)
    if missing:
        raise MissingInputs(missing)
    return out


def golden_case(template, golden_root=Path("tests/golden")):
    for case_json in sorted(Path(golden_root).glob("*/case.json")):
        case = json.loads(case_json.read_text(encoding="utf-8"))
        if case.get("template") == template["id"]:
            case["dir"] = case_json.parent
            return case
    return None


def prove(template, conn, golden_root=Path("tests/golden")):
    """(proven, reason). Proven = rendering the golden case's userInputs reproduces its files exactly."""
    case = golden_case(template, golden_root)
    if not case:
        return False, "no golden case"
    try:
        out = render(template, resolve(template, case["userInputs"], conn, case["today"]))
    except (MissingInputs, FieldNotAvailable) as exc:
        return False, str(exc)
    for name, content in out.items():
        golden = case["dir"] / name
        if not golden.is_file():
            return False, f"golden case has no {name}"
        if golden.read_text(encoding="utf-8").replace("\r\n", "\n") != content.replace("\r\n", "\n"):
            return False, f"{name} differs from the golden file"
    return True, "matches golden case " + case["name"]


CATALOGUE = TEMPLATES / "catalogue.json"
TEMPLATES_SCHEMA_VERSION = 1


def export_templates(out, catalogue=CATALOGUE, root=TEMPLATES, conns=None, golden_root=Path("tests/golden")):
    """Write templates.json for T24Tools: the language/type catalogue with
    `proven` computed here (never hand-set) plus each template's files and its
    golden case (userInputs, values resolved per release, expected output) so
    the JS renderer can be tested for parity. A template is proven only if it
    proves against every release DB in `conns`."""
    conns = conns or {}
    templates = {t["id"]: t for t in load_templates(root)}
    cat = json.loads(Path(catalogue).read_text(encoding="utf-8"))
    exported, languages = {}, []
    for lang in cat["languages"]:
        types = []
        for typ in lang["types"]:
            tid = f"{lang['id']}/{typ['id']}"
            entry = {"id": typ["id"], "label": typ["label"], "proven": False}
            template = templates.get(tid)
            if template:
                results = {rel: prove(template, conn, golden_root) for rel, conn in conns.items()}
                proven = bool(results) and all(ok for ok, _ in results.values())
                if not proven:
                    print(f"WARNING: template {tid} not proven: "
                          + "; ".join(f"{rel}: {why}" for rel, (ok, why) in results.items() if not ok)
                          + ("no release DB to prove against" if not results else ""))
                else:
                    case = golden_case(template, golden_root)
                    resolved = {rel: resolve(template, case["userInputs"], conn, case["today"])
                                for rel, conn in conns.items()}
                    exported[tid] = {
                        **{k: v for k, v in template.items() if k != "files"},
                        "files": template["files"],
                        "golden": {"case": case["name"], "userInputs": case["userInputs"], "today": case["today"],
                                   "resolved": resolved,
                                   "output": render(template, next(iter(resolved.values())))},
                    }
                    entry.update(proven=True, template=tid)
            types.append(entry)
        languages.append({"id": lang["id"], "label": lang["label"], "types": types})
    doc = {"schemaVersion": TEMPLATES_SCHEMA_VERSION, "languages": languages, "templates": exported}
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return doc
