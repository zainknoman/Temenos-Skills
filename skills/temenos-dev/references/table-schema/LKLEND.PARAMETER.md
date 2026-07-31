# LKLEND.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LKLEND.PARAMETER` in `LKLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKLEND.PARAMETER.LOAN.STATUS` | `LklendParameter_LoanStatus` |  |  |  |
| 2 | `LKLEND.PARAMETER.MONITORING.PERIOD` | `LklendParameter_MonitoringPeriod` |  |  |  |
| 3 | `LKLEND.PARAMETER.PERFORMING.CLASS` | `LklendParameter_PerformingClass` |  |  |  |
| 4 | `LKLEND.PARAMETER.RESERVED.9` | `LklendParameter_Reserved9` | TField |  |  |
| 5 | `LKLEND.PARAMETER.RESERVED.8` | `LklendParameter_Reserved8` | TField |  |  |
| 6 | `LKLEND.PARAMETER.RESERVED.7` | `LklendParameter_Reserved7` | TField |  |  |
| 7 | `LKLEND.PARAMETER.RESERVED.6` | `LklendParameter_Reserved6` | TField |  |  |
| 8 | `LKLEND.PARAMETER.RESERVED.5` | `LklendParameter_Reserved5` | TField |  |  |
| 9 | `LKLEND.PARAMETER.RESERVED.4` | `LklendParameter_Reserved4` | TField |  |  |
| 10 | `LKLEND.PARAMETER.RESERVED.3` | `LklendParameter_Reserved3` | TField |  |  |
| 11 | `LKLEND.PARAMETER.RESERVED.2` | `LklendParameter_Reserved2` | TField |  |  |
| 12 | `LKLEND.PARAMETER.RESERVED.1` | `LklendParameter_Reserved1` | TField |  |  |
| 13 | `LKLEND.PARAMETER.LOCAL.REF` | `LklendParameter_LocalRef` |  |  |  |
| 14 | `LKLEND.PARAMETER.OVERRIDE` | `LklendParameter_Override` |  |  |  |
| 15 | `LKLEND.PARAMETER.RECORD.STATUS` | `LklendParameter_RecordStatus` | String |  |  |
| 16 | `LKLEND.PARAMETER.CURR.NO` | `LklendParameter_CurrNo` | String |  |  |
| 17 | `LKLEND.PARAMETER.INPUTTER` | `LklendParameter_Inputter` |  |  |  |
| 18 | `LKLEND.PARAMETER.DATE.TIME` | `LklendParameter_DateTime` |  |  |  |
| 19 | `LKLEND.PARAMETER.AUTHORISER` | `LklendParameter_Authoriser` | String |  |  |
| 20 | `LKLEND.PARAMETER.CO.CODE` | `LklendParameter_CoCode` | String |  |  |
| 21 | `LKLEND.PARAMETER.DEPT.CODE` | `LklendParameter_DeptCode` | String |  |  |
| 22 | `LKLEND.PARAMETER.AUDITOR.CODE` | `LklendParameter_AuditorCode` | String |  |  |
| 23 | `LKLEND.PARAMETER.AUDIT.DATE.TIME` | `LklendParameter_AuditDateTime` | String |  |  |
