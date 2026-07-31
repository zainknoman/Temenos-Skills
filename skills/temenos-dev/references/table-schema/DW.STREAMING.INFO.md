# DW.STREAMING.INFO — Table Schema

> Source: `INSERTS/I_F.DW.STREAMING.INFO` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.SI.SCHEMA.ID` | `DwStreamingInfo_SchemaId` | TField |  | This field stores the ID of the latest version of schema for the application |
| 2 | `DW.SI.RESERVED.6` | `DwStreamingInfo_Reserved6` | TField |  |  |
| 3 | `DW.SI.RESERVED.5` | `DwStreamingInfo_Reserved5` | TField |  |  |
| 4 | `DW.SI.RESERVED.4` | `DwStreamingInfo_Reserved4` | TField |  |  |
| 5 | `DW.SI.RESERVED.3` | `DwStreamingInfo_Reserved3` | TField |  |  |
| 6 | `DW.SI.RESERVED.2` | `DwStreamingInfo_Reserved2` | TField |  |  |
| 7 | `DW.SI.RESERVED.1` | `DwStreamingInfo_Reserved1` | TField |  |  |
