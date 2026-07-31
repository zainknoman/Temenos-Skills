# ACCR.ACCT.CR2 — Table Schema

> Source: `INSERTS/I_F.ACCR.ACCT.CR2` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.ACRC2.PERIOD.FIRST.DATE` | `AccrAcctCr2_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the last credit 2 interest application (Capitalisation) as stored in the CAP.DATE.C2.INT field in the ACCOUNT record. Validation Rules: 9 date characters DD MMM YYYY. |
| 2 | `IC.ACRC2.PERIOD.LAST.DATE` | `AccrAcctCr2_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the ACCOUNT up to and including the last end of day processing. The calculation includes all balances from the day after the last credit 2 interest capitalisation, as stored in the ACCOUNT record (in the CAP.DATE.C2.INT field) up to and including the monthend accrual date specified in the MTH.END.UPTO.DAY in the ACCOUNT.ACCRUAL file. Validation Rules: 9 date characters DD MMM YYYY. |
| 3 | `IC.ACRC2.CR2.INT.DATE` | `AccrAcctCr2_Cr2IntDate` |  |  |  |
| 4 | `IC.ACRC2.CR2.NO.OF.DAYS` | `AccrAcctCr2_Cr2NoOfDays` |  |  |  |
| 5 | `IC.ACRC2.CR2.VAL.BALANCE` | `AccrAcctCr2_Cr2ValBalance` |  |  |  |
| 6 | `IC.ACRC2.CR2.INT.RATE` | `AccrAcctCr2_Cr2IntRate` |  |  |  |
| 7 | `IC.ACRC2.CR2.INT.AMT` | `AccrAcctCr2_Cr2IntAmt` |  |  |  |
| 8 | `IC.ACRC2.CR2.INT.CATEG` | `AccrAcctCr2_Cr2IntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when credit 2 interest is accrued. Validation Rules: 4 or 5 numeric characters. |
| 9 | `IC.ACRC2.CR2.INT.TR.AC` | `AccrAcctCr2_Cr2IntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when credit 2 interest is capitalisaed. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 10 | `IC.ACRC2.CR2.INT.TR.PL` | `AccrAcctCr2_Cr2IntTrPl` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated when credit 2 interest is accrued. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.ACRC2.C2.INT.TAX.CODE` | `AccrAcctCr2_C2IntTaxCode` |  |  |  |
| 12 | `IC.ACRC2.C2.INT.TAX.RATE` | `AccrAcctCr2_C2IntTaxRate` |  |  |  |
| 13 | `IC.ACRC2.C2.INT.TAX.AMT` | `AccrAcctCr2_C2IntTaxAmt` |  |  |  |
| 14 | `IC.ACRC2.C2.INT.TAXCATEG` | `AccrAcctCr2_C2IntTaxcateg` |  |  |  |
| 15 | `IC.ACRC2.C2.INT.TAXTRSDR` | `AccrAcctCr2_C2IntTaxtrsdr` |  |  |  |
| 16 | `IC.ACRC2.C2.INT.TAXTRSCR` | `AccrAcctCr2_C2IntTaxtrscr` |  |  |  |
| 17 | `IC.ACRC2.LIQUIDITY.ACCOUNT` | `AccrAcctCr2_LiquidityAccount` | TField |  | Where Interest and charges are to be passed to an alternative Account, the number of the alternative Account is shown by this field. Validation Rules: Standard account format. |
| 18 | `IC.ACRC2.COMPENS.ACCOUNT` | `AccrAcctCr2_CompensAccount` |  |  |  |
| 19 | `IC.ACRC2.INT.NO.BOOKING` | `AccrAcctCr2_IntNoBooking` | TField |  | If interest and charges are to be calculated for information purposes only and not passed to the account or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit and Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the ACCOUNT record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 20 | `IC.ACRC2.TOTAL.INTEREST` | `AccrAcctCr2_TotalInterest` | TField |  | Total amount of Interest before Tax has been deducted. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.ACRC2.TAX.FOR.CUSTOMER` | `AccrAcctCr2_TaxForCustomer` | TField |  | Not used in ACCR.ACCT.CR2 records. Validation Rules: Null. |
| 22 | `IC.ACRC2.TAX.FOR.BANK` | `AccrAcctCr2_TaxForBank` | TField |  | Not used in ACCR.ACCT.CR2 records. Validation Rules: Null. |
| 23 | `IC.ACRC2.GRAND.TOTAL` | `AccrAcctCr2_GrandTotal` | TField |  | Total interest accrued since last capitalisation. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 24 | `IC.ACRC2.CORRECTION.NUMBER` | `AccrAcctCr2_CorrectionNumber` | TField |  | Not used in ACCR.ACCT.CR2 records. Validation Rules: Null. |
| 25 | `IC.ACRC2.LIQUIDITY.CCY` | `AccrAcctCr2_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) characters or 1-3 numeric characters. |
| 26 | `IC.ACRC2.ICA.POST.INTEREST` | `AccrAcctCr2_IcaPostInterest` | TField |  | Not used in ACCR.ACCT.CR2 records. Validation Rules: Null. |
| 27 | `IC.ACRC2.ICA.MAIN.ACCT` | `AccrAcctCr2_IcaMainAcct` |  |  |  |
| 28 | `IC.ACRC2.ICA.DIST.RATIO` | `AccrAcctCr2_IcaDistRatio` |  |  |  |
| 29 | `IC.ACRC2.ICA.DIST.TYPE` | `AccrAcctCr2_IcaDistType` |  |  |  |
| 30 | `IC.ACRC2.ICA.INT.CATEG` | `AccrAcctCr2_IcaIntCateg` |  |  |  |
| 31 | `IC.ACRC2.ICA.TR.AC` | `AccrAcctCr2_IcaTrAc` |  |  |  |
| 32 | `IC.ACRC2.ICA.TR.PL` | `AccrAcctCr2_IcaTrPl` |  |  |  |
| 33 | `IC.ACRC2.ICA.MAIN.INT` | `AccrAcctCr2_IcaMainInt` |  |  |  |
| 34 | `IC.ACRC2.ICA.SUB.INT` | `AccrAcctCr2_IcaSubInt` |  |  |  |
| 35 | `IC.ACRC2.RESERVED.1` | `AccrAcctCr2_Reserved1` | TField |  |  |
| 36 | `IC.ACRC2.RESERVED.2` | `AccrAcctCr2_Reserved2` | TField |  |  |
| 37 | `IC.ACRC2.RESERVED.3` | `AccrAcctCr2_Reserved3` | TField |  |  |
| 38 | `IC.ACRC2.RESERVED.4` | `AccrAcctCr2_Reserved4` | TField |  |  |
| 39 | `IC.ACRC2.CR2.MIN.VALUE` | `AccrAcctCr2_Cr2MinValue` | TField |  | If relevant the minimum amount of credit 2 interest to apply if the calculated amount of interest is less than the minimum value and CR.MIN.WAIVE is not set to "YES". |
| 40 | `IC.ACRC2.CR2.MIN.WAIVE` | `AccrAcctCr2_Cr2MinWaive` | TField |  | If set to "YES" and the amount of interest calculated is less than the CR2.MIN.VALUE then no interest will be booked. |
| 41 | `IC.ACRC2.UNADJ.TOTAL.INT` | `AccrAcctCr2_UnadjTotalInt` | TField |  | The calculated amount of accrued interest. THis can be different from the total amount of interest if there has been a manual adjustment. For example if interest has already been booked in another system prior to take on. |
| 42 | `IC.ACRC2.INT.POST.DATE` | `AccrAcctCr2_IntPostDate` | TField |  | The date that interest was posted, not relevant to ACCR.ACCT.CR2. |
| 43 | `IC.ACRC2.TAX.EXCH.RATE` | `AccrAcctCr2_TaxExchRate` | TField |  | Not used in ACCR.ACCT.CR2 records. Validation Rules: Null. |
| 44 | `IC.ACRC2.MANUAL.ADJ.AMT` | `AccrAcctCr2_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 45 | `IC.ACRC2.CORRECTION.ID` | `AccrAcctCr2_CorrectionId` |  |  |  |
| 46 | `IC.ACRC2.ADJ.INT.AMT` | `AccrAcctCr2_AdjIntAmt` |  |  |  |
| 47 | `IC.ACRC2.ADJ.TAX.AMT` | `AccrAcctCr2_AdjTaxAmt` |  |  |  |
| 48 | `IC.ACRC2.WITHHELD.INT.AMT` | `AccrAcctCr2_WithheldIntAmt` |  |  |  |
| 49 | `IC.ACRC2.DB.NETTING.AMT` | `AccrAcctCr2_DbNettingAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 50 | `IC.ACRC2.CORRECTION.DATE` | `AccrAcctCr2_CorrectionDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 51 | `IC.ACRC2.WAIVE.AMT` | `AccrAcctCr2_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 52 | `IC.ACRC2.WAIVE.RATE` | `AccrAcctCr2_WaiveRate` | TField |  |  |
| 53 | `IC.ACRC2.RESERVED.03` | `AccrAcctCr2_Reserved03` | TField |  |  |
| 54 | `IC.ACRC2.RESERVED.02` | `AccrAcctCr2_Reserved02` | TField |  |  |
| 55 | `IC.ACRC2.RESERVED.01` | `AccrAcctCr2_Reserved01` | TField |  |  |
