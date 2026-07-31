# SC.BULK.CHILD.AUTHORISE — Table Schema

> Source: `INSERTS/I_F.SC.BULK.CHILD.AUTHORISE` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BCA.PARENT.ID` | `ScBulkChildAuthorise_ParentId` |  |  |  |
| 2 | `SC.BCA.RESERVED.05` | `ScBulkChildAuthorise_Reserved05` | TField |  |  |
| 3 | `SC.BCA.RESERVED.04` | `ScBulkChildAuthorise_Reserved04` | TField |  |  |
| 4 | `SC.BCA.RESERVED.03` | `ScBulkChildAuthorise_Reserved03` | TField |  |  |
| 5 | `SC.BCA.RESERVED.02` | `ScBulkChildAuthorise_Reserved02` | TField |  |  |
| 6 | `SC.BCA.LOCAL.REF` | `ScBulkChildAuthorise_LocalRef` |  |  |  |
| 7 | `SC.BCA.OVERRIDE` | `ScBulkChildAuthorise_Override` |  |  |  |
| 8 | `SC.BCA.RECORD.STATUS` | `ScBulkChildAuthorise_RecordStatus` | String |  |  |
| 9 | `SC.BCA.CURR.NO` | `ScBulkChildAuthorise_CurrNo` | String |  |  |
| 10 | `SC.BCA.INPUTTER` | `ScBulkChildAuthorise_Inputter` |  |  |  |
| 11 | `SC.BCA.DATE.TIME` | `ScBulkChildAuthorise_DateTime` |  |  |  |
| 12 | `SC.BCA.AUTHORISER` | `ScBulkChildAuthorise_Authoriser` | String |  |  |
| 13 | `SC.BCA.CO.CODE` | `ScBulkChildAuthorise_CoCode` | String |  |  |
| 14 | `SC.BCA.DEPT.CODE` | `ScBulkChildAuthorise_DeptCode` | String |  |  |
| 15 | `SC.BCA.AUDITOR.CODE` | `ScBulkChildAuthorise_AuditorCode` | String |  |  |
| 16 | `SC.BCA.AUDIT.DATE.TIME` | `ScBulkChildAuthorise_AuditDateTime` | String |  |  |
