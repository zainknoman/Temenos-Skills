import json
import pytest
from pathlib import Path
from pipeline.cache_utils import compute_jar_hash, is_cache_current, write_jar_cache


@pytest.fixture
def tmp_jar(tmp_path):
    jar = tmp_path / 'test.jar'
    jar.write_bytes(b'fake jar content')
    return jar


@pytest.fixture
def cache_dir(tmp_path):
    d = tmp_path / 'cache'
    d.mkdir()
    return d


def test_hash_is_64_hex_chars(tmp_jar):
    h = compute_jar_hash(tmp_jar)
    assert len(h) == 64 and all(c in '0123456789abcdef' for c in h)


def test_hash_is_deterministic(tmp_jar):
    assert compute_jar_hash(tmp_jar) == compute_jar_hash(tmp_jar)


def test_hash_differs_for_different_content(tmp_path):
    a, b = tmp_path / 'a.jar', tmp_path / 'b.jar'
    a.write_bytes(b'AAA'), b.write_bytes(b'BBB')
    assert compute_jar_hash(a) != compute_jar_hash(b)


def test_cache_current_false_when_no_file(tmp_jar, cache_dir):
    assert is_cache_current(tmp_jar, cache_dir) is False


def test_cache_current_true_after_write(tmp_jar, cache_dir):
    write_jar_cache(tmp_jar, cache_dir, [])
    assert is_cache_current(tmp_jar, cache_dir) is True


def test_cache_current_false_after_content_change(tmp_jar, cache_dir):
    write_jar_cache(tmp_jar, cache_dir, [])
    tmp_jar.write_bytes(b'completely different')
    assert is_cache_current(tmp_jar, cache_dir) is False


def test_write_creates_json_file(tmp_jar, cache_dir):
    write_jar_cache(tmp_jar, cache_dir, [])
    assert (cache_dir / 'test.json').exists()


def test_write_json_has_required_keys(tmp_jar, cache_dir):
    write_jar_cache(tmp_jar, cache_dir, [])
    data = json.loads((cache_dir / 'test.json').read_text())
    for key in ('jar', 'prefix', 'hash', 'extracted_at', 'classes'):
        assert key in data


def test_prefix_extracted_from_underscore_name(tmp_path, cache_dir):
    jar = tmp_path / 'AA_ActivityHook.jar'
    jar.write_bytes(b'x')
    write_jar_cache(jar, cache_dir, [])
    data = json.loads((cache_dir / 'AA_ActivityHook.json').read_text())
    assert data['prefix'] == 'AA'


def test_prefix_falls_back_to_stem_when_no_underscore(tmp_path, cache_dir):
    jar = tmp_path / 'Tables.jar'
    jar.write_bytes(b'x')
    write_jar_cache(jar, cache_dir, [])
    data = json.loads((cache_dir / 'Tables.json').read_text())
    assert data['prefix'] == 'Tables'
