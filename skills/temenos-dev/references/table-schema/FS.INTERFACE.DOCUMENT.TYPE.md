# FS.INTERFACE.DOCUMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.INTERFACE.DOCUMENT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.INTERFACE.DOCUMENT.TYPE.DESCRIPTION` | `FsInterfaceDocumentType_Description` |  |  |  |
| 2 | `FS.INTERFACE.DOCUMENT.TYPE.FILTER.KEY` | `FsInterfaceDocumentType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.INTERFACE.DOCUMENT.TYPE.RECORD.ID` | `FsInterfaceDocumentType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED10` | `FsInterfaceDocumentType_Reserved10` | TField |  |  |
| 5 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED9` | `FsInterfaceDocumentType_Reserved9` | TField |  |  |
| 6 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED8` | `FsInterfaceDocumentType_Reserved8` | TField |  |  |
| 7 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED7` | `FsInterfaceDocumentType_Reserved7` | TField |  |  |
| 8 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED6` | `FsInterfaceDocumentType_Reserved6` | TField |  |  |
| 9 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED5` | `FsInterfaceDocumentType_Reserved5` | TField |  |  |
| 10 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED4` | `FsInterfaceDocumentType_Reserved4` | TField |  |  |
| 11 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED3` | `FsInterfaceDocumentType_Reserved3` | TField |  |  |
| 12 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED2` | `FsInterfaceDocumentType_Reserved2` | TField |  |  |
| 13 | `FS.INTERFACE.DOCUMENT.TYPE.RESERVED1` | `FsInterfaceDocumentType_Reserved1` | TField |  |  |
| 14 | `FS.INTERFACE.DOCUMENT.TYPE.LOCAL.REF` | `FsInterfaceDocumentType_LocalRef` |  |  |  |
| 15 | `FS.INTERFACE.DOCUMENT.TYPE.OVERRIDE` | `FsInterfaceDocumentType_Override` |  |  |  |
| 16 | `FS.INTERFACE.DOCUMENT.TYPE.RECORD.STATUS` | `FsInterfaceDocumentType_RecordStatus` | String |  |  |
| 17 | `FS.INTERFACE.DOCUMENT.TYPE.CURR.NO` | `FsInterfaceDocumentType_CurrNo` | String |  |  |
| 18 | `FS.INTERFACE.DOCUMENT.TYPE.INPUTTER` | `FsInterfaceDocumentType_Inputter` |  |  |  |
| 19 | `FS.INTERFACE.DOCUMENT.TYPE.DATE.TIME` | `FsInterfaceDocumentType_DateTime` |  |  |  |
| 20 | `FS.INTERFACE.DOCUMENT.TYPE.AUTHORISER` | `FsInterfaceDocumentType_Authoriser` | String |  |  |
| 21 | `FS.INTERFACE.DOCUMENT.TYPE.CO.CODE` | `FsInterfaceDocumentType_CoCode` | String |  |  |
| 22 | `FS.INTERFACE.DOCUMENT.TYPE.DEPT.CODE` | `FsInterfaceDocumentType_DeptCode` | String |  |  |
| 23 | `FS.INTERFACE.DOCUMENT.TYPE.AUDITOR.CODE` | `FsInterfaceDocumentType_AuditorCode` | String |  |  |
| 24 | `FS.INTERFACE.DOCUMENT.TYPE.AUDIT.DATE.TIME` | `FsInterfaceDocumentType_AuditDateTime` | String |  |  |
