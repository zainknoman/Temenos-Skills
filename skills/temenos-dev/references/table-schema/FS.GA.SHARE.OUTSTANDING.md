# FS.GA.SHARE.OUTSTANDING — Table Schema

> Source: `INSERTS/I_F.FS.GA.SHARE.OUTSTANDING` in `FS_FundMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SHARE.OUTSTANDING.PARENT.REF.ID` | `FsGaShareOutstanding_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SHARE.OUTSTANDING.ORA.ROWID` | `FsGaShareOutstanding_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SHARE.OUTSTANDING.FUND.ID` | `FsGaShareOutstanding_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.SHARE.OUTSTANDING.CORRESPONDENT` | `FsGaShareOutstanding_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 5 | `FS.GA.SHARE.OUTSTANDING.SHARE.CLASS.CODE` | `FsGaShareOutstanding_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 6 | `FS.GA.SHARE.OUTSTANDING.OPERATION.CODE` | `FsGaShareOutstanding_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 7 | `FS.GA.SHARE.OUTSTANDING.SUBSCRIPTION.REDEMPTION.SETTLE` | `FsGaShareOutstanding_SubscriptionRedemptionSettle` | TField |  | Subscription Redemption Settle Multifonds DB Column is CODE_NB_DATE_JACT. |
| 8 | `FS.GA.SHARE.OUTSTANDING.RESERVED10` | `FsGaShareOutstanding_Reserved10` | TField |  |  |
| 9 | `FS.GA.SHARE.OUTSTANDING.RESERVED9` | `FsGaShareOutstanding_Reserved9` | TField |  |  |
| 10 | `FS.GA.SHARE.OUTSTANDING.RESERVED8` | `FsGaShareOutstanding_Reserved8` | TField |  |  |
| 11 | `FS.GA.SHARE.OUTSTANDING.RESERVED7` | `FsGaShareOutstanding_Reserved7` | TField |  |  |
| 12 | `FS.GA.SHARE.OUTSTANDING.RESERVED6` | `FsGaShareOutstanding_Reserved6` | TField |  |  |
| 13 | `FS.GA.SHARE.OUTSTANDING.RESERVED5` | `FsGaShareOutstanding_Reserved5` | TField |  |  |
| 14 | `FS.GA.SHARE.OUTSTANDING.RESERVED4` | `FsGaShareOutstanding_Reserved4` | TField |  |  |
| 15 | `FS.GA.SHARE.OUTSTANDING.RESERVED3` | `FsGaShareOutstanding_Reserved3` | TField |  |  |
| 16 | `FS.GA.SHARE.OUTSTANDING.RESERVED2` | `FsGaShareOutstanding_Reserved2` | TField |  |  |
| 17 | `FS.GA.SHARE.OUTSTANDING.RESERVED1` | `FsGaShareOutstanding_Reserved1` | TField |  |  |
| 18 | `FS.GA.SHARE.OUTSTANDING.LOCAL.REF` | `FsGaShareOutstanding_LocalRef` |  |  |  |
| 19 | `FS.GA.SHARE.OUTSTANDING.OVERRIDE` | `FsGaShareOutstanding_Override` |  |  |  |
| 20 | `FS.GA.SHARE.OUTSTANDING.RECORD.STATUS` | `FsGaShareOutstanding_RecordStatus` | String |  |  |
| 21 | `FS.GA.SHARE.OUTSTANDING.CURR.NO` | `FsGaShareOutstanding_CurrNo` | String |  |  |
| 22 | `FS.GA.SHARE.OUTSTANDING.INPUTTER` | `FsGaShareOutstanding_Inputter` |  |  |  |
| 23 | `FS.GA.SHARE.OUTSTANDING.DATE.TIME` | `FsGaShareOutstanding_DateTime` |  |  |  |
| 24 | `FS.GA.SHARE.OUTSTANDING.AUTHORISER` | `FsGaShareOutstanding_Authoriser` | String |  |  |
| 25 | `FS.GA.SHARE.OUTSTANDING.CO.CODE` | `FsGaShareOutstanding_CoCode` | String |  |  |
| 26 | `FS.GA.SHARE.OUTSTANDING.DEPT.CODE` | `FsGaShareOutstanding_DeptCode` | String |  |  |
| 27 | `FS.GA.SHARE.OUTSTANDING.AUDITOR.CODE` | `FsGaShareOutstanding_AuditorCode` | String |  |  |
| 28 | `FS.GA.SHARE.OUTSTANDING.AUDIT.DATE.TIME` | `FsGaShareOutstanding_AuditDateTime` | String |  |  |
