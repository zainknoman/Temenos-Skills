import pytest
from pathlib import Path
from pipeline.javadoc_parser import parse_javadoc_dir, _fqcn_from_path, _parse_page

JAVADOC_DIR = Path('T24.javadoc/T24.javadoc')

MINIMAL_HTML = """
<html>
<head><title>ContractApi (T24 API)</title></head>
<body>
<div class="header">
  <h2 title="Class ContractApi" class="title">Class ContractApi</h2>
</div>
<div class="description">
  <ul class="blockList"><li class="blockList">
    <div class="block">Provides access to AA contract data and balances.</div>
  </li></ul>
</div>
<div class="details">
  <ul class="blockList"><li class="blockList"><ul class="blockList"><li class="blockList">
    <a name="getAvailableBalance-java.lang.String-"></a>
    <h4>getAvailableBalance</h4>
    <div class="block">Returns the available balance for the arrangement.</div>
  </li></ul></li></ul>
</div>
</body>
</html>
"""


class TestFqcnFromPath:
    def test_nested_path(self, tmp_path):
        base = tmp_path / 'javadoc'
        file = base / 'com' / 'temenos' / 't24' / 'api' / 'ContractApi.html'
        assert _fqcn_from_path(file, base) == 'com.temenos.t24.api.ContractApi'

    def test_single_level(self, tmp_path):
        file = tmp_path / 'MyClass.html'
        assert _fqcn_from_path(file, tmp_path) == 'MyClass'


class TestParsePage:
    def test_extracts_description(self):
        result = _parse_page(MINIMAL_HTML)
        assert result is not None
        assert 'Provides access to AA contract data' in result['description']

    def test_extracts_method_description(self):
        result = _parse_page(MINIMAL_HTML)
        assert result is not None
        assert 'getAvailableBalance' in result['methods']
        assert 'available balance' in result['methods']['getAvailableBalance']

    def test_returns_none_for_non_class_page(self):
        assert _parse_page('<html><body><h1>Overview</h1></body></html>') is None


class TestParseJavadocDir:
    def test_returns_dict(self):
        if not JAVADOC_DIR.exists():
            pytest.skip('T24.javadoc/T24.javadoc not found')
        assert isinstance(parse_javadoc_dir(JAVADOC_DIR), dict)

    def test_has_entries(self):
        if not JAVADOC_DIR.exists():
            pytest.skip('T24.javadoc/T24.javadoc not found')
        assert len(parse_javadoc_dir(JAVADOC_DIR)) > 0

    def test_keys_are_dotted_fqcns(self):
        if not JAVADOC_DIR.exists():
            pytest.skip('T24.javadoc/T24.javadoc not found')
        result = parse_javadoc_dir(JAVADOC_DIR)
        for key in list(result.keys())[:5]:
            assert '.' in key

    def test_entries_have_description_and_methods(self):
        if not JAVADOC_DIR.exists():
            pytest.skip('T24.javadoc/T24.javadoc not found')
        for entry in list(parse_javadoc_dir(JAVADOC_DIR).values())[:5]:
            assert 'description' in entry
            assert isinstance(entry['methods'], dict)
