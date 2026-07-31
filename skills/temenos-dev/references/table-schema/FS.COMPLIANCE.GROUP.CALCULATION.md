# FS.COMPLIANCE.GROUP.CALCULATION — Table Schema

> Source: `INSERTS/I_F.FS.COMPLIANCE.GROUP.CALCULATION` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COMPLIANCE.GROUP.CALCULATION.DESCRIPTION` | `FsComplianceGroupCalculation_Description` |  |  |  |
| 2 | `FS.COMPLIANCE.GROUP.CALCULATION.FILTER.KEY` | `FsComplianceGroupCalculation_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COMPLIANCE.GROUP.CALCULATION.RECORD.ID` | `FsComplianceGroupCalculation_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED10` | `FsComplianceGroupCalculation_Reserved10` | TField |  |  |
| 5 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED9` | `FsComplianceGroupCalculation_Reserved9` | TField |  |  |
| 6 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED8` | `FsComplianceGroupCalculation_Reserved8` | TField |  |  |
| 7 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED7` | `FsComplianceGroupCalculation_Reserved7` | TField |  |  |
| 8 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED6` | `FsComplianceGroupCalculation_Reserved6` | TField |  |  |
| 9 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED5` | `FsComplianceGroupCalculation_Reserved5` | TField |  |  |
| 10 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED4` | `FsComplianceGroupCalculation_Reserved4` | TField |  |  |
| 11 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED3` | `FsComplianceGroupCalculation_Reserved3` | TField |  |  |
| 12 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED2` | `FsComplianceGroupCalculation_Reserved2` | TField |  |  |
| 13 | `FS.COMPLIANCE.GROUP.CALCULATION.RESERVED1` | `FsComplianceGroupCalculation_Reserved1` | TField |  |  |
| 14 | `FS.COMPLIANCE.GROUP.CALCULATION.LOCAL.REF` | `FsComplianceGroupCalculation_LocalRef` |  |  |  |
| 15 | `FS.COMPLIANCE.GROUP.CALCULATION.OVERRIDE` | `FsComplianceGroupCalculation_Override` |  |  |  |
| 16 | `FS.COMPLIANCE.GROUP.CALCULATION.RECORD.STATUS` | `FsComplianceGroupCalculation_RecordStatus` | String |  |  |
| 17 | `FS.COMPLIANCE.GROUP.CALCULATION.CURR.NO` | `FsComplianceGroupCalculation_CurrNo` | String |  |  |
| 18 | `FS.COMPLIANCE.GROUP.CALCULATION.INPUTTER` | `FsComplianceGroupCalculation_Inputter` |  |  |  |
| 19 | `FS.COMPLIANCE.GROUP.CALCULATION.DATE.TIME` | `FsComplianceGroupCalculation_DateTime` |  |  |  |
| 20 | `FS.COMPLIANCE.GROUP.CALCULATION.AUTHORISER` | `FsComplianceGroupCalculation_Authoriser` | String |  |  |
| 21 | `FS.COMPLIANCE.GROUP.CALCULATION.CO.CODE` | `FsComplianceGroupCalculation_CoCode` | String |  |  |
| 22 | `FS.COMPLIANCE.GROUP.CALCULATION.DEPT.CODE` | `FsComplianceGroupCalculation_DeptCode` | String |  |  |
| 23 | `FS.COMPLIANCE.GROUP.CALCULATION.AUDITOR.CODE` | `FsComplianceGroupCalculation_AuditorCode` | String |  |  |
| 24 | `FS.COMPLIANCE.GROUP.CALCULATION.AUDIT.DATE.TIME` | `FsComplianceGroupCalculation_AuditDateTime` | String |  |  |
