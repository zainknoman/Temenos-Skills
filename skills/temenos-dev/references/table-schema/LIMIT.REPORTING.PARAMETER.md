# LIMIT.REPORTING.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LIMIT.REPORTING.PARAMETER` in `LI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.LRP.EXP.SPLIT.CUST` | `LimitReportingParameter_ExpSplitCust` | TField |  | Field to mention whether pro-rata calculation has to be done irrespective of manual percentage in Common Exposure Reports Validation Rules: Either Yes or No |
| 2 | `LI.LRP.CHECK.VAL.LIM.BREACH` | `LimitReportingParameter_CheckValLimBreach` | TField |  | This field is used to indicate if the breaches to validation limits have to be reported in a separate live file LIMIT.HIERARCHY.BAL.BREACH Validation Rules: Valid values are YES and NULL |
| 3 | `LI.LRP.REP.EXP.LIMITS` | `LimitReportingParameter_RepExpLimits` | TField |  | Defines if report needs to be generated for expiring limits or not. Validation Rules: Either Yes or No. Default is Yes which means report will be generated for expiring limits. |
| 4 | `LI.LRP.RESERVED.08` | `LimitReportingParameter_Reserved08` | TField |  |  |
| 5 | `LI.LRP.RESERVED.07` | `LimitReportingParameter_Reserved07` | TField |  |  |
| 6 | `LI.LRP.RESERVED.06` | `LimitReportingParameter_Reserved06` | TField |  |  |
| 7 | `LI.LRP.RESERVED.05` | `LimitReportingParameter_Reserved05` | TField |  |  |
| 8 | `LI.LRP.RESERVED.04` | `LimitReportingParameter_Reserved04` | TField |  |  |
| 9 | `LI.LRP.RESERVED.03` | `LimitReportingParameter_Reserved03` | TField |  |  |
| 10 | `LI.LRP.RESERVED.02` | `LimitReportingParameter_Reserved02` | TField |  |  |
| 11 | `LI.LRP.RESERVED.01` | `LimitReportingParameter_Reserved01` | TField |  |  |
| 12 | `LI.LRP.LOCAL.REF` | `LimitReportingParameter_LocalRef` |  |  |  |
| 13 | `LI.LRP.OVERRIDE` | `LimitReportingParameter_Override` |  |  |  |
| 14 | `LI.LRP.RECORD.STATUS` | `LimitReportingParameter_RecordStatus` | String |  |  |
| 15 | `LI.LRP.CURR.NO` | `LimitReportingParameter_CurrNo` | String |  |  |
| 16 | `LI.LRP.INPUTTER` | `LimitReportingParameter_Inputter` |  |  |  |
| 17 | `LI.LRP.DATE.TIME` | `LimitReportingParameter_DateTime` |  |  |  |
| 18 | `LI.LRP.AUTHORISER` | `LimitReportingParameter_Authoriser` | String |  |  |
| 19 | `LI.LRP.CO.CODE` | `LimitReportingParameter_CoCode` | String |  |  |
| 20 | `LI.LRP.DEPT.CODE` | `LimitReportingParameter_DeptCode` | String |  |  |
| 21 | `LI.LRP.AUDITOR.CODE` | `LimitReportingParameter_AuditorCode` | String |  |  |
| 22 | `LI.LRP.AUDIT.DATE.TIME` | `LimitReportingParameter_AuditDateTime` | String |  |  |
