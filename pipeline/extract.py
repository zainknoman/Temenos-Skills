#!/usr/bin/env python3
"""
extract.py — Phase 1 of the Temenos T24 knowledge pipeline.

Reads 2,050 T24 JAR files in parallel, extracts class and method metadata
from every .class file, and writes one JSON cache file per JAR.

Subsequent runs skip unchanged JARs (SHA-256 incremental cache).

Usage:
    python extract.py --jars jar/t24lib --cache cache --workers 8

Output (one file per JAR):
    cache/<jar-stem>.json

Each JSON file contains:
    {
        "jar":      "AA_ContractApi.jar",
        "sha256":   "abc123...",
        "classes":  [
            {
                "name":        "Contract",
                "package":     "com.temenos.t24.api.arrangement.accounting",
                "qualified":   "com.temenos.t24.api.arrangement.accounting.Contract",
                "superclass":  "",
                "interfaces":  [],
                "is_interface": false,
                "is_abstract":  false,
                "is_public":    true,
                "component_type": "public-api",   # classifier (see classify_component)
                "domain":      "aa",
                "methods": [
                    {
                        "name":        "setContractId",
                        "return_type": "void",
                        "params":      ["java.lang.String"],
                        "is_public":   true,
                        "is_static":   false,
                        "is_abstract": false
                    },
                    ...
                ],
                "fields": [
                    {
                        "name":      "contractId",
                        "type":      "java.lang.String",
                        "is_public": false,
                        "is_static": false
                    }
                ]
            }
        ]
    }

Requirements:
    pip install javatools
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from io import BytesIO
from pathlib import Path
from typing import Optional

try:
    from javatools import unpack_class, ClassUnpackException
except ImportError:
    sys.exit(
        "ERROR: javatools not installed.\n"
        "Run:  pip install javatools"
    )

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("extract")


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class MethodInfo:
    name: str
    return_type: str
    params: list[str]
    is_public: bool
    is_static: bool
    is_abstract: bool


@dataclass
class FieldInfo:
    name: str
    type: str
    is_public: bool
    is_static: bool


@dataclass
class ClassInfo:
    name: str                   # simple name, e.g. "Contract"
    package: str                # e.g. "com.temenos.t24.api.arrangement.accounting"
    qualified: str              # package.name
    superclass: str
    interfaces: list[str]
    is_interface: bool
    is_abstract: bool
    is_public: bool
    component_type: str         # classified bucket (see classify_component)
    domain: str                 # t24 domain tag
    methods: list[MethodInfo] = field(default_factory=list)
    fields: list[FieldInfo] = field(default_factory=list)


@dataclass
class JarResult:
    jar: str
    sha256: str
    classes: list[ClassInfo]
    error: Optional[str] = None


# ---------------------------------------------------------------------------
# Component classifier — 11 rules matching the original pipeline heuristics
# ---------------------------------------------------------------------------
_COMPONENT_RULES: list[tuple[list[str], str]] = [
    # Rule 1 — explicit public API JARs
    (["Api.jar", "API.jar"],                     "public-api"),
    # Rule 2 — hook interfaces (lifecycle, validation, event)
    (["Hook.jar", "Lifecycle.jar"],              "hook"),
    # Rule 3 — service JARs (t24service suffix)
    (["t24service.jar"],                         "service"),
    # Rule 4 — data / DTO JARs
    (["-Data.jar", "Record.jar"],                "data"),
    # Rule 5 — test JARs
    (["test", "Test", "spec", "Spec"],           "test"),
    # Rule 6 — foundation / framework
    (["Foundation.jar", "Framework.jar",
      "Platform.jar", "Core.jar"],               "framework"),
    # Rule 7 — integration / connector
    (["Connect.jar", "Connector.jar",
      "Adapter.jar", "Integration.jar"],         "integration"),
    # Rule 8 — CA / custom add-on prefix
    (["CA"],                                     "custom"),
    # Rule 9 — installer / tooling
    (["Installer.jar", "Plugin.jar",
      "Tool.jar", "Studio.jar"],                 "tooling"),
    # Rule 10 — report / batch
    (["Report.jar", "Batch.jar", "COB.jar"],    "batch"),
    # Rule 11 — fallback
    ([],                                         "internal"),
]


def classify_component(jar_name: str) -> str:
    for patterns, label in _COMPONENT_RULES:
        if not patterns:          # fallback rule
            return label
        if any(p in jar_name for p in patterns):
            return label
    return "internal"


# ---------------------------------------------------------------------------
# Domain mapper — infer T24 module from package / JAR prefix
# ---------------------------------------------------------------------------
_DOMAIN_MAP: dict[str, str] = {
    "com.temenos.t24.api.arrangement":  "aa",
    "com.temenos.t24.api.account":      "accounts",
    "com.temenos.t24.api.accounting":   "accounts",
    "com.temenos.t24.api.contract":     "lending",
    "com.temenos.services.customer":    "customer",
    "com.temenos.services.dda":         "accounts",
    "com.temenos.t24.api.payment":      "payments",
    "com.temenos.t24.api.securities":   "securities",
    "com.temenos.hook":                 "hook",
    "com.temenos.t24.api.hook":         "hook",
    "com.temenos.services":             "service",
}

_JAR_PREFIX_DOMAIN: dict[str, str] = {
    "AA_": "aa",
    "AC_": "accounts",
    "FT_": "payments",
    "LD_": "lending",
    "ST_": "customer",
    "SC_": "securities",
    "PP_": "payments",
    "TP_": "tph",
    "TT_": "atm",
    "EB_": "core",
    "RE_": "reporting",
    "PW_": "workflow",
    "IF_": "integration",
    "DE_": "de",
    "DS_": "tooling",
    "IN_": "regulatory",
    "IA_": "accounting",
}


def infer_domain(package: str, jar_name: str) -> str:
    # Package-based (most precise)
    for prefix, domain in _DOMAIN_MAP.items():
        if package.startswith(prefix):
            return domain
    # JAR prefix (fallback)
    for prefix, domain in _JAR_PREFIX_DOMAIN.items():
        if jar_name.startswith(prefix):
            return domain
    return "misc"


# ---------------------------------------------------------------------------
# Type prettifier — convert JVM descriptor to human-readable Java type
# ---------------------------------------------------------------------------
_PRIMITIVES = {
    "B": "byte",
    "C": "char",
    "D": "double",
    "F": "float",
    "I": "int",
    "J": "long",
    "S": "short",
    "V": "void",
    "Z": "boolean",
}


def pretty_jvm_type(descriptor: str) -> str:
    """Convert a JVM type descriptor like Ljava/lang/String; to java.lang.String."""
    if not descriptor:
        return ""
    arrays = 0
    while descriptor.startswith("["):
        arrays += 1
        descriptor = descriptor[1:]
    if descriptor in _PRIMITIVES:
        base = _PRIMITIVES[descriptor]
    elif descriptor.startswith("L") and descriptor.endswith(";"):
        base = descriptor[1:-1].replace("/", ".")
    else:
        base = descriptor.replace("/", ".")
    return base + ("[]" * arrays)


# ---------------------------------------------------------------------------
# Core class-file parser
# ---------------------------------------------------------------------------

def parse_class_bytes(data: bytes, jar_name: str) -> Optional[ClassInfo]:
    """Parse a single .class file's bytes into a ClassInfo."""
    try:
        ci = unpack_class(BytesIO(data))
    except Exception:
        return None

    if not ci.is_public():
        return None  # skip non-public classes entirely

    qualified = ci.pretty_this().replace("/", ".")
    if "." in qualified:
        package, _, simple_name = qualified.rpartition(".")
    else:
        package, simple_name = "", qualified

    superclass = ""
    try:
        s = ci.pretty_super()
        if s and s != "java/lang/Object":
            superclass = s.replace("/", ".")
    except Exception:
        pass

    interfaces: list[str] = []
    try:
        for iface in ci.get_interfaces():
            interfaces.append(iface.replace("/", "."))
    except Exception:
        pass

    component_type = classify_component(jar_name)
    domain = infer_domain(package, jar_name)

    methods: list[MethodInfo] = []
    try:
        for m in ci.methods:
            if not m.is_public():
                continue
            if m.get_name() in ("<init>", "<clinit>"):
                continue   # skip constructors and static initializers
            try:
                ret = pretty_jvm_type(m.get_type_descriptor())
                params = [pretty_jvm_type(p) for p in m.get_arg_type_descriptors()]
                methods.append(MethodInfo(
                    name=m.get_name(),
                    return_type=ret,
                    params=params,
                    is_public=True,
                    is_static=m.is_static(),
                    is_abstract=m.is_abstract(),
                ))
            except Exception:
                continue
    except Exception:
        pass

    fields_out: list[FieldInfo] = []
    try:
        for f in ci.fields:
            try:
                fields_out.append(FieldInfo(
                    name=f.get_name(),
                    type=pretty_jvm_type(f.get_type_descriptor()),
                    is_public=f.is_public(),
                    is_static=f.is_static(),
                ))
            except Exception:
                continue
    except Exception:
        pass

    return ClassInfo(
        name=simple_name,
        package=package,
        qualified=qualified,
        superclass=superclass,
        interfaces=interfaces,
        is_interface=ci.is_interface(),
        is_abstract=ci.is_abstract(),
        is_public=True,
        component_type=component_type,
        domain=domain,
        methods=methods,
        fields=fields_out,
    )


