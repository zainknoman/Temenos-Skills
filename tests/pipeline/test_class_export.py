import json

from class_export import METHOD_TYPES, build_class_index, load_cache, write_class_index


def _cls(name, package, jar_type, *, superclass="", interfaces=(), is_interface=0, is_abstract=0,
         is_public=True, methods=()):
    return {"name": name, "package": package, "qualified": f"{package}.{name}", "superclass": superclass,
            "interfaces": list(interfaces), "is_interface": is_interface, "is_abstract": is_abstract,
            "is_public": is_public, "component_type": jar_type, "domain": "x",
            "methods": [{"name": m, "return_type": "java.lang.String", "params": ["java.lang.String"],
                         "is_public": pub, "is_static": 0, "is_abstract": 0} for m, pub in methods]}


HOOK = _cls("RecordLifecycle", "com.temenos.t24.api.hook.system", "hook",
            superclass="com.temenos.tafj.api.client.impl.T24Context",
            methods=[("checkId", True), ("secret", False)])
INTERNAL = _cls("Helper", "com.temenos.t24.internal", "internal", is_abstract=4,
                methods=[("run", True)])
IFACE = _cls("Dup", "com.temenos.shared", "internal", is_interface=512)


def _jars():
    return [("EB_TemplateHook.jar", [HOOK]), ("ZZ_Internal.jar", [INTERNAL, IFACE]), ("AA_Other.jar", [IFACE])]


def _decode(doc):
    out = {}
    for t in doc["classes"]:
        q = f"{doc['packages'][t[1]]}.{t[0]}"
        out.setdefault(q, []).append({"jar": doc["jars"][t[2]], "type": doc["types"][t[3]], "flags": t[4],
                                      "superclass": t[5], "interfaces": t[6],
                                      "methods": t[7] if len(t) > 7 else None})
    return out


def test_header_and_string_tables_are_sorted():
    doc = build_class_index(_jars(), "R23", "2026-10-05T00:00:00Z")
    assert doc["kind"] == "t24-classes" and doc["schemaVersion"] == 1 and doc["release"] == "R23"
    assert doc["jars"] == sorted(doc["jars"])
    assert doc["packages"] == sorted(doc["packages"])
    assert doc["types"] == sorted(doc["types"])


def test_record_lifecycle_round_trips_to_its_jar_and_superclass():
    entry = _decode(build_class_index(_jars(), "R23", "t"))["com.temenos.t24.api.hook.system.RecordLifecycle"]
    assert entry == [{"jar": "EB_TemplateHook.jar", "type": "hook", "flags": 0,
                      "superclass": "com.temenos.tafj.api.client.impl.T24Context", "interfaces": [],
                      "methods": [["checkId", "java.lang.String", ["java.lang.String"]]]}]


def test_methods_only_for_method_types_and_only_public():
    assert {"hook", "public-api", "batch", "service", "integration"} == METHOD_TYPES
    decoded = _decode(build_class_index(_jars(), "R23", "t"))
    assert decoded["com.temenos.t24.internal.Helper"][0]["methods"] is None


def test_flags_interface_and_abstract():
    decoded = _decode(build_class_index(_jars(), "R23", "t"))
    assert decoded["com.temenos.t24.internal.Helper"][0]["flags"] == 2
    assert all(e["flags"] == 1 for e in decoded["com.temenos.shared.Dup"])


def test_class_in_two_jars_is_listed_once_per_jar_in_jar_order():
    decoded = _decode(build_class_index(_jars(), "R23", "t"))
    assert [e["jar"] for e in decoded["com.temenos.shared.Dup"]] == ["AA_Other.jar", "ZZ_Internal.jar"]


def test_output_is_deterministic():
    a = json.dumps(build_class_index(_jars(), "R23", "t"))
    b = json.dumps(build_class_index(list(reversed(_jars())), "R23", "t"))
    assert a == b


def test_write_adds_classes_json_to_existing_manifest(tmp_path):
    cache = tmp_path / "cache"; cache.mkdir()
    for jar, classes in _jars():
        (cache / jar.replace(".jar", ".json")).write_text(json.dumps({"jar": jar, "sha256": "x", "classes": classes}))
    (cache / "broken.json").write_text("{not json")
    out = tmp_path / "out"; out.mkdir()
    (out / "manifest.json").write_text(json.dumps({"release": "R23", "files": {"fields.json": {"bytes": 1, "sha256": "a"}}}))
    entry = write_class_index(load_cache(cache), out, "R23", now="2026-10-05T00:00:00Z")
    manifest = json.loads((out / "manifest.json").read_text())
    data = (out / "classes.json").read_bytes()
    import hashlib
    assert manifest["files"]["fields.json"] == {"bytes": 1, "sha256": "a"}
    assert manifest["files"]["classes.json"] == entry == {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    assert manifest["classes"] == 4 and manifest["jars"] == 3
