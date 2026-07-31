# CORR.ACCT.DR2 — Table Schema

> Source: `INSERTS/I_F.CORR.ACCT.DR2` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.CORD2.PERIOD.FIRST.DATE` | `CorrAcctDr2_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the previous debit 2 interest application (Capitalisation) as stored in the CAP.DATE.DR2.INT field in the ACCOUNT record. Validation Rules: 9 date characters - DD MMM YYYY. |
| 2 | `IC.CORD2.PERIOD.LAST.DATE` | `CorrAcctDr2_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the ACCOUNT up to and including the day on which the interest capitalisation is processed. The calculation includes all balances from the day after the previous debit 2 interest capitalisation, as stored in the ACCOUNT record (in the CAP.DATE.DR2.INT field) up to the capitalisation date specified, or, if the LAST.DAY.INCLUSIVE field in the ACCOUNT.ACCRUAL file contains 'NO', up to the working day prior to the processing date. Validation Rules: 9 date characters - DD MMM YYYY. |
| 3 | `IC.CORD2.DR2.INT.DATE` | `CorrAcctDr2_Dr2IntDate` |  |  |  |
| 4 | `IC.CORD2.DR2.NO.OF.DAYS` | `CorrAcctDr2_Dr2NoOfDays` |  |  |  |
| 5 | `IC.CORD2.DR2.VAL.BALANCE` | `CorrAcctDr2_Dr2ValBalance` |  |  |  |
| 6 | `IC.CORD2.DR2.INT.RATE` | `CorrAcctDr2_Dr2IntRate` |  |  |  |
| 7 | `IC.CORD2.DR2.INT.AMT` | `CorrAcctDr2_Dr2IntAmt` |  |  |  |
| 8 | `IC.CORD2.DR2.INT.CATEG` | `CorrAcctDr2_Dr2IntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when debit 2 interest is accrued. Validation Rules: 4 or 5 numeric characters. |
| 9 | `IC.CORD2.DR2.INT.TR.AC` | `CorrAcctDr2_Dr2IntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when debit 2 interest is capitalised. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 10 | `IC.CORD2.DR2.INT.TR.PL` | `CorrAcctDr2_Dr2IntTrPl` | TField |  | Identifies the Transaction code to be assigned to P&amp;L entries generated when debit 2 interest is capitalised. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.CORD2.D2.INT.TAX.CODE` | `CorrAcctDr2_D2IntTaxCode` |  |  |  |
| 12 | `IC.CORD2.D2.INT.TAX.RATE` | `CorrAcctDr2_D2IntTaxRate` |  |  |  |
| 13 | `IC.CORD2.D2.INT.TAX.AMT` | `CorrAcctDr2_D2IntTaxAmt` |  |  |  |
| 14 | `IC.CORD2.D2.INT.TAXCATEG` | `CorrAcctDr2_D2IntTaxcateg` |  |  |  |
| 15 | `IC.CORD2.D2.INT.TAXTRSDR` | `CorrAcctDr2_D2IntTaxtrsdr` |  |  |  |
| 16 | `IC.CORD2.D2.INT.TAXTRSCR` | `CorrAcctDr2_D2IntTaxtrscr` |  |  |  |
| 17 | `IC.CORD2.LIQUIDITY.ACCOUNT` | `CorrAcctDr2_LiquidityAccount` | TField |  | Where interest and charges are to be passed to an alternative Account, the number of the alternative ACCOUNT is shown by this field. Where interest and charges are to be passed to an alternative Account, the alternative account number should be entered in the INTEREST.LIQU.ACCT field on the original customer ACCOUNT record. Validation Rules: 2-16 numeric characters. |
| 18 | `IC.CORD2.COMPENS.ACCOUNT` | `CorrAcctDr2_CompensAccount` |  |  |  |
| 19 | `IC.CORD2.INT.NO.BOOKING` | `CorrAcctDr2_IntNoBooking` | TField |  | If interest and charges are to be calculated for information purposes only and not passed to the account, or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit or Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the Account record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 20 | `IC.CORD2.TOTAL.INTEREST` | `CorrAcctDr2_TotalInterest` | TField |  | Amount of interest before Tax. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.CORD2.TOTAL.TAX` | `CorrAcctDr2_TotalTax` | TField |  | Total amount of Tax on Interest (if applicable). Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 22 | `IC.CORD2.GRAND.TOTAL` | `CorrAcctDr2_GrandTotal` | TField |  | Total amount to be debited to customer's account including debit 2 interest and tax (if applicable). Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 23 | `IC.CORD2.CORRECTION.NUMBER` | `CorrAcctDr2_CorrectionNumber` | TField |  | Incremented every time an interest correction take place |
| 24 | `IC.CORD2.DEFERRED.DATE` | `CorrAcctDr2_DeferredDate` | TField |  | This field will hold the deferred application date of the debit interest in case pending debit interest processing was being performed on this account. |
| 25 | `IC.CORD2.LIQUIDITY.CCY` | `CorrAcctDr2_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) characters or 1-3 numeric characters. |
| 26 | `IC.CORD2.ICA.POST.INTEREST` | `CorrAcctDr2_IcaPostInterest` | TField |  | Indicates whether ICA interest is actually posted to this account, or is just calculated for information purposes. |
| 27 | `IC.CORD2.ICA.MAIN.ACCT` | `CorrAcctDr2_IcaMainAcct` |  |  |  |
| 28 | `IC.CORD2.ICA.DIST.TYPE` | `CorrAcctDr2_IcaDistType` |  |  |  |
| 29 | `IC.CORD2.ICA.DIST.RATIO` | `CorrAcctDr2_IcaDistRatio` |  |  |  |
| 30 | `IC.CORD2.ICA.INT.CATEG` | `CorrAcctDr2_IcaIntCateg` |  |  |  |
| 31 | `IC.CORD2.ICA.TR.AC` | `CorrAcctDr2_IcaTrAc` |  |  |  |
| 32 | `IC.CORD2.ICA.TR.PL` | `CorrAcctDr2_IcaTrPl` |  |  |  |
| 33 | `IC.CORD2.ICA.MAIN.INT` | `CorrAcctDr2_IcaMainInt` |  |  |  |
| 34 | `IC.CORD2.ICA.SUB.INT` | `CorrAcctDr2_IcaSubInt` |  |  |  |
| 35 | `IC.CORD2.DR2.MIN.VALUE` | `CorrAcctDr2_Dr2MinValue` | TField |  | Indicates that the minimum amount of debit 2 interest has been applied. If the calculated amount of interest was less than the minimum value then this will be applied, assuming that the amount is not to be waived. |
| 36 | `IC.CORD2.DR2.MIN.WAIVE` | `CorrAcctDr2_Dr2MinWaive` | TField |  | Indicates whether debit 2 interest is set to zero if it is less than the minimum value. Set to "YES" is interest below the minimum value is to be waived. |
| 37 | `IC.CORD2.UNADJ.TOTAL.INT` | `CorrAcctDr2_UnadjTotalInt` | TField |  | The calculated total interest amount, this will differ from the total interest that is posted when a manual interest adjustment has been made. |
| 38 | `IC.CORD2.INT.POST.DATE` | `CorrAcctDr2_IntPostDate` | TField |  | The date that interest was posted to the account |
| 39 | `IC.CORD2.MANUAL.ADJ.AMT` | `CorrAcctDr2_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 40 | `IC.CORD2.DEF.TOTAL.INT` | `CorrAcctDr2_DefTotalInt` | TField |  | The amount of deferred interest that was posted |
| 41 | `IC.CORD2.DEF.TOTAL.TAX` | `CorrAcctDr2_DefTotalTax` | TField |  | The amount of deferred tax on interest that was posted. |
| 42 | `IC.CORD2.DEF.WAIVE.ALL` | `CorrAcctDr2_DefWaiveAll` | TField |  | YES indicates that all debit interest and tax was waived for this period, if set to YES then no debit interest or tax will apply to this period for back valued corrections. But it will be calculated |
| 43 | `IC.CORD2.CORRECTION.ID` | `CorrAcctDr2_CorrectionId` |  |  |  |
| 44 | `IC.CORD2.ADJ.INT.AMT` | `CorrAcctDr2_AdjIntAmt` |  |  |  |
| 45 | `IC.CORD2.ADJ.TAX.AMT` | `CorrAcctDr2_AdjTaxAmt` |  |  |  |
| 46 | `IC.CORD2.WITHHELD.INT.AMT` | `CorrAcctDr2_WithheldIntAmt` |  |  |  |
| 47 | `IC.CORD2.DB.NETTING.AMT` | `CorrAcctDr2_DbNettingAmt` | TField |  | This field will be updated if CR interest is netted with corresponding DR interest. |
| 48 | `IC.CORD2.CORRECTION.DATE` | `CorrAcctDr2_CorrectionDate` | TField |  | This field will contain the period end date of the current capitalisation period. |
| 49 | `IC.CORD2.WAIVE.AMT` | `CorrAcctDr2_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 50 | `IC.CORD2.WAIVE.RATE` | `CorrAcctDr2_WaiveRate` | TField |  |  |
| 51 | `IC.CORD2.RESERVED.03` | `CorrAcctDr2_Reserved03` | TField |  |  |
| 52 | `IC.CORD2.RESERVED.02` | `CorrAcctDr2_Reserved02` | TField |  |  |
| 53 | `IC.CORD2.RESERVED.01` | `CorrAcctDr2_Reserved01` | TField |  |  |
