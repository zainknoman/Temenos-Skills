# FS.GI.LP.FEE.GROUP.MGMT.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.GROUP.MGMT.PROCESS` in `FS_LimitedPartnershipProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.PARENT.REF.ID` | `FsGiLpFeeGroupMgmtProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.ORA.ROWID` | `FsGiLpFeeGroupMgmtProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.GROUP.ID.IN` | `FsGiLpFeeGroupMgmtProcess_GroupIdIn` | TField |  | Fee group ID filter field. Multifonds DB Column is GROUP_ID_IN. |
| 4 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.VALID.START.DATE.IN` | `FsGiLpFeeGroupMgmtProcess_ValidStartDateIn` | TField |  | Fee group membership valid start date filter field. Multifonds DB Column is DVALID_START_IN. |
| 5 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.EXPIRY.DATE.IN` | `FsGiLpFeeGroupMgmtProcess_ExpiryDateIn` | TField |  | Fee group membership expiry date filter field. Multifonds DB Column is EXPIRY_DATE_IN. |
| 6 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.GROUP.TYPE.IN` | `FsGiLpFeeGroupMgmtProcess_GroupTypeIn` | TField |  | Type of fee group filter field. Multifonds DB Column is GROUP_TYPE_IN. |
| 7 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.FEE.TYPE.IN` | `FsGiLpFeeGroupMgmtProcess_FeeTypeIn` | TField |  | Fee type (Asset based fee or Incentive fee) filter field. Multifonds DB Column is CFEE_TYPE_IN. |
| 8 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.PROCESS.TYPE` | `FsGiLpFeeGroupMgmtProcess_ProcessType` | TField |  | Group Management process type Multifonds DB Column is PROCESS_TYPE. |
| 9 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.FEE.TYPE` | `FsGiLpFeeGroupMgmtProcess_FeeType` | TField |  | Fee type (Asset based fee or Incentive fee). Multifonds DB Column is CFEE_TYPE. |
| 10 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.GROUP.TYPE` | `FsGiLpFeeGroupMgmtProcess_GroupType` | TField |  | Type of Fee group. Multifonds DB Column is GROUP_TYPE. |
| 11 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.GROUP.ID` | `FsGiLpFeeGroupMgmtProcess_GroupId` | TField |  | Fee Group ID. Multifonds DB Column is GROUP_ID. |
| 12 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.REGISTER.ID` | `FsGiLpFeeGroupMgmtProcess_RegisterId` | TField |  | Register linked to fee group membership Multifonds DB Column is NREGISTER. |
| 13 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.TA.FUND.ID` | `FsGiLpFeeGroupMgmtProcess_TaFundId` | TField |  | Fund linked to fee group. Multifonds DB Column is NPTF. |
| 14 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.SHARE.CLASS.CODE` | `FsGiLpFeeGroupMgmtProcess_ShareClassCode` | TField |  | Share class of the fund linked to fee group. Multifonds DB Column is TPART. |
| 15 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.TRANCHE.ID` | `FsGiLpFeeGroupMgmtProcess_TrancheId` | TField |  | Tranche of the register linked to Fee group membership. Multifonds DB Column is TRANCHE. |
| 16 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.STATUS` | `FsGiLpFeeGroupMgmtProcess_Status` | TField |  | Partner book data status of the fund as of the current BP start date. Multifonds DB Column is STATUS. |
| 17 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.VALID.START.DATE` | `FsGiLpFeeGroupMgmtProcess_ValidStartDate` | TField |  | Fee group membership valid start date. Multifonds DB Column is DVALID_START. |
| 18 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.EXPIRY.DATE` | `FsGiLpFeeGroupMgmtProcess_ExpiryDate` | TField |  | Fee group membership expiry date. Multifonds DB Column is EXPIRY_DATE. |
| 19 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.FUND.ID` | `FsGiLpFeeGroupMgmtProcess_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 20 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.CLASS.CURRENCY` | `FsGiLpFeeGroupMgmtProcess_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 21 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED10` | `FsGiLpFeeGroupMgmtProcess_Reserved10` | TField |  |  |
| 22 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED9` | `FsGiLpFeeGroupMgmtProcess_Reserved9` | TField |  |  |
| 23 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED8` | `FsGiLpFeeGroupMgmtProcess_Reserved8` | TField |  |  |
| 24 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED7` | `FsGiLpFeeGroupMgmtProcess_Reserved7` | TField |  |  |
| 25 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED6` | `FsGiLpFeeGroupMgmtProcess_Reserved6` | TField |  |  |
| 26 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED5` | `FsGiLpFeeGroupMgmtProcess_Reserved5` | TField |  |  |
| 27 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED4` | `FsGiLpFeeGroupMgmtProcess_Reserved4` | TField |  |  |
| 28 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED3` | `FsGiLpFeeGroupMgmtProcess_Reserved3` | TField |  |  |
| 29 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED2` | `FsGiLpFeeGroupMgmtProcess_Reserved2` | TField |  |  |
| 30 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RESERVED1` | `FsGiLpFeeGroupMgmtProcess_Reserved1` | TField |  |  |
| 31 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.LOCAL.REF` | `FsGiLpFeeGroupMgmtProcess_LocalRef` |  |  |  |
| 32 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.OVERRIDE` | `FsGiLpFeeGroupMgmtProcess_Override` |  |  |  |
| 33 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.RECORD.STATUS` | `FsGiLpFeeGroupMgmtProcess_RecordStatus` | String |  |  |
| 34 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.CURR.NO` | `FsGiLpFeeGroupMgmtProcess_CurrNo` | String |  |  |
| 35 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.INPUTTER` | `FsGiLpFeeGroupMgmtProcess_Inputter` |  |  |  |
| 36 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.DATE.TIME` | `FsGiLpFeeGroupMgmtProcess_DateTime` |  |  |  |
| 37 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.AUTHORISER` | `FsGiLpFeeGroupMgmtProcess_Authoriser` | String |  |  |
| 38 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.CO.CODE` | `FsGiLpFeeGroupMgmtProcess_CoCode` | String |  |  |
| 39 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.DEPT.CODE` | `FsGiLpFeeGroupMgmtProcess_DeptCode` | String |  |  |
| 40 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.AUDITOR.CODE` | `FsGiLpFeeGroupMgmtProcess_AuditorCode` | String |  |  |
| 41 | `FS.GI.LP.FEE.GROUP.MGMT.PROCESS.AUDIT.DATE.TIME` | `FsGiLpFeeGroupMgmtProcess_AuditDateTime` | String |  |  |
