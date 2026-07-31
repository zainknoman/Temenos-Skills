# FS.GI.LP.GL.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.FUND` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.FUND.PARENT.REF.ID` | `FsGiLpGlFund_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.FUND.ORA.ROWID` | `FsGiLpGlFund_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.FUND.FUND.ID` | `FsGiLpGlFund_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 4 | `FS.GI.LP.GL.FUND.CLASS.CURRENCY` | `FsGiLpGlFund_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 5 | `FS.GI.LP.GL.FUND.TA.FUND.ID` | `FsGiLpGlFund_TaFundId` | TField |  | Partnership fund identification number. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.LP.GL.FUND.RESERVED10` | `FsGiLpGlFund_Reserved10` | TField |  |  |
| 7 | `FS.GI.LP.GL.FUND.RESERVED9` | `FsGiLpGlFund_Reserved9` | TField |  |  |
| 8 | `FS.GI.LP.GL.FUND.RESERVED8` | `FsGiLpGlFund_Reserved8` | TField |  |  |
| 9 | `FS.GI.LP.GL.FUND.RESERVED7` | `FsGiLpGlFund_Reserved7` | TField |  |  |
| 10 | `FS.GI.LP.GL.FUND.RESERVED6` | `FsGiLpGlFund_Reserved6` | TField |  |  |
| 11 | `FS.GI.LP.GL.FUND.RESERVED5` | `FsGiLpGlFund_Reserved5` | TField |  |  |
| 12 | `FS.GI.LP.GL.FUND.RESERVED4` | `FsGiLpGlFund_Reserved4` | TField |  |  |
| 13 | `FS.GI.LP.GL.FUND.RESERVED3` | `FsGiLpGlFund_Reserved3` | TField |  |  |
| 14 | `FS.GI.LP.GL.FUND.RESERVED2` | `FsGiLpGlFund_Reserved2` | TField |  |  |
| 15 | `FS.GI.LP.GL.FUND.RESERVED1` | `FsGiLpGlFund_Reserved1` | TField |  |  |
| 16 | `FS.GI.LP.GL.FUND.LOCAL.REF` | `FsGiLpGlFund_LocalRef` |  |  |  |
| 17 | `FS.GI.LP.GL.FUND.OVERRIDE` | `FsGiLpGlFund_Override` |  |  |  |
| 18 | `FS.GI.LP.GL.FUND.RECORD.STATUS` | `FsGiLpGlFund_RecordStatus` | String |  |  |
| 19 | `FS.GI.LP.GL.FUND.CURR.NO` | `FsGiLpGlFund_CurrNo` | String |  |  |
| 20 | `FS.GI.LP.GL.FUND.INPUTTER` | `FsGiLpGlFund_Inputter` |  |  |  |
| 21 | `FS.GI.LP.GL.FUND.DATE.TIME` | `FsGiLpGlFund_DateTime` |  |  |  |
| 22 | `FS.GI.LP.GL.FUND.AUTHORISER` | `FsGiLpGlFund_Authoriser` | String |  |  |
| 23 | `FS.GI.LP.GL.FUND.CO.CODE` | `FsGiLpGlFund_CoCode` | String |  |  |
| 24 | `FS.GI.LP.GL.FUND.DEPT.CODE` | `FsGiLpGlFund_DeptCode` | String |  |  |
| 25 | `FS.GI.LP.GL.FUND.AUDITOR.CODE` | `FsGiLpGlFund_AuditorCode` | String |  |  |
| 26 | `FS.GI.LP.GL.FUND.AUDIT.DATE.TIME` | `FsGiLpGlFund_AuditDateTime` | String |  |  |
