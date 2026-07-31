# PS.CONFIG.LAYOUT — Table Schema

> Source: `INSERTS/I_F.PS.CONFIG.LAYOUT` in `EI_PresentationServices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PS.CON.DESCRIPTION` | `PsConfigLayout_Description` |  |  |  |
| 2 | `PS.CON.USER` | `PsConfigLayout_User` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `PS.CON.CONFIG.CATEGORY` | `PsConfigLayout_ConfigCategory` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `PS.CON.CONFIG.XML` | `PsConfigLayout_ConfigXml` |  |  |  |
| 5 | `PS.CON.RESERVED08` | `PsConfigLayout_Reserved08` | TField |  |  |
| 6 | `PS.CON.RESERVED07` | `PsConfigLayout_Reserved07` | TField |  |  |
| 7 | `PS.CON.RESERVED06` | `PsConfigLayout_Reserved06` | TField |  |  |
| 8 | `PS.CON.RESERVED05` | `PsConfigLayout_Reserved05` | TField |  |  |
| 9 | `PS.CON.RESERVED04` | `PsConfigLayout_Reserved04` | TField |  |  |
| 10 | `PS.CON.RESERVED03` | `PsConfigLayout_Reserved03` | TField |  |  |
| 11 | `PS.CON.RESERVED02` | `PsConfigLayout_Reserved02` | TField |  |  |
| 12 | `PS.CON.RESERVED01` | `PsConfigLayout_Reserved01` | TField |  |  |
| 13 | `PS.CON.OVERRIDE` | `PsConfigLayout_Override` |  |  |  |
