# FS.OPERATION.CODE — Table Schema

> Source: `INSERTS/I_F.FS.OPERATION.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.OPERATION.CODE.DESCRIPTION` | `FsOperationCode_Description` |  |  |  |
| 2 | `FS.OPERATION.CODE.FILTER.KEY` | `FsOperationCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.OPERATION.CODE.RECORD.ID` | `FsOperationCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.OPERATION.CODE.RESERVED10` | `FsOperationCode_Reserved10` | TField |  |  |
| 5 | `FS.OPERATION.CODE.RESERVED9` | `FsOperationCode_Reserved9` | TField |  |  |
| 6 | `FS.OPERATION.CODE.RESERVED8` | `FsOperationCode_Reserved8` | TField |  |  |
| 7 | `FS.OPERATION.CODE.RESERVED7` | `FsOperationCode_Reserved7` | TField |  |  |
| 8 | `FS.OPERATION.CODE.RESERVED6` | `FsOperationCode_Reserved6` | TField |  |  |
| 9 | `FS.OPERATION.CODE.RESERVED5` | `FsOperationCode_Reserved5` | TField |  |  |
| 10 | `FS.OPERATION.CODE.RESERVED4` | `FsOperationCode_Reserved4` | TField |  |  |
| 11 | `FS.OPERATION.CODE.RESERVED3` | `FsOperationCode_Reserved3` | TField |  |  |
| 12 | `FS.OPERATION.CODE.RESERVED2` | `FsOperationCode_Reserved2` | TField |  |  |
| 13 | `FS.OPERATION.CODE.RESERVED1` | `FsOperationCode_Reserved1` | TField |  |  |
| 14 | `FS.OPERATION.CODE.LOCAL.REF` | `FsOperationCode_LocalRef` |  |  |  |
| 15 | `FS.OPERATION.CODE.OVERRIDE` | `FsOperationCode_Override` |  |  |  |
| 16 | `FS.OPERATION.CODE.RECORD.STATUS` | `FsOperationCode_RecordStatus` | String |  |  |
| 17 | `FS.OPERATION.CODE.CURR.NO` | `FsOperationCode_CurrNo` | String |  |  |
| 18 | `FS.OPERATION.CODE.INPUTTER` | `FsOperationCode_Inputter` |  |  |  |
| 19 | `FS.OPERATION.CODE.DATE.TIME` | `FsOperationCode_DateTime` |  |  |  |
| 20 | `FS.OPERATION.CODE.AUTHORISER` | `FsOperationCode_Authoriser` | String |  |  |
| 21 | `FS.OPERATION.CODE.CO.CODE` | `FsOperationCode_CoCode` | String |  |  |
| 22 | `FS.OPERATION.CODE.DEPT.CODE` | `FsOperationCode_DeptCode` | String |  |  |
| 23 | `FS.OPERATION.CODE.AUDITOR.CODE` | `FsOperationCode_AuditorCode` | String |  |  |
| 24 | `FS.OPERATION.CODE.AUDIT.DATE.TIME` | `FsOperationCode_AuditDateTime` | String |  |  |
