# PP.VIRTUAL.QUEUE.LIST — Table Schema

> Source: `INSERTS/I_F.PP.VIRTUAL.QUEUE.LIST` in `PP_InquiryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.VQL.VirtualQName` | `PpVirtualQueueList_Virtualqname` |  |  |  |
| 2 | `PP.VQL.RECORD.STATUS` | `PpVirtualQueueList_RecordStatus` | String |  |  |
| 3 | `PP.VQL.CURR.NO` | `PpVirtualQueueList_CurrNo` | String |  |  |
| 4 | `PP.VQL.INPUTTER` | `PpVirtualQueueList_Inputter` |  |  |  |
| 5 | `PP.VQL.DATE.TIME` | `PpVirtualQueueList_DateTime` |  |  |  |
| 6 | `PP.VQL.AUTHORISER` | `PpVirtualQueueList_Authoriser` | String |  |  |
| 7 | `PP.VQL.CO.CODE` | `PpVirtualQueueList_CoCode` | String |  |  |
| 8 | `PP.VQL.DEPT.CODE` | `PpVirtualQueueList_DeptCode` | String |  |  |
| 9 | `PP.VQL.AUDITOR.CODE` | `PpVirtualQueueList_AuditorCode` | String |  |  |
| 10 | `PP.VQL.AUDIT.DATE.TIME` | `PpVirtualQueueList_AuditDateTime` | String |  |  |
