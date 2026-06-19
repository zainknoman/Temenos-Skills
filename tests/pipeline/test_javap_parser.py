import pytest
from pathlib import Path
from pipeline.javap_parser import parse_javap_output, extract_classes_from_jar

LIFECYCLE_HOOK_OUTPUT = """
Compiled from "ActivityHook.java"
public class com.temenos.t24.aa.activity.ActivityHook extends com.temenos.t24.api.hook.RecordLifecycle {
  private static final org.apache.logging.log4j.Logger LOG;
  public com.temenos.t24.aa.activity.ActivityHook();
  public void validateRecord(java.lang.String, com.temenos.t24.aa.record.AAActivityRecord);
  public void postUpdateRequest(java.lang.String, com.temenos.t24.aa.record.AAActivityRecord);
  public void authoriseRecord(java.lang.String, com.temenos.t24.aa.record.AAActivityRecord);
}
"""

SERVICE_INTERFACE_OUTPUT = """
Compiled from "PaymentService.java"
public interface com.temenos.t24.payments.PaymentService {
  public abstract void processPayment(java.lang.String, com.temenos.t24.payments.PaymentRecord);
  public abstract java.lang.String getStatus(java.lang.String);
}
"""

MULTI_INTERFACE_OUTPUT = """
Compiled from "SomeClass.java"
public class com.temenos.t24.utils.SomeClass extends java.lang.Object implements java.io.Serializable, java.lang.Cloneable {
  public com.temenos.t24.utils.SomeClass();
}
"""


class TestParseJavapOutput:
    def test_class_name(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        assert result['name'] == 'com.temenos.t24.aa.activity.ActivityHook'

    def test_superclass(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        assert result['superclass'] == 'com.temenos.t24.api.hook.RecordLifecycle'

    def test_is_class_not_interface(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        assert result['is_interface'] is False

    def test_is_interface(self):
        result = parse_javap_output(SERVICE_INTERFACE_OUTPUT)
        assert result['is_interface'] is True

    def test_public_methods_extracted(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        names = [m['name'] for m in result['methods']]
        assert 'validateRecord' in names
        assert 'postUpdateRequest' in names
        assert 'authoriseRecord' in names

    def test_method_return_type(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        m = next(x for x in result['methods'] if x['name'] == 'validateRecord')
        assert m['return_type'] == 'void'

    def test_method_params_contain_string(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        m = next(x for x in result['methods'] if x['name'] == 'validateRecord')
        assert any('String' in p for p in m['params'])

    def test_method_visibility_public(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        m = next(x for x in result['methods'] if x['name'] == 'validateRecord')
        assert m['visibility'] == 'public'

    def test_private_field_extracted(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        names = [f['name'] for f in result['fields']]
        assert 'LOG' in names

    def test_private_field_visibility(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        f = next(x for x in result['fields'] if x['name'] == 'LOG')
        assert f['visibility'] == 'private'

    def test_multiple_interfaces(self):
        result = parse_javap_output(MULTI_INTERFACE_OUTPUT)
        assert 'java.io.Serializable' in result['interfaces']
        assert 'java.lang.Cloneable' in result['interfaces']

    def test_empty_output_returns_empty_name(self):
        result = parse_javap_output('')
        assert result['name'] == ''

    def test_constructor_not_in_methods(self):
        result = parse_javap_output(LIFECYCLE_HOOK_OUTPUT)
        names = [m['name'] for m in result['methods']]
        assert 'ActivityHook' not in names


class TestExtractClassesFromJar:
    def test_extracts_at_least_one_class(self):
        jar = Path('jar/t24lib/AA_ActivityHook.jar')
        if not jar.exists():
            pytest.skip('jar/t24lib/AA_ActivityHook.jar not found')
        classes = extract_classes_from_jar(jar)
        assert len(classes) > 0

    def test_classes_have_required_keys(self):
        jar = Path('jar/t24lib/AA_ActivityHook.jar')
        if not jar.exists():
            pytest.skip('jar/t24lib/AA_ActivityHook.jar not found')
        for cls in extract_classes_from_jar(jar):
            for key in ('name', 'superclass', 'interfaces', 'methods', 'fields'):
                assert key in cls

    def test_skips_inner_classes(self):
        jar = Path('jar/t24lib/AA_ActivityHook.jar')
        if not jar.exists():
            pytest.skip('jar/t24lib/AA_ActivityHook.jar not found')
        for cls in extract_classes_from_jar(jar):
            assert '$' not in cls['name']
