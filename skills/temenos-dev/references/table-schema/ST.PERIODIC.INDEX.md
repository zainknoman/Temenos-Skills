# ST.PERIODIC.INDEX — Table Schema

> Source: `INSERTS/I_F.ST.PERIODIC.INDEX` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PR.IND.DESCRIPTION` | `StPeriodicIndex_Description` |  |  |  |
| 2 | `PR.IND.ALLOW.AMT` | `StPeriodicIndex_AllowAmt` | TField |  | Options field to specify whether AMT definition is allowed in PERIODIC.INTEREST application. When ST.PERIODIC.INDEX record is automatically created by the system, then ALLOW.AMT field will be updated as YES / NULL. Valid values are YES , NO , NULL YES/NULL - Definition of AMT is allowed (existing behaviour) NO - Definition of AMT is not allowed Validation rules: This is a NOCHANGE field |
| 3 | `PR.IND.PROCESS.ONLINE` | `StPeriodicIndex_Reserved5` |  |  |  |
| 4 | `PR.IND.RESERVED.4` | `StPeriodicIndex_Reserved4` |  |  |  |
| 5 | `PR.IND.RESERVED.3` | `StPeriodicIndex_Reserved3` | TField |  |  |
| 6 | `PR.IND.RESERVED.2` | `StPeriodicIndex_Reserved2` | TField |  |  |
| 7 | `PR.IND.RESERVED.1` | `StPeriodicIndex_Reserved1` | TField |  |  |
| 8 | `PR.IND.LOCAL.REF` | `StPeriodicIndex_LocalRef` |  |  |  |
| 9 | `PR.IND.OVERRIDE` | `StPeriodicIndex_Override` |  |  |  |
| 10 | `PR.IND.RECORD.STATUS` | `StPeriodicIndex_RecordStatus` | String |  |  |
| 11 | `PR.IND.CURR.NO` | `StPeriodicIndex_CurrNo` | String |  |  |
| 12 | `PR.IND.INPUTTER` | `StPeriodicIndex_Inputter` |  |  |  |
| 13 | `PR.IND.DATE.TIME` | `StPeriodicIndex_DateTime` |  |  |  |
| 14 | `PR.IND.AUTHORISER` | `StPeriodicIndex_Authoriser` | String |  |  |
| 15 | `PR.IND.CO.CODE` | `StPeriodicIndex_CoCode` | String |  |  |
| 16 | `PR.IND.DEPT.CODE` | `StPeriodicIndex_DeptCode` | String |  |  |
| 17 | `PR.IND.AUDITOR.CODE` | `StPeriodicIndex_AuditorCode` | String |  |  |
| 18 | `PR.IND.AUDIT.DATE.TIME` | `StPeriodicIndex_AuditDateTime` | String |  |  |
