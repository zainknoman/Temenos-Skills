# FS.GI.FUND.MANAGEMENT.COMPANY — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.MANAGEMENT.COMPANY` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.MANAGEMENT.COMPANY.PARENT.REF.ID` | `FsGiFundManagementCompany_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.MANAGEMENT.COMPANY.ORA.ROWID` | `FsGiFundManagementCompany_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.MANAGEMENT.COMPANY.FUND.ID` | `FsGiFundManagementCompany_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.MANAGEMENT.COMPANY.MANAGEMENT.COMPANY.ID` | `FsGiFundManagementCompany_ManagementCompanyId` | TField |  | Management company internal ID. Multifonds DB Column is NCSP. |
| 5 | `FS.GI.FUND.MANAGEMENT.COMPANY.MANAGEMENT.COMPANY.ROLE` | `FsGiFundManagementCompany_ManagementCompanyRole` | TField |  | Role of management company. Multifonds DB Column is CROLE. |
| 6 | `FS.GI.FUND.MANAGEMENT.COMPANY.MIFID.RELATIONSHIP` | `FsGiFundManagementCompany_MifidRelationship` | TField |  | MIFID relationship to determine if the management company is under the MIFID directive or not. Multifonds DB Column is MIFID_REL. |
| 7 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED10` | `FsGiFundManagementCompany_Reserved10` | TField |  |  |
| 8 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED9` | `FsGiFundManagementCompany_Reserved9` | TField |  |  |
| 9 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED8` | `FsGiFundManagementCompany_Reserved8` | TField |  |  |
| 10 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED7` | `FsGiFundManagementCompany_Reserved7` | TField |  |  |
| 11 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED6` | `FsGiFundManagementCompany_Reserved6` | TField |  |  |
| 12 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED5` | `FsGiFundManagementCompany_Reserved5` | TField |  |  |
| 13 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED4` | `FsGiFundManagementCompany_Reserved4` | TField |  |  |
| 14 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED3` | `FsGiFundManagementCompany_Reserved3` | TField |  |  |
| 15 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED2` | `FsGiFundManagementCompany_Reserved2` | TField |  |  |
| 16 | `FS.GI.FUND.MANAGEMENT.COMPANY.RESERVED1` | `FsGiFundManagementCompany_Reserved1` | TField |  |  |
| 17 | `FS.GI.FUND.MANAGEMENT.COMPANY.LOCAL.REF` | `FsGiFundManagementCompany_LocalRef` |  |  |  |
| 18 | `FS.GI.FUND.MANAGEMENT.COMPANY.OVERRIDE` | `FsGiFundManagementCompany_Override` |  |  |  |
| 19 | `FS.GI.FUND.MANAGEMENT.COMPANY.RECORD.STATUS` | `FsGiFundManagementCompany_RecordStatus` | String |  |  |
| 20 | `FS.GI.FUND.MANAGEMENT.COMPANY.CURR.NO` | `FsGiFundManagementCompany_CurrNo` | String |  |  |
| 21 | `FS.GI.FUND.MANAGEMENT.COMPANY.INPUTTER` | `FsGiFundManagementCompany_Inputter` |  |  |  |
| 22 | `FS.GI.FUND.MANAGEMENT.COMPANY.DATE.TIME` | `FsGiFundManagementCompany_DateTime` |  |  |  |
| 23 | `FS.GI.FUND.MANAGEMENT.COMPANY.AUTHORISER` | `FsGiFundManagementCompany_Authoriser` | String |  |  |
| 24 | `FS.GI.FUND.MANAGEMENT.COMPANY.CO.CODE` | `FsGiFundManagementCompany_CoCode` | String |  |  |
| 25 | `FS.GI.FUND.MANAGEMENT.COMPANY.DEPT.CODE` | `FsGiFundManagementCompany_DeptCode` | String |  |  |
| 26 | `FS.GI.FUND.MANAGEMENT.COMPANY.AUDITOR.CODE` | `FsGiFundManagementCompany_AuditorCode` | String |  |  |
| 27 | `FS.GI.FUND.MANAGEMENT.COMPANY.AUDIT.DATE.TIME` | `FsGiFundManagementCompany_AuditDateTime` | String |  |  |
