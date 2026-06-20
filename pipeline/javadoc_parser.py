from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

_SKIP_STEMS = frozenset({
    'index', 'index-all', 'index2', 'overview-summary', 'overview-frame',
    'overview-tree', 'allclasses-frame', 'allclasses-noframe', 'package-summary',
    'package-frame', 'package-tree', 'deprecated-list', 'help-doc',
    'constant-values', 'serialized-form',
})

_TAG_RE = re.compile(r'<[^>]{0,500}>')
_MAX_FILE_BYTES = 500_000
_WORKERS = 8


def _strip_tags(s: str) -> str:
    return _TAG_RE.sub(' ', s).strip()


def _fqcn_from_path(html_file: Path, base_dir: Path) -> str:
    """Derive dotted FQCN from HTML file path relative to base_dir."""
    return '.'.join(html_file.relative_to(base_dir).with_suffix('').parts)


def _parse_page(html_content: str) -> dict | None:
    """
    Fast regex-based Javadoc HTML class page parser.
    Returns {'description': str, 'methods': {name: str}} or None if not a class page.
    """
    # Quick reject using only the first 3 KB (title always appears in header)
    head = html_content[:3072]
    if 'class="title"' not in head and "class='title'" not in head:
        return None
    if not re.search(r'(?:Class|Interface|Enum|Annotation)\s+\w', head, re.IGNORECASE):
        return None

    # Description: find div.description then first div.block within it
    description = ''
    idx = html_content.find('class="description"')
    if idx == -1:
        idx = html_content.find("class='description'")
    if idx != -1:
        chunk = html_content[idx: idx + 6000]
        bi = chunk.find('<div class="block">')
        if bi == -1:
            bi = chunk.find("<div class='block'>")
        if bi != -1:
            end_tag = '</div>'
            ei = chunk.find(end_tag, bi + 19)
            if ei != -1:
                description = _strip_tags(chunk[bi + 19: ei])[:500]

    # Method descriptions from anchor name patterns (old-style Javadoc)
    methods: dict[str, str] = {}
    for m in re.finditer(r'<a\s+name=["\']([a-zA-Z_$][^"\']{0,80})["\']', html_content):
        raw_name: str = m.group(1)
        method_name = raw_name.split('-')[0]
        if not re.match(r'^[a-zA-Z_$]', method_name):
            continue
        nearby = html_content[m.end(): m.end() + 2000]
        bi = nearby.find('<div class="block">')
        if bi == -1:
            bi = nearby.find("<div class='block'>")
        if bi != -1:
            ei = nearby.find('</div>', bi + 19)
            if ei != -1:
                methods[method_name] = _strip_tags(nearby[bi + 19: ei])[:300]

    return {'description': description, 'methods': methods}


def _process_file(html_file: Path, base_dir: Path) -> tuple[str, dict] | None:
    """Read and parse one HTML file; return (fqcn, data) or None to skip."""
    try:
        if html_file.stat().st_size > _MAX_FILE_BYTES:
            return None
        content = html_file.read_text(encoding='utf-8', errors='ignore')
        data = _parse_page(content)
        if data is None:
            return None
        return _fqcn_from_path(html_file, base_dir), data
    except OSError:
        return None


def parse_javadoc_dir(javadoc_dir: Path) -> dict:
    """
    Walk a Javadoc HTML tree and return a dict keyed by FQCN.
    Result: { fqcn: {'description': str, 'methods': {method_name: str}} }
    Uses a thread pool for parallel I/O.
    """
    files = [
        f for f in javadoc_dir.rglob('*.html')
        if f.stem not in _SKIP_STEMS and not f.stem.startswith('exportPDF')
    ]

    result: dict = {}
    with ThreadPoolExecutor(max_workers=_WORKERS) as pool:
        futures = {pool.submit(_process_file, f, javadoc_dir): f for f in files}
        for future in as_completed(futures):
            entry = future.result()
            if entry is not None:
                fqcn, data = entry
                result[fqcn] = data
    return result
