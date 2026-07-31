# US.LEGAL.DOCUMENT — Table Schema

> Source: `INSERTS/I_F.US.LEGAL.DOCUMENT` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.LEGAL.PERSON.ENTITY` | `UsLegalDocument_PersonEntity` | TField |  | Not Used |
| 2 | `US.LEGAL.DOCUMENT.TYPE` | `UsLegalDocument_DocumentType` | TField |  | Not Used |
| 3 | `US.LEGAL.RESERVED.9` | `UsLegalDocument_Reserved9` | TField |  |  |
| 4 | `US.LEGAL.RESERVED.8` | `UsLegalDocument_Reserved8` | TField |  |  |
| 5 | `US.LEGAL.RESERVED.7` | `UsLegalDocument_Reserved7` | TField |  |  |
| 6 | `US.LEGAL.RESERVED.6` | `UsLegalDocument_Reserved6` | TField |  |  |
| 7 | `US.LEGAL.RESERVED.5` | `UsLegalDocument_Reserved5` | TField |  |  |
| 8 | `US.LEGAL.RESERVED.4` | `UsLegalDocument_Reserved4` | TField |  |  |
| 9 | `US.LEGAL.RESERVED.3` | `UsLegalDocument_Reserved3` | TField |  |  |
| 10 | `US.LEGAL.RESERVED.2` | `UsLegalDocument_Reserved2` | TField |  |  |
| 11 | `US.LEGAL.RESERVED.1` | `UsLegalDocument_Reserved1` | TField |  |  |
| 12 | `US.LEGAL.OVERRIDE` | `UsLegalDocument_Override` |  |  |  |
