# CR.COMMON.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.CR.COMMON.ACTIVITY` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.COMMON.DESC` | `CrCommonActivity_Desc` |  |  |  |
| 2 | `CR.COMMON.RESERVED.10` | `CrCommonActivity_Reserved10` |  |  |  |
| 3 | `CR.COMMON.RESERVED.09` | `CrCommonActivity_Reserved09` |  |  |  |
| 4 | `CR.COMMON.RESERVED.08` | `CrCommonActivity_Reserved08` |  |  |  |
| 5 | `CR.COMMON.RESERVED.07` | `CrCommonActivity_Reserved07` |  |  |  |
| 6 | `CR.COMMON.RESERVED.06` | `CrCommonActivity_Reserved06` |  |  |  |
| 7 | `CR.COMMON.RESERVED.05` | `CrCommonActivity_Reserved05` |  |  |  |
| 8 | `CR.COMMON.RESERVED.04` | `CrCommonActivity_Reserved04` |  |  |  |
| 9 | `CR.COMMON.RESERVED.03` | `CrCommonActivity_Reserved03` |  |  |  |
| 10 | `CR.COMMON.RESERVED.02` | `CrCommonActivity_Reserved02` |  |  |  |
| 11 | `CR.COMMON.RESERVED.01` | `CrCommonActivity_Reserved01` |  |  |  |
| 12 | `CR.COMMON.LOCAL.REF` | `CrCommonActivity_LocalRef` |  |  |  |
| 13 | `CR.COMMON.RECORD.STATUS` | `CrCommonActivity_RecordStatus` |  |  |  |
| 14 | `CR.COMMON.CURR.NO` | `CrCommonActivity_CurrNo` |  |  |  |
| 15 | `CR.COMMON.INPUTTER` | `CrCommonActivity_Inputter` |  |  |  |
| 16 | `CR.COMMON.DATE.TIME` | `CrCommonActivity_DateTime` |  |  |  |
| 17 | `CR.COMMON.AUTHORISER` | `CrCommonActivity_Authoriser` |  |  |  |
| 18 | `CR.COMMON.CO.CODE` | `CrCommonActivity_CoCode` |  |  |  |
| 19 | `CR.COMMON.DEPT.CODE` | `CrCommonActivity_DeptCode` |  |  |  |
| 20 | `CR.COMMON.AUDITOR.CODE` | `CrCommonActivity_AuditorCode` |  |  |  |
| 21 | `CR.COMMON.AUDIT.DATE.TIME` | `CrCommonActivity_AuditDateTime` |  |  |  |
