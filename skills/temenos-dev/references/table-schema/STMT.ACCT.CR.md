# STMT.ACCT.CR — Table Schema

> Source: `INSERTS/I_F.STMT.ACCT.CR` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.STMCR.PERIOD.FIRST.DATE` | `StmtAcctCr_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the previous credit interest application (Capitalisation) as stored in the CAP DATE CR INT field in the ACCOUNT record. Validation Rules: 9 date characters - DD MMM YYYY. |
| 2 | `IC.STMCR.PERIOD.LAST.DATE` | `StmtAcctCr_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the ACCOUNT up to and including the last end of day processing. The calculation includes all balances from the day after the last credit interest capitalisation, as stored in the ACCOUNT record (in the CAP DATE CR INT field) up to the capitalisation date specified, or, if the LAST DAY INCLUSIVE field in the ACCOUNT.ACCRUAL file contains 'NO', up to the working day prior to the processing date. Validation Rules: 9 date characters - DD MMM YYYY. |
| 3 | `IC.STMCR.CR.INT.DATE` | `StmtAcctCr_CrIntDate` |  |  |  |
| 4 | `IC.STMCR.CR.NO.OF.DAYS` | `StmtAcctCr_CrNoOfDays` |  |  |  |
| 5 | `IC.STMCR.CR.VAL.BALANCE` | `StmtAcctCr_CrValBalance` |  |  |  |
| 6 | `IC.STMCR.CR.INT.RATE` | `StmtAcctCr_CrIntRate` |  |  |  |
| 7 | `IC.STMCR.CR.INT.AMT` | `StmtAcctCr_CrIntAmt` |  |  |  |
| 8 | `IC.STMCR.CR.INT.CATEG` | `StmtAcctCr_CrIntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when credit interest is accrued. Validation Rules: 4 or 5 numeric character Category code. |
| 9 | `IC.STMCR.CR.INT.TR.AC` | `StmtAcctCr_CrIntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when credit interest is capitalisaed. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 10 | `IC.STMCR.CR.INT.TR.PL` | `StmtAcctCr_CrIntTrPl` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated when credit interest is accrued. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.STMCR.CR.INT.TAX.CODE` | `StmtAcctCr_CrIntTaxCode` |  |  |  |
| 12 | `IC.STMCR.CR.INT.TAX.RATE` | `StmtAcctCr_CrIntTaxRate` |  |  |  |
| 13 | `IC.STMCR.CR.INT.TAX.AMT` | `StmtAcctCr_CrIntTaxAmt` |  |  |  |
| 14 | `IC.STMCR.CR.INT.TAXCATEG` | `StmtAcctCr_CrIntTaxcateg` |  |  |  |
| 15 | `IC.STMCR.CR.INT.TAXTRSDR` | `StmtAcctCr_CrIntTaxtrsdr` |  |  |  |
| 16 | `IC.STMCR.CR.INT.TAXTRSCR` | `StmtAcctCr_CrIntTaxtrscr` |  |  |  |
| 17 | `IC.STMCR.LIQUIDITY.ACCOUNT` | `StmtAcctCr_LiquidityAccount` | TField |  | Where Credit Interest is to be passed to an alternative ACCOUNT, the number of the ACCOUNT is shown by this field. Validation Rules: Standard account format. |
| 18 | `IC.STMCR.COMPENS.ACCOUNT` | `StmtAcctCr_CompensAccount` |  |  |  |
| 19 | `IC.STMCR.INT.NO.BOOKING` | `StmtAcctCr_IntNoBooking` | TField |  | If credit interest is to be calculated for information purposes only and not passed to the account or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit and Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the Account record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 20 | `IC.STMCR.TOTAL.INTEREST` | `StmtAcctCr_TotalInterest` | TField |  | Total amount of Interest before Tax has been deducted. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.STMCR.TAX.FOR.CUSTOMER` | `StmtAcctCr_TaxForCustomer` | TField |  | Amount of Tax deducted from the credit interest due to the Customer, if applicable. Where Tax is payable on credit interest, the interest rate may be quoted 'Gross' (before deduction of Tax) or 'Net' (after deduction of Tax). This is determined by the TAX OPERAND field in the applicable TAX record. If the TAX OPERAND contains 'MINUS', the interest rate is quoted 'Gross' and the Tax amount in this field is payable by the Customer. If the TAX OPERAND contains 'PLUS', the interest rate is quoted 'Net' and the Tax amount in the next field is payable by the Bank. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 22 | `IC.STMCR.TAX.FOR.BANK` | `StmtAcctCr_TaxForBank` | TField |  | Amount of Tax to be paid by the Bank on behalf of the Customer, if applicable. Where Tax is payable on credit interest, the interest rate may be quoted 'Gross' (before deduction of Tax) or 'Net' (after deduction of Tax). This is determined by the TAX OPERAND field in the applicable TAX record. If the TAX OPERAND contains 'MINUS', the interest rate is quoted 'Gross' and the Tax amount in the previous field is payable by the Customer. If the TAX OPERAND contains 'PLUS', the interest rate is quoted 'Net' and the Tax amount in this field is payable by the Bank. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 23 | `IC.STMCR.GRAND.TOTAL` | `StmtAcctCr_GrandTotal` | TField |  | Total interest to be credited to the customers account after deduction of Tax (if applicable). Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 24 | `IC.STMCR.CORRECTION.NUMBER` | `StmtAcctCr_CorrectionNumber` | TField |  | Sequential number of corrected record generated after back-valued entries, rate changes or condition changes. Only present in records which have been corrected. If any entries are processed with VALUE DATEs prior to the last Capitalisation date (as stored in the CAP DATE CR INT field in the ACCOUNT record), the end of day program EOD.CAPITALIS.CORR automatically recalculates the interest for the capitalisation period(s) from the one containing the earliest back-valued entry, up to the last Capitalisation date. The new STMT.ACCT.CR record is compared with the one previously calculated, and if there is any difference, the old one is stored in the CORR.ACCT.CR file, the corrected one is written in this file and appropriate accounting entries are processed for the differences. Each time the same capitalisation is corrected, the CORRECTION NUMBER is incremented by 1. When interest rates or conditions are amended, back-value recalculations are not processed automatically, but can be requested via the table TABLE CAPITALIS CORR. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 25 | `IC.STMCR.LIQUIDITY.CCY` | `StmtAcctCr_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) character or 1-3 numeric character currency code. |
| 26 | `IC.STMCR.ICA.POST.INTEREST` | `StmtAcctCr_IcaPostInterest` | TField |  | ICA.POST.INTEREST YES indicates that interest will be posted to the account if the account is an ICA group member. INFO indicates that interest is calculated but not posted if the account is an ICA group member. Validation Rules: No Input field Can contain YES or INFO. |
| 27 | `IC.STMCR.ICA.MAIN.ACCT` | `StmtAcctCr_IcaMainAcct` |  |  |  |
| 28 | `IC.STMCR.ICA.DIST.TYPE` | `StmtAcctCr_IcaDistType` |  |  |  |
| 29 | `IC.STMCR.ICA.DIST.RATIO` | `StmtAcctCr_IcaDistRatio` |  |  |  |
| 30 | `IC.STMCR.ICA.INT.CATEG` | `StmtAcctCr_IcaIntCateg` |  |  |  |
| 31 | `IC.STMCR.ICA.TR.AC` | `StmtAcctCr_IcaTrAc` |  |  |  |
| 32 | `IC.STMCR.ICA.TR.PL` | `StmtAcctCr_IcaTrPl` |  |  |  |
| 33 | `IC.STMCR.ICA.MAIN.INT` | `StmtAcctCr_IcaMainInt` |  |  |  |
| 34 | `IC.STMCR.ICA.SUB.INT` | `StmtAcctCr_IcaSubInt` |  |  |  |
| 35 | `IC.STMCR.RESERVED.1` | `StmtAcctCr_Reserved1` | TField |  |  |
| 36 | `IC.STMCR.RESERVED.2` | `StmtAcctCr_Reserved2` | TField |  |  |
| 37 | `IC.STMCR.RESERVED.3` | `StmtAcctCr_Reserved3` | TField |  |  |
| 38 | `IC.STMCR.RESERVED.4` | `StmtAcctCr_Reserved4` | TField |  |  |
| 39 | `IC.STMCR.CR.MIN.VALUE` | `StmtAcctCr_CrMinValue` | TField |  | Indicates that the minimum amount of credit interest has been applied. If the calculated amount of interest was less than the minimum value then this will be applied, assuming that the amount is not to be waived. |
| 40 | `IC.STMCR.CR.MIN.WAIVE` | `StmtAcctCr_CrMinWaive` | TField |  | Indicates whether credit interest is set to zero if it is less than the minimum value. Set to "YES" is interest below the minimum value is to be waived. |
| 41 | `IC.STMCR.UNADJ.TOTAL.INT` | `StmtAcctCr_UnadjTotalInt` | TField |  | The calculated total interest amount, this will differ from the total interest that is posted when a manual interest adjustment has been made. |
| 42 | `IC.STMCR.INT.POST.DATE` | `StmtAcctCr_IntPostDate` | TField |  | The date that interest was posted to the account. This is normally set when the interest posting is deferred. |
| 43 | `IC.STMCR.TAX.EXCH.RATE` | `StmtAcctCr_TaxExchRate` | TField |  | The exchange rate used when tax was calculated for this account. |
| 44 | `IC.STMCR.MANUAL.ADJ.AMT` | `StmtAcctCr_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 45 | `IC.STMCR.CORRECTION.ID` | `StmtAcctCr_CorrectionId` |  |  |  |
| 46 | `IC.STMCR.ADJ.INT.AMT` | `StmtAcctCr_AdjIntAmt` |  |  |  |
| 47 | `IC.STMCR.ADJ.TAX.AMT` | `StmtAcctCr_AdjTaxAmt` |  |  |  |
| 48 | `IC.STMCR.WITHHELD.INT.AMT` | `StmtAcctCr_WithheldIntAmt` |  |  |  |
| 49 | `IC.STMCR.DB.NETTING.AMT` | `StmtAcctCr_DbNettingAmt` | TField |  | This field will be updated if CR interest is netted with corresponding DR interest. |
| 50 | `IC.STMCR.CORRECTION.DATE` | `StmtAcctCr_CorrectionDate` | TField |  | This field will contain the period end date of the current capitalisation period. |
| 51 | `IC.STMCR.WAIVE.AMT` | `StmtAcctCr_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 52 | `IC.STMCR.WAIVE.RATE` | `StmtAcctCr_WaiveRate` | TField |  |  |
| 53 | `IC.STMCR.RESERVED.03` | `StmtAcctCr_Reserved03` | TField |  |  |
| 54 | `IC.STMCR.RESERVED.02` | `StmtAcctCr_Reserved02` | TField |  |  |
| 55 | `IC.STMCR.RESERVED.01` | `StmtAcctCr_Reserved01` | TField |  |  |
