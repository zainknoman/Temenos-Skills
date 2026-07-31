# FS.GI.LP.FUND.SELECT.GL.ACC.CAT — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FUND.SELECT.GL.ACC.CAT` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.TA.FUND.ID` | `FsGiLpFundSelectGlAccCat_TaFundId` | TField |  | Partnership fund identification number. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.FUND.ID` | `FsGiLpFundSelectGlAccCat_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 3 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.CLASS.CURRENCY` | `FsGiLpFundSelectGlAccCat_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 4 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.COMMENTS` | `FsGiLpFundSelectGlAccCat_Comments` | TField |  | Free text field to add additional details of the GL account category journey. Multifonds DB Column is COMMENTS. |
| 5 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED10` | `FsGiLpFundSelectGlAccCat_Reserved10` | TField |  |  |
| 6 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED9` | `FsGiLpFundSelectGlAccCat_Reserved9` | TField |  |  |
| 7 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED8` | `FsGiLpFundSelectGlAccCat_Reserved8` | TField |  |  |
| 8 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED7` | `FsGiLpFundSelectGlAccCat_Reserved7` | TField |  |  |
| 9 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED6` | `FsGiLpFundSelectGlAccCat_Reserved6` | TField |  |  |
| 10 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED5` | `FsGiLpFundSelectGlAccCat_Reserved5` | TField |  |  |
| 11 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED4` | `FsGiLpFundSelectGlAccCat_Reserved4` | TField |  |  |
| 12 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED3` | `FsGiLpFundSelectGlAccCat_Reserved3` | TField |  |  |
| 13 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED2` | `FsGiLpFundSelectGlAccCat_Reserved2` | TField |  |  |
| 14 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RESERVED1` | `FsGiLpFundSelectGlAccCat_Reserved1` | TField |  |  |
| 15 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.LOCAL.REF` | `FsGiLpFundSelectGlAccCat_LocalRef` |  |  |  |
| 16 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.OVERRIDE` | `FsGiLpFundSelectGlAccCat_Override` |  |  |  |
| 17 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.RECORD.STATUS` | `FsGiLpFundSelectGlAccCat_RecordStatus` | String |  |  |
| 18 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.CURR.NO` | `FsGiLpFundSelectGlAccCat_CurrNo` | String |  |  |
| 19 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.INPUTTER` | `FsGiLpFundSelectGlAccCat_Inputter` |  |  |  |
| 20 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.DATE.TIME` | `FsGiLpFundSelectGlAccCat_DateTime` |  |  |  |
| 21 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.AUTHORISER` | `FsGiLpFundSelectGlAccCat_Authoriser` | String |  |  |
| 22 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.CO.CODE` | `FsGiLpFundSelectGlAccCat_CoCode` | String |  |  |
| 23 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.DEPT.CODE` | `FsGiLpFundSelectGlAccCat_DeptCode` | String |  |  |
| 24 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.AUDITOR.CODE` | `FsGiLpFundSelectGlAccCat_AuditorCode` | String |  |  |
| 25 | `FS.GI.LP.FUND.SELECT.GL.ACC.CAT.AUDIT.DATE.TIME` | `FsGiLpFundSelectGlAccCat_AuditDateTime` | String |  |  |
