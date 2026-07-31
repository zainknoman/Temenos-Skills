# DW.OL.DATA.STORE — Table Schema

> Source: `INSERTS/I_F.DW.OL.DATA.STORE` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.ODS.QUERY` | `DwOlDataStore_Query` | TField |  | This field is a no-input field used for invoking IF API with the DW Query |
| 2 | `DW.ODS.RESERVED.1` | `DwOlDataStore_Reserved1` | TField |  |  |
| 3 | `DW.ODS.RESERVED.2` | `DwOlDataStore_Reserved2` | TField |  |  |
| 4 | `DW.ODS.RESERVED.3` | `DwOlDataStore_Reserved3` | TField |  |  |
| 5 | `DW.ODS.RESERVED.4` | `DwOlDataStore_Reserved4` | TField |  |  |
| 6 | `DW.ODS.RESERVED.5` | `DwOlDataStore_Reserved5` | TField |  |  |