# ---------------------------------------------------------------------------
# JAR processor
# ---------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def process_jar(jar_path: Path, cache_dir: Path) -> JarResult:
    jar_name = jar_path.name
    cache_file = cache_dir / (jar_path.stem + ".json")

    # --- Incremental: skip if cached and hash matches ---
    sha = sha256_file(jar_path)
    if cache_file.exists():
        try:
            with open(cache_file, encoding="utf-8") as f:
                cached = json.load(f)
            if cached.get("sha256") == sha:
                log.debug("  SKIP  %s (unchanged)", jar_name)
                classes = [ClassInfo(**{
                    **c,
                    "methods": [MethodInfo(**m) for m in c["methods"]],
                    "fields":  [FieldInfo(**fi) for fi in c["fields"]],
                }) for c in cached["classes"]]
                return JarResult(jar=jar_name, sha256=sha, classes=classes)
        except Exception:
            pass  # re-process if cache is corrupt

    # --- Parse the JAR ---
    classes: list[ClassInfo] = []
    try:
        with zipfile.ZipFile(jar_path, "r") as zf:
            for entry in zf.infolist():
                if not entry.filename.endswith(".class"):
                    continue
                try:
                    data = zf.read(entry.filename)
                except Exception:
                    continue
                ci = parse_class_bytes(data, jar_name)
                if ci:
                    classes.append(ci)
    except zipfile.BadZipFile as e:
        return JarResult(jar=jar_name, sha256=sha, classes=[], error=str(e))
    except Exception as e:
        return JarResult(jar=jar_name, sha256=sha, classes=[], error=str(e))

    # --- Write cache ---
    result = JarResult(jar=jar_name, sha256=sha, classes=classes)
    payload = {
        "jar":     jar_name,
        "sha256":  sha,
        "classes": [
            {**asdict(c),
             "methods": [asdict(m) for m in c.methods],
             "fields":  [asdict(fi) for fi in c.fields]}
            for c in classes
        ],
    }
    tmp = cache_file.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))
    tmp.replace(cache_file)

    log.debug("  DONE  %s — %d public classes", jar_name, len(classes))
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Phase 1: extract class/method metadata from T24 JARs."
    )
    ap.add_argument("--jars",    required=True,
                    help="Directory containing T24 JAR files (searched recursively)")
    ap.add_argument("--cache",   required=True,
                    help="Output directory for JSON cache files")
    ap.add_argument("--workers", type=int, default=8,
                    help="Parallel worker threads (default: 8)")
    ap.add_argument("--verbose", action="store_true",
                    help="Show per-class debug output")
    args = ap.parse_args()

    if args.verbose:
        log.setLevel(logging.DEBUG)

    jars_dir  = Path(args.jars)
    cache_dir = Path(args.cache)

    if not jars_dir.is_dir():
        sys.exit(f"ERROR: --jars directory not found: {jars_dir}")
    cache_dir.mkdir(parents=True, exist_ok=True)

    jar_paths = sorted(jars_dir.rglob("*.jar"))
    if not jar_paths:
        sys.exit(f"ERROR: No JAR files found under {jars_dir}")

    log.info("Found %d JAR files — processing with %d workers", len(jar_paths), args.workers)

    total_classes  = 0
    total_methods  = 0
    errors         = 0
    processed      = 0

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_jar, p, cache_dir): p for p in jar_paths}
        for i, future in enumerate(as_completed(futures), 1):
            jar_path = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                log.error("FATAL %s: %s", jar_path.name, exc)
                errors += 1
                continue

            if result.error:
                log.warning("ERROR %s: %s", result.jar, result.error)
                errors += 1
            else:
                nc = len(result.classes)
                nm = sum(len(c.methods) for c in result.classes)
                total_classes += nc
                total_methods += nm
                processed += 1

            # Progress every 50 JARs
            if i % 50 == 0 or i == len(jar_paths):
                log.info(
                    "  [%d/%d]  classes so far: %d  methods: %d  errors: %d",
                    i, len(jar_paths), total_classes, total_methods, errors,
                )

    log.info("─" * 60)
    log.info("Complete.")
    log.info("  JARs processed : %d / %d (%d errors)", processed, len(jar_paths), errors)
    log.info("  Classes found  : %d", total_classes)
    log.info("  Methods found  : %d", total_methods)
    log.info("  Cache written  : %s/", cache_dir)


if __name__ == "__main__":
    main()
