# SC.BULK.REPLACE — Table Schema

> Source: `INSERTS/I_F.SC.BULK.REPLACE` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BRE.PARENT.ID` | `ScBulkReplace_ParentId` |  |  |  |
| 2 | `SC.BRE.RESERVED.05` | `ScBulkReplace_Reserved05` | TField |  |  |
| 3 | `SC.BRE.RESERVED.04` | `ScBulkReplace_Reserved04` | TField |  |  |
| 4 | `SC.BRE.RESERVED.03` | `ScBulkReplace_Reserved03` | TField |  |  |
| 5 | `SC.BRE.RESERVED.02` | `ScBulkReplace_Reserved02` | TField |  |  |
| 6 | `SC.BRE.LOCAL.REF` | `ScBulkReplace_LocalRef` |  |  |  |
| 7 | `SC.BRE.OVERRIDE` | `ScBulkReplace_Override` |  |  |  |
| 8 | `SC.BRE.RECORD.STATUS` | `ScBulkReplace_RecordStatus` | String |  |  |
| 9 | `SC.BRE.CURR.NO` | `ScBulkReplace_CurrNo` | String |  |  |
| 10 | `SC.BRE.INPUTTER` | `ScBulkReplace_Inputter` |  |  |  |
| 11 | `SC.BRE.DATE.TIME` | `ScBulkReplace_DateTime` |  |  |  |
| 12 | `SC.BRE.AUTHORISER` | `ScBulkReplace_Authoriser` | String |  |  |
| 13 | `SC.BRE.CO.CODE` | `ScBulkReplace_CoCode` | String |  |  |
| 14 | `SC.BRE.DEPT.CODE` | `ScBulkReplace_DeptCode` | String |  |  |
| 15 | `SC.BRE.AUDITOR.CODE` | `ScBulkReplace_AuditorCode` | String |  |  |
| 16 | `SC.BRE.AUDIT.DATE.TIME` | `ScBulkReplace_AuditDateTime` | String |  |  |
