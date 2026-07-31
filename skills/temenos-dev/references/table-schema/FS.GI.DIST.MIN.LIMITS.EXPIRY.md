# FS.GI.DIST.MIN.LIMITS.EXPIRY — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.MIN.LIMITS.EXPIRY` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.PARENT.REF.ID` | `FsGiDistMinLimitsExpiry_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.ORA.ROWID` | `FsGiDistMinLimitsExpiry_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.REGISTER.ID` | `FsGiDistMinLimitsExpiry_RegisterId` | TField |  | Register Internal ID Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.TA.FUND.ID` | `FsGiDistMinLimitsExpiry_TaFundId` | TField |  | Fund internal ID Multifonds DB Column is NPTF. |
| 5 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.SHARE.CLASS.CODE` | `FsGiDistMinLimitsExpiry_ShareClassCode` | TField |  | Fund share class Multifonds DB Column is TPART. |
| 6 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.APPROVAL.EXPIRY.DATE` | `FsGiDistMinLimitsExpiry_ApprovalExpiryDate` | TField |  | Expiry date for the auto approval of orders which do not meet the minimum investment limit. Multifonds DB Column is EXPIRY_DATE. |
| 7 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.LIMITS.MET.FLAG` | `FsGiDistMinLimitsExpiry_LimitsMetFlag` | TField |  | Flag to indicate that the investor has maintained the first subscription limit during approval period. Multifonds DB Column is FLG_LIMITS_MET. |
| 8 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.MET.FLAG` | `FsGiDistMinLimitsExpiry_MetFlag` | TField |  | Flag to indicate that minimum expiry limit met for the entity. Multifonds DB Column is FLG_MET. |
| 9 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.MIN.LIMIT.EXPIRY.ID` | `FsGiDistMinLimitsExpiry_MinLimitExpiryId` | TField |  | Unique Internal identifier for Minimum limits expriry record. Multifonds DB Column is INTERNAL_ID. |
| 10 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.FUND.ID` | `FsGiDistMinLimitsExpiry_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 11 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.CLASS.CURRENCY` | `FsGiDistMinLimitsExpiry_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 12 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED10` | `FsGiDistMinLimitsExpiry_Reserved10` | TField |  |  |
| 13 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED9` | `FsGiDistMinLimitsExpiry_Reserved9` | TField |  |  |
| 14 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED8` | `FsGiDistMinLimitsExpiry_Reserved8` | TField |  |  |
| 15 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED7` | `FsGiDistMinLimitsExpiry_Reserved7` | TField |  |  |
| 16 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED6` | `FsGiDistMinLimitsExpiry_Reserved6` | TField |  |  |
| 17 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED5` | `FsGiDistMinLimitsExpiry_Reserved5` | TField |  |  |
| 18 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED4` | `FsGiDistMinLimitsExpiry_Reserved4` | TField |  |  |
| 19 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED3` | `FsGiDistMinLimitsExpiry_Reserved3` | TField |  |  |
| 20 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED2` | `FsGiDistMinLimitsExpiry_Reserved2` | TField |  |  |
| 21 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RESERVED1` | `FsGiDistMinLimitsExpiry_Reserved1` | TField |  |  |
| 22 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.LOCAL.REF` | `FsGiDistMinLimitsExpiry_LocalRef` |  |  |  |
| 23 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.OVERRIDE` | `FsGiDistMinLimitsExpiry_Override` |  |  |  |
| 24 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.RECORD.STATUS` | `FsGiDistMinLimitsExpiry_RecordStatus` | String |  |  |
| 25 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.CURR.NO` | `FsGiDistMinLimitsExpiry_CurrNo` | String |  |  |
| 26 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.INPUTTER` | `FsGiDistMinLimitsExpiry_Inputter` |  |  |  |
| 27 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.DATE.TIME` | `FsGiDistMinLimitsExpiry_DateTime` |  |  |  |
| 28 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.AUTHORISER` | `FsGiDistMinLimitsExpiry_Authoriser` | String |  |  |
| 29 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.CO.CODE` | `FsGiDistMinLimitsExpiry_CoCode` | String |  |  |
| 30 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.DEPT.CODE` | `FsGiDistMinLimitsExpiry_DeptCode` | String |  |  |
| 31 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.AUDITOR.CODE` | `FsGiDistMinLimitsExpiry_AuditorCode` | String |  |  |
| 32 | `FS.GI.DIST.MIN.LIMITS.EXPIRY.AUDIT.DATE.TIME` | `FsGiDistMinLimitsExpiry_AuditDateTime` | String |  |  |
