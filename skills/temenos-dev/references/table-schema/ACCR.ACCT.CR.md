# ACCR.ACCT.CR — Table Schema

> Source: `INSERTS/I_F.ACCR.ACCT.CR` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.ACRCR.PERIOD.FIRST.DATE` | `AccrAcctCr_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the last credit interest application (Capitalisation) as stored in the CAP.DATE.CR.INT field in the ACCOUNT record. Validation Rules: 9 date characters DD MMM YYYY. |
| 2 | `IC.ACRCR.PERIOD.LAST.DATE` | `AccrAcctCr_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the ACCOUNT up to and including the last end of day processing. The calculation includes all balances from the day after the last credit interest capitalisation, as stored in the ACCOUNT record (in the CAP.DATE.CR.INT field) up to and including the month end accrual date specified in the MTH.END.UPTO.DAY field in the ACCOUNT.ACCRUAL file. Validation Rules: 9 date characters DD MMM YYYY. |
| 3 | `IC.ACRCR.CR.INT.DATE` | `AccrAcctCr_CrIntDate` |  |  |  |
| 4 | `IC.ACRCR.CR.NO.OF.DAYS` | `AccrAcctCr_CrNoOfDays` |  |  |  |
| 5 | `IC.ACRCR.CR.VAL.BALANCE` | `AccrAcctCr_CrValBalance` |  |  |  |
| 6 | `IC.ACRCR.CR.INT.RATE` | `AccrAcctCr_CrIntRate` |  |  |  |
| 7 | `IC.ACRCR.CR.INT.AMT` | `AccrAcctCr_CrIntAmt` |  |  |  |
| 8 | `IC.ACRCR.CR.INT.CATEG` | `AccrAcctCr_CrIntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when credit interest is accrued. Validation Rules: 4 or 5 numeric characters. |
| 9 | `IC.ACRCR.CR.INT.TR.AC` | `AccrAcctCr_CrIntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when credit interest is capitalised. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 10 | `IC.ACRCR.CR.INT.TR.PL` | `AccrAcctCr_CrIntTrPl` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated when credit interest is accrued. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.ACRCR.CR.INT.TAX.CODE` | `AccrAcctCr_CrIntTaxCode` |  |  |  |
| 12 | `IC.ACRCR.CR.INT.TAX.RATE` | `AccrAcctCr_CrIntTaxRate` |  |  |  |
| 13 | `IC.ACRCR.CR.INT.TAX.AMT` | `AccrAcctCr_CrIntTaxAmt` |  |  |  |
| 14 | `IC.ACRCR.CR.INT.TAXCATEG` | `AccrAcctCr_CrIntTaxcateg` |  |  |  |
| 15 | `IC.ACRCR.CR.INT.TAXTRSDR` | `AccrAcctCr_CrIntTaxtrsdr` |  |  |  |
| 16 | `IC.ACRCR.CR.INT.TAXTRSCR` | `AccrAcctCr_CrIntTaxtrscr` |  |  |  |
| 17 | `IC.ACRCR.LIQUIDITY.ACCOUNT` | `AccrAcctCr_LiquidityAccount` | TField |  | Where Credit Interest is to be passed to an alternative ACCOUNT, the number of the ACCOUNT is shown by this field. Validation Rules: Standard account format. |
| 18 | `IC.ACRCR.COMPENS.ACCOUNT` | `AccrAcctCr_CompensAccount` |  |  |  |
| 19 | `IC.ACRCR.INT.NO.BOOKING` | `AccrAcctCr_IntNoBooking` | TField |  | If credit interest is to be calculated for information purposes only and not passed to the account or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit and Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the Account record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 20 | `IC.ACRCR.TOTAL.INTEREST` | `AccrAcctCr_TotalInterest` | TField |  | Total amount of Interest calculated. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.ACRCR.TAX.FOR.CUSTOMER` | `AccrAcctCr_TaxForCustomer` | TField |  | Not used in ACCR.ACCT.CR records. Validation Rules: Null. |
| 22 | `IC.ACRCR.TAX.FOR.BANK` | `AccrAcctCr_TaxForBank` | TField |  | Not used in ACCR.ACCT.CR records. Validation Rules: Null. |
| 23 | `IC.ACRCR.GRAND.TOTAL` | `AccrAcctCr_GrandTotal` | TField |  | Total interest accrued since last capitalisation. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 24 | `IC.ACRCR.CORRECTION.NUMBER` | `AccrAcctCr_CorrectionNumber` | TField |  | Not relevant to accruals, included to maintain compatability witht eh CORR.ACCT.CR and STMT.ACCT.CR tables |
| 25 | `IC.ACRCR.LIQUIDITY.CCY` | `AccrAcctCr_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) characters or 1-3 numeric characters. |
| 26 | `IC.ACRCR.ICA.POST.INTEREST` | `AccrAcctCr_IcaPostInterest` | TField |  | ICA (Interest compansation account hiearchy_ interest is not accrued so not relevant to this table. Field present to maintatin compatibilty with STMT.ACCT.CR and CORR.ACCT.CR. |
| 27 | `IC.ACRCR.ICA.MAIN.ACCT` | `AccrAcctCr_IcaMainAcct` |  |  |  |
| 28 | `IC.ACRCR.ICA.DIST.TYPE` | `AccrAcctCr_IcaDistType` |  |  |  |
| 29 | `IC.ACRCR.ICA.DIST.RATIO` | `AccrAcctCr_IcaDistRatio` |  |  |  |
| 30 | `IC.ACRCR.ICA.INT.CATEG` | `AccrAcctCr_IcaIntCateg` |  |  |  |
| 31 | `IC.ACRCR.ICA.TR.AC` | `AccrAcctCr_IcaTrAc` |  |  |  |
| 32 | `IC.ACRCR.ICA.TR.PL` | `AccrAcctCr_IcaTrPl` |  |  |  |
| 33 | `IC.ACRCR.ICA.MAIN.INT` | `AccrAcctCr_IcaMainInt` |  |  |  |
| 34 | `IC.ACRCR.ICA.SUB.INT` | `AccrAcctCr_IcaSubInt` |  |  |  |
| 35 | `IC.ACRCR.RESERVED.1` | `AccrAcctCr_Reserved1` | TField |  |  |
| 36 | `IC.ACRCR.RESERVED.2` | `AccrAcctCr_Reserved2` | TField |  |  |
| 37 | `IC.ACRCR.RESERVED.3` | `AccrAcctCr_Reserved3` | TField |  |  |
| 38 | `IC.ACRCR.RESERVED.4` | `AccrAcctCr_Reserved4` | TField |  |  |
| 39 | `IC.ACRCR.CR.MIN.VALUE` | `AccrAcctCr_CrMinValue` | TField |  | Indicates that the minimum amount of credit interest has been applied. If the calculated amount of interest was less than the minimum value then this will be applied, assuming that the amount is not to be waived. |
| 40 | `IC.ACRCR.CR.MIN.WAIVE` | `AccrAcctCr_CrMinWaive` | TField |  | Indicates whether credit interest is set to zero if it is less than the minimum value. Set to "YES" is interest below the minimum value is to be waived. |
| 41 | `IC.ACRCR.UNADJ.TOTAL.INT` | `AccrAcctCr_UnadjTotalInt` | TField |  | The unadjusted calculated total interest amount. |
| 42 | `IC.ACRCR.INT.POST.DATE` | `AccrAcctCr_IntPostDate` | TField |  | Not relevant to account interest accruals, field is persent to provide compatibilty with CORR.ACCT.CR and ACCR.ACCT.CR tables. |
| 43 | `IC.ACRCR.TAX.EXCH.RATE` | `AccrAcctCr_TaxExchRate` | TField |  | Not used in ACCR.ACCT.CR records. Validation Rules: Null. |
| 44 | `IC.ACRCR.MANUAL.ADJ.AMT` | `AccrAcctCr_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 45 | `IC.ACRCR.CORRECTION.ID` | `AccrAcctCr_CorrectionId` |  |  |  |
| 46 | `IC.ACRCR.ADJ.INT.AMT` | `AccrAcctCr_AdjIntAmt` |  |  |  |
| 47 | `IC.ACRCR.ADJ.TAX.AMT` | `AccrAcctCr_AdjTaxAmt` |  |  |  |
| 48 | `IC.ACRCR.WITHHELD.INT.AMT` | `AccrAcctCr_WithheldIntAmt` |  |  |  |
| 49 | `IC.ACRCR.DB.NETTING.AMT` | `AccrAcctCr_DbNettingAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 50 | `IC.ACRCR.CORRECTION.DATE` | `AccrAcctCr_CorrectionDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 51 | `IC.ACRCR.WAIVE.AMT` | `AccrAcctCr_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 52 | `IC.ACRCR.WAIVE.RATE` | `AccrAcctCr_WaiveRate` | TField |  |  |
| 53 | `IC.ACRCR.RESERVED.03` | `AccrAcctCr_Reserved03` | TField |  |  |
| 54 | `IC.ACRCR.RESERVED.02` | `AccrAcctCr_Reserved02` | TField |  |  |
| 55 | `IC.ACRCR.RESERVED.01` | `AccrAcctCr_Reserved01` | TField |  |  |
