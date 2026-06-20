from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def compute_jar_hash(jar_path: Path) -> str:
    """Return the SHA-256 hex digest of the JAR file bytes."""
    return hashlib.sha256(jar_path.read_bytes()).hexdigest()


def is_cache_current(jar_path: Path, cache_dir: Path) -> bool:
    """True if cache JSON exists and its stored hash matches the current JAR."""
    cache_file = cache_dir / (jar_path.stem + '.json')
    if not cache_file.exists():
        return False
    try:
        data = json.loads(cache_file.read_text(encoding='utf-8'))
        return data.get('hash') == compute_jar_hash(jar_path)
    except (json.JSONDecodeError, KeyError, OSError):
        return False


def write_jar_cache(jar_path: Path, cache_dir: Path, classes: list[dict]) -> None:
    """Write extracted class list for jar_path to cache_dir/<stem>.json."""
    stem = jar_path.stem
    prefix = stem.split('_')[0] if '_' in stem else stem
    payload = {
        'jar': jar_path.name,
        'prefix': prefix,
        'hash': compute_jar_hash(jar_path),
        'extracted_at': datetime.now(timezone.utc).isoformat(),
        'classes': classes,
    }
    (cache_dir / (stem + '.json')).write_text(
        json.dumps(payload, indent=2), encoding='utf-8'
    )
