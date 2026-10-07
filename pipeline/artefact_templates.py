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

from artefact_fields import dotted_prefix, record_class

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


def _has_table(conn, name):
    return conn.execute("SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?", (name,)).fetchone() is not None


def _field_value(language, conn, app, field_name):
    row = conn.execute("SELECT java_alias FROM fields WHERE app = ? AND field_name = ?",
                       (app, field_name)).fetchone()
    if not row:
        raise FieldNotAvailable(f"{field_name} is not a field of {app} in this release")
    if language == "infobasic":
        return field_name, None
    if language == "java":
        # Java templates call rec.get<Field>().getValue() / rec.set<Field>(v). A single-value field
        # takes that as it is; a multi-value field that Java reaches in one indexed step (field_kinds
        # group_getter, from record_parse.py) is rewritten to its first value by java_multi_value().
        suffix = row[0].split("_", 1)[1]
        if _has_table(conn, "field_kinds"):
            access = _java_access(conn, app, field_name)
            if access is None:
                raise FieldNotAvailable(f"{field_name} has no single-value getter on the {app} record class")
            return suffix, None, access
        return suffix, None, ""
    try:
        hit = _primary_jbc_name(conn, app, field_name)
    except Exception:  # no component_fields table
        hit = None
    if not hit:
        raise FieldNotAvailable(f"{field_name} has no componentised (jBC) name in this release")
    return hit


def _java_access(conn, app, field_name):
    """'' for a single-value field, 'MV' for a list of TField, 'MV-GROUP:<getter>:<class>' for a
    member of a multi-value group; None when the record class has no getter. Raises
    FieldNotAvailable for a multi-value field Java cannot reach in one indexed step."""
    columns = {r[1] for r in conn.execute("PRAGMA table_info(field_kinds)")}
    group_col = "group_getter" if "group_getter" in columns else "NULL"
    row = conn.execute(f"SELECT kind, getter_class, {group_col} FROM field_kinds WHERE app = ? AND field_name = ?",
                       (app, field_name)).fetchone()
    if row is None:
        return None
    kind, group_class, group_getter = row
    if kind == "SV":
        return ""
    if group_getter is None:
        raise FieldNotAvailable(f"{field_name} is a multi-value field ({kind}) that Java cannot reach in one "
                                f"step (sub-values, a nested group or a read-only audit field)")
    return "MV" if kind == "MV" else f"MV-GROUP:{group_getter}:{group_class}"


def resolve(template, user_inputs, conn, today):
    values = {k: str(v) for k, v in user_inputs.items()}
    values["TODAY"] = today
    language = template["language"]
    for spec in template["inputs"]:
        if spec.get("kind") != "field" or spec["id"] not in user_inputs:
            continue
        app = user_inputs[spec["of"]].upper()
        equ = user_inputs[spec["id"]].upper()
        value, component, *access = _field_value(language, conn, app, equ)
        values[spec["id"]] = value
        if access and access[0]:
            # rewritten by java_multi_value() at render time; the app input's record package
            # (<OF>_PACKAGE) is where a group class is imported from
            values[f"{spec['id']}_ACCESS"] = f"{access[0]}:{spec['of']}" if access[0] != "MV" else "MV"
        # <ID>_NAME: the field name without the app prefix -- what OFS messages and
        # enquiry/SELECT statements use (FT.CREDIT.ACCT.NO -> CREDIT.ACCT.NO).
        prefix = dotted_prefix([r[0] for r in conn.execute("SELECT field_name FROM fields WHERE app = ?", (app,))])
        values[f"{spec['id']}_NAME"] = equ[len(prefix):] if prefix and equ.startswith(prefix) else equ
        if component:
            # ST.Customer.Customer.EbCusMnemonic -> APP_COMPONENT ST.Customer, APP_RECORD Customer
            values.setdefault(f"{spec['of']}_COMPONENT", component)
            values.setdefault(f"{spec['of']}_RECORD", value[len(component) + 1:].split(".")[0])
    for spec in template["inputs"]:
        if spec.get("kind") == "app" and spec["id"] in user_inputs:
            cls = record_class(user_inputs[spec["id"]].upper())
            values[f"{spec['id']}_CLASS"] = cls          # per app input, e.g. LINK_APP_CLASS
            values[f"{spec['id']}_PACKAGE"] = cls.lower()  # records.<package>.<Class>Record
            values.setdefault("RECORD_CLASS", cls)          # first app input
            values.setdefault("RECORD_PACKAGE", cls.lower())
    return values


