# SE.MS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SE.MS.PARAMETER` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MS.PAR.TOTAL.MS.INJECTION` | `SeMsParameter_TotalMsInjection` | TField |  |  |
| 2 | `MS.PAR.CHECK.POINT.NAME` | `SeMsParameter_CheckPointName` |  |  |  |
| 3 | `MS.PAR.CHECK.POINT.INJECT` | `SeMsParameter_CheckPointInject` |  |  |  |
| 4 | `MS.PAR.SHELL.CMD` | `SeMsParameter_ShellCmd` |  |  |  |
| 5 | `MS.PAR.RESERVED.05` | `SeMsParameter_Reserved05` | TField |  |  |
| 6 | `MS.PAR.RESERVED.04` | `SeMsParameter_Reserved04` | TField |  |  |
| 7 | `MS.PAR.RESERVED.03` | `SeMsParameter_Reserved03` | TField |  |  |
| 8 | `MS.PAR.RESERVED.02` | `SeMsParameter_Reserved02` | TField |  |  |
| 9 | `MS.PAR.RESERVED.01` | `SeMsParameter_Reserved01` | TField |  |  |
| 10 | `MS.PAR.RECORD.STATUS` | `SeMsParameter_RecordStatus` | String |  |  |
| 11 | `MS.PAR.CURR.NO` | `SeMsParameter_CurrNo` | String |  |  |
| 12 | `MS.PAR.INPUTTER` | `SeMsParameter_Inputter` |  |  |  |
| 13 | `MS.PAR.DATE.TIME` | `SeMsParameter_DateTime` |  |  |  |
| 14 | `MS.PAR.AUTHORISER` | `SeMsParameter_Authoriser` | String |  |  |
| 15 | `MS.PAR.CO.CODE` | `SeMsParameter_CoCode` | String |  |  |
| 16 | `MS.PAR.DEPT.CODE` | `SeMsParameter_DeptCode` | String |  |  |
| 17 | `MS.PAR.AUDITOR.CODE` | `SeMsParameter_AuditorCode` | String |  |  |
| 18 | `MS.PAR.AUDIT.DATE.TIME` | `SeMsParameter_AuditDateTime` | String |  |  |
