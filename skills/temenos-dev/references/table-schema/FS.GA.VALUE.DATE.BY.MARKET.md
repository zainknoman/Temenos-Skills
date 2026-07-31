# FS.GA.VALUE.DATE.BY.MARKET — Table Schema

> Source: `INSERTS/I_F.FS.GA.VALUE.DATE.BY.MARKET` in `FS_SystemConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.VALUE.DATE.BY.MARKET.PARENT.REF.ID` | `FsGaValueDateByMarket_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.VALUE.DATE.BY.MARKET.ORA.ROWID` | `FsGaValueDateByMarket_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.VALUE.DATE.BY.MARKET.QUOTATION.PLACE` | `FsGaValueDateByMarket_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 4 | `FS.GA.VALUE.DATE.BY.MARKET.WORKING.DAYS` | `FsGaValueDateByMarket_WorkingDays` | TField |  | If set, the number of days entered will be added as business days to the trade date on a capstock or deal to obtain the value date Multifonds DB Column is FJOUVR. |
| 5 | `FS.GA.VALUE.DATE.BY.MARKET.DAYS.OF.ACCRUED.INTEREST` | `FsGaValueDateByMarket_DaysOfAccruedInterest` | TField |  | Number of days of purchase/sale interest in a transaction done on an interest bearing instrument Multifonds DB Column is NBJOURS. |
| 6 | `FS.GA.VALUE.DATE.BY.MARKET.GTI.CODE` | `FsGaValueDateByMarket_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 7 | `FS.GA.VALUE.DATE.BY.MARKET.DAY.OF.THE.MONTH` | `FsGaValueDateByMarket_DayOfTheMonth` | TField |  | If set, the value date will be on a fixed date of the month. This function is particularly useful for mortgage-backed securities, for instance, where pay-downs occur on a pre-defined day of the month. Multifonds DB Column is FLG_DAY_MONTH. |
| 8 | `FS.GA.VALUE.DATE.BY.MARKET.CORRESPONDENT` | `FsGaValueDateByMarket_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 9 | `FS.GA.VALUE.DATE.BY.MARKET.MANAGEMENT.COMP` | `FsGaValueDateByMarket_ManagementComp` | TField |  | Enter management company Multifonds DB Column is NMGMNT_CPY. |
| 10 | `FS.GA.VALUE.DATE.BY.MARKET.DISC.WORKING.OR.HOLIDAY` | `FsGaValueDateByMarket_DiscWorkingOrHoliday` | TField |  | Disc working or holiday flag Multifonds DB Column is FLG_DIS_DAY. |
| 11 | `FS.GA.VALUE.DATE.BY.MARKET.NB.DAYS.FOR.SEC.VALUE.DATE` | `FsGaValueDateByMarket_NbDaysForSecValueDate` | TField |  | To define security value date number of days Multifonds DB Column is NBJOURS_SEC. |
| 12 | `FS.GA.VALUE.DATE.BY.MARKET.INTERNAL.SECURITY.ID` | `FsGaValueDateByMarket_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 13 | `FS.GA.VALUE.DATE.BY.MARKET.OPERATION.CODE` | `FsGaValueDateByMarket_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 14 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED10` | `FsGaValueDateByMarket_Reserved10` | TField |  |  |
| 15 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED9` | `FsGaValueDateByMarket_Reserved9` | TField |  |  |
| 16 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED8` | `FsGaValueDateByMarket_Reserved8` | TField |  |  |
| 17 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED7` | `FsGaValueDateByMarket_Reserved7` | TField |  |  |
| 18 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED6` | `FsGaValueDateByMarket_Reserved6` | TField |  |  |
| 19 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED5` | `FsGaValueDateByMarket_Reserved5` | TField |  |  |
| 20 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED4` | `FsGaValueDateByMarket_Reserved4` | TField |  |  |
| 21 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED3` | `FsGaValueDateByMarket_Reserved3` | TField |  |  |
| 22 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED2` | `FsGaValueDateByMarket_Reserved2` | TField |  |  |
| 23 | `FS.GA.VALUE.DATE.BY.MARKET.RESERVED1` | `FsGaValueDateByMarket_Reserved1` | TField |  |  |
| 24 | `FS.GA.VALUE.DATE.BY.MARKET.LOCAL.REF` | `FsGaValueDateByMarket_LocalRef` |  |  |  |
| 25 | `FS.GA.VALUE.DATE.BY.MARKET.OVERRIDE` | `FsGaValueDateByMarket_Override` |  |  |  |
| 26 | `FS.GA.VALUE.DATE.BY.MARKET.RECORD.STATUS` | `FsGaValueDateByMarket_RecordStatus` | String |  |  |
| 27 | `FS.GA.VALUE.DATE.BY.MARKET.CURR.NO` | `FsGaValueDateByMarket_CurrNo` | String |  |  |
| 28 | `FS.GA.VALUE.DATE.BY.MARKET.INPUTTER` | `FsGaValueDateByMarket_Inputter` |  |  |  |
| 29 | `FS.GA.VALUE.DATE.BY.MARKET.DATE.TIME` | `FsGaValueDateByMarket_DateTime` |  |  |  |
| 30 | `FS.GA.VALUE.DATE.BY.MARKET.AUTHORISER` | `FsGaValueDateByMarket_Authoriser` | String |  |  |
| 31 | `FS.GA.VALUE.DATE.BY.MARKET.CO.CODE` | `FsGaValueDateByMarket_CoCode` | String |  |  |
| 32 | `FS.GA.VALUE.DATE.BY.MARKET.DEPT.CODE` | `FsGaValueDateByMarket_DeptCode` | String |  |  |
| 33 | `FS.GA.VALUE.DATE.BY.MARKET.AUDITOR.CODE` | `FsGaValueDateByMarket_AuditorCode` | String |  |  |
| 34 | `FS.GA.VALUE.DATE.BY.MARKET.AUDIT.DATE.TIME` | `FsGaValueDateByMarket_AuditDateTime` | String |  |  |
