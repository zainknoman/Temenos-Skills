"""Component type of a T24 JAR from its file name (shared by extract.py and jar_classes.py; no javatools needed)."""

_COMPONENT_RULES: list[tuple[list[str], str]] = [
    # Rule 1 — explicit public API JARs
    (["Api.jar", "API.jar"],                     "public-api"),
    # Rule 2 — hook interfaces (lifecycle, validation, event)
    (["Hook.jar", "Lifecycle.jar"],              "hook"),
    # Rule 3 — service JARs (t24service suffix)
    (["t24service.jar"],                         "service"),
    # Rule 4 — data / DTO JARs
    (["-Data.jar", "Record.jar"],                "data"),
    # Rule 5 — test JARs
    (["test", "Test", "spec", "Spec"],           "test"),
    # Rule 6 — foundation / framework
    (["Foundation.jar", "Framework.jar",
      "Platform.jar", "Core.jar"],               "framework"),
    # Rule 7 — integration / connector
    (["Connect.jar", "Connector.jar",
      "Adapter.jar", "Integration.jar"],         "integration"),
    # Rule 8 — CA / custom add-on prefix
    (["CA"],                                     "custom"),
    # Rule 9 — installer / tooling
    (["Installer.jar", "Plugin.jar",
      "Tool.jar", "Studio.jar"],                 "tooling"),
    # Rule 10 — report / batch
    (["Report.jar", "Batch.jar", "COB.jar"],    "batch"),
    # Rule 11 — fallback
    ([],                                         "internal"),
]


def classify_component(jar_name: str) -> str:
    for patterns, label in _COMPONENT_RULES:
        if not patterns:          # fallback rule
            return label
        if any(p in jar_name for p in patterns):
            return label
    return "internal"
