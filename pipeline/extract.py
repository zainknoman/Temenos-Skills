"""Phase 1: Extract class metadata from JARs and JavaDoc -> cache/

Usage:
    python pipeline/extract.py --jars jar/t24lib --javadoc T24.javadoc/T24.javadoc --cache cache
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from pipeline.cache_utils import is_cache_current, write_jar_cache
from pipeline.javadoc_parser import parse_javadoc_dir
from pipeline.javap_parser import extract_classes_from_jar

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S')
log = logging.getLogger(__name__)


def _process_jar(jar_path: Path, cache_dir: Path) -> tuple[str, str]:
    """Worker: extract one JAR. Returns (jar_name, 'cached'|'extracted'|'error:<msg>')."""
    if is_cache_current(jar_path, cache_dir):
        return jar_path.name, 'cached'
    try:
        classes = extract_classes_from_jar(jar_path)
        write_jar_cache(jar_path, cache_dir, classes)
        return jar_path.name, 'extracted'
    except Exception as exc:
        (cache_dir / (jar_path.stem + '.error.json')).write_text(
            json.dumps({'jar': jar_path.name, 'error': str(exc)}), encoding='utf-8'
        )
        return jar_path.name, f'error:{exc}'


def run_extract(jars_dir: Path, javadoc_dir: Path, cache_dir: Path, workers: int = 8) -> None:
    """Phase 1 entry point: process all JARs in parallel, then parse JavaDoc."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    jar_paths = sorted(jars_dir.glob('*.jar'))
    log.info('Found %d JARs in %s', len(jar_paths), jars_dir)

    counts = {'cached': 0, 'extracted': 0, 'error': 0}
    total = len(jar_paths)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_process_jar, p, cache_dir): p for p in jar_paths}
        for i, future in enumerate(as_completed(futures), 1):
            name, status = future.result()
            if status == 'cached':
                counts['cached'] += 1
            elif status == 'extracted':
                counts['extracted'] += 1
                log.info('[%d/%d] Extracted %s', i, total, name)
            else:
                counts['error'] += 1
                log.warning('[%d/%d] Error in %s: %s', i, total, name, status)

    log.info('JARs -- extracted: %d, cached: %d, errors: %d',
             counts['extracted'], counts['cached'], counts['error'])

    javadoc_cache = cache_dir / 'javadoc.json'
    if javadoc_cache.exists():
        log.info('JavaDoc cache exists -- skipping. Delete %s to refresh.', javadoc_cache)
    else:
        log.info('Parsing JavaDoc from %s ...', javadoc_dir)
        javadoc = parse_javadoc_dir(javadoc_dir)
        javadoc_cache.write_text(json.dumps(javadoc, indent=2), encoding='utf-8')
        log.info('JavaDoc: %d pages parsed -> %s', len(javadoc), javadoc_cache)


def _parse_args(argv=None):
    p = argparse.ArgumentParser(description='Phase 1: JAR + JavaDoc -> cache JSON')
    p.add_argument('--jars', required=True, type=Path)
    p.add_argument('--javadoc', required=True, type=Path)
    p.add_argument('--cache', required=True, type=Path)
    p.add_argument('--workers', type=int, default=8)
    return p.parse_args(argv)


if __name__ == '__main__':
    args = _parse_args()
    run_extract(args.jars, args.javadoc, args.cache, args.workers)
