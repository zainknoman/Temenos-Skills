#!/usr/bin/env python3
"""Find T24 field references in generated source and check them against
the Layer A schema DB. Legacy Infobasic uses EQU names (AC.CATEGORY);
componentised jBC uses <Comp>.<Module>.<Record>.<Field>, whose <Field> part is
NOT the java alias (see check_fields) -- those are listed for the compiler to
check. Java L3 code is not checked here --
javac against the R25 record classes is the field gate for Java."""
import os
import re
from collections import namedtuple

FieldRefs = namedtuple("FieldRefs", "legacy componentised")
FieldCheck = namedtuple("FieldCheck", "app verified missing compiler_checked")


class UnknownApp(Exception):
    pass


def record_class(app):
    return "".join(part.capitalize() for part in app.split("."))


def app_prefix(conn, app):
    names = [r[0] for r in conn.execute("SELECT field_name FROM fields WHERE app = ?", (app,))]
    if not names:
        raise UnknownApp(f"no schema rows for app '{app}'")
    common = os.path.commonprefix(names)
    return common[: common.rfind(".") + 1]


def _strip_comments(source):
    lines = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("*") or stripped.startswith("!"):
            continue
        lines.append(line.split(";*")[0])
    return "\n".join(lines)


def extract_refs(source, prefix, record_cls):
    code = _strip_comments(source)
    legacy = set()
    if prefix:
        pattern = re.compile(r"(?<![\w.])" + re.escape(prefix) + r"[A-Z0-9]+(?:\.[A-Z0-9]+)*(?![\w.(])")
        legacy = set(pattern.findall(code))
    comp_pattern = re.compile(
        r"\b[A-Z]{2,}\.[A-Z][A-Za-z0-9]*\." + re.escape(record_cls) + r"\.([A-Z][A-Za-z0-9]*)\b(?!\s*\()"
    )
    componentised = {f"{record_cls}_{m}" for m in comp_pattern.findall(code)}
    return FieldRefs(legacy, componentised)


def check_fields(conn, app, source):
    """Legacy EQU names are verified against the schema DB. Componentised names
    are NOT java aliases -- R25 maps EB.CUS.SHORT.NAME to Customer.EbCusShortName
    but AC.CATEGORY to Account.Category -- so they are reported as compiler_checked
    and left to tCompile, which rejects unknown ones ("X undefined in ST.Customer")."""
    app = app.upper()
    cls = record_class(app)
    refs = extract_refs(source, app_prefix(conn, app), cls)
    names = {r[0] for r in conn.execute("SELECT field_name FROM fields WHERE app = ?", (app,))}
    missing = sorted(f for f in refs.legacy if f not in names)
    verified = sorted(refs.legacy - set(missing))
    compiler_checked = sorted(a.replace(f"{cls}_", f"{cls}.", 1) for a in refs.componentised)
    return FieldCheck(app, verified, missing, compiler_checked)
