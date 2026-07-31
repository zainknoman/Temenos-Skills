# CORR.ACCT.CR — Table Schema

> Source: `INSERTS/I_F.CORR.ACCT.CR` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.CORCR.PERIOD.FIRST.DATE` | `CorrAcctCr_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the previous credit interest application (Capitalisation) as stored in the CAP DATE CR INT field in the ACCOUNT record. Validation Rules: 9 date characters - DD MMM YYYY. |
| 2 | `IC.CORCR.PERIOD.LAST.DATE` | `CorrAcctCr_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the ACCOUNT up to and including the last end of day processing. The calculation includes all balances from the day after the last credit interest capitalisation, as stored in the ACCOUNT record (in the CAP DATE CR INT field) up to the capitalisation date specified, or, if the LAST DAY INCLUSIVE field in the ACCOUNT.ACCRUAL file contains 'NO', up to the working day prior to the processing date. Validation Rules: 9 date characters - DD MMM YYYY. |
| 3 | `IC.CORCR.CR.INT.DATE` | `CorrAcctCr_CrIntDate` |  |  |  |
| 4 | `IC.CORCR.CR.NO.OF.DAYS` | `CorrAcctCr_CrNoOfDays` |  |  |  |
| 5 | `IC.CORCR.CR.VAL.BALANCE` | `CorrAcctCr_CrValBalance` |  |  |  |
| 6 | `IC.CORCR.CR.INT.RATE` | `CorrAcctCr_CrIntRate` |  |  |  |
| 7 | `IC.CORCR.CR.INT.AMT` | `CorrAcctCr_CrIntAmt` |  |  |  |
| 8 | `IC.CORCR.CR.INT.CATEG` | `CorrAcctCr_CrIntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when credit interest is accrued. Validation Rules: 4 or 5 numeric character Category code. |
| 9 | `IC.CORCR.CR.INT.TR.AC` | `CorrAcctCr_CrIntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when credit interest is capitalisaed. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 10 | `IC.CORCR.CR.INT.TR.PL` | `CorrAcctCr_CrIntTrPl` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated when credit interest is accrued. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.CORCR.CR.INT.TAX.CODE` | `CorrAcctCr_CrIntTaxCode` |  |  |  |
| 12 | `IC.CORCR.CR.INT.TAX.RATE` | `CorrAcctCr_CrIntTaxRate` |  |  |  |
| 13 | `IC.CORCR.CR.INT.TAX.AMT` | `CorrAcctCr_CrIntTaxAmt` |  |  |  |
| 14 | `IC.CORCR.CR.INT.TAXCATEG` | `CorrAcctCr_CrIntTaxcateg` |  |  |  |
| 15 | `IC.CORCR.CR.INT.TAXTRSDR` | `CorrAcctCr_CrIntTaxtrsdr` |  |  |  |
| 16 | `IC.CORCR.CR.INT.TAXTRSCR` | `CorrAcctCr_CrIntTaxtrscr` |  |  |  |
| 17 | `IC.CORCR.LIQUIDITY.ACCOUNT` | `CorrAcctCr_LiquidityAccount` | TField |  | Where Credit Interest is to be passed to an alternative ACCOUNT, the number of the ACCOUNT is shown by this field. Validation Rules: 2-16 numeric character account number. |
| 18 | `IC.CORCR.COMPENS.ACCOUNT` | `CorrAcctCr_CompensAccount` |  |  |  |
| 19 | `IC.CORCR.INT.NO.BOOKING` | `CorrAcctCr_IntNoBooking` | TField |  | If credit interest is to be calculated for information purposes only and not passed to the account or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit and Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the Account record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 20 | `IC.CORCR.TOTAL.INTEREST` | `CorrAcctCr_TotalInterest` | TField |  | Total amount of Interest before Tax has been deducted. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.CORCR.TAX.FOR.CUSTOMER` | `CorrAcctCr_TaxForCustomer` | TField |  | Amount of Tax deducted from the credit interest due to the Customer, if applicable. Where Tax is payable on credit interest, the interest rate may be quoted 'Gross' (before deduction of Tax) or 'Net' (after deduction of Tax). This is determined by the TAX OPERAND field in the applicable TAX record. If the TAX OPERAND contains 'MINUS', the interest rate is quoted 'Gross' and the Tax amount in this field is payable by the Customer. If the TAX OPERAND contains 'PLUS', the interest rate is quoted 'Net' and the Tax amount in the next field is payable by the Bank. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 22 | `IC.CORCR.TAX.FOR.BANK` | `CorrAcctCr_TaxForBank` | TField |  | Amount of Tax to be paid by the Bank on behalf of the Customer, if applicable. Where Tax is payable on credit interest, the interest rate may be quoted 'Gross' (before deduction of Tax) or 'Net' (after deduction of Tax). This is determined by the TAX OPERAND field in the applicable TAX record. If the TAX OPERAND contains 'MINUS', the interest rate is quoted 'Gross' and the Tax amount in the previous field is payable by the Customer. If the TAX OPERAND contains 'PLUS', the interest rate is quoted 'Net' and the Tax amount in this field is payable by the Bank. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 23 | `IC.CORCR.GRAND.TOTAL` | `CorrAcctCr_GrandTotal` | TField |  | Total interest to be credited to the customers account after deduction of Tax (if applicable). Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 24 | `IC.CORCR.CORRECTION.NUMBER` | `CorrAcctCr_CorrectionNumber` | TField |  | Incremented every time that an interest correction is applied |
| 25 | `IC.CORCR.LIQUIDITY.CCY` | `CorrAcctCr_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) character or 1-3 numeric character currency code. |
| 26 | `IC.CORCR.ICA.POST.INTEREST` | `CorrAcctCr_IcaPostInterest` | TField |  | Indicates whether ICA interest is actually posted to this account, or is just calculated for information purposes. |
| 27 | `IC.CORCR.ICA.MAIN.ACCT` | `CorrAcctCr_IcaMainAcct` |  |  |  |
| 28 | `IC.CORCR.ICA.DIST.TYPE` | `CorrAcctCr_IcaDistType` |  |  |  |
| 29 | `IC.CORCR.ICA.DIST.RATIO` | `CorrAcctCr_IcaDistRatio` |  |  |  |
| 30 | `IC.CORCR.ICA.INT.CATEG` | `CorrAcctCr_IcaIntCateg` |  |  |  |
| 31 | `IC.CORCR.ICA.TR.AC` | `CorrAcctCr_IcaTrAc` |  |  |  |
| 32 | `IC.CORCR.ICA.TR.PL` | `CorrAcctCr_IcaTrPl` |  |  |  |
| 33 | `IC.CORCR.ICA.MAIN.INT` | `CorrAcctCr_IcaMainInt` |  |  |  |
| 34 | `IC.CORCR.ICA.SUB.INT` | `CorrAcctCr_IcaSubInt` |  |  |  |
| 35 | `IC.CORCR.RESERVED.1` | `CorrAcctCr_Reserved1` | TField |  |  |
| 36 | `IC.CORCR.RESERVED.2` | `CorrAcctCr_Reserved2` | TField |  |  |
| 37 | `IC.CORCR.RESERVED.3` | `CorrAcctCr_Reserved3` | TField |  |  |
| 38 | `IC.CORCR.RESERVED.4` | `CorrAcctCr_Reserved4` | TField |  |  |
| 39 | `IC.CORCR.CR.MIN.VALUE` | `CorrAcctCr_CrMinValue` | TField |  | Indicates that the minimum amount of credit interest has been applied. If the calculated amount of interest was less than the minimum value then this will be applied, assuming that the amount is not to be waived. |
| 40 | `IC.CORCR.CR.MIN.WAIVE` | `CorrAcctCr_CrMinWaive` | TField |  | Indicates whether credit interest is set to zero if it is less than the minimum value. Set to "YES" is interest below the minimum value is to be waived. |
| 41 | `IC.CORCR.UNADJ.TOTAL.INT` | `CorrAcctCr_UnadjTotalInt` | TField |  | The calculated total interest amount, this will differ from the total interest that is posted when a manual interest adjustment has been made. |
| 42 | `IC.CORCR.INT.POST.DATE` | `CorrAcctCr_IntPostDate` | TField |  | The date that interest was posted to the account |
| 43 | `IC.CORCR.TAX.EXCH.RATE` | `CorrAcctCr_TaxExchRate` | TField |  | The exchange rate used when tax was calculated for this account. |
| 44 | `IC.CORCR.MANUAL.ADJ.AMT` | `CorrAcctCr_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 45 | `IC.CORCR.CORRECTION.ID` | `CorrAcctCr_CorrectionId` |  |  |  |
| 46 | `IC.CORCR.ADJ.INT.AMT` | `CorrAcctCr_AdjIntAmt` |  |  |  |
| 47 | `IC.CORCR.ADJ.TAX.AMT` | `CorrAcctCr_AdjTaxAmt` |  |  |  |
| 48 | `IC.CORCR.WITHHELD.INT.AMT` | `CorrAcctCr_WithheldIntAmt` |  |  |  |
| 49 | `IC.CORCR.DB.NETTING.AMT` | `CorrAcctCr_DbNettingAmt` | TField |  | This field will be updated if CR interest is netted with corresponding DR interest. |
| 50 | `IC.CORCR.CORRECTION.DATE` | `CorrAcctCr_CorrectionDate` | TField |  | This field will contain the period end date of the current capitalisation period. |
| 51 | `IC.CORCR.WAIVE.AMT` | `CorrAcctCr_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 52 | `IC.CORCR.WAIVE.RATE` | `CorrAcctCr_WaiveRate` | TField |  |  |
| 53 | `IC.CORCR.RESERVED.03` | `CorrAcctCr_Reserved03` | TField |  |  |
| 54 | `IC.CORCR.RESERVED.02` | `CorrAcctCr_Reserved02` | TField |  |  |
| 55 | `IC.CORCR.RESERVED.01` | `CorrAcctCr_Reserved01` | TField |  |  |
