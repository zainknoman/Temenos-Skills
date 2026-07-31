# FS.COMPLIANCE.LAW.CODES — Table Schema

> Source: `INSERTS/I_F.FS.COMPLIANCE.LAW.CODES` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COMPLIANCE.LAW.CODES.DESCRIPTION` | `FsComplianceLawCodes_Description` |  |  |  |
| 2 | `FS.COMPLIANCE.LAW.CODES.FILTER.KEY` | `FsComplianceLawCodes_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COMPLIANCE.LAW.CODES.RECORD.ID` | `FsComplianceLawCodes_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COMPLIANCE.LAW.CODES.RESERVED10` | `FsComplianceLawCodes_Reserved10` | TField |  |  |
| 5 | `FS.COMPLIANCE.LAW.CODES.RESERVED9` | `FsComplianceLawCodes_Reserved9` | TField |  |  |
| 6 | `FS.COMPLIANCE.LAW.CODES.RESERVED8` | `FsComplianceLawCodes_Reserved8` | TField |  |  |
| 7 | `FS.COMPLIANCE.LAW.CODES.RESERVED7` | `FsComplianceLawCodes_Reserved7` | TField |  |  |
| 8 | `FS.COMPLIANCE.LAW.CODES.RESERVED6` | `FsComplianceLawCodes_Reserved6` | TField |  |  |
| 9 | `FS.COMPLIANCE.LAW.CODES.RESERVED5` | `FsComplianceLawCodes_Reserved5` | TField |  |  |
| 10 | `FS.COMPLIANCE.LAW.CODES.RESERVED4` | `FsComplianceLawCodes_Reserved4` | TField |  |  |
| 11 | `FS.COMPLIANCE.LAW.CODES.RESERVED3` | `FsComplianceLawCodes_Reserved3` | TField |  |  |
| 12 | `FS.COMPLIANCE.LAW.CODES.RESERVED2` | `FsComplianceLawCodes_Reserved2` | TField |  |  |
| 13 | `FS.COMPLIANCE.LAW.CODES.RESERVED1` | `FsComplianceLawCodes_Reserved1` | TField |  |  |
| 14 | `FS.COMPLIANCE.LAW.CODES.LOCAL.REF` | `FsComplianceLawCodes_LocalRef` |  |  |  |
| 15 | `FS.COMPLIANCE.LAW.CODES.OVERRIDE` | `FsComplianceLawCodes_Override` |  |  |  |
| 16 | `FS.COMPLIANCE.LAW.CODES.RECORD.STATUS` | `FsComplianceLawCodes_RecordStatus` | String |  |  |
| 17 | `FS.COMPLIANCE.LAW.CODES.CURR.NO` | `FsComplianceLawCodes_CurrNo` | String |  |  |
| 18 | `FS.COMPLIANCE.LAW.CODES.INPUTTER` | `FsComplianceLawCodes_Inputter` |  |  |  |
| 19 | `FS.COMPLIANCE.LAW.CODES.DATE.TIME` | `FsComplianceLawCodes_DateTime` |  |  |  |
| 20 | `FS.COMPLIANCE.LAW.CODES.AUTHORISER` | `FsComplianceLawCodes_Authoriser` | String |  |  |
| 21 | `FS.COMPLIANCE.LAW.CODES.CO.CODE` | `FsComplianceLawCodes_CoCode` | String |  |  |
| 22 | `FS.COMPLIANCE.LAW.CODES.DEPT.CODE` | `FsComplianceLawCodes_DeptCode` | String |  |  |
| 23 | `FS.COMPLIANCE.LAW.CODES.AUDITOR.CODE` | `FsComplianceLawCodes_AuditorCode` | String |  |  |
| 24 | `FS.COMPLIANCE.LAW.CODES.AUDIT.DATE.TIME` | `FsComplianceLawCodes_AuditDateTime` | String |  |  |
