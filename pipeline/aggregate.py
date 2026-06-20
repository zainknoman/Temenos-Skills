"""Phase 2: Aggregate cache JSON -> reference markdown files.

Usage:
    python pipeline/aggregate.py --cache cache --output .claude/skills/temenos-universal-analyzer/references
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Allow running as `python pipeline/aggregate.py` from the repo root
sys.path.insert(0, str(Path(__file__).parent.parent))

from jinja2 import Environment, FileSystemLoader

from pipeline.classify import detect_component_type

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S')
log = logging.getLogger(__name__)

_TEMPLATES_DIR = Path(__file__).parent / 'templates'

_PREFIX_DOMAIN: dict[str, str] = {
    'AA': 'aa',
    'FT': 'payments', 'PP': 'payments', 'FS': 'payments', 'SW': 'payments',
    'AC': 'accounts', 'EB': 'accounts',
    'LD': 'lending', 'LM': 'lending',
    'SC': 'securities', 'SE': 'securities', 'ST': 'securities',
    'AM': 'asset-management',
    'TT': 'teller', 'CNTELL': 'teller',
    'CO': 'cob',
    'DX': 'dx',
}

_REGULATORY_RE = re.compile(
    r'^(AU|UK|US|NL|NZ|HU|FR|IL|SA|QA|BR|CN|DE|HK|JP|LU|MX|NO|SG|IT|IN|PL|RU|ZA)\w*$'
)

_ALL_DOMAINS = ['aa', 'payments', 'accounts', 'lending', 'securities',
                'asset-management', 'teller', 'cob', 'dx', 'regulatory', 'misc']

_DOMAIN_TITLES = {
    'aa': 'Arrangement Architecture (AA)', 'payments': 'Payments & Funds Transfer',
    'accounts': 'Accounts & Core Banking', 'lending': 'Lending',
    'securities': 'Securities', 'asset-management': 'Asset Management',
    'teller': 'Teller', 'cob': 'Close of Business (COB)',
    'dx': 'Data Exchange (DX)', 'regulatory': 'Regulatory & Country Localisations',
    'misc': 'Miscellaneous & Frameworks',
}

_DOMAIN_FILE = {
    'aa': 'products/aa.md', 'payments': 'products/payments.md',
    'accounts': 'products/accounts.md', 'lending': 'products/lending.md',
    'securities': 'products/securities.md', 'asset-management': 'products/asset-management.md',
    'teller': 'products/teller.md', 'cob': 'products/cob.md',
    'dx': 'products/dx.md', 'regulatory': 'products/regulatory.md',
    'misc': 'products/misc.md',
}

_ALL_TYPES = ['lifecycle-hook', 'aa-activity-hook', 'service-hook', 'enquiry-routine',
              'validation-hook', 'auth-hook', 'public-api', 'rest-endpoint',
              'service-interface', 'record-model', 'event', 'unknown']


def get_domain(prefix: str) -> str:
    """Map a JAR prefix string to a domain name."""
    if prefix in _PREFIX_DOMAIN:
        return _PREFIX_DOMAIN[prefix]
    if _REGULATORY_RE.match(prefix):
        return 'regulatory'
    return 'misc'


def enrich_class(cls: dict, jar_name: str, prefix: str, javadoc: dict) -> dict:
    """Add computed fields to a raw class dict."""
    fqcn = cls.get('name', '')
    parts = fqcn.rsplit('.', 1)
    short_name = parts[-1]
    package = parts[0] if len(parts) == 2 else ''
    domain = get_domain(prefix)
    component_type = detect_component_type(cls)
    description = javadoc.get(fqcn, {}).get('description', '')
    public_methods = [m for m in cls.get('methods', []) if m.get('visibility') == 'public']
    return {
        **cls,
        'short_name': short_name,
        'package': package,
        'jar': jar_name,
        'prefix': prefix,
        'domain': domain,
        'component_type': component_type,
        'javadoc_description': description,
        'public_methods': public_methods,
    }


def load_cache(cache_dir: Path) -> tuple[list[dict], dict]:
    """Load and enrich all cache JSON files. Returns (classes, javadoc)."""
    javadoc_file = cache_dir / 'javadoc.json'
    javadoc: dict = json.loads(javadoc_file.read_text(encoding='utf-8')) if javadoc_file.exists() else {}

    all_classes: list[dict] = []
    for f in sorted(cache_dir.glob('*.json')):
        if f.name in ('javadoc.json',) or f.name.endswith('.error.json'):
            continue
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
            jar_name = data.get('jar', f.stem + '.jar')
            prefix = data.get('prefix', '')
            for cls in data.get('classes', []):
                all_classes.append(enrich_class(cls, jar_name, prefix, javadoc))
        except (json.JSONDecodeError, OSError) as exc:
            log.warning('Skipping %s: %s', f.name, exc)

    return all_classes, javadoc


def group_by_domain(classes: list[dict]) -> dict[str, list[dict]]:
    """Group enriched class dicts by domain. All domains always present in result."""
    grouped: dict[str, list[dict]] = {d: [] for d in _ALL_DOMAINS}
    for cls in classes:
        grouped.setdefault(cls.get('domain', 'misc'), []).append(cls)
    return grouped


def _by_type(classes: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {t: [] for t in _ALL_TYPES}
    for cls in classes:
        grouped.setdefault(cls.get('component_type', 'unknown'), []).append(cls)
    return grouped


def _by_jar(classes: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for cls in classes:
        grouped.setdefault(cls.get('jar', 'unknown.jar'), []).append(cls)
    return grouped


def render_references(
    classes: list[dict],
    javadoc: dict,
    output_dir: Path,
    templates_dir: Path = _TEMPLATES_DIR,
) -> None:
    """Render all reference markdown files from enriched class list."""
    now = datetime.now(timezone.utc).isoformat()
    env = Environment(loader=FileSystemLoader(str(templates_dir)),
                      autoescape=False, trim_blocks=True, lstrip_blocks=True)

    # Per-domain product files
    product_tmpl = env.get_template('product.md.j2')
    for domain, domain_classes in group_by_domain(classes).items():
        if not domain_classes:
            continue
        out = output_dir / _DOMAIN_FILE[domain]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(product_tmpl.render(
            domain=domain, domain_title=_DOMAIN_TITLES.get(domain, domain),
            jar_count=len({c['jar'] for c in domain_classes}),
            generated_at=now, by_type=_by_type(domain_classes),
            by_jar=_by_jar(domain_classes),
        ), encoding='utf-8')
        log.info('Wrote %s (%d classes)', out, len(domain_classes))

    # Cross-cutting hooks files
    hooks_tmpl = env.get_template('hooks.md.j2')
    all_by_type = _by_type(classes)
    hook_ctx = {t: all_by_type.get(t, []) for t in
                ['lifecycle-hook', 'aa-activity-hook', 'service-hook', 'validation-hook', 'auth-hook']}
    for filename in ('hooks/lifecycle-hooks.md', 'hooks/event-hooks.md', 'hooks/validation-hooks.md'):
        out = output_dir / filename
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(hooks_tmpl.render(generated_at=now, by_type=hook_ctx), encoding='utf-8')
        log.info('Wrote %s', out)

    # class-index.md
    out = output_dir / 'classes/class-index.md'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(env.get_template('class-index.md.j2').render(
        classes=classes, total=len(classes), generated_at=now,
    ), encoding='utf-8')
    log.info('Wrote %s (%d classes)', out, len(classes))

    # java-api.md + rest-api.md
    api_tmpl = env.get_template('api-catalog.md.j2')
    for filename, comp_type in (('apis/java-api.md', 'public-api'), ('apis/rest-api.md', 'rest-endpoint')):
        filtered = [c for c in classes if c['component_type'] == comp_type]
        out = output_dir / filename
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(api_tmpl.render(classes=filtered, total=len(filtered), generated_at=now),
                       encoding='utf-8')
        log.info('Wrote %s (%d classes)', out, len(filtered))

    # package-index.md
    seen: set[str] = set()
    packages = []
    for cls in sorted(classes, key=lambda c: c.get('package', '')):
        pkg = cls.get('package', '')
        if pkg and pkg not in seen:
            seen.add(pkg)
            packages.append({'package': pkg, 'jar': cls['jar'], 'domain': cls['domain']})
    out = output_dir / 'packages/package-index.md'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(env.get_template('package-index.md.j2').render(
        packages=packages, total=len(packages), generated_at=now,
    ), encoding='utf-8')
    log.info('Wrote %s (%d packages)', out, len(packages))

    # architecture/application-map.md
    app_re = re.compile(r'(Account|Customer|Payment|Arrangement|Activity|Contract|Teller|Trade|Securities)')
    app_classes = [c for c in classes if app_re.search(c.get('short_name', ''))]
    out = output_dir / 'architecture/application-map.md'
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [f'# T24 Application Map\n\n> Generated {now}\n\n',
             '| Class | JAR | Domain | Component Type |\n',
             '|-------|-----|--------|----------------|\n']
    for cls in sorted(app_classes, key=lambda c: c.get('short_name', '')):
        lines.append(f"| `{cls['short_name']}` | `{cls['jar']}` | `{cls['domain']}` | `{cls['component_type']}` |\n")
    out.write_text(''.join(lines), encoding='utf-8')
    log.info('Wrote %s (%d classes)', out, len(app_classes))

    # relationships/dependency-graph.md
    jar_set = sorted({c['jar'] for c in classes})
    out = output_dir / 'relationships/dependency-graph.md'
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [f'# T24 JAR Dependency Graph\n\n> Generated {now} — {len(jar_set)} JARs.\n\n',
             '| JAR | Domain | Class Count |\n', '|-----|--------|------------|\n']
    for jar in jar_set:
        jc = [c for c in classes if c['jar'] == jar]
        domain = jc[0]['domain'] if jc else 'misc'
        lines.append(f'| `{jar}` | `{domain}` | {len(jc)} |\n')
    out.write_text(''.join(lines), encoding='utf-8')
    log.info('Wrote %s (%d JARs)', out, len(jar_set))


def run_aggregate(cache_dir: Path, output_dir: Path) -> None:
    """Phase 2 entry point: load cache, enrich classes, render reference markdown."""
    log.info('Loading cache from %s ...', cache_dir)
    classes, javadoc = load_cache(cache_dir)
    log.info('Loaded %d classes, %d JavaDoc entries', len(classes), len(javadoc))
    render_references(classes, javadoc, output_dir)
    log.info('Done — reference files written to %s', output_dir)


def _parse_args(argv=None):
    p = argparse.ArgumentParser(description='Phase 2: cache JSON -> reference markdown')
    p.add_argument('--cache', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    return p.parse_args(argv)


if __name__ == '__main__':
    args = _parse_args()
    run_aggregate(args.cache, args.output)
