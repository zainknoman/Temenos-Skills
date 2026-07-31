# SC.BULK.UPDATE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SC.BULK.UPDATE.PARAMETER` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BUP.FIELD.NAME` | `ScBulkUpdateParameter_FieldName` |  |  |  |
| 2 | `SC.BUP.RESERVED.05` | `ScBulkUpdateParameter_Reserved05` | TField |  |  |
| 3 | `SC.BUP.RESERVED.04` | `ScBulkUpdateParameter_Reserved04` | TField |  |  |
| 4 | `SC.BUP.RESERVED.03` | `ScBulkUpdateParameter_Reserved03` | TField |  |  |
| 5 | `SC.BUP.RESERVED.02` | `ScBulkUpdateParameter_Reserved02` | TField |  |  |
| 6 | `SC.BUP.LOCAL.REF` | `ScBulkUpdateParameter_LocalRef` |  |  |  |
| 7 | `SC.BUP.OVERRIDE` | `ScBulkUpdateParameter_Override` |  |  |  |
| 8 | `SC.BUP.RECORD.STATUS` | `ScBulkUpdateParameter_RecordStatus` | String |  |  |
| 9 | `SC.BUP.CURR.NO` | `ScBulkUpdateParameter_CurrNo` | String |  |  |
| 10 | `SC.BUP.INPUTTER` | `ScBulkUpdateParameter_Inputter` |  |  |  |
| 11 | `SC.BUP.DATE.TIME` | `ScBulkUpdateParameter_DateTime` |  |  |  |
| 12 | `SC.BUP.AUTHORISER` | `ScBulkUpdateParameter_Authoriser` | String |  |  |
| 13 | `SC.BUP.CO.CODE` | `ScBulkUpdateParameter_CoCode` | String |  |  |
| 14 | `SC.BUP.DEPT.CODE` | `ScBulkUpdateParameter_DeptCode` | String |  |  |
| 15 | `SC.BUP.AUDITOR.CODE` | `ScBulkUpdateParameter_AuditorCode` | String |  |  |
| 16 | `SC.BUP.AUDIT.DATE.TIME` | `ScBulkUpdateParameter_AuditDateTime` | String |  |  |
