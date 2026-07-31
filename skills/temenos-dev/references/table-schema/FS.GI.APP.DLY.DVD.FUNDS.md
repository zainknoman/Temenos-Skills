# FS.GI.APP.DLY.DVD.FUNDS — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.DLY.DVD.FUNDS` in `FS_InvestorAccountStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.DLY.DVD.FUNDS.PARENT.REF.ID` | `FsGiAppDlyDvdFunds_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.DLY.DVD.FUNDS.ORA.ROWID` | `FsGiAppDlyDvdFunds_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.DLY.DVD.FUNDS.REGISTER.ID` | `FsGiAppDlyDvdFunds_RegisterId` | TField |  | Register internal ID. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.APP.DLY.DVD.FUNDS.TA.FUND.ID` | `FsGiAppDlyDvdFunds_TaFundId` | TField |  | Fund internal ID Multifonds DB Column is NPTF. |
| 5 | `FS.GI.APP.DLY.DVD.FUNDS.SHARE.CLASS.CODE` | `FsGiAppDlyDvdFunds_ShareClassCode` | TField |  | Fund share class Multifonds DB Column is TPART. |
| 6 | `FS.GI.APP.DLY.DVD.FUNDS.DAILY.DIV.PAYMENT.TYPE` | `FsGiAppDlyDvdFunds_DailyDivPaymentType` | TField |  | Dividend Payout type (i.e., Payout or Reinvest) for distribution in a fund share class. Multifonds DB Column is DLYDIV_PAYMTHD. |
| 7 | `FS.GI.APP.DLY.DVD.FUNDS.DAILY.DIV.FUNDS.ID` | `FsGiAppDlyDvdFunds_DailyDivFundsId` | TField |  | Unique internal identifier for dividend payout type record. Multifonds DB Column is INTERNAL_ID. |
| 8 | `FS.GI.APP.DLY.DVD.FUNDS.FUND.ID` | `FsGiAppDlyDvdFunds_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.APP.DLY.DVD.FUNDS.CLASS.CURRENCY` | `FsGiAppDlyDvdFunds_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED10` | `FsGiAppDlyDvdFunds_Reserved10` | TField |  |  |
| 11 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED9` | `FsGiAppDlyDvdFunds_Reserved9` | TField |  |  |
| 12 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED8` | `FsGiAppDlyDvdFunds_Reserved8` | TField |  |  |
| 13 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED7` | `FsGiAppDlyDvdFunds_Reserved7` | TField |  |  |
| 14 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED6` | `FsGiAppDlyDvdFunds_Reserved6` | TField |  |  |
| 15 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED5` | `FsGiAppDlyDvdFunds_Reserved5` | TField |  |  |
| 16 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED4` | `FsGiAppDlyDvdFunds_Reserved4` | TField |  |  |
| 17 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED3` | `FsGiAppDlyDvdFunds_Reserved3` | TField |  |  |
| 18 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED2` | `FsGiAppDlyDvdFunds_Reserved2` | TField |  |  |
| 19 | `FS.GI.APP.DLY.DVD.FUNDS.RESERVED1` | `FsGiAppDlyDvdFunds_Reserved1` | TField |  |  |
| 20 | `FS.GI.APP.DLY.DVD.FUNDS.LOCAL.REF` | `FsGiAppDlyDvdFunds_LocalRef` |  |  |  |
| 21 | `FS.GI.APP.DLY.DVD.FUNDS.OVERRIDE` | `FsGiAppDlyDvdFunds_Override` |  |  |  |
| 22 | `FS.GI.APP.DLY.DVD.FUNDS.RECORD.STATUS` | `FsGiAppDlyDvdFunds_RecordStatus` | String |  |  |
| 23 | `FS.GI.APP.DLY.DVD.FUNDS.CURR.NO` | `FsGiAppDlyDvdFunds_CurrNo` | String |  |  |
| 24 | `FS.GI.APP.DLY.DVD.FUNDS.INPUTTER` | `FsGiAppDlyDvdFunds_Inputter` |  |  |  |
| 25 | `FS.GI.APP.DLY.DVD.FUNDS.DATE.TIME` | `FsGiAppDlyDvdFunds_DateTime` |  |  |  |
| 26 | `FS.GI.APP.DLY.DVD.FUNDS.AUTHORISER` | `FsGiAppDlyDvdFunds_Authoriser` | String |  |  |
| 27 | `FS.GI.APP.DLY.DVD.FUNDS.CO.CODE` | `FsGiAppDlyDvdFunds_CoCode` | String |  |  |
| 28 | `FS.GI.APP.DLY.DVD.FUNDS.DEPT.CODE` | `FsGiAppDlyDvdFunds_DeptCode` | String |  |  |
| 29 | `FS.GI.APP.DLY.DVD.FUNDS.AUDITOR.CODE` | `FsGiAppDlyDvdFunds_AuditorCode` | String |  |  |
| 30 | `FS.GI.APP.DLY.DVD.FUNDS.AUDIT.DATE.TIME` | `FsGiAppDlyDvdFunds_AuditDateTime` | String |  |  |
