# FS.GI.EXCHANGE.RATE.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GI.EXCHANGE.RATE.DETAIL` in `FS_ExchangeRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.EXCHANGE.RATE.DETAIL.PARENT.REF.ID` | `FsGiExchangeRateDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.EXCHANGE.RATE.DETAIL.ORA.ROWID` | `FsGiExchangeRateDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.EXCHANGE.RATE.DETAIL.FUND.MASTER.CCY` | `FsGiExchangeRateDetail_FundMasterCcy` | TField |  | Reference Currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMONREF. |
| 4 | `FS.GI.EXCHANGE.RATE.DETAIL.CURRENCY` | `FsGiExchangeRateDetail_Currency` | TField |  | Currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CODMON. |
| 5 | `FS.GI.EXCHANGE.RATE.DETAIL.RANK` | `FsGiExchangeRateDetail_Rank` | TField |  | Currency rank used to decide whether exchange rate has to be used as direct or an indirect quote for each currency record. Multifonds DB Column is CRANG. |
| 6 | `FS.GI.EXCHANGE.RATE.DETAIL.DECIMALS` | `FsGiExchangeRateDetail_Decimals` | TField |  | Number of decimals to be taken for currency amount. For JPY currency it is 0. Multifonds DB Column is CDEC. |
| 7 | `FS.GI.EXCHANGE.RATE.DETAIL.ROUNDING.DIFFERENCE` | `FsGiExchangeRateDetail_RoundingDifference` | TField |  | Smallest trading unit of a currency generally the smallest currency would be 0.01 (with 2 decimals). For JPY currency this field is set as 1. Multifonds DB Column is CARRONDI. |
| 8 | `FS.GI.EXCHANGE.RATE.DETAIL.NUMBER.OF.CURRENCY.UNITS` | `FsGiExchangeRateDetail_NumberOfCurrencyUnits` | TField |  | Number of currency units to be translated into foreign currency. For instance 1000 JPY = n USD. Multifonds DB Column is CUNITE. |
| 9 | `FS.GI.EXCHANGE.RATE.DETAIL.INTEREST.CALCULATION` | `FsGiExchangeRateDetail_InterestCalculation` | TField |  | Interest calculation algorithm applies for the currency. Multifonds DB Column is CUSA. |
| 10 | `FS.GI.EXCHANGE.RATE.DETAIL.EX.RATE.DATE` | `FsGiExchangeRateDetail_ExRateDate` | TField |  | Date of the exchange rate linked to value date. Multifonds DB Column is DCTA_TCHG. |
| 11 | `FS.GI.EXCHANGE.RATE.DETAIL.VALUE.DATE` | `FsGiExchangeRateDetail_ValueDate` | TField |  | Value date of the exchange rate Multifonds DB Column is DCTA. |
| 12 | `FS.GI.EXCHANGE.RATE.DETAIL.EXCHANGE.RATE` | `FsGiExchangeRateDetail_ExchangeRate` | TField |  | Exchange rate expressed against the application currency. The quotation will depend on the currency rank that has been defined. Multifonds DB Column is TCOURS. |
| 13 | `FS.GI.EXCHANGE.RATE.DETAIL.MAX.TOLERANCE.PCT.EX.RATE` | `FsGiExchangeRateDetail_MaxTolerancePctExRate` | TField |  | Maximum tolerance percentage for exchange rate deviations. Multifonds DB Column is PCT_COURS. |
| 14 | `FS.GI.EXCHANGE.RATE.DETAIL.MAX.TOLERANCE.PCT.INTEREST` | `FsGiExchangeRateDetail_MaxTolerancePctInterest` | TField |  | Maximum tolerance percentage for interest rate deviations. Not used in MFGI. Multifonds DB Column is PCT_TAUX. |
| 15 | `FS.GI.EXCHANGE.RATE.DETAIL.EURO.CURRENCY.FLAG` | `FsGiExchangeRateDetail_EuroCurrencyFlag` | TField |  | Euro currency. Multifonds DB Column is EURO_CUR. |
| 16 | `FS.GI.EXCHANGE.RATE.DETAIL.START.DATE` | `FsGiExchangeRateDetail_StartDate` | TField |  | Start date. Multifonds DB Column is DCALC. |
| 17 | `FS.GI.EXCHANGE.RATE.DETAIL.DECIMALS.EURO` | `FsGiExchangeRateDetail_DecimalsEuro` | TField |  | Number of decimals to be taken for euro currency amount. Multifonds DB Column is CDEC_EURO. |
| 18 | `FS.GI.EXCHANGE.RATE.DETAIL.ROUNDING.DIFFERENCE.EURO` | `FsGiExchangeRateDetail_RoundingDifferenceEuro` | TField |  | Smallest trading unit of euro currency. Multifonds DB Column is CARRONDI_EURO. |
| 19 | `FS.GI.EXCHANGE.RATE.DETAIL.EXCHANGE.RATE.DATE` | `FsGiExchangeRateDetail_ExchangeRateDate` | TField |  | Date of the exchange rate. Multifonds DB Column is DMAJCOURS. |
| 20 | `FS.GI.EXCHANGE.RATE.DETAIL.EXCHANGE.GROUP` | `FsGiExchangeRateDetail_ExchangeGroup` | TField |  | Fund exchange group to which the rate is applied. Multifonds DB Column is GROUPE. |
| 21 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED10` | `FsGiExchangeRateDetail_Reserved10` | TField |  |  |
| 22 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED9` | `FsGiExchangeRateDetail_Reserved9` | TField |  |  |
| 23 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED8` | `FsGiExchangeRateDetail_Reserved8` | TField |  |  |
| 24 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED7` | `FsGiExchangeRateDetail_Reserved7` | TField |  |  |
| 25 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED6` | `FsGiExchangeRateDetail_Reserved6` | TField |  |  |
| 26 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED5` | `FsGiExchangeRateDetail_Reserved5` | TField |  |  |
| 27 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED4` | `FsGiExchangeRateDetail_Reserved4` | TField |  |  |
| 28 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED3` | `FsGiExchangeRateDetail_Reserved3` | TField |  |  |
| 29 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED2` | `FsGiExchangeRateDetail_Reserved2` | TField |  |  |
| 30 | `FS.GI.EXCHANGE.RATE.DETAIL.RESERVED1` | `FsGiExchangeRateDetail_Reserved1` | TField |  |  |
| 31 | `FS.GI.EXCHANGE.RATE.DETAIL.LOCAL.REF` | `FsGiExchangeRateDetail_LocalRef` |  |  |  |
| 32 | `FS.GI.EXCHANGE.RATE.DETAIL.OVERRIDE` | `FsGiExchangeRateDetail_Override` |  |  |  |
| 33 | `FS.GI.EXCHANGE.RATE.DETAIL.RECORD.STATUS` | `FsGiExchangeRateDetail_RecordStatus` | String |  |  |
| 34 | `FS.GI.EXCHANGE.RATE.DETAIL.CURR.NO` | `FsGiExchangeRateDetail_CurrNo` | String |  |  |
| 35 | `FS.GI.EXCHANGE.RATE.DETAIL.INPUTTER` | `FsGiExchangeRateDetail_Inputter` |  |  |  |
| 36 | `FS.GI.EXCHANGE.RATE.DETAIL.DATE.TIME` | `FsGiExchangeRateDetail_DateTime` |  |  |  |
| 37 | `FS.GI.EXCHANGE.RATE.DETAIL.AUTHORISER` | `FsGiExchangeRateDetail_Authoriser` | String |  |  |
| 38 | `FS.GI.EXCHANGE.RATE.DETAIL.CO.CODE` | `FsGiExchangeRateDetail_CoCode` | String |  |  |
| 39 | `FS.GI.EXCHANGE.RATE.DETAIL.DEPT.CODE` | `FsGiExchangeRateDetail_DeptCode` | String |  |  |
| 40 | `FS.GI.EXCHANGE.RATE.DETAIL.AUDITOR.CODE` | `FsGiExchangeRateDetail_AuditorCode` | String |  |  |
| 41 | `FS.GI.EXCHANGE.RATE.DETAIL.AUDIT.DATE.TIME` | `FsGiExchangeRateDetail_AuditDateTime` | String |  |  |
