import json
import pytest
from pathlib import Path
from pipeline.aggregate import get_domain, enrich_class, group_by_domain, load_cache

# --- get_domain ---

def test_domain_aa():          assert get_domain('AA') == 'aa'
def test_domain_ft():          assert get_domain('FT') == 'payments'
def test_domain_pp():          assert get_domain('PP') == 'payments'
def test_domain_ac():          assert get_domain('AC') == 'accounts'
def test_domain_eb():          assert get_domain('EB') == 'accounts'
def test_domain_ld():          assert get_domain('LD') == 'lending'
def test_domain_sc():          assert get_domain('SC') == 'securities'
def test_domain_tt():          assert get_domain('TT') == 'teller'
def test_domain_co():          assert get_domain('CO') == 'cob'
def test_domain_dx():          assert get_domain('DX') == 'dx'
def test_domain_au_regulatory(): assert get_domain('AUACCT') == 'regulatory'
def test_domain_uk_regulatory(): assert get_domain('UKBASE') == 'regulatory'
def test_domain_misc():        assert get_domain('XYZUNKNOWN') == 'misc'

# --- enrich_class ---

_RAW = {
    'name': 'com.temenos.t24.aa.activity.ActivityHook',
    'superclass': 'com.temenos.t24.api.hook.RecordLifecycle',
    'interfaces': [], 'annotations': [], 'is_interface': False, 'component_type': None,
    'methods': [
        {'name': 'validateRecord', 'return_type': 'void', 'params': ['java.lang.String'], 'visibility': 'public'},
        {'name': 'helper', 'return_type': 'void', 'params': [], 'visibility': 'private'},
    ],
    'fields': [],
}

_JAVADOC = {
    'com.temenos.t24.aa.activity.ActivityHook': {
        'description': 'Validates AA activity.', 'methods': {}
    }
}

def test_enrich_short_name():
    assert enrich_class(_RAW, 'AA_ActivityHook.jar', 'AA', _JAVADOC)['short_name'] == 'ActivityHook'

def test_enrich_package():
    assert enrich_class(_RAW, 'AA_ActivityHook.jar', 'AA', _JAVADOC)['package'] == 'com.temenos.t24.aa.activity'

def test_enrich_domain():
    assert enrich_class(_RAW, 'AA_ActivityHook.jar', 'AA', _JAVADOC)['domain'] == 'aa'

def test_enrich_component_type():
    assert enrich_class(_RAW, 'AA_ActivityHook.jar', 'AA', _JAVADOC)['component_type'] == 'lifecycle-hook'

def test_enrich_javadoc_description():
    assert 'Validates AA activity' in enrich_class(_RAW, 'AA_ActivityHook.jar', 'AA', _JAVADOC)['javadoc_description']

def test_enrich_public_methods_only():
    result = enrich_class(_RAW, 'AA_ActivityHook.jar', 'AA', _JAVADOC)
    names = [m['name'] for m in result['public_methods']]
    assert 'validateRecord' in names and 'helper' not in names

def test_enrich_empty_javadoc():
    assert enrich_class(_RAW, 'AA_ActivityHook.jar', 'AA', {})['javadoc_description'] == ''

# --- group_by_domain ---

def test_group_separates_domains():
    classes = [{'domain': 'aa'}, {'domain': 'payments'}, {'domain': 'aa'}]
    g = group_by_domain(classes)
    assert len(g['aa']) == 2 and len(g['payments']) == 1

def test_group_all_domains_present():
    g = group_by_domain([{'domain': 'lending'}])
    for d in ('aa', 'payments', 'accounts', 'lending', 'securities',
              'asset-management', 'teller', 'cob', 'dx', 'regulatory', 'misc'):
        assert d in g

# --- load_cache ---

def test_load_cache_reads_classes(tmp_path):
    cache = tmp_path / 'cache'
    cache.mkdir()
    (cache / 'javadoc.json').write_text('{}')
    (cache / 'AA_Test.json').write_text(json.dumps({
        'jar': 'AA_Test.jar', 'prefix': 'AA', 'hash': 'x', 'extracted_at': '',
        'classes': [{'name': 'com.X', 'superclass': '', 'interfaces': [], 'annotations': [],
                     'methods': [], 'fields': [], 'is_interface': False, 'component_type': None}]
    }))
    classes, _ = load_cache(cache)
    assert len(classes) == 1 and classes[0]['jar'] == 'AA_Test.jar'

def test_load_cache_skips_error_files(tmp_path):
    cache = tmp_path / 'cache'
    cache.mkdir()
    (cache / 'javadoc.json').write_text('{}')
    (cache / 'Bad.error.json').write_text('{"error": "oops"}')
    classes, _ = load_cache(cache)
    assert classes == []

def test_load_cache_returns_javadoc(tmp_path):
    cache = tmp_path / 'cache'
    cache.mkdir()
    (cache / 'javadoc.json').write_text('{"com.X": {"description": "Test", "methods": {}}}')
    _, javadoc = load_cache(cache)
    assert 'com.X' in javadoc
