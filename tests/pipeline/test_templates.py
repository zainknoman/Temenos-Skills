import pytest
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = Path('pipeline/templates')

@pytest.fixture
def jinja_env():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False, trim_blocks=True, lstrip_blocks=True,
    )
    env.filters['mdcell'] = lambda s: str(s).replace('|', '\\|').replace('\n', ' ')
    return env

_HOOK_CLASS = {
    'name': 'com.temenos.t24.aa.activity.ActivityHook',
    'short_name': 'ActivityHook',
    'jar': 'AA_ActivityHook.jar',
    'prefix': 'AA',
    'domain': 'aa',
    'component_type': 'lifecycle-hook',
    'superclass': 'com.temenos.t24.api.hook.RecordLifecycle',
    'interfaces': [],
    'annotations': [],
    'methods': [{'name': 'validateRecord', 'return_type': 'void',
                 'params': ['java.lang.String', 'com.temenos.t24.aa.record.AAActivityRecord'],
                 'visibility': 'public'}],
    'public_methods': [{'name': 'validateRecord', 'return_type': 'void',
                        'params': ['java.lang.String', 'com.temenos.t24.aa.record.AAActivityRecord'],
                        'visibility': 'public'}],
    'fields': [],
    'javadoc_description': 'Validates AA activity before authorisation.',
    'package': 'com.temenos.t24.aa.activity',
}

_API_CLASS = {
    'name': 'com.temenos.t24.api.arrangement.ContractApi',
    'short_name': 'ContractApi',
    'jar': 'AA_ContractApi.jar',
    'prefix': 'AA',
    'domain': 'aa',
    'component_type': 'public-api',
    'superclass': '',
    'interfaces': [],
    'annotations': [],
    'methods': [{'name': 'getAvailableBalance', 'return_type': 'java.math.BigDecimal',
                 'params': ['java.lang.String'], 'visibility': 'public'}],
    'public_methods': [{'name': 'getAvailableBalance', 'return_type': 'java.math.BigDecimal',
                        'params': ['java.lang.String'], 'visibility': 'public'}],
    'fields': [],
    'javadoc_description': 'Returns available balance for an arrangement.',
    'package': 'com.temenos.t24.api.arrangement',
}

_ALL_TYPES = {t: [] for t in ['lifecycle-hook', 'aa-activity-hook', 'service-hook',
                                'enquiry-routine', 'validation-hook', 'auth-hook',
                                'public-api', 'rest-endpoint', 'service-interface',
                                'record-model', 'event', 'unknown']}

def _product_ctx():
    ctx = {**_ALL_TYPES,
           'domain': 'aa', 'domain_title': 'Arrangement Architecture (AA)',
           'jar_count': 99, 'generated_at': '2026-06-20T10:00:00',
           'by_jar': {'AA_ActivityHook.jar': [_HOOK_CLASS]}}
    ctx['by_type'] = {**_ALL_TYPES, 'lifecycle-hook': [_HOOK_CLASS], 'public-api': [_API_CLASS]}
    return ctx

class TestProductTemplate:
    def test_renders(self, jinja_env):
        assert jinja_env.get_template('product.md.j2').render(_product_ctx())

    def test_domain_title_present(self, jinja_env):
        assert 'Arrangement Architecture (AA)' in jinja_env.get_template('product.md.j2').render(_product_ctx())

    def test_hook_class_present(self, jinja_env):
        assert 'ActivityHook' in jinja_env.get_template('product.md.j2').render(_product_ctx())

    def test_method_name_present(self, jinja_env):
        assert 'validateRecord' in jinja_env.get_template('product.md.j2').render(_product_ctx())

    def test_api_class_present(self, jinja_env):
        assert 'ContractApi' in jinja_env.get_template('product.md.j2').render(_product_ctx())

    def test_jar_name_present(self, jinja_env):
        assert 'AA_ActivityHook.jar' in jinja_env.get_template('product.md.j2').render(_product_ctx())

def _hooks_ctx():
    return {'generated_at': '2026-06-20T10:00:00',
            'by_type': {'lifecycle-hook': [_HOOK_CLASS], 'aa-activity-hook': [],
                        'service-hook': [], 'validation-hook': [], 'auth-hook': []}}

class TestHooksTemplate:
    def test_renders(self, jinja_env):
        assert jinja_env.get_template('hooks.md.j2').render(_hooks_ctx())

    def test_lifecycle_section_present(self, jinja_env):
        out = jinja_env.get_template('hooks.md.j2').render(_hooks_ctx())
        assert 'Lifecycle' in out

    def test_hook_class_present(self, jinja_env):
        assert 'ActivityHook' in jinja_env.get_template('hooks.md.j2').render(_hooks_ctx())

def _class_index_ctx():
    return {'classes': [_HOOK_CLASS, _API_CLASS], 'total': 2, 'generated_at': '2026-06-20T10:00:00'}

class TestClassIndexTemplate:
    def test_renders(self, jinja_env):
        assert jinja_env.get_template('class-index.md.j2').render(_class_index_ctx())

    def test_both_classes_present(self, jinja_env):
        out = jinja_env.get_template('class-index.md.j2').render(_class_index_ctx())
        assert 'ActivityHook' in out and 'ContractApi' in out
