# OA.ARCHIVE.LOG — Table Schema

> Source: `INSERTS/I_F.OA.ARCHIVE.LOG` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.ARC.FAILURE.APPLICATION` | `OaArchiveLog_FailureApplication` |  |  |  |
| 2 | `OA.ARC.FAILURE.APP.REFERENCE` | `OaArchiveLog_FailureAppReference` |  |  |  |
| 3 | `OA.ARC.FAILURE.DETAILS` | `OaArchiveLog_FailureDetails` |  |  |  |
| 4 | `OA.ARC.RESERVED.FIELD.5` | `OaArchiveLog_ReservedField5` | TField |  |  |
| 5 | `OA.ARC.RESERVED.FIELD.4` | `OaArchiveLog_ReservedField4` | TField |  |  |
| 6 | `OA.ARC.RESERVED.FIELD.3` | `OaArchiveLog_ReservedField3` | TField |  |  |
| 7 | `OA.ARC.RESERVED.FIELD.2` | `OaArchiveLog_ReservedField2` | TField |  |  |
| 8 | `OA.ARC.RESERVED.FIELD.1` | `OaArchiveLog_ReservedField1` | TField |  |  |
