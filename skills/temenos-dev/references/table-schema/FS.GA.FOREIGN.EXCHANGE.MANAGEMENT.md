# FS.GA.FOREIGN.EXCHANGE.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.FOREIGN.EXCHANGE.MANAGEMENT` in `FS_ExchangeRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.PARENT.REF.ID` | `FsGaForeignExchangeManagement_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.ORA.ROWID` | `FsGaForeignExchangeManagement_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.BOOK.CURRENCY` | `FsGaForeignExchangeManagement_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 4 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CURRENCY.CODE` | `FsGaForeignExchangeManagement_CurrencyCode` | TField |  | Currency Code like USD, EUR Multifonds DB Column is CODMON. |
| 5 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CURRENCY.RANK` | `FsGaForeignExchangeManagement_CurrencyRank` | TField |  | Define Rank for currency.Exchange rates can be used as a direct or an indirect quote depending on the currency rank defined for each currency record. A) EUR 00 B) USD 50 1 EUR = x USD Rank A &gt; Rank B Multifonds DB Column is CRANG. |
| 6 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.DECIMAL.ROUNDING.CODE` | `FsGaForeignExchangeManagement_DecimalRoundingCode` | TField |  | Number of decimals to be taken for currency amounts . Generally,the number of decimals would be 2 except for currencies like Japanese Yen for instance, where the number of decimals is equal to zero. Multifonds DB Column is CDEC. |
| 7 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CCY.USANCE.CODE` | `FsGaForeignExchangeManagement_CcyUsanceCode` | TField |  | Interest calculation algorithm to apply for this currency. This will merely act as a default value. This can be changed during the input on deposits, IRS deals, interest on current accounts, etc. Multifonds DB Column is CUSA. |
| 8 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CCY.ROUNDING.RULES` | `FsGaForeignExchangeManagement_CcyRoundingRules` | TField |  | Enter the smallest trading unit of a currency. Generally the smallest currency unit would be 0, 01 (with 2 decimals). If for instance a rounding to the next multiple of 0, 05 is desired, enter 0.05. Multifonds DB Column is CARRONDI. |
| 9 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CCY.UNIT.VALUE` | `FsGaForeignExchangeManagement_CcyUnitValue` | TField |  | Enter the number of currency units to be translated into foreign currency, for instance 1000 JPY = n USD. Note that using the quotation unit only makes sense when using the indirect quotation method. Multifonds DB Column is CUNITE. |
| 10 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.TRANSACTION.PRICE` | `FsGaForeignExchangeManagement_TransactionPrice` | TField |  | The unit price of an instrument which is being transacted. Multifonds DB Column is TCOURS. |
| 11 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.DATE2` | `FsGaForeignExchangeManagement_Date2` | TField |  | Date2 Multifonds DB Column is DMAJCOURS. |
| 12 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE0` | `FsGaForeignExchangeManagement_ExchangeRate0` | TField |  | Exchange Rate0 Multifonds DB Column is CHGI. |
| 13 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE.1` | `FsGaForeignExchangeManagement_ExchangeRate1` | TField |  | Exchange Rate 1 Multifonds DB Column is CHGI_1. |
| 14 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE.2` | `FsGaForeignExchangeManagement_ExchangeRate2` | TField |  | Exchange Rate 2 Multifonds DB Column is CHGI_2. |
| 15 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE.3` | `FsGaForeignExchangeManagement_ExchangeRate3` | TField |  | Exchange Rate 3 Multifonds DB Column is CHGI_3. |
| 16 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE.6` | `FsGaForeignExchangeManagement_ExchangeRate6` | TField |  | Exchange Rate 6 Multifonds DB Column is CHGI_6. |
| 17 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE.9` | `FsGaForeignExchangeManagement_ExchangeRate9` | TField |  | Exchange Rate 9 Multifonds DB Column is CHGI_9. |
| 18 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE.12` | `FsGaForeignExchangeManagement_ExchangeRate12` | TField |  | Exchange Rate 12 Multifonds DB Column is CHGI_12. |
| 19 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.ACTUAL.COURS.DATE` | `FsGaForeignExchangeManagement_ActualCoursDate` | TField |  | Actual Cours Date Multifonds DB Column is DATE_COURS_ACTUEL. |
| 20 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.PREVIOUS.COURS.DATE` | `FsGaForeignExchangeManagement_PreviousCoursDate` | TField |  | Previous Cours Date Multifonds DB Column is DATE_COURS_PREC. |
| 21 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EUR.CURRENCY` | `FsGaForeignExchangeManagement_EurCurrency` | TField |  | If the box is ticked, the currency is a Euro IN-Currency. Multifonds DB Column is EURO_CUR. |
| 22 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CCY.ROUNDING.RULES.EURO` | `FsGaForeignExchangeManagement_CcyRoundingRulesEuro` | TField |  | Rounding rule for the Euro intermediate amount (Currency conversion rule) Multifonds DB Column is CARRONDI_EURO. |
| 23 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CCY.DECIMAL.RULES.EURO` | `FsGaForeignExchangeManagement_CcyDecimalRulesEuro` | TField |  | Number of decimals for the Euro intermediate amount (Currency conversion rule) Multifonds DB Column is CDEC_EURO. |
| 24 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.START.DATE` | `FsGaForeignExchangeManagement_StartDate` | TField |  | Starting date of the currency application Multifonds DB Column is DCALC. |
| 25 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.INTEREST.RATES` | `FsGaForeignExchangeManagement_InterestRates` | TField |  | Enter a maximum tolerance percentage for interest rate deviations. The percentage indicated here will be used in the control report. Multifonds DB Column is PCT_TAUX. |
| 26 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.EXCHANGE.RATE.PERCENTAGE` | `FsGaForeignExchangeManagement_ExchangeRatePercentage` | TField |  | Enter a maximum tolerance percentage for exchange rate deviations. The percentage indicated here will be used in the control report Multifonds DB Column is PCT_COURS. |
| 27 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.INTERNAL.SIZE` | `FsGaForeignExchangeManagement_InternalSize` | TField |  | Internal Size Multifonds DB Column is FLG_INT_SIZE. |
| 28 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CCY.INTERNAL.SEC.ID` | `FsGaForeignExchangeManagement_CcyInternalSecId` | TField |  | The Security Id linked to the currency. Used for reporting purposes Multifonds DB Column is NOVAL_MON. |
| 29 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.APPLICATION.CCY` | `FsGaForeignExchangeManagement_ApplicationCcy` | TField |  | Flag the application currency record Multifonds DB Column is FLG_APPL_CRANG. |
| 30 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED10` | `FsGaForeignExchangeManagement_Reserved10` | TField |  |  |
| 31 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED9` | `FsGaForeignExchangeManagement_Reserved9` | TField |  |  |
| 32 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED8` | `FsGaForeignExchangeManagement_Reserved8` | TField |  |  |
| 33 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED7` | `FsGaForeignExchangeManagement_Reserved7` | TField |  |  |
| 34 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED6` | `FsGaForeignExchangeManagement_Reserved6` | TField |  |  |
| 35 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED5` | `FsGaForeignExchangeManagement_Reserved5` | TField |  |  |
| 36 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED4` | `FsGaForeignExchangeManagement_Reserved4` | TField |  |  |
| 37 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED3` | `FsGaForeignExchangeManagement_Reserved3` | TField |  |  |
| 38 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED2` | `FsGaForeignExchangeManagement_Reserved2` | TField |  |  |
| 39 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RESERVED1` | `FsGaForeignExchangeManagement_Reserved1` | TField |  |  |
| 40 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.LOCAL.REF` | `FsGaForeignExchangeManagement_LocalRef` |  |  |  |
| 41 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.OVERRIDE` | `FsGaForeignExchangeManagement_Override` |  |  |  |
| 42 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.RECORD.STATUS` | `FsGaForeignExchangeManagement_RecordStatus` | String |  |  |
| 43 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CURR.NO` | `FsGaForeignExchangeManagement_CurrNo` | String |  |  |
| 44 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.INPUTTER` | `FsGaForeignExchangeManagement_Inputter` |  |  |  |
| 45 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.DATE.TIME` | `FsGaForeignExchangeManagement_DateTime` |  |  |  |
| 46 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.AUTHORISER` | `FsGaForeignExchangeManagement_Authoriser` | String |  |  |
| 47 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.CO.CODE` | `FsGaForeignExchangeManagement_CoCode` | String |  |  |
| 48 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.DEPT.CODE` | `FsGaForeignExchangeManagement_DeptCode` | String |  |  |
| 49 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.AUDITOR.CODE` | `FsGaForeignExchangeManagement_AuditorCode` | String |  |  |
| 50 | `FS.GA.FOREIGN.EXCHANGE.MANAGEMENT.AUDIT.DATE.TIME` | `FsGaForeignExchangeManagement_AuditDateTime` | String |  |  |
