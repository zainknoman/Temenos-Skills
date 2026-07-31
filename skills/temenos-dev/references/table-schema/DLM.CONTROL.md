# DLM.CONTROL — Table Schema

> Source: `INSERTS/I_F.DLM.CONTROL` in `DL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DLM.AGENT.NUMBER` | `DlmControl_AgentNumber` | TField |  | Agent number in which the application records processed Validation Rules: |
| 2 | `DLM.LAST.UPDATE.TIME` | `DlmControl_LastUpdateTime` |  |  |  |
| 3 | `DLM.STATUS` | `DlmControl_Status` | TField |  | Application process status.Once the application process starts, it will update the status as started. After successful process of all the application records, It will be updated as completed Validation Rules: |
| 4 | `DLM.LAST.REVIEW.COUNT` | `DlmControl_LastReviewCount` | TField |  | Holds Count of RO.COPY.KEYLIST it will updated as per the REVIEW.TIME configuration in DLM.PARAMETER Validation Rules: |
| 5 | `DLM.RESERVED.10` | `DlmControl_Reserved10` | TField |  |  |
| 6 | `DLM.RESERVED.9` | `DlmControl_Reserved9` | TField |  |  |
| 7 | `DLM.RESERVED.8` | `DlmControl_Reserved8` | TField |  |  |
| 8 | `DLM.RESERVED.7` | `DlmControl_Reserved7` | TField |  |  |
| 9 | `DLM.RESERVED.6` | `DlmControl_Reserved6` | TField |  |  |
| 10 | `DLM.RESERVED.5` | `DlmControl_Reserved5` | TField |  |  |
| 11 | `DLM.RESERVED.4` | `DlmControl_Reserved4` | TField |  |  |
| 12 | `DLM.RESERVED.3` | `DlmControl_Reserved3` | TField |  |  |
| 13 | `DLM.RESERVED.2` | `DlmControl_Reserved2` | TField |  |  |
| 14 | `DLM.RESERVED.1` | `DlmControl_Reserved1` | TField |  |  |
