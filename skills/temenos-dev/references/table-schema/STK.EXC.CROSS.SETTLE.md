# STK.EXC.CROSS.SETTLE — Table Schema

> Source: `INSERTS/I_F.STK.EXC.CROSS.SETTLE` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.STK.MKT.IDN.CODE` | `StkExcCrossSettle_MktIdnCode` |  |  |  |
| 2 | `SC.STK.ISIN.EXCEPTION` | `StkExcCrossSettle_IsinException` |  |  |  |
| 3 | `SC.STK.LOCAL.REF` | `StkExcCrossSettle_LocalRef` |  |  |  |
| 4 | `SC.STK.OVERRIDE` | `StkExcCrossSettle_Override` |  |  |  |
| 5 | `SC.STK.RECORD.STATUS` | `StkExcCrossSettle_RecordStatus` | String |  |  |
| 6 | `SC.STK.CURR.NO` | `StkExcCrossSettle_CurrNo` | String |  |  |
| 7 | `SC.STK.INPUTTER` | `StkExcCrossSettle_Inputter` |  |  |  |
| 8 | `SC.STK.DATE.TIME` | `StkExcCrossSettle_DateTime` |  |  |  |
| 9 | `SC.STK.AUTHORISER` | `StkExcCrossSettle_Authoriser` | String |  |  |
| 10 | `SC.STK.CO.CODE` | `StkExcCrossSettle_CoCode` | String |  |  |
| 11 | `SC.STK.DEPT.CODE` | `StkExcCrossSettle_DeptCode` | String |  |  |
| 12 | `SC.STK.AUDITOR.CODE` | `StkExcCrossSettle_AuditorCode` | String |  |  |
| 13 | `SC.STK.AUDIT.DATE.TIME` | `StkExcCrossSettle_AuditDateTime` | String |  |  |
