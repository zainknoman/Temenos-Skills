# FS.GI.LP.FEE.GROUP.MEMBERSHIP — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.GROUP.MEMBERSHIP` in `FS_LimitedPartnershipProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.PARENT.REF.ID` | `FsGiLpFeeGroupMembership_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.ORA.ROWID` | `FsGiLpFeeGroupMembership_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.FEE.TYPE` | `FsGiLpFeeGroupMembership_FeeType` | TField |  | Fee type (Asset based fee or Incentive fee). Multifonds DB Column is CFEE_TYPE. |
| 4 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.GROUP.ID` | `FsGiLpFeeGroupMembership_GroupId` | TField |  | Fee group ID. Multifonds DB Column is GROUP_ID. |
| 5 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.GROUP.DESCRIPTION` | `FsGiLpFeeGroupMembership_GroupDescription` | TField |  | Fee group description. Multifonds DB Column is GROUP_DESCRIPTION. |
| 6 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.VALID.FROM` | `FsGiLpFeeGroupMembership_ValidFrom` | TField |  | Fee group membership valid start date. Multifonds DB Column is DVALID_START. |
| 7 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.GROUP.TYPE` | `FsGiLpFeeGroupMembership_GroupType` | TField |  | Type of fee group. Multifonds DB Column is GROUP_TYPE. |
| 8 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.TA.FUND.ID` | `FsGiLpFeeGroupMembership_TaFundId` | TField |  | Fund linked to fee group. Multifonds DB Column is NPTF. |
| 9 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.SHARE.CLASS.CODE` | `FsGiLpFeeGroupMembership_ShareClassCode` | TField |  | Share class of the fund linked to fee group. Multifonds DB Column is TPART. |
| 10 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.REGISTER.ID` | `FsGiLpFeeGroupMembership_RegisterId` | TField |  | Register linked to fee group membership Multifonds DB Column is NREGISTER. |
| 11 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.TRANCHE.ID` | `FsGiLpFeeGroupMembership_TrancheId` | TField |  | Tranche of the register linked to Fee group membership. Multifonds DB Column is TRANCHE. |
| 12 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.EXPIRY.DATE` | `FsGiLpFeeGroupMembership_ExpiryDate` | TField |  | Fee group membership expiry date. Multifonds DB Column is EXPIRY_DATE. |
| 13 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.FUND.ID` | `FsGiLpFeeGroupMembership_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 14 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.CLASS.CURRENCY` | `FsGiLpFeeGroupMembership_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 15 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED10` | `FsGiLpFeeGroupMembership_Reserved10` | TField |  |  |
| 16 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED9` | `FsGiLpFeeGroupMembership_Reserved9` | TField |  |  |
| 17 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED8` | `FsGiLpFeeGroupMembership_Reserved8` | TField |  |  |
| 18 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED7` | `FsGiLpFeeGroupMembership_Reserved7` | TField |  |  |
| 19 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED6` | `FsGiLpFeeGroupMembership_Reserved6` | TField |  |  |
| 20 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED5` | `FsGiLpFeeGroupMembership_Reserved5` | TField |  |  |
| 21 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED4` | `FsGiLpFeeGroupMembership_Reserved4` | TField |  |  |
| 22 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED3` | `FsGiLpFeeGroupMembership_Reserved3` | TField |  |  |
| 23 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED2` | `FsGiLpFeeGroupMembership_Reserved2` | TField |  |  |
| 24 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RESERVED1` | `FsGiLpFeeGroupMembership_Reserved1` | TField |  |  |
| 25 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.LOCAL.REF` | `FsGiLpFeeGroupMembership_LocalRef` |  |  |  |
| 26 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.OVERRIDE` | `FsGiLpFeeGroupMembership_Override` |  |  |  |
| 27 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.RECORD.STATUS` | `FsGiLpFeeGroupMembership_RecordStatus` | String |  |  |
| 28 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.CURR.NO` | `FsGiLpFeeGroupMembership_CurrNo` | String |  |  |
| 29 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.INPUTTER` | `FsGiLpFeeGroupMembership_Inputter` |  |  |  |
| 30 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.DATE.TIME` | `FsGiLpFeeGroupMembership_DateTime` |  |  |  |
| 31 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.AUTHORISER` | `FsGiLpFeeGroupMembership_Authoriser` | String |  |  |
| 32 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.CO.CODE` | `FsGiLpFeeGroupMembership_CoCode` | String |  |  |
| 33 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.DEPT.CODE` | `FsGiLpFeeGroupMembership_DeptCode` | String |  |  |
| 34 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.AUDITOR.CODE` | `FsGiLpFeeGroupMembership_AuditorCode` | String |  |  |
| 35 | `FS.GI.LP.FEE.GROUP.MEMBERSHIP.AUDIT.DATE.TIME` | `FsGiLpFeeGroupMembership_AuditDateTime` | String |  |  |
