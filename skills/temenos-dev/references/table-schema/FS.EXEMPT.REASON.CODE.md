# FS.EXEMPT.REASON.CODE — Table Schema

> Source: `INSERTS/I_F.FS.EXEMPT.REASON.CODE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.EXEMPT.REASON.CODE.DESCRIPTION` | `FsExemptReasonCode_Description` |  |  |  |
| 2 | `FS.EXEMPT.REASON.CODE.FILTER.KEY` | `FsExemptReasonCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.EXEMPT.REASON.CODE.RECORD.ID` | `FsExemptReasonCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.EXEMPT.REASON.CODE.RESERVED10` | `FsExemptReasonCode_Reserved10` | TField |  |  |
| 5 | `FS.EXEMPT.REASON.CODE.RESERVED9` | `FsExemptReasonCode_Reserved9` | TField |  |  |
| 6 | `FS.EXEMPT.REASON.CODE.RESERVED8` | `FsExemptReasonCode_Reserved8` | TField |  |  |
| 7 | `FS.EXEMPT.REASON.CODE.RESERVED7` | `FsExemptReasonCode_Reserved7` | TField |  |  |
| 8 | `FS.EXEMPT.REASON.CODE.RESERVED6` | `FsExemptReasonCode_Reserved6` | TField |  |  |
| 9 | `FS.EXEMPT.REASON.CODE.RESERVED5` | `FsExemptReasonCode_Reserved5` | TField |  |  |
| 10 | `FS.EXEMPT.REASON.CODE.RESERVED4` | `FsExemptReasonCode_Reserved4` | TField |  |  |
| 11 | `FS.EXEMPT.REASON.CODE.RESERVED3` | `FsExemptReasonCode_Reserved3` | TField |  |  |
| 12 | `FS.EXEMPT.REASON.CODE.RESERVED2` | `FsExemptReasonCode_Reserved2` | TField |  |  |
| 13 | `FS.EXEMPT.REASON.CODE.RESERVED1` | `FsExemptReasonCode_Reserved1` | TField |  |  |
| 14 | `FS.EXEMPT.REASON.CODE.LOCAL.REF` | `FsExemptReasonCode_LocalRef` |  |  |  |
| 15 | `FS.EXEMPT.REASON.CODE.OVERRIDE` | `FsExemptReasonCode_Override` |  |  |  |
| 16 | `FS.EXEMPT.REASON.CODE.RECORD.STATUS` | `FsExemptReasonCode_RecordStatus` | String |  |  |
| 17 | `FS.EXEMPT.REASON.CODE.CURR.NO` | `FsExemptReasonCode_CurrNo` | String |  |  |
| 18 | `FS.EXEMPT.REASON.CODE.INPUTTER` | `FsExemptReasonCode_Inputter` |  |  |  |
| 19 | `FS.EXEMPT.REASON.CODE.DATE.TIME` | `FsExemptReasonCode_DateTime` |  |  |  |
| 20 | `FS.EXEMPT.REASON.CODE.AUTHORISER` | `FsExemptReasonCode_Authoriser` | String |  |  |
| 21 | `FS.EXEMPT.REASON.CODE.CO.CODE` | `FsExemptReasonCode_CoCode` | String |  |  |
| 22 | `FS.EXEMPT.REASON.CODE.DEPT.CODE` | `FsExemptReasonCode_DeptCode` | String |  |  |
| 23 | `FS.EXEMPT.REASON.CODE.AUDITOR.CODE` | `FsExemptReasonCode_AuditorCode` | String |  |  |
| 24 | `FS.EXEMPT.REASON.CODE.AUDIT.DATE.TIME` | `FsExemptReasonCode_AuditDateTime` | String |  |  |
