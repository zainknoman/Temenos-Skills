# SC.BULK.TRANS.MATCHING — Table Schema

> Source: `INSERTS/I_F.SC.BULK.TRANS.MATCHING` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BTM.FIELD.NAME` | `ScBulkTransMatching_FieldName` |  |  |  |
| 2 | `SC.BTM.ORDER.EXCEP.CHECK` | `ScBulkTransMatching_OrderExcepCheck` | TField |  | This field will determine whether exception checks are to be performed for order so that parent order will not be allowed to authorise until all child orders are authorised. Validation Rules: Allowed value is YES |
| 3 | `SC.BTM.ORD.FIELD.NAME` | `ScBulkTransMatching_OrdFieldName` |  |  |  |
| 4 | `SC.BTM.RESERVED.03` | `ScBulkTransMatching_Reserved03` | TField |  |  |
| 5 | `SC.BTM.RESERVED.02` | `ScBulkTransMatching_Reserved02` | TField |  |  |
| 6 | `SC.BTM.LOCAL.REF` | `ScBulkTransMatching_LocalRef` |  |  |  |
| 7 | `SC.BTM.OVERRIDE` | `ScBulkTransMatching_Override` |  |  |  |
| 8 | `SC.BTM.RECORD.STATUS` | `ScBulkTransMatching_RecordStatus` | String |  |  |
| 9 | `SC.BTM.CURR.NO` | `ScBulkTransMatching_CurrNo` | String |  |  |
| 10 | `SC.BTM.INPUTTER` | `ScBulkTransMatching_Inputter` |  |  |  |
| 11 | `SC.BTM.DATE.TIME` | `ScBulkTransMatching_DateTime` |  |  |  |
| 12 | `SC.BTM.AUTHORISER` | `ScBulkTransMatching_Authoriser` | String |  |  |
| 13 | `SC.BTM.CO.CODE` | `ScBulkTransMatching_CoCode` | String |  |  |
| 14 | `SC.BTM.DEPT.CODE` | `ScBulkTransMatching_DeptCode` | String |  |  |
| 15 | `SC.BTM.AUDITOR.CODE` | `ScBulkTransMatching_AuditorCode` | String |  |  |
| 16 | `SC.BTM.AUDIT.DATE.TIME` | `ScBulkTransMatching_AuditDateTime` | String |  |  |
