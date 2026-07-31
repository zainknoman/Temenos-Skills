# FS.GI.LP.GL.ACCOUNT.CATEGORY — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.ACCOUNT.CATEGORY` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.PARENT.REF.ID` | `FsGiLpGlAccountCategory_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.ORA.ROWID` | `FsGiLpGlAccountCategory_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.TA.FUND.ID` | `FsGiLpGlAccountCategory_TaFundId` | TField |  | Fund Internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.SHARE.CLASS.CODE` | `FsGiLpGlAccountCategory_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.GL.ACCOUNT.NO` | `FsGiLpGlAccountCategory_GlAccountNo` | TField |  | GL External Code linked to the fund accounting trail balance. Multifonds DB Column is GL_ACCOUNT_NO. |
| 6 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.GL.CATEGORY.ID` | `FsGiLpGlAccountCategory_GlCategoryId` | TField |  | GL Internal code for GL External code. Multifonds DB Column is GL_CATEGORY. |
| 7 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.GL.CATEGORY.ID.DESC` | `FsGiLpGlAccountCategory_GlCategoryIdDesc` | TField |  | GL Internal code description. Multifonds DB Column is LIBELLE. |
| 8 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.FUND.ID` | `FsGiLpGlAccountCategory_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.CLASS.CURRENCY` | `FsGiLpGlAccountCategory_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.GL.ACCOUNT.TYPE` | `FsGiLpGlAccountCategory_GlAccountType` | TField |  | Account type for GL category. For example Income,Expense,Gain or Loss. Multifonds DB Column is ACCOUNT_TYPE. |
| 11 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED10` | `FsGiLpGlAccountCategory_Reserved10` | TField |  |  |
| 12 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED9` | `FsGiLpGlAccountCategory_Reserved9` | TField |  |  |
| 13 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED8` | `FsGiLpGlAccountCategory_Reserved8` | TField |  |  |
| 14 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED7` | `FsGiLpGlAccountCategory_Reserved7` | TField |  |  |
| 15 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED6` | `FsGiLpGlAccountCategory_Reserved6` | TField |  |  |
| 16 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED5` | `FsGiLpGlAccountCategory_Reserved5` | TField |  |  |
| 17 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED4` | `FsGiLpGlAccountCategory_Reserved4` | TField |  |  |
| 18 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED3` | `FsGiLpGlAccountCategory_Reserved3` | TField |  |  |
| 19 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED2` | `FsGiLpGlAccountCategory_Reserved2` | TField |  |  |
| 20 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RESERVED1` | `FsGiLpGlAccountCategory_Reserved1` | TField |  |  |
| 21 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.LOCAL.REF` | `FsGiLpGlAccountCategory_LocalRef` |  |  |  |
| 22 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.OVERRIDE` | `FsGiLpGlAccountCategory_Override` |  |  |  |
| 23 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.RECORD.STATUS` | `FsGiLpGlAccountCategory_RecordStatus` | String |  |  |
| 24 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.CURR.NO` | `FsGiLpGlAccountCategory_CurrNo` | String |  |  |
| 25 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.INPUTTER` | `FsGiLpGlAccountCategory_Inputter` |  |  |  |
| 26 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.DATE.TIME` | `FsGiLpGlAccountCategory_DateTime` |  |  |  |
| 27 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.AUTHORISER` | `FsGiLpGlAccountCategory_Authoriser` | String |  |  |
| 28 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.CO.CODE` | `FsGiLpGlAccountCategory_CoCode` | String |  |  |
| 29 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.DEPT.CODE` | `FsGiLpGlAccountCategory_DeptCode` | String |  |  |
| 30 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.AUDITOR.CODE` | `FsGiLpGlAccountCategory_AuditorCode` | String |  |  |
| 31 | `FS.GI.LP.GL.ACCOUNT.CATEGORY.AUDIT.DATE.TIME` | `FsGiLpGlAccountCategory_AuditDateTime` | String |  |  |
