from __future__ import annotations

import re
import subprocess
import tempfile
import zipfile
from pathlib import Path


def parse_javap_output(output: str) -> dict:
    """Parse raw stdout from `javap -p` into a structured class dict."""
    result: dict = {
        'name': '',
        'superclass': '',
        'interfaces': [],
        'annotations': [],
        'methods': [],
        'fields': [],
        'is_interface': False,
    }

    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line or line.startswith('Compiled from') or line in ('{', '}'):
            continue

        # Class / interface / enum declaration
        decl = re.match(
            r'(?:(?:public|protected|private|abstract|final|strictfp)\s+)*'
            r'(class|interface|enum|@interface)\s+'
            r'([\w.$]+)'
            r'(?:\s+extends\s+([\w.$]+(?:\s*,\s*[\w.$]+)*))?'
            r'(?:\s+implements\s+([\w.$]+(?:\s*,\s*[\w.$]+)*))?'
            r'\s*\{?\s*$',
            line,
        )
        if decl:
            result['is_interface'] = decl.group(1) == 'interface'
            result['name'] = decl.group(2)
            if decl.group(3):
                result['superclass'] = decl.group(3).strip().split(',')[0].strip()
            if decl.group(4):
                result['interfaces'] = [i.strip() for i in decl.group(4).split(',')]
            continue

        # Method (has parentheses, ends with ;)
        if '(' in line and line.endswith(';'):
            method = re.match(
                r'(?:(?:public|protected|private|static|final|abstract|'
                r'native|synchronized|default)\s+)*'
                r'(?:<[^>]+>\s+)?'
                r'([\w.$\[\]]+(?:<[^>]*>)?)'
                r'\s+([\w$]+)'
                r'\s*\(([^)]*)\)'
                r'(?:\s+throws\s+[\w.$,\s]+)?'
                r'\s*;?\s*$',
                line,
            )
            if method:
                method_name = method.group(2)
                # Skip constructors (simple name matches enclosing class)
                class_simple = result['name'].rsplit('.', 1)[-1] if result['name'] else ''
                if method_name == class_simple:
                    continue
                params_raw = method.group(3).strip()
                params = [p.strip() for p in params_raw.split(',')] if params_raw else []
                visibility = (
                    'public' if 'public' in line else
                    'protected' if 'protected' in line else
                    'private' if 'private' in line else
                    'package'
                )
                result['methods'].append({
                    'name': method_name,
                    'return_type': method.group(1).strip(),
                    'params': params,
                    'visibility': visibility,
                })
            continue

        # Field (no parentheses, ends with ;)
        if '(' not in line and line.endswith(';'):
            field = re.match(
                r'(?:(?:public|protected|private|static|final|'
                r'volatile|transient|native)\s+)*'
                r'([\w.$\[\]]+(?:<[^>]*>)?)'
                r'\s+([\w$]+)'
                r'\s*;?\s*$',
                line,
            )
            if field:
                visibility = (
                    'public' if 'public' in line else
                    'protected' if 'protected' in line else
                    'private' if 'private' in line else
                    'package'
                )
                result['fields'].append({
                    'name': field.group(2),
                    'type': field.group(1).strip(),
                    'visibility': visibility,
                })

    return result


_JAVAP_BATCH = 100  # class files per JVM invocation


def _split_javap_blocks(output: str) -> list[str]:
    """Split combined javap output for multiple classes into per-class blocks.

    Handles both 'Compiled from' style output and bare class declarations by
    tracking brace depth — a block ends when the top-level '}' closes.
    """
    blocks: list[str] = []
    current: list[str] = []
    depth = 0
    for line in output.splitlines():
        stripped = line.strip()
        # 'Compiled from' marks the start of a new class (some javap versions)
        if stripped.startswith('Compiled from ') and depth == 0 and current:
            block = '\n'.join(current).strip()
            if '{' in block:
                blocks.append(block)
            current = []
        current.append(line)
        depth += stripped.count('{') - stripped.count('}')
        depth = max(0, depth)
        # Top-level closing brace: class body complete
        if depth == 0 and stripped == '}':
            block = '\n'.join(current).strip()
            if '{' in block:
                blocks.append(block)
            current = []
    if current:
        block = '\n'.join(current).strip()
        if '{' in block:
            blocks.append(block)
    return blocks


def extract_classes_from_jar(jar_path: Path) -> list[dict]:
    """Extract all non-inner-class metadata from a JAR using batched `javap -p` calls.

    Batches _JAVAP_BATCH classes per JVM invocation to amortise startup cost.
    """
    classes: list[dict] = []
    with zipfile.ZipFile(jar_path, 'r') as zf:
        entries = [e for e in zf.namelist() if e.endswith('.class') and '$' not in e]
        if not entries:
            return classes
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            for entry in entries:
                zf.extract(entry, tmpdir)
            for i in range(0, len(entries), _JAVAP_BATCH):
                batch = entries[i: i + _JAVAP_BATCH]
                class_files = [str(tmp / e) for e in batch]
                try:
                    proc = subprocess.run(
                        ['javap', '-p'] + class_files,
                        capture_output=True, text=True, timeout=120,
                    )
                    if proc.returncode == 0 and proc.stdout:
                        for block in _split_javap_blocks(proc.stdout):
                            cls = parse_javap_output(block)
                            if cls['name']:
                                classes.append(cls)
                except (subprocess.TimeoutExpired, OSError):
                    # Fallback: process each class file individually
                    for class_file in class_files:
                        try:
                            proc = subprocess.run(
                                ['javap', '-p', class_file],
                                capture_output=True, text=True, timeout=15,
                            )
                            if proc.returncode == 0 and proc.stdout:
                                cls = parse_javap_output(proc.stdout)
                                if cls['name']:
                                    classes.append(cls)
                        except (subprocess.TimeoutExpired, OSError):
                            pass
    return classes
