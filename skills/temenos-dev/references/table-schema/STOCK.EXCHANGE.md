# STOCK.EXCHANGE — Table Schema

> Source: `INSERTS/I_F.STOCK.EXCHANGE` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.STE.DESCRIPTION` | `StockExchange_Description` |  |  |  |
| 2 | `SC.STE.SHORT.DESCR` | `StockExchange_ShortDescr` |  |  |  |
| 3 | `SC.STE.CALC.COUNTRY` | `StockExchange_CalcCountry` | TField |  | This field will link the Stock Exchange to a country code which then will access the Stock Exchange calculation tables for automatic calculation of commissions and charges applicable. Each Stock Exchange calculation table has a unique code which happens to be the country code (common T24 country code table) Validation Rules: 2 Alpha character input. Standard country code. Must be a valid Country Code which exists on the Country Code Table. |
| 4 | `SC.STE.SETTLEMENT.DAYS` | `StockExchange_SettlementDays` |  |  |  |
| 5 | `SC.STE.TRANSACTION.TYPE` | `StockExchange_TransactionType` |  |  |  |
| 6 | `SC.STE.TRADE.CURRENCY` | `StockExchange_TradeCurrency` |  |  |  |
| 7 | `SC.STE.RESERVED.12` | `StockExchange_Reserved12` | TField |  |  |
| 8 | `SC.STE.RESERVED.11` | `StockExchange_Reserved11` | TField |  |  |
| 9 | `SC.STE.RESERVED.10` | `StockExchange_Reserved10` | TField |  |  |
| 10 | `SC.STE.SETT.DAYS.BASIS` | `StockExchange_SettDaysBasis` | TField | Yes | Indicates whether the value date is to be calculated on a business or calendar day basis. The basis entered in this field will be used to determine how the value date will be calculated given the trade date and the settlement days for this stock exchange. Example The holiday table being set up with Saturdays and Sundays as the weekend days. Trade date of Thursday 4th March and settlement days of 2. If the basis is BUSINESS then the value date will be Monday 8th. If the basis is CALENDAR then the value date will be Saturday 6th. If the basis is FIXED, then the value date will be cal culated on the basis of calendar defined for that particular Stock Exchange &amp; Year in STK.EXCH.CALENDAR (where a Settlement Day is defined for a period) Validation Rules: Values allowed are BUSINESS OR CALENDAR OR FIXED. (Mandatory Input) |
| 11 | `SC.STE.DOMICILE` | `StockExchange_Domicile` | TField | No | Specifices the country of domicile of the Stock Exchange. Each Stock Exchange calculation table has a unique code which happens to be the country code (common T24 country code table) Validation Rules: 2 Alpha character input. Standard country code. (Optional Input) Must be a valid Country Code which exists on the Country Code Table. |
| 12 | `SC.STE.BOND.LEVY.DATE` | `StockExchange_BondLevyDate` |  |  |  |
| 13 | `SC.STE.BR.BOND.CNTY` | `StockExchange_BrBondCnty` |  |  |  |
| 14 | `SC.STE.BR.BOND.COMM` | `StockExchange_BrBondComm` |  |  |  |
| 15 | `SC.STE.CU.BOND.CNTY` | `StockExchange_CuBondCnty` |  |  |  |
| 16 | `SC.STE.CU.BOND.COMM` | `StockExchange_CuBondComm` |  |  |  |
| 17 | `SC.STE.SHARE.LEVY.DATE` | `StockExchange_ShareLevyDate` |  |  |  |
| 18 | `SC.STE.BR.SHR.CNTY` | `StockExchange_BrShrCnty` |  |  |  |
| 19 | `SC.STE.BR.SHR.COMM` | `StockExchange_BrShrComm` |  |  |  |
| 20 | `SC.STE.CU.SHR.CNTY` | `StockExchange_CuShrCnty` |  |  |  |
| 21 | `SC.STE.CU.SHR.COMM` | `StockExchange_CuShrComm` |  |  |  |
| 22 | `SC.STE.MKT.IDN.CODE` | `StockExchange_MktIdnCode` | TField |  | The swift market identifier code is defined in this field Validation Rules: 4 Alphabetical characters |
| 23 | `SC.STE.MIFID.COMPLIANT` | `StockExchange_MifidCompliant` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 24 | `SC.STE.CUT.OFF.TIME` | `StockExchange_CutOffTime` | TField |  | This Field accepts time .Which is cutoff time for stock exchange |
| 25 | `SC.STE.AGGREGATION` | `StockExchange_Aggregation` | TField |  | Allowed value is YES Field to determine whether stock exchange is enabled for aggregation. This will be additionally checked if broker is enabled for aggregation. Aggregation will be performed only if stock exchange and broker are enabled for aggregation. |
| 26 | `SC.STE.AGGR.CUT.OFF.TIME` | `StockExchange_AggrCutOffTime` | TField |  | This Field accepts time Cut off time at which trades will be authorised OR mt515 will be received to authorise the aggregated trades. |
| 27 | `SC.STE.SUSPEND.TRADING` | `StockExchange_SuspendTrading` | TField |  | Trading can be suspended in the stock exchange due to some unforeseen circumstances such as a natural calamity. Such a suspension is communicated to the system by setting this field to "Yes". Once the trading resumes, this flag needs to be cleared |
| 28 | `SC.STE.EOD.ACCOUNTING` | `StockExchange_EodAccounting` | TField |  | This field will be set to indicate that the stock exchange is likely to face frequent settlement disruptions Eg: Frequent typhoons Even if system is parameterised to settle automatically at Start of Day, for this custodian, contractual trades will be automatically settled only during End of Day processing if this field is set to YES Validation Rules: Allowed values are 'YES' / 'NO' |
| 29 | `SC.STE.SUSPEND.SETTLEMENT` | `StockExchange_SuspendSettlement` | TField |  | This field will be set to indicate that the settlement is suspended due to an emergency If this field is set to YES, then the emergency continues and settlement services remain suspended. This should be manually re-set to NO to indicate that the normal activities have resumed Validation Rules: Input allowed only if EOD.ACCOUNTING is set to YES. Allowed values are 'YES' / 'NO' |
| 30 | `SC.STE.PRIMARY.EXCHG` | `StockExchange_PrimaryExchg` | TField |  | Many stock exchanges or trading venues exist within a Primary stock exchange. Under such cases this field denotes the Primary stock exchange. Validation Rules: The Primary stock exchange field should be a valid STOCK.EXCHANGE record |
| 31 | `SC.STE.RESERVED.5` | `StockExchange_Reserved5` | TField |  |  |
| 32 | `SC.STE.RESERVED.4` | `StockExchange_Reserved4` | TField |  |  |
| 33 | `SC.STE.RESERVED.3` | `StockExchange_Reserved3` | TField |  |  |
| 34 | `SC.STE.RESERVED.2` | `StockExchange_Reserved2` | TField |  |  |
| 35 | `SC.STE.RESERVED.1` | `StockExchange_Reserved1` | TField |  |  |
| 36 | `SC.STE.LOCAL.REF` | `StockExchange_LocalRef` |  |  |  |
| 37 | `SC.STE.RECORD.STATUS` | `StockExchange_RecordStatus` | String |  |  |
| 38 | `SC.STE.CURR.NO` | `StockExchange_CurrNo` | String |  |  |
| 39 | `SC.STE.INPUTTER` | `StockExchange_Inputter` |  |  |  |
| 40 | `SC.STE.DATE.TIME` | `StockExchange_DateTime` |  |  |  |
| 41 | `SC.STE.AUTHORISER` | `StockExchange_Authoriser` | String |  |  |
| 42 | `SC.STE.CO.CODE` | `StockExchange_CoCode` | String |  |  |
| 43 | `SC.STE.DEPT.CODE` | `StockExchange_DeptCode` | String |  |  |
| 44 | `SC.STE.AUDITOR.CODE` | `StockExchange_AuditorCode` | String |  |  |
| 45 | `SC.STE.AUDIT.DATE.TIME` | `StockExchange_AuditDateTime` | String |  |  |
