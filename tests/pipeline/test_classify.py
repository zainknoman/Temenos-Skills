import pytest
from pipeline.classify import detect_component_type


def _cls(name='', superclass='', interfaces=None, annotations=None, is_interface=False):
    return {
        'name': name,
        'superclass': superclass,
        'interfaces': interfaces or [],
        'annotations': annotations or [],
        'is_interface': is_interface,
    }


def test_lifecycle_hook():
    c = _cls(name='com.temenos.t24.aa.ActivityHook',
             superclass='com.temenos.t24.api.hook.RecordLifecycle')
    assert detect_component_type(c) == 'lifecycle-hook'


def test_service_hook():
    c = _cls(superclass='com.temenos.t24.api.hook.ServiceLifecycle')
    assert detect_component_type(c) == 'service-hook'


def test_aa_activity_hook():
    c = _cls(superclass='com.temenos.t24.aa.hook.ActivityLifecycle')
    assert detect_component_type(c) == 'aa-activity-hook'


def test_enquiry_routine():
    c = _cls(superclass='com.temenos.t24.api.enquiry.Enquiry')
    assert detect_component_type(c) == 'enquiry-routine'


def test_nofile_enquiry():
    c = _cls(superclass='com.temenos.t24.api.enquiry.NofileEnquiry')
    assert detect_component_type(c) == 'enquiry-routine'


def test_validation_hook():
    c = _cls(name='com.temenos.t24.aa.ActivityValidation')
    assert detect_component_type(c) == 'validation-hook'


def test_auth_hook():
    c = _cls(name='com.temenos.t24.aa.ActivityAuthorization')
    assert detect_component_type(c) == 'auth-hook'


def test_rest_endpoint_get():
    c = _cls(annotations=['@GET', '@Path'])
    assert detect_component_type(c) == 'rest-endpoint'


def test_rest_endpoint_post():
    c = _cls(annotations=['@POST'])
    assert detect_component_type(c) == 'rest-endpoint'


def test_public_api_by_package():
    c = _cls(name='com.temenos.t24.api.arrangement.ContractApi')
    assert detect_component_type(c) == 'public-api'


def test_public_api_by_suffix_API():
    c = _cls(name='com.temenos.t24.payments.FundsTransferAPI')
    assert detect_component_type(c) == 'public-api'


def test_public_api_by_suffix_Api():
    c = _cls(name='com.temenos.t24.payments.PaymentApi')
    assert detect_component_type(c) == 'public-api'


def test_service_interface():
    c = _cls(name='com.temenos.t24.payments.PaymentService', is_interface=True)
    assert detect_component_type(c) == 'service-interface'


def test_service_class_not_interface():
    # A class (not interface) ending in Service → unknown, not service-interface
    c = _cls(name='com.temenos.t24.payments.PaymentService', is_interface=False)
    assert detect_component_type(c) == 'unknown'


def test_record_model():
    c = _cls(name='com.temenos.t24.aa.AAActivityRecord')
    assert detect_component_type(c) == 'record-model'


def test_event():
    c = _cls(name='com.temenos.t24.aa.ActivityCompletedEvent')
    assert detect_component_type(c) == 'event'


def test_unknown():
    c = _cls(name='com.temenos.t24.utils.StringUtils')
    assert detect_component_type(c) == 'unknown'


def test_lifecycle_takes_priority_over_name_suffix():
    # RecordLifecycle superclass wins over Validation name suffix
    c = _cls(name='com.temenos.t24.SomeValidation',
             superclass='com.temenos.t24.api.hook.RecordLifecycle')
    assert detect_component_type(c) == 'lifecycle-hook'
