# FS.GA.INTEREST.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.INTEREST.MANAGEMENT` in `FS_PricesRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INTEREST.MANAGEMENT.FUND.ID` | `FsGaInterestManagement_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.INTEREST.MANAGEMENT.GL.ACCOUNT` | `FsGaInterestManagement_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 3 | `FS.GA.INTEREST.MANAGEMENT.GL.ACCOUNT.SUFFIX` | `FsGaInterestManagement_GlAccountSuffix` | TField |  | Suffix number tagged to the account number. In case of cash this identifies the correspondent and for other P and L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 4 | `FS.GA.INTEREST.MANAGEMENT.LOCAL.CURRENCY` | `FsGaInterestManagement_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 5 | `FS.GA.INTEREST.MANAGEMENT.PAY.DATE` | `FsGaInterestManagement_PayDate` | TField |  | Dval Multifonds DB Column is DVAL. |
| 6 | `FS.GA.INTEREST.MANAGEMENT.SETTLE.DATE` | `FsGaInterestManagement_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 7 | `FS.GA.INTEREST.MANAGEMENT.STATUS.CODE` | `FsGaInterestManagement_StatusCode` | TField |  | Status Code Multifonds DB Column is STATUS. |
| 8 | `FS.GA.INTEREST.MANAGEMENT.SPREAD.OF.ASSETS.INTEREST` | `FsGaInterestManagement_SpreadOfAssetsInterest` | TField |  | Spread Of Assets Interest Multifonds DB Column is TINTDB. |
| 9 | `FS.GA.INTEREST.MANAGEMENT.SPREAD.OF.LIABILITIES.INTEREST` | `FsGaInterestManagement_SpreadOfLiabilitiesInterest` | TField |  | Spread Of Liabilities Interest Multifonds DB Column is TINTCR. |
| 10 | `FS.GA.INTEREST.MANAGEMENT.INTEREST.RATE.TYPE` | `FsGaInterestManagement_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 11 | `FS.GA.INTEREST.MANAGEMENT.MANAGER.CODE` | `FsGaInterestManagement_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 12 | `FS.GA.INTEREST.MANAGEMENT.ACCOUNTING.DATE` | `FsGaInterestManagement_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 13 | `FS.GA.INTEREST.MANAGEMENT.TRANSACTION.NUMBER` | `FsGaInterestManagement_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 14 | `FS.GA.INTEREST.MANAGEMENT.TRANSACTION.SERVICE.CODE` | `FsGaInterestManagement_TransactionServiceCode` | TField |  | This is the transaction type. Multifonds DB Column is CSERV. |
| 15 | `FS.GA.INTEREST.MANAGEMENT.TAX.AMOUNT` | `FsGaInterestManagement_TaxAmount` | TField |  | Tax Amount Multifonds DB Column is MNT_IMPOT_DEV. |
| 16 | `FS.GA.INTEREST.MANAGEMENT.IMPOT.AMOUNT` | `FsGaInterestManagement_ImpotAmount` | TField |  | Impot Amount Multifonds DB Column is MNT_IMPOT. |
| 17 | `FS.GA.INTEREST.MANAGEMENT.GROSS.INTEREST.AMOUNT` | `FsGaInterestManagement_GrossInterestAmount` | TField |  | Gross Interest Amount Multifonds DB Column is MNT_GROSS_DEV. |
| 18 | `FS.GA.INTEREST.MANAGEMENT.TRADE.DATE` | `FsGaInterestManagement_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 19 | `FS.GA.INTEREST.MANAGEMENT.REVISION.CODE` | `FsGaInterestManagement_RevisionCode` | TField |  | Defined the calculation method for the rate defined in "Int rate type" and "maturity" Multifonds DB Column is REVISION_CODE. |
| 20 | `FS.GA.INTEREST.MANAGEMENT.MATURITY.CODE` | `FsGaInterestManagement_MaturityCode` | TField |  | Maturity code of the floating interest rate that needs to be applied for commission accrual on a lending/borrowing transaction Multifonds DB Column is CODE_MOIS. |
| 21 | `FS.GA.INTEREST.MANAGEMENT.CURRENCY.OF.INTEREST` | `FsGaInterestManagement_CurrencyOfInterest` | TField |  | Currency of Interest Multifonds DB Column is CMON_TAUX. |
| 22 | `FS.GA.INTEREST.MANAGEMENT.REVISED.INTEREST.RATE` | `FsGaInterestManagement_RevisedInterestRate` | TField |  | Revised Interest Rate Multifonds DB Column is TAUX_RATE. |
| 23 | `FS.GA.INTEREST.MANAGEMENT.REFERENCE.INTEREST.TYPE` | `FsGaInterestManagement_ReferenceInterestType` | TField |  | Reference Interest Type Multifonds DB Column is TYP_TAUX_CALC. |
| 24 | `FS.GA.INTEREST.MANAGEMENT.FREQUENCY.CODE` | `FsGaInterestManagement_FrequencyCode` | TField |  | Frequency code for processing Multifonds DB Column is CFREQ. |
| 25 | `FS.GA.INTEREST.MANAGEMENT.PAYMENT.DAY` | `FsGaInterestManagement_PaymentDay` | TField |  | Payment Day Multifonds DB Column is DFREQ. |
| 26 | `FS.GA.INTEREST.MANAGEMENT.CALCULATION.PAYMENT.DATE` | `FsGaInterestManagement_CalculationPaymentDate` | TField |  | Logic to decide if payment date falls on a non working day should it process payment on same date or prior/next working day. Multifonds DB Column is CTR_DATE. |
| 27 | `FS.GA.INTEREST.MANAGEMENT.FLAG.CAP` | `FsGaInterestManagement_FlagCap` | TField |  | Flag Cap Multifonds DB Column is FLG_CAP. |
| 28 | `FS.GA.INTEREST.MANAGEMENT.ARCHIVE` | `FsGaInterestManagement_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 29 | `FS.GA.INTEREST.MANAGEMENT.RESERVED10` | `FsGaInterestManagement_Reserved10` | TField |  |  |
| 30 | `FS.GA.INTEREST.MANAGEMENT.RESERVED9` | `FsGaInterestManagement_Reserved9` | TField |  |  |
| 31 | `FS.GA.INTEREST.MANAGEMENT.RESERVED8` | `FsGaInterestManagement_Reserved8` | TField |  |  |
| 32 | `FS.GA.INTEREST.MANAGEMENT.RESERVED7` | `FsGaInterestManagement_Reserved7` | TField |  |  |
| 33 | `FS.GA.INTEREST.MANAGEMENT.RESERVED6` | `FsGaInterestManagement_Reserved6` | TField |  |  |
| 34 | `FS.GA.INTEREST.MANAGEMENT.RESERVED5` | `FsGaInterestManagement_Reserved5` | TField |  |  |
| 35 | `FS.GA.INTEREST.MANAGEMENT.RESERVED4` | `FsGaInterestManagement_Reserved4` | TField |  |  |
| 36 | `FS.GA.INTEREST.MANAGEMENT.RESERVED3` | `FsGaInterestManagement_Reserved3` | TField |  |  |
| 37 | `FS.GA.INTEREST.MANAGEMENT.RESERVED2` | `FsGaInterestManagement_Reserved2` | TField |  |  |
| 38 | `FS.GA.INTEREST.MANAGEMENT.RESERVED1` | `FsGaInterestManagement_Reserved1` | TField |  |  |
| 39 | `FS.GA.INTEREST.MANAGEMENT.OVERRIDE` | `FsGaInterestManagement_Override` |  |  |  |
| 40 | `FS.GA.INTEREST.MANAGEMENT.LOCAL.REF` | `FsGaInterestManagement_LocalRef` |  |  |  |
| 41 | `FS.GA.INTEREST.MANAGEMENT.RECORD.STATUS` | `FsGaInterestManagement_RecordStatus` | String |  |  |
| 42 | `FS.GA.INTEREST.MANAGEMENT.CURR.NO` | `FsGaInterestManagement_CurrNo` | String |  |  |
| 43 | `FS.GA.INTEREST.MANAGEMENT.INPUTTER` | `FsGaInterestManagement_Inputter` |  |  |  |
| 44 | `FS.GA.INTEREST.MANAGEMENT.DATE.TIME` | `FsGaInterestManagement_DateTime` |  |  |  |
| 45 | `FS.GA.INTEREST.MANAGEMENT.AUTHORISER` | `FsGaInterestManagement_Authoriser` | String |  |  |
| 46 | `FS.GA.INTEREST.MANAGEMENT.CO.CODE` | `FsGaInterestManagement_CoCode` | String |  |  |
| 47 | `FS.GA.INTEREST.MANAGEMENT.DEPT.CODE` | `FsGaInterestManagement_DeptCode` | String |  |  |
| 48 | `FS.GA.INTEREST.MANAGEMENT.AUDITOR.CODE` | `FsGaInterestManagement_AuditorCode` | String |  |  |
| 49 | `FS.GA.INTEREST.MANAGEMENT.AUDIT.DATE.TIME` | `FsGaInterestManagement_AuditDateTime` | String |  |  |
