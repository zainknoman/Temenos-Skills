# ACCR.ACCT.DR2 — Table Schema

> Source: `INSERTS/I_F.ACCR.ACCT.DR2` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.ACRD2.PERIOD.FIRST.DATE` | `AccrAcctDr2_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the last debit 2 interest application (Capitalisation) as stored in the CAP.DATE.D2.INT field in the ACCOUNT record. Validation Rules: 9 date characters DD MMM YYYY. |
| 2 | `IC.ACRD2.PERIOD.LAST.DATE` | `AccrAcctDr2_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the Account up to and including the last end of day processing. The calculation includes all balances from the day after the last debit 2 interest capitalisation, as stored in the ACCOUNT record (in the CAP.DATE.D2.INT field) up to and including the month end accrual date specified in the MTH.END.UPTO.DAY field in the ACCOUNT.ACCRUAL record. Validation Rules: 9 date characters DD MMM YYYY. |
| 3 | `IC.ACRD2.DR2.INT.DATE` | `AccrAcctDr2_Dr2IntDate` |  |  |  |
| 4 | `IC.ACRD2.DR2.NO.OF.DAYS` | `AccrAcctDr2_Dr2NoOfDays` |  |  |  |
| 5 | `IC.ACRD2.DR2.VAL.BALANCE` | `AccrAcctDr2_Dr2ValBalance` |  |  |  |
| 6 | `IC.ACRD2.DR2.INT.RATE` | `AccrAcctDr2_Dr2IntRate` |  |  |  |
| 7 | `IC.ACRD2.DR2.INT.AMT` | `AccrAcctDr2_Dr2IntAmt` |  |  |  |
| 8 | `IC.ACRD2.DR2.INT.CATEG` | `AccrAcctDr2_Dr2IntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when debit 2 interest is accrued. Validation Rules: 4 or 5 numeric characters. |
| 9 | `IC.ACRD2.DR2.INT.TR.AC` | `AccrAcctDr2_Dr2IntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when debit 2 interest is capitalised. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 10 | `IC.ACRD2.DR2.INT.TR.PL` | `AccrAcctDr2_Dr2IntTrPl` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated when debit 2 interest is accrued. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.ACRD2.D2.INT.TAX.CODE` | `AccrAcctDr2_D2IntTaxCode` |  |  |  |
| 12 | `IC.ACRD2.D2.INT.TAX.RATE` | `AccrAcctDr2_D2IntTaxRate` |  |  |  |
| 13 | `IC.ACRD2.D2.INT.TAX.AMT` | `AccrAcctDr2_D2IntTaxAmt` |  |  |  |
| 14 | `IC.ACRD2.D2.INT.TAXCATEG` | `AccrAcctDr2_D2IntTaxcateg` |  |  |  |
| 15 | `IC.ACRD2.D2.INT.TAXTRSDR` | `AccrAcctDr2_D2IntTaxtrsdr` |  |  |  |
| 16 | `IC.ACRD2.D2.INT.TAXTRSCR` | `AccrAcctDr2_D2IntTaxtrscr` |  |  |  |
| 17 | `IC.ACRD2.LIQUIDITY.ACCOUNT` | `AccrAcctDr2_LiquidityAccount` | TField |  | Where interest and charges are to be passed to an alternative Account, the number of the alternative ACCOUNT is shown by this field. Where interest and charges are to be passed to an alternative Account, the alternative account number should be entered in the INTEREST.LIQU.ACCT field on the original customer ACCOUNT record. Validation Rules: Standard account format. |
| 18 | `IC.ACRD2.COMPENS.ACCOUNT` | `AccrAcctDr2_CompensAccount` |  |  |  |
| 19 | `IC.ACRD2.INT.NO.BOOKING` | `AccrAcctDr2_IntNoBooking` | TField |  | If interest and charges are to be calculated for information purposes only and not passed to the account, or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit or Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the Account record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 20 | `IC.ACRD2.TOTAL.INTEREST` | `AccrAcctDr2_TotalInterest` | TField |  | Amount of interest. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.ACRD2.TOTAL.TAX` | `AccrAcctDr2_TotalTax` | TField |  | Not used in ACCR.ACCT.DR2 records. Validation Rules: Null. |
| 22 | `IC.ACRD2.GRAND.TOTAL` | `AccrAcctDr2_GrandTotal` | TField |  | Total amount booked to Profit and Loss since the last capitalisation. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 23 | `IC.ACRD2.CORRECTION.NUMBER` | `AccrAcctDr2_CorrectionNumber` | TField |  | Not used in ACCR.ACCT.DR2 records. Validation Rules: Null. |
| 24 | `IC.ACRD2.DEFERRED.DATE` | `AccrAcctDr2_DeferredDate` | TField |  | This field will hold the deferred application date of the debit interest in case pending debit interest processing was being performed on this account. |
| 25 | `IC.ACRD2.LIQUIDITY.CCY` | `AccrAcctDr2_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) characters or 1-3 numeric characters. |
| 26 | `IC.ACRD2.ICA.POST.INTEREST` | `AccrAcctDr2_IcaPostInterest` | TField |  | Not used in ACCR.ACCT.DR2 records. Validation Rules: Null. |
| 27 | `IC.ACRD2.ICA.MAIN.ACCT` | `AccrAcctDr2_IcaMainAcct` |  |  |  |
| 28 | `IC.ACRD2.ICA.DIST.TYPE` | `AccrAcctDr2_IcaDistType` |  |  |  |
| 29 | `IC.ACRD2.ICA.DIST.RATIO` | `AccrAcctDr2_IcaDistRatio` |  |  |  |
| 30 | `IC.ACRD2.ICA.INT.CATEG` | `AccrAcctDr2_IcaIntCateg` |  |  |  |
| 31 | `IC.ACRD2.ICA.TR.AC` | `AccrAcctDr2_IcaTrAc` |  |  |  |
| 32 | `IC.ACRD2.ICA.TR.PL` | `AccrAcctDr2_IcaTrPl` |  |  |  |
| 33 | `IC.ACRD2.ICA.MAIN.INT` | `AccrAcctDr2_IcaMainInt` |  |  |  |
| 34 | `IC.ACRD2.ICA.SUB.INT` | `AccrAcctDr2_IcaSubInt` |  |  |  |
| 35 | `IC.ACRD2.DR2.MIN.VALUE` | `AccrAcctDr2_Dr2MinValue` | TField |  | If relevant the minimum amount of debit 2 interest to apply if the calculated amount of interest is less than the minimum value and DR2.MIN.WAIVE is not set to "YES". |
| 36 | `IC.ACRD2.DR2.MIN.WAIVE` | `AccrAcctDr2_Dr2MinWaive` | TField |  | If set to "YES" and the amount of interest calculated is less than the DR2.MIN.VALUE then no interest will be booked. |
| 37 | `IC.ACRD2.UNADJ.TOTAL.INT` | `AccrAcctDr2_UnadjTotalInt` | TField |  | The total calculated amount of interest which can differ from the amount booked in the case of manual adjustments to debit 2 interest. |
| 38 | `IC.ACRD2.INT.POST.DATE` | `AccrAcctDr2_IntPostDate` | TField |  | The date interest was posted for this capitalisation perio. Not relevant to accruals. |
| 39 | `IC.ACRD2.MANUAL.ADJ.AMT` | `AccrAcctDr2_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 40 | `IC.ACRD2.DEF.TOTAL.INT` | `AccrAcctDr2_DefTotalInt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 41 | `IC.ACRD2.DEF.TOTAL.TAX` | `AccrAcctDr2_DefTotalTax` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 42 | `IC.ACRD2.DEF.WAIVE.ALL` | `AccrAcctDr2_DefWaiveAll` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 43 | `IC.ACRD2.CORRECTION.ID` | `AccrAcctDr2_CorrectionId` |  |  |  |
| 44 | `IC.ACRD2.ADJ.INT.AMT` | `AccrAcctDr2_AdjIntAmt` |  |  |  |
| 45 | `IC.ACRD2.ADJ.TAX.AMT` | `AccrAcctDr2_AdjTaxAmt` |  |  |  |
| 46 | `IC.ACRD2.WITHHELD.INT.AMT` | `AccrAcctDr2_WithheldIntAmt` |  |  |  |
| 47 | `IC.ACRD2.DB.NETTING.AMT` | `AccrAcctDr2_DbNettingAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 48 | `IC.ACRD2.CORRECTION.DATE` | `AccrAcctDr2_CorrectionDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 49 | `IC.ACRD2.WAIVE.AMT` | `AccrAcctDr2_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 50 | `IC.ACRD2.WAIVE.RATE` | `AccrAcctDr2_WaiveRate` | TField |  |  |
| 51 | `IC.ACRD2.RESERVED.03` | `AccrAcctDr2_Reserved03` | TField |  |  |
| 52 | `IC.ACRD2.RESERVED.02` | `AccrAcctDr2_Reserved02` | TField |  |  |
| 53 | `IC.ACRD2.RESERVED.01` | `AccrAcctDr2_Reserved01` | TField |  |  |
