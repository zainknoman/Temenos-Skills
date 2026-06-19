from __future__ import annotations

# Rules applied in priority order — first match wins.
_RULES: list[tuple[str, object]] = [
    ('lifecycle-hook',    lambda c: 'RecordLifecycle' in c.get('superclass', '')),
    ('service-hook',      lambda c: 'ServiceLifecycle' in c.get('superclass', '')),
    ('aa-activity-hook',  lambda c: 'ActivityLifecycle' in c.get('superclass', '')),
    ('enquiry-routine',   lambda c: any(k in c.get('superclass', '')
                                        for k in ('Enquiry', 'NofileEnquiry'))),
    ('rest-endpoint',     lambda c: any(a in c.get('annotations', [])
                                        for a in ('@GET', '@POST', '@PUT', '@DELETE', '@Path'))),
    ('public-api',        lambda c: '.api.' in c.get('name', '')
                                    or c.get('name', '').endswith(('API', 'Api'))),
    ('validation-hook',   lambda c: c.get('name', '').endswith('Validation')),
    ('auth-hook',         lambda c: c.get('name', '').endswith('Authorization')),
    ('service-interface', lambda c: c.get('is_interface', False)
                                    and c.get('name', '').endswith('Service')),
    ('record-model',      lambda c: c.get('name', '').endswith('Record')),
    ('event',             lambda c: c.get('name', '').endswith('Event')),
]


def detect_component_type(class_info: dict) -> str:
    """
    Detect Temenos component type from class metadata dict.

    Args:
        class_info: dict with keys name (str FQCN), superclass (str),
                    interfaces (list[str]), annotations (list[str]),
                    is_interface (bool).

    Returns:
        One of: lifecycle-hook, service-hook, aa-activity-hook,
        enquiry-routine, validation-hook, auth-hook, public-api,
        rest-endpoint, service-interface, record-model, event, unknown.
    """
    for component_type, predicate in _RULES:
        if predicate(class_info):
            return component_type
    return 'unknown'
