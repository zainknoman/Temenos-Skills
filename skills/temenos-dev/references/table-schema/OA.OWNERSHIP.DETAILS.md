# OA.OWNERSHIP.DETAILS — Table Schema

> Source: `INSERTS/I_F.OA.OWNERSHIP.DETAILS` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.OWDT.STATUS.CODES` | `OaOwnershipDetails_StatusCodes` |  |  |  |
| 2 | `OA.OWDT.RESERVED.5` | `OaOwnershipDetails_Reserved5` | TField |  | System field reserved for future use |
| 3 | `OA.OWDT.RESERVED.4` | `OaOwnershipDetails_Reserved4` | TField |  | System field reserved for future use |
| 4 | `OA.OWDT.RESERVED.3` | `OaOwnershipDetails_Reserved3` | TField |  | System field reserved for future use |
| 5 | `OA.OWDT.RESERVED.2` | `OaOwnershipDetails_Reserved2` | TField |  | System field reserved for future use |
| 6 | `OA.OWDT.RESERVED.1` | `OaOwnershipDetails_Reserved1` | TField |  | System field reserved for future use |
