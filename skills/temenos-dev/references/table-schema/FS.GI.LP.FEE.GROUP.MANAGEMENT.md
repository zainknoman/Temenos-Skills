# FS.GI.LP.FEE.GROUP.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.GROUP.MANAGEMENT` in `FS_LimitedPartnershipProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.PARENT.REF.ID` | `FsGiLpFeeGroupManagement_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.ORA.ROWID` | `FsGiLpFeeGroupManagement_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.GROUP.ID` | `FsGiLpFeeGroupManagement_GroupId` | TField |  | Fee Group ID. Multifonds DB Column is GROUP_ID. |
| 4 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.GROUP.DESCRIPTION` | `FsGiLpFeeGroupManagement_GroupDescription` | TField |  | Fee Group ID description. Multifonds DB Column is GROUP_DESCRIPTION. |
| 5 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.GROUP.TYPE` | `FsGiLpFeeGroupManagement_GroupType` | TField |  | Type of Fee group. Multifonds DB Column is GROUP_TYPE. |
| 6 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.FEE.TYPE` | `FsGiLpFeeGroupManagement_FeeType` | TField |  | Fee type (Asset based fee or Incentive fee). Multifonds DB Column is CFEE_TYPE. |
| 7 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.TA.FUND.ID` | `FsGiLpFeeGroupManagement_TaFundId` | TField |  | Fund linked to fee group. Multifonds DB Column is NPTF. |
| 8 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.SHARE.CLASS.CODE` | `FsGiLpFeeGroupManagement_ShareClassCode` | TField |  | Share class of the fund linked to fee group. Multifonds DB Column is TPART. |
| 9 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.REGISRTER.ID` | `FsGiLpFeeGroupManagement_RegisrterId` | TField |  | Register linked to fee group membership Multifonds DB Column is NREGISTER. |
| 10 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.TRANCHE.ID` | `FsGiLpFeeGroupManagement_TrancheId` | TField |  | Tranche of the register linked to Fee group membership. Multifonds DB Column is TRANCHE. |
| 11 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.BP.START.DATE` | `FsGiLpFeeGroupManagement_BpStartDate` | TField |  | Current BP start date of the fund. Multifonds DB Column is BP_START_DATE. |
| 12 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.PBD.STATUS` | `FsGiLpFeeGroupManagement_PbdStatus` | TField |  | Partner book data status of the fund as of the current BP start date. Multifonds DB Column is PBD_STATUS. |
| 13 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.VALID.FROM` | `FsGiLpFeeGroupManagement_ValidFrom` | TField |  | Fee group membership valid from date. Multifonds DB Column is DVALID_FROM. |
| 14 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.EXPIRY.DATE` | `FsGiLpFeeGroupManagement_ExpiryDate` | TField |  | Fee group membership expiry date. Multifonds DB Column is EXPIRY_DATE. |
| 15 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.FUND.ID` | `FsGiLpFeeGroupManagement_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 16 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.CLASS.CURRENCY` | `FsGiLpFeeGroupManagement_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 17 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED10` | `FsGiLpFeeGroupManagement_Reserved10` | TField |  |  |
| 18 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED9` | `FsGiLpFeeGroupManagement_Reserved9` | TField |  |  |
| 19 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED8` | `FsGiLpFeeGroupManagement_Reserved8` | TField |  |  |
| 20 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED7` | `FsGiLpFeeGroupManagement_Reserved7` | TField |  |  |
| 21 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED6` | `FsGiLpFeeGroupManagement_Reserved6` | TField |  |  |
| 22 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED5` | `FsGiLpFeeGroupManagement_Reserved5` | TField |  |  |
| 23 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED4` | `FsGiLpFeeGroupManagement_Reserved4` | TField |  |  |
| 24 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED3` | `FsGiLpFeeGroupManagement_Reserved3` | TField |  |  |
| 25 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED2` | `FsGiLpFeeGroupManagement_Reserved2` | TField |  |  |
| 26 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RESERVED1` | `FsGiLpFeeGroupManagement_Reserved1` | TField |  |  |
| 27 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.LOCAL.REF` | `FsGiLpFeeGroupManagement_LocalRef` |  |  |  |
| 28 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.OVERRIDE` | `FsGiLpFeeGroupManagement_Override` |  |  |  |
| 29 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.RECORD.STATUS` | `FsGiLpFeeGroupManagement_RecordStatus` | String |  |  |
| 30 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.CURR.NO` | `FsGiLpFeeGroupManagement_CurrNo` | String |  |  |
| 31 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.INPUTTER` | `FsGiLpFeeGroupManagement_Inputter` |  |  |  |
| 32 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.DATE.TIME` | `FsGiLpFeeGroupManagement_DateTime` |  |  |  |
| 33 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.AUTHORISER` | `FsGiLpFeeGroupManagement_Authoriser` | String |  |  |
| 34 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.CO.CODE` | `FsGiLpFeeGroupManagement_CoCode` | String |  |  |
| 35 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.DEPT.CODE` | `FsGiLpFeeGroupManagement_DeptCode` | String |  |  |
| 36 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.AUDITOR.CODE` | `FsGiLpFeeGroupManagement_AuditorCode` | String |  |  |
| 37 | `FS.GI.LP.FEE.GROUP.MANAGEMENT.AUDIT.DATE.TIME` | `FsGiLpFeeGroupManagement_AuditDateTime` | String |  |  |