def _fill(text, values, missing):
    def sub(m):
        if m.group(1) not in values:
            missing.append(m.group(1))
            return m.group(0)
        return values[m.group(1)]
    return PLACEHOLDER.sub(sub, text)


def _first_import_gap(text):
    lines = text.split("\n")
    last = max((i for i, line in enumerate(lines) if re.match(r"\s*import\s+[\w.]+\s*;", line)), default=None)
    return lines, last


def java_multi_value(text, suffix, access, package):
    """Rewrite the three ways a Java template uses a field -- read (x.get<F>().getValue()), flag
    (x.get<F>().setError(...);) and write (x.set<F>(...);) -- for the field's first value when it
    is multi-value. `access` is 'MV' or 'MV-GROUP:<getter>:<class>'. Reads are guarded (get(0) on
    an empty list throws); writes go through the indexed setter, which grows the list; a group
    member is written on its group, then the group is set back on the record."""
    s = re.escape(suffix)
    if access == "MV":
        def read(v):
            return f'({v}.get{suffix}().isEmpty() ? "" : {v}.get{suffix}(0).getValue())'

        def ensure(ind, v):
            return f'{ind}if ({v}.get{suffix}().isEmpty()) {{\n{ind}    {v}.set{suffix}("", 0);\n{ind}}}\n'

        def element(v):
            return f"{v}.get{suffix}(0)"

        def write(ind, v, arg):
            return f"{ind}{v}.set{suffix}({arg}, 0);"
        group_class = None
    else:
        _, getter, group_class = access.split(":")

        def read(v):
            return f'({v}.get{getter}().isEmpty() ? "" : {v}.get{getter}(0).get{suffix}().getValue())'

        def ensure(ind, v):
            return f"{ind}if ({v}.get{getter}().isEmpty()) {{\n{ind}    {v}.set{getter}(new {group_class}(), 0);\n{ind}}}\n"

        def element(v):
            return f"{v}.get{getter}(0).get{suffix}()"

        def write(ind, v, arg):
            return (f"{ind}{group_class} group{suffix} = {v}.get{getter}().isEmpty() ? new {group_class}() : "
                    f"{v}.get{getter}(0);\n{ind}group{suffix}.set{suffix}({arg});\n{ind}{v}.set{getter}(group{suffix}, 0);")
    out = re.sub(rf"^([ \t]*)(\w+)\.set{s}\((.*)\);[ \t]*$", lambda m: write(m[1], m[2], m[3]), text, flags=re.M)
    out = re.sub(rf"^([ \t]*)(\w+)\.get{s}\(\)\.setError\((.*)\);[ \t]*$",
                 lambda m: ensure(m[1], m[2]) + f"{m[1]}{element(m[2])}.setError({m[3]});", out, flags=re.M)
    out = re.sub(rf"\b(\w+)\.get{s}\(\)\.getValue\(\)", lambda m: read(m[1]), out)
    if group_class and out != text:
        line = f"import com.temenos.t24.api.records.{package}.{group_class};"
        lines, last = _first_import_gap(out)
        if line not in lines and last is not None:
            lines.insert(last + 1, line)
            out = "\n".join(lines)
    return out


def _multi_value_fields(values):
    """[(field value, access, record package)] of every multi-value Java field in `values`."""
    found = []
    for key, access in values.items():
        if key.endswith("_ACCESS") and key[:-7] in values:
            kind, _, of = access.rpartition(":") if access != "MV" else (access, "", "")
            package = values.get(f"{of}_PACKAGE", "") if of else ""
            found.append((values[key[:-7]], kind or access, package))
    return found


def render(template, values):
    missing, out = [], {}
    for name, content in template["files"].items():
        out[_fill(name, values, missing)] = _fill(content, values, missing)
    if missing:
        raise MissingInputs(missing)
    for suffix, access, package in _multi_value_fields(values):
        for name in out:
            if name.endswith(".java"):
                out[name] = java_multi_value(out[name], suffix, access, package)
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
                    # compiled: the golden case passed the R25 compile gate. A proven template whose case says
                    # "compiled": false renders and field-checks, but has never been compiled on T24.
                    entry.update(proven=True, template=tid, compiled=case.get("compiled", True))
            types.append(entry)
        languages.append({"id": lang["id"], "label": lang["label"], "types": types})
    doc = {"schemaVersion": TEMPLATES_SCHEMA_VERSION, "languages": languages, "templates": exported}
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return doc
