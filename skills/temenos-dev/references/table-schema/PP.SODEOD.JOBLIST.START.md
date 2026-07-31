# PP.SODEOD.JOBLIST.START — Table Schema

> Source: `INSERTS/I_F.PP.SODEOD.JOBLIST.START` in `PP_SODEODService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SJS.ServiceName` | `PpSodeodJoblistStart_Servicename` |  |  |  |
| 2 | `PP.SJS.Action` | `PpSodeodJoblistStart_Action` |  |  |  |
| 3 | `PP.SJS.OVERRIDE` | `PpSodeodJoblistStart_Override` |  |  |  |
| 4 | `PP.SJS.RECORD.STATUS` | `PpSodeodJoblistStart_RecordStatus` |  |  |  |
| 5 | `PP.SJS.CURR.NO` | `PpSodeodJoblistStart_CurrNo` |  |  |  |
| 6 | `PP.SJS.INPUTTER` | `PpSodeodJoblistStart_Inputter` |  |  |  |
| 7 | `PP.SJS.DATE.TIME` | `PpSodeodJoblistStart_DateTime` |  |  |  |
| 8 | `PP.SJS.AUTHORISER` | `PpSodeodJoblistStart_Authoriser` |  |  |  |
| 9 | `PP.SJS.CO.CODE` | `PpSodeodJoblistStart_CoCode` |  |  |  |
| 10 | `PP.SJS.DEPT.CODE` | `PpSodeodJoblistStart_DeptCode` |  |  |  |
| 11 | `PP.SJS.AUDITOR.CODE` | `PpSodeodJoblistStart_AuditorCode` |  |  |  |
| 12 | `PP.SJS.AUDIT.DATE.TIME` | `PpSodeodJoblistStart_AuditDateTime` |  |  |  |
