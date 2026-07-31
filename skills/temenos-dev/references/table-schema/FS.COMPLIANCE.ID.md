# FS.COMPLIANCE.ID — Table Schema

> Source: `INSERTS/I_F.FS.COMPLIANCE.ID` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COMPLIANCE.ID.DESCRIPTION` | `FsComplianceId_Description` |  |  |  |
| 2 | `FS.COMPLIANCE.ID.FILTER.KEY` | `FsComplianceId_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COMPLIANCE.ID.RECORD.ID` | `FsComplianceId_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COMPLIANCE.ID.RESERVED10` | `FsComplianceId_Reserved10` | TField |  |  |
| 5 | `FS.COMPLIANCE.ID.RESERVED9` | `FsComplianceId_Reserved9` | TField |  |  |
| 6 | `FS.COMPLIANCE.ID.RESERVED8` | `FsComplianceId_Reserved8` | TField |  |  |
| 7 | `FS.COMPLIANCE.ID.RESERVED7` | `FsComplianceId_Reserved7` | TField |  |  |
| 8 | `FS.COMPLIANCE.ID.RESERVED6` | `FsComplianceId_Reserved6` | TField |  |  |
| 9 | `FS.COMPLIANCE.ID.RESERVED5` | `FsComplianceId_Reserved5` | TField |  |  |
| 10 | `FS.COMPLIANCE.ID.RESERVED4` | `FsComplianceId_Reserved4` | TField |  |  |
| 11 | `FS.COMPLIANCE.ID.RESERVED3` | `FsComplianceId_Reserved3` | TField |  |  |
| 12 | `FS.COMPLIANCE.ID.RESERVED2` | `FsComplianceId_Reserved2` | TField |  |  |
| 13 | `FS.COMPLIANCE.ID.RESERVED1` | `FsComplianceId_Reserved1` | TField |  |  |
| 14 | `FS.COMPLIANCE.ID.LOCAL.REF` | `FsComplianceId_LocalRef` |  |  |  |
| 15 | `FS.COMPLIANCE.ID.OVERRIDE` | `FsComplianceId_Override` |  |  |  |
| 16 | `FS.COMPLIANCE.ID.RECORD.STATUS` | `FsComplianceId_RecordStatus` | String |  |  |
| 17 | `FS.COMPLIANCE.ID.CURR.NO` | `FsComplianceId_CurrNo` | String |  |  |
| 18 | `FS.COMPLIANCE.ID.INPUTTER` | `FsComplianceId_Inputter` |  |  |  |
| 19 | `FS.COMPLIANCE.ID.DATE.TIME` | `FsComplianceId_DateTime` |  |  |  |
| 20 | `FS.COMPLIANCE.ID.AUTHORISER` | `FsComplianceId_Authoriser` | String |  |  |
| 21 | `FS.COMPLIANCE.ID.CO.CODE` | `FsComplianceId_CoCode` | String |  |  |
| 22 | `FS.COMPLIANCE.ID.DEPT.CODE` | `FsComplianceId_DeptCode` | String |  |  |
| 23 | `FS.COMPLIANCE.ID.AUDITOR.CODE` | `FsComplianceId_AuditorCode` | String |  |  |
| 24 | `FS.COMPLIANCE.ID.AUDIT.DATE.TIME` | `FsComplianceId_AuditDateTime` | String |  |  |
