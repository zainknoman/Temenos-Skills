# FS.COMPLIANCE.BASE.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.FS.COMPLIANCE.BASE.DESCRIPTION` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COMPLIANCE.BASE.DESCRIPTION.DESCRIPTION` | `FsComplianceBaseDescription_Description` |  |  |  |
| 2 | `FS.COMPLIANCE.BASE.DESCRIPTION.FILTER.KEY` | `FsComplianceBaseDescription_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COMPLIANCE.BASE.DESCRIPTION.RECORD.ID` | `FsComplianceBaseDescription_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED10` | `FsComplianceBaseDescription_Reserved10` | TField |  |  |
| 5 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED9` | `FsComplianceBaseDescription_Reserved9` | TField |  |  |
| 6 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED8` | `FsComplianceBaseDescription_Reserved8` | TField |  |  |
| 7 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED7` | `FsComplianceBaseDescription_Reserved7` | TField |  |  |
| 8 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED6` | `FsComplianceBaseDescription_Reserved6` | TField |  |  |
| 9 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED5` | `FsComplianceBaseDescription_Reserved5` | TField |  |  |
| 10 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED4` | `FsComplianceBaseDescription_Reserved4` | TField |  |  |
| 11 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED3` | `FsComplianceBaseDescription_Reserved3` | TField |  |  |
| 12 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED2` | `FsComplianceBaseDescription_Reserved2` | TField |  |  |
| 13 | `FS.COMPLIANCE.BASE.DESCRIPTION.RESERVED1` | `FsComplianceBaseDescription_Reserved1` | TField |  |  |
| 14 | `FS.COMPLIANCE.BASE.DESCRIPTION.LOCAL.REF` | `FsComplianceBaseDescription_LocalRef` |  |  |  |
| 15 | `FS.COMPLIANCE.BASE.DESCRIPTION.OVERRIDE` | `FsComplianceBaseDescription_Override` |  |  |  |
| 16 | `FS.COMPLIANCE.BASE.DESCRIPTION.RECORD.STATUS` | `FsComplianceBaseDescription_RecordStatus` | String |  |  |
| 17 | `FS.COMPLIANCE.BASE.DESCRIPTION.CURR.NO` | `FsComplianceBaseDescription_CurrNo` | String |  |  |
| 18 | `FS.COMPLIANCE.BASE.DESCRIPTION.INPUTTER` | `FsComplianceBaseDescription_Inputter` |  |  |  |
| 19 | `FS.COMPLIANCE.BASE.DESCRIPTION.DATE.TIME` | `FsComplianceBaseDescription_DateTime` |  |  |  |
| 20 | `FS.COMPLIANCE.BASE.DESCRIPTION.AUTHORISER` | `FsComplianceBaseDescription_Authoriser` | String |  |  |
| 21 | `FS.COMPLIANCE.BASE.DESCRIPTION.CO.CODE` | `FsComplianceBaseDescription_CoCode` | String |  |  |
| 22 | `FS.COMPLIANCE.BASE.DESCRIPTION.DEPT.CODE` | `FsComplianceBaseDescription_DeptCode` | String |  |  |
| 23 | `FS.COMPLIANCE.BASE.DESCRIPTION.AUDITOR.CODE` | `FsComplianceBaseDescription_AuditorCode` | String |  |  |
| 24 | `FS.COMPLIANCE.BASE.DESCRIPTION.AUDIT.DATE.TIME` | `FsComplianceBaseDescription_AuditDateTime` | String |  |  |
