#!/usr/bin/env python3
"""Find T24 field references in generated source and check them against
the Layer A schema DB. Legacy Infobasic uses EQU names (AC.CATEGORY);
componentised jBC uses <Comp>.<Module>.<Record>.<Field>, verified against the
component_fields table (component_parse.py) -- NOT the java alias. Without
that table they are left to the compiler. Java L3 code is not checked here --
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


def dotted_prefix(names):
    """Longest common prefix of the field names, cut back to a '.' boundary
    ("AC.CUSTOMER", "AC.CATEGORY" -> "AC."); "" when the names share none."""
    common = os.path.commonprefix(list(names))
    return common[: common.rfind(".") + 1]


def app_prefix(conn, app):
    names = [r[0] for r in conn.execute("SELECT field_name FROM fields WHERE app = ?", (app,))]
    if not names:
        raise UnknownApp(f"no schema rows for app '{app}'")
    return dotted_prefix(names)


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
        r"\b[A-Z]{2,}\.[A-Z][A-Za-z0-9]*\." + re.escape(record_cls) + r"\.[A-Z][A-Za-z0-9]*\b(?!\s*\()"
    )
    componentised = set(comp_pattern.findall(code))
    return FieldRefs(legacy, componentised)


def _has_component_table(conn):
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'component_fields'").fetchone() is not None


def check_fields(conn, app, source):
    """Legacy EQU names are verified against the `fields` table. Componentised
    names (<Comp>.<Module>.<Record>.<Field>) are verified against the
    `component_fields` table built by component_parse.py from the component
    classes -- they are NOT java aliases (EB.CUS.SHORT.NAME is
    ST.Customer.Customer.EbCusShortName, AC.CATEGORY is
    AC.AccountOpening.Account.Category). Without that table they are reported
    as compiler_checked and tCompile decides."""
    app = app.upper()
    refs = extract_refs(source, app_prefix(conn, app), record_class(app))
    names = {r[0] for r in conn.execute("SELECT field_name FROM fields WHERE app = ?", (app,))}
    missing = [f for f in refs.legacy if f not in names]
    verified = [f for f in refs.legacy if f in names]
    compiler_checked = []
    if _has_component_table(conn):
        known = {f"{c}.{r}.{f}" for c, r, f in conn.execute(
            "SELECT component, record, comp_field FROM component_fields WHERE app = ?", (app,))}
        verified += [r for r in refs.componentised if r in known]
        missing += [r for r in refs.componentised if r not in known]
    else:
        compiler_checked = sorted(refs.componentised)
    return FieldCheck(app, sorted(verified), sorted(missing), compiler_checked)
