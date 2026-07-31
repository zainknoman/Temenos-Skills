# FS.AML.DOCUMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.AML.DOCUMENT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.AML.DOCUMENT.TYPE.DESCRIPTION` | `FsAmlDocumentType_Description` |  |  |  |
| 2 | `FS.AML.DOCUMENT.TYPE.FILTER.KEY` | `FsAmlDocumentType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.AML.DOCUMENT.TYPE.RECORD.ID` | `FsAmlDocumentType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.AML.DOCUMENT.TYPE.RESERVED10` | `FsAmlDocumentType_Reserved10` | TField |  |  |
| 5 | `FS.AML.DOCUMENT.TYPE.RESERVED9` | `FsAmlDocumentType_Reserved9` | TField |  |  |
| 6 | `FS.AML.DOCUMENT.TYPE.RESERVED8` | `FsAmlDocumentType_Reserved8` | TField |  |  |
| 7 | `FS.AML.DOCUMENT.TYPE.RESERVED7` | `FsAmlDocumentType_Reserved7` | TField |  |  |
| 8 | `FS.AML.DOCUMENT.TYPE.RESERVED6` | `FsAmlDocumentType_Reserved6` | TField |  |  |
| 9 | `FS.AML.DOCUMENT.TYPE.RESERVED5` | `FsAmlDocumentType_Reserved5` | TField |  |  |
| 10 | `FS.AML.DOCUMENT.TYPE.RESERVED4` | `FsAmlDocumentType_Reserved4` | TField |  |  |
| 11 | `FS.AML.DOCUMENT.TYPE.RESERVED3` | `FsAmlDocumentType_Reserved3` | TField |  |  |
| 12 | `FS.AML.DOCUMENT.TYPE.RESERVED2` | `FsAmlDocumentType_Reserved2` | TField |  |  |
| 13 | `FS.AML.DOCUMENT.TYPE.RESERVED1` | `FsAmlDocumentType_Reserved1` | TField |  |  |
| 14 | `FS.AML.DOCUMENT.TYPE.LOCAL.REF` | `FsAmlDocumentType_LocalRef` |  |  |  |
| 15 | `FS.AML.DOCUMENT.TYPE.OVERRIDE` | `FsAmlDocumentType_Override` |  |  |  |
| 16 | `FS.AML.DOCUMENT.TYPE.RECORD.STATUS` | `FsAmlDocumentType_RecordStatus` | String |  |  |
| 17 | `FS.AML.DOCUMENT.TYPE.CURR.NO` | `FsAmlDocumentType_CurrNo` | String |  |  |
| 18 | `FS.AML.DOCUMENT.TYPE.INPUTTER` | `FsAmlDocumentType_Inputter` |  |  |  |
| 19 | `FS.AML.DOCUMENT.TYPE.DATE.TIME` | `FsAmlDocumentType_DateTime` |  |  |  |
| 20 | `FS.AML.DOCUMENT.TYPE.AUTHORISER` | `FsAmlDocumentType_Authoriser` | String |  |  |
| 21 | `FS.AML.DOCUMENT.TYPE.CO.CODE` | `FsAmlDocumentType_CoCode` | String |  |  |
| 22 | `FS.AML.DOCUMENT.TYPE.DEPT.CODE` | `FsAmlDocumentType_DeptCode` | String |  |  |
| 23 | `FS.AML.DOCUMENT.TYPE.AUDITOR.CODE` | `FsAmlDocumentType_AuditorCode` | String |  |  |
| 24 | `FS.AML.DOCUMENT.TYPE.AUDIT.DATE.TIME` | `FsAmlDocumentType_AuditDateTime` | String |  |  |
