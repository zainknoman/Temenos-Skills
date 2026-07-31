# FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.FUND.ID` | `FsGiLpGlAccountBalanceReview_FundId` | TField |  | Fund Internal Id. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.SHARE.CLASS.CODE` | `FsGiLpGlAccountBalanceReview_ShareClassCode` | TField |  | Fund share class code Multifonds DB Column is TPART. |
| 3 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.FUND.MASTER.CCY` | `FsGiLpGlAccountBalanceReview_FundMasterCcy` | TField |  | Reporting Currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMONREF. |
| 4 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.NAV.DATE` | `FsGiLpGlAccountBalanceReview_NavDate` | TField |  | Price date of the fund share class. It is equivalent to the break period end date Multifonds DB Column is NAVDATE. |
| 5 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.GL.ACCOUNT.NO` | `FsGiLpGlAccountBalanceReview_GlAccountNo` | TField |  | GL account no linked to the fund accounting trail balance Multifonds DB Column is ACCOUNT_NO. |
| 6 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.GL.ACCOUNT.BALANCE` | `FsGiLpGlAccountBalanceReview_GlAccountBalance` | TField |  | GL balance amount based on GL account Multifonds DB Column is MNT_BAL. |
| 7 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED10` | `FsGiLpGlAccountBalanceReview_Reserved10` | TField |  |  |
| 8 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED9` | `FsGiLpGlAccountBalanceReview_Reserved9` | TField |  |  |
| 9 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED8` | `FsGiLpGlAccountBalanceReview_Reserved8` | TField |  |  |
| 10 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED7` | `FsGiLpGlAccountBalanceReview_Reserved7` | TField |  |  |
| 11 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED6` | `FsGiLpGlAccountBalanceReview_Reserved6` | TField |  |  |
| 12 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED5` | `FsGiLpGlAccountBalanceReview_Reserved5` | TField |  |  |
| 13 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED4` | `FsGiLpGlAccountBalanceReview_Reserved4` | TField |  |  |
| 14 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED3` | `FsGiLpGlAccountBalanceReview_Reserved3` | TField |  |  |
| 15 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED2` | `FsGiLpGlAccountBalanceReview_Reserved2` | TField |  |  |
| 16 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RESERVED1` | `FsGiLpGlAccountBalanceReview_Reserved1` | TField |  |  |
| 17 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.OVERRIDE` | `FsGiLpGlAccountBalanceReview_Override` |  |  |  |
| 18 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.LOCAL.REF` | `FsGiLpGlAccountBalanceReview_LocalRef` |  |  |  |
| 19 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.RECORD.STATUS` | `FsGiLpGlAccountBalanceReview_RecordStatus` | String |  |  |
| 20 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.CURR.NO` | `FsGiLpGlAccountBalanceReview_CurrNo` | String |  |  |
| 21 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.INPUTTER` | `FsGiLpGlAccountBalanceReview_Inputter` |  |  |  |
| 22 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.DATE.TIME` | `FsGiLpGlAccountBalanceReview_DateTime` |  |  |  |
| 23 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.AUTHORISER` | `FsGiLpGlAccountBalanceReview_Authoriser` | String |  |  |
| 24 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.CO.CODE` | `FsGiLpGlAccountBalanceReview_CoCode` | String |  |  |
| 25 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.DEPT.CODE` | `FsGiLpGlAccountBalanceReview_DeptCode` | String |  |  |
| 26 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.AUDITOR.CODE` | `FsGiLpGlAccountBalanceReview_AuditorCode` | String |  |  |
| 27 | `FS.GI.LP.GL.ACCOUNT.BALANCE.REVIEW.AUDIT.DATE.TIME` | `FsGiLpGlAccountBalanceReview_AuditDateTime` | String |  |  |
