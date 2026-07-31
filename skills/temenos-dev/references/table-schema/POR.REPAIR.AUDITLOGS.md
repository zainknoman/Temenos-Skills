# POR.REPAIR.AUDITLOGS — Table Schema

> Source: `INSERTS/I_F.POR.REPAIR.AUDITLOGS` in `PP_PaymentWorkflowDASService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPRAL.CurrNo` | `PorRepairAuditlogs_Currno` |  |  |  |
| 2 | `PPRAL.Inputter` | `PorRepairAuditlogs_Inputter` |  |  |  |
| 3 | `PPRAL.InputterDate` | `PorRepairAuditlogs_Inputterdate` |  |  |  |
| 4 | `PPRAL.InputterTime` | `PorRepairAuditlogs_Inputtertime` |  |  |  |
| 5 | `PPRAL.Authoriser1` | `PorRepairAuditlogs_Authoriser1` |  |  |  |
| 6 | `PPRAL.Authoriser1Date` | `PorRepairAuditlogs_Authoriser1date` |  |  |  |
| 7 | `PPRAL.Authoriser1Time` | `PorRepairAuditlogs_Authoriser1time` |  |  |  |
| 8 | `PPRAL.Authoriser2` | `PorRepairAuditlogs_Authoriser2` |  |  |  |
| 9 | `PPRAL.Authoriser2Date` | `PorRepairAuditlogs_Authoriser2date` |  |  |  |
| 10 | `PPRAL.Authoriser2Time` | `PorRepairAuditlogs_Authoriser2time` |  |  |  |
| 11 | `PPRAL.FieldPrompt` | `PorRepairAuditlogs_Fieldprompt` |  |  |  |
| 12 | `PPRAL.OldValue` | `PorRepairAuditlogs_Oldvalue` |  |  |  |
| 13 | `PPRAL.NewValue` | `PorRepairAuditlogs_Newvalue` |  |  |  |
| 14 | `PPRAL.RECORD.STATUS` | `PorRepairAuditlogs_RecordStatus` |  |  |  |
| 15 | `PPRAL.CURR.NO` | `PorRepairAuditlogs_CurrNo` |  |  |  |
| 16 | `PPRAL.INPUTTER` | `PorRepairAuditlogs_Inputter` |  |  |  |
| 17 | `PPRAL.DATE.TIME` | `PorRepairAuditlogs_DateTime` |  |  |  |
| 18 | `PPRAL.AUTHORISER` | `PorRepairAuditlogs_Authoriser` |  |  |  |
| 19 | `PPRAL.CO.CODE` | `PorRepairAuditlogs_CoCode` |  |  |  |
| 20 | `PPRAL.DEPT.CODE` | `PorRepairAuditlogs_DeptCode` |  |  |  |
| 21 | `PPRAL.AUDITOR.CODE` | `PorRepairAuditlogs_AuditorCode` |  |  |  |
| 22 | `PPRAL.AUDIT.DATE.TIME` | `PorRepairAuditlogs_AuditDateTime` |  |  |  |
