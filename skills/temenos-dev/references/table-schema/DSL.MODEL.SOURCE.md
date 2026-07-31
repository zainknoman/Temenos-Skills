# DSL.MODEL.SOURCE — Table Schema

> Source: `INSERTS/I_F.DSL.MODEL.SOURCE` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DSL.MOD.COMPONENT` | `DslModelSource_Component` | TField |  | Specifies the Component to which the model artefact belongs to Validation Rules: Must be a valid record in EB.COMPONENT table |
| 2 | `DSL.MOD.SOURCE.RELEASE` | `DslModelSource_SourceRelease` | TField |  | Specifies the T24 Release or the T24 Updates release in which the model artefact was last released |
| 3 | `DSL.MOD.CONTENT` | `DslModelSource_Content` |  |  |  |
