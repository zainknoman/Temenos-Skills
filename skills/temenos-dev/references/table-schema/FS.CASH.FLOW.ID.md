# FS.CASH.FLOW.ID — Table Schema

> Source: `INSERTS/I_F.FS.CASH.FLOW.ID` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CASH.FLOW.ID.DESCRIPTION` | `FsCashFlowId_Description` |  |  |  |
| 2 | `FS.CASH.FLOW.ID.FILTER.KEY` | `FsCashFlowId_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CASH.FLOW.ID.RECORD.ID` | `FsCashFlowId_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CASH.FLOW.ID.RESERVED10` | `FsCashFlowId_Reserved10` | TField |  |  |
| 5 | `FS.CASH.FLOW.ID.RESERVED9` | `FsCashFlowId_Reserved9` | TField |  |  |
| 6 | `FS.CASH.FLOW.ID.RESERVED8` | `FsCashFlowId_Reserved8` | TField |  |  |
| 7 | `FS.CASH.FLOW.ID.RESERVED7` | `FsCashFlowId_Reserved7` | TField |  |  |
| 8 | `FS.CASH.FLOW.ID.RESERVED6` | `FsCashFlowId_Reserved6` | TField |  |  |
| 9 | `FS.CASH.FLOW.ID.RESERVED5` | `FsCashFlowId_Reserved5` | TField |  |  |
| 10 | `FS.CASH.FLOW.ID.RESERVED4` | `FsCashFlowId_Reserved4` | TField |  |  |
| 11 | `FS.CASH.FLOW.ID.RESERVED3` | `FsCashFlowId_Reserved3` | TField |  |  |
| 12 | `FS.CASH.FLOW.ID.RESERVED2` | `FsCashFlowId_Reserved2` | TField |  |  |
| 13 | `FS.CASH.FLOW.ID.RESERVED1` | `FsCashFlowId_Reserved1` | TField |  |  |
| 14 | `FS.CASH.FLOW.ID.LOCAL.REF` | `FsCashFlowId_LocalRef` |  |  |  |
| 15 | `FS.CASH.FLOW.ID.OVERRIDE` | `FsCashFlowId_Override` |  |  |  |
| 16 | `FS.CASH.FLOW.ID.RECORD.STATUS` | `FsCashFlowId_RecordStatus` | String |  |  |
| 17 | `FS.CASH.FLOW.ID.CURR.NO` | `FsCashFlowId_CurrNo` | String |  |  |
| 18 | `FS.CASH.FLOW.ID.INPUTTER` | `FsCashFlowId_Inputter` |  |  |  |
| 19 | `FS.CASH.FLOW.ID.DATE.TIME` | `FsCashFlowId_DateTime` |  |  |  |
| 20 | `FS.CASH.FLOW.ID.AUTHORISER` | `FsCashFlowId_Authoriser` | String |  |  |
| 21 | `FS.CASH.FLOW.ID.CO.CODE` | `FsCashFlowId_CoCode` | String |  |  |
| 22 | `FS.CASH.FLOW.ID.DEPT.CODE` | `FsCashFlowId_DeptCode` | String |  |  |
| 23 | `FS.CASH.FLOW.ID.AUDITOR.CODE` | `FsCashFlowId_AuditorCode` | String |  |  |
| 24 | `FS.CASH.FLOW.ID.AUDIT.DATE.TIME` | `FsCashFlowId_AuditDateTime` | String |  |  |
