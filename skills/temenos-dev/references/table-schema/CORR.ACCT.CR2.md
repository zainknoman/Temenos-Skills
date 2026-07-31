# CORR.ACCT.CR2 — Table Schema

> Source: `INSERTS/I_F.CORR.ACCT.CR2` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.CORC2.PERIOD.FIRST.DATE` | `CorrAcctCr2_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the previous credit 2 interest application (Capitalisation) as stored in the CAP.DATE.CR2.INT field in the ACCOUNT record. Validation Rules: Standard account format. |
| 2 | `IC.CORC2.PERIOD.LAST.DATE` | `CorrAcctCr2_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the ACCOUNT up to and including the day on which the interest capitalisation is processed. The calculation includes all balances from the day after the previous credit 2 interest capitalisation, as stored in the ACCOUNT record (in the CAP.DATE.CR2.INT field) up to the capitalisation date specified, or, if the LAST.DAY.INCLUSIVE field in the ACCOUNT.ACCRUAL file contains 'NO', up to the working day prior to the processing date. Validation Rules: 9 date characters - DD MMM YYYY. |
| 3 | `IC.CORC2.CR2.INT.DATE` | `CorrAcctCr2_Cr2IntDate` |  |  |  |
| 4 | `IC.CORC2.CR2.NO.OF.DAYS` | `CorrAcctCr2_Cr2NoOfDays` |  |  |  |
| 5 | `IC.CORC2.CR2.VAL.BALANCE` | `CorrAcctCr2_Cr2ValBalance` |  |  |  |
| 6 | `IC.CORC2.CR2.INT.RATE` | `CorrAcctCr2_Cr2IntRate` |  |  |  |
| 7 | `IC.CORC2.CR2.INT.AMT` | `CorrAcctCr2_Cr2IntAmt` |  |  |  |
| 8 | `IC.CORC2.CR2.INT.CATEG` | `CorrAcctCr2_Cr2IntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when credit 2 interest is accrued. Validation Rules: 4 or 5 numeric characters. |
| 9 | `IC.CORC2.CR2.INT.TR.AC` | `CorrAcctCr2_Cr2IntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when credit 2 interest is capitalisaed. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 10 | `IC.CORC2.CR2.INT.TR.PL` | `CorrAcctCr2_Cr2IntTrPl` | TField |  | Identifies the P&amp;L category code to be assigned to Account entries generated when credit 2 interest is capitalisaed. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.CORC2.C2.INT.TAX.CODE` | `CorrAcctCr2_C2IntTaxCode` |  |  |  |
| 12 | `IC.CORC2.C2.INT.TAX.RATE` | `CorrAcctCr2_C2IntTaxRate` |  |  |  |
| 13 | `IC.CORC2.C2.INT.TAX.AMT` | `CorrAcctCr2_C2IntTaxAmt` |  |  |  |
| 14 | `IC.CORC2.C2.INT.TAXCATEG` | `CorrAcctCr2_C2IntTaxcateg` |  |  |  |
| 15 | `IC.CORC2.C2.INT.TAXTRSDR` | `CorrAcctCr2_C2IntTaxtrsdr` |  |  |  |
| 16 | `IC.CORC2.C2.INT.TAXTRSCR` | `CorrAcctCr2_C2IntTaxtrscr` |  |  |  |
| 17 | `IC.CORC2.LIQUIDITY.ACCOUNT` | `CorrAcctCr2_LiquidityAccount` | TField |  | Where Interest and charges are to be passed to an alternative Account, the number of the alternative Account is shown by this field. Validation Rules: Standard account format. |
| 18 | `IC.CORC2.COMPENS.ACCOUNT` | `CorrAcctCr2_CompensAccount` |  |  |  |
| 19 | `IC.CORC2.INT.NO.BOOKING` | `CorrAcctCr2_IntNoBooking` | TField |  | If interest and charges are to be calculated for information purposes only and not passed to the account or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit and Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the ACCOUNT record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 20 | `IC.CORC2.TOTAL.INTEREST` | `CorrAcctCr2_TotalInterest` | TField |  | Total amount of Interest before Tax has been deducted. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.CORC2.TAX.FOR.CUSTOMER` | `CorrAcctCr2_TaxForCustomer` | TField |  | Amount of Tax deducted from the credit 2 interest due to the Customer, if applicable. Where Tax is payable on credit interest, the interest rate may be quoted 'Gross' (before deduction of Tax) or 'Net' (after deduction of Tax). This is determined by the TAX.OPERAND field in the applicable TAX record. If the TAX.OPERAND contains 'MINUS', the interest rate is quoted 'Gross' and the Tax amount in this field is payable by the Customer. If the TAX.OPERAND contains 'PLUS', the interest rate is quoted 'Net' and the Tax amount in the next field is payable by the Bank. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 22 | `IC.CORC2.TAX.FOR.BANK` | `CorrAcctCr2_TaxForBank` | TField |  | Amount of Tax to be paid by the Bank on behalf of the Customer, if applicable. Where Tax is payable on credit interest, the interest rate may be quoted 'Gross' (before deduction of Tax) or 'Net' (after deduction of Tax). This is determined by the TAX.OPERAND field in the applicable TAX record. If the TAX.OPERAND contains 'MINUS', the interest rate is quoted 'Gross' and the Tax amount in the previous field is payable by the Customer. If the TAX.OPERAND contains 'PLUS', the interest rate is quoted 'Net' and the Tax amount in this field is payable by the Bank. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 23 | `IC.CORC2.GRAND.TOTAL` | `CorrAcctCr2_GrandTotal` | TField |  | Total interest to be credited to the customer's account after deduction of Tax (if applicable). Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 24 | `IC.CORC2.CORRECTION.NUMBER` | `CorrAcctCr2_CorrectionNumber` | TField |  | Incremented each time an interest correction takes place |
| 25 | `IC.CORC2.LIQUIDITY.CCY` | `CorrAcctCr2_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) characters or 1-3 numeric characters. |
| 26 | `IC.CORC2.ICA.POST.INTEREST` | `CorrAcctCr2_IcaPostInterest` | TField |  | Indicates whether ICA interest is actually posted to this account, or is just calculated for information purposes. |
| 27 | `IC.CORC2.ICA.MAIN.ACCT` | `CorrAcctCr2_IcaMainAcct` |  |  |  |
| 28 | `IC.CORC2.ICA.DIST.RATIO` | `CorrAcctCr2_IcaDistRatio` |  |  |  |
| 29 | `IC.CORC2.ICA.DIST.TYPE` | `CorrAcctCr2_IcaDistType` |  |  |  |
| 30 | `IC.CORC2.ICA.INT.CATEG` | `CorrAcctCr2_IcaIntCateg` |  |  |  |
| 31 | `IC.CORC2.ICA.TR.AC` | `CorrAcctCr2_IcaTrAc` |  |  |  |
| 32 | `IC.CORC2.ICA.TR.PL` | `CorrAcctCr2_IcaTrPl` |  |  |  |
| 33 | `IC.CORC2.ICA.MAIN.INT` | `CorrAcctCr2_IcaMainInt` |  |  |  |
| 34 | `IC.CORC2.ICA.SUB.INT` | `CorrAcctCr2_IcaSubInt` |  |  |  |
| 35 | `IC.CORC2.RESERVED.1` | `CorrAcctCr2_Reserved1` | TField |  |  |
| 36 | `IC.CORC2.RESERVED.2` | `CorrAcctCr2_Reserved2` | TField |  |  |
| 37 | `IC.CORC2.RESERVED.3` | `CorrAcctCr2_Reserved3` | TField |  |  |
| 38 | `IC.CORC2.RESERVED.4` | `CorrAcctCr2_Reserved4` | TField |  |  |
| 39 | `IC.CORC2.CR2.MIN.VALUE` | `CorrAcctCr2_Cr2MinValue` | TField |  | Indicates that the minimum amount of credit interest has been applied. If the calculated amount of interest was less than the minimum value then this will be applied, assuming that the amount is not to be waived. |
| 40 | `IC.CORC2.CR2.MIN.WAIVE` | `CorrAcctCr2_Cr2MinWaive` | TField |  | Indicates whether credit interest is set to zero if it is less than the minimum value. Set to "YES" is interest below the minimum value is to be waived. |
| 41 | `IC.CORC2.UNADJ.TOTAL.INT` | `CorrAcctCr2_UnadjTotalInt` | TField |  | The calculated total interest amount, this will differ from the total interest that is posted when a manual interest adjustment has been made. |
| 42 | `IC.CORC2.INT.POST.DATE` | `CorrAcctCr2_IntPostDate` | TField |  | The date that interest was posted to the account. |
| 43 | `IC.CORC2.TAX.EXCH.RATE` | `CorrAcctCr2_TaxExchRate` | TField |  | The exchange rate used when tax was calculated for this account. |
| 44 | `IC.CORC2.MANUAL.ADJ.AMT` | `CorrAcctCr2_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 45 | `IC.CORC2.CORRECTION.ID` | `CorrAcctCr2_CorrectionId` |  |  |  |
| 46 | `IC.CORC2.ADJ.INT.AMT` | `CorrAcctCr2_AdjIntAmt` |  |  |  |
| 47 | `IC.CORC2.ADJ.TAX.AMT` | `CorrAcctCr2_AdjTaxAmt` |  |  |  |
| 48 | `IC.CORC2.WITHHELD.INT.AMT` | `CorrAcctCr2_WithheldIntAmt` |  |  |  |
| 49 | `IC.CORC2.DB.NETTING.AMT` | `CorrAcctCr2_DbNettingAmt` | TField |  | This field will be updated if CR interest is netted with corresponding DR interest. |
| 50 | `IC.CORC2.CORRECTION.DATE` | `CorrAcctCr2_CorrectionDate` | TField |  | This field will contain the period end date of the current capitalisation period. |
| 51 | `IC.CORC2.WAIVE.AMT` | `CorrAcctCr2_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 52 | `IC.CORC2.WAIVE.RATE` | `CorrAcctCr2_WaiveRate` | TField |  |  |
| 53 | `IC.CORC2.RESERVED.03` | `CorrAcctCr2_Reserved03` | TField |  |  |
| 54 | `IC.CORC2.RESERVED.02` | `CorrAcctCr2_Reserved02` | TField |  |  |
| 55 | `IC.CORC2.RESERVED.01` | `CorrAcctCr2_Reserved01` | TField |  |  |
