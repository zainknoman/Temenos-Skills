# FS.GA.FUND.COPY.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUND.COPY.TEMPLATE` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUND.COPY.TEMPLATE.PARENT.REF.ID` | `FsGaFundCopyTemplate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUND.COPY.TEMPLATE.ORA.ROWID` | `FsGaFundCopyTemplate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUND.COPY.TEMPLATE.FUND.MODEL.ID` | `FsGaFundCopyTemplate_FundModelId` | TField |  | Fund Model Id Multifonds DB Column is NPTF_MODEL_ID. |
| 4 | `FS.GA.FUND.COPY.TEMPLATE.FUND.SHELL.COPY` | `FsGaFundCopyTemplate_FundShellCopy` | TField |  | Fund shell copy Multifonds DB Column is NPTF_SHELL_SRC. |
| 5 | `FS.GA.FUND.COPY.TEMPLATE.TAX.REGIME` | `FsGaFundCopyTemplate_TaxRegime` | TField |  | A group of Tax rules can be defined in the Tax tables against a Tax regime and all the funds defined with the respective Tax regime would follow the tax rules defined under this Tax regime. Multifonds DB Column is TAX_REG. |
| 6 | `FS.GA.FUND.COPY.TEMPLATE.WEM.GROUP` | `FsGaFundCopyTemplate_WemGroup` | TField |  | WEM Group Multifonds DB Column is WEM_GROUP_ID. |
| 7 | `FS.GA.FUND.COPY.TEMPLATE.WEM.FAMILY.ID` | `FsGaFundCopyTemplate_WemFamilyId` | TField |  | WEM Family ID Multifonds DB Column is WEM_FAMILY_ID. |
| 8 | `FS.GA.FUND.COPY.TEMPLATE.WEM.MODEL.ID` | `FsGaFundCopyTemplate_WemModelId` | TField |  | WEM Model ID Multifonds DB Column is WEM_MODEL_ID. |
| 9 | `FS.GA.FUND.COPY.TEMPLATE.NAV.GROUP.CODE` | `FsGaFundCopyTemplate_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 10 | `FS.GA.FUND.COPY.TEMPLATE.INTERNAL.SECURITY.ID` | `FsGaFundCopyTemplate_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 11 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED10` | `FsGaFundCopyTemplate_Reserved10` | TField |  |  |
| 12 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED9` | `FsGaFundCopyTemplate_Reserved9` | TField |  |  |
| 13 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED8` | `FsGaFundCopyTemplate_Reserved8` | TField |  |  |
| 14 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED7` | `FsGaFundCopyTemplate_Reserved7` | TField |  |  |
| 15 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED6` | `FsGaFundCopyTemplate_Reserved6` | TField |  |  |
| 16 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED5` | `FsGaFundCopyTemplate_Reserved5` | TField |  |  |
| 17 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED4` | `FsGaFundCopyTemplate_Reserved4` | TField |  |  |
| 18 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED3` | `FsGaFundCopyTemplate_Reserved3` | TField |  |  |
| 19 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED2` | `FsGaFundCopyTemplate_Reserved2` | TField |  |  |
| 20 | `FS.GA.FUND.COPY.TEMPLATE.RESERVED1` | `FsGaFundCopyTemplate_Reserved1` | TField |  |  |
| 21 | `FS.GA.FUND.COPY.TEMPLATE.LOCAL.REF` | `FsGaFundCopyTemplate_LocalRef` |  |  |  |
| 22 | `FS.GA.FUND.COPY.TEMPLATE.OVERRIDE` | `FsGaFundCopyTemplate_Override` |  |  |  |
| 23 | `FS.GA.FUND.COPY.TEMPLATE.RECORD.STATUS` | `FsGaFundCopyTemplate_RecordStatus` | String |  |  |
| 24 | `FS.GA.FUND.COPY.TEMPLATE.CURR.NO` | `FsGaFundCopyTemplate_CurrNo` | String |  |  |
| 25 | `FS.GA.FUND.COPY.TEMPLATE.INPUTTER` | `FsGaFundCopyTemplate_Inputter` |  |  |  |
| 26 | `FS.GA.FUND.COPY.TEMPLATE.DATE.TIME` | `FsGaFundCopyTemplate_DateTime` |  |  |  |
| 27 | `FS.GA.FUND.COPY.TEMPLATE.AUTHORISER` | `FsGaFundCopyTemplate_Authoriser` | String |  |  |
| 28 | `FS.GA.FUND.COPY.TEMPLATE.CO.CODE` | `FsGaFundCopyTemplate_CoCode` | String |  |  |
| 29 | `FS.GA.FUND.COPY.TEMPLATE.DEPT.CODE` | `FsGaFundCopyTemplate_DeptCode` | String |  |  |
| 30 | `FS.GA.FUND.COPY.TEMPLATE.AUDITOR.CODE` | `FsGaFundCopyTemplate_AuditorCode` | String |  |  |
| 31 | `FS.GA.FUND.COPY.TEMPLATE.AUDIT.DATE.TIME` | `FsGaFundCopyTemplate_AuditDateTime` | String |  |  |
