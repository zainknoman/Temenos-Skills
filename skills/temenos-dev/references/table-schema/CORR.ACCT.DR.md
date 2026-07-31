# CORR.ACCT.DR — Table Schema

> Source: `INSERTS/I_F.CORR.ACCT.DR` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.CORDR.PERIOD.FIRST.DATE` | `CorrAcctDr_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the previous debit interest application (Capitalisation) as stored in the CAP.DATE.DR.INT field in the ACCOUNT record. Validation Rules: 9 date characters - DD MMM YYYY. |
| 2 | `IC.CORDR.PERIOD.LAST.DATE` | `CorrAcctDr_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the Account up to and including the last end of day processing. The calculation includes all balances from the day after the last debit interest capitalisation, as stored in the ACCOUNT record (in the CAP.DATE.DR.INT field) up to the capitalisation date specified, or, if the LAST.DAY.INCLUSIVE field in the ACCOUNT.ACCRUAL file contains 'NO', up to the working day prior to the processing date. Validation Rules: 9 date characters - DD MMM YYYY. |
| 3 | `IC.CORDR.DR.INT.DATE` | `CorrAcctDr_DrIntDate` |  |  |  |
| 4 | `IC.CORDR.DR.NO.OF.DAYS` | `CorrAcctDr_DrNoOfDays` |  |  |  |
| 5 | `IC.CORDR.DR.VAL.BALANCE` | `CorrAcctDr_DrValBalance` |  |  |  |
| 6 | `IC.CORDR.DR.INT.RATE` | `CorrAcctDr_DrIntRate` |  |  |  |
| 7 | `IC.CORDR.UNADJ.DR.INT` | `CorrAcctDr_UnadjDrInt` |  |  |  |
| 8 | `IC.CORDR.DR.INT.AMT` | `CorrAcctDr_DrIntAmt` |  |  |  |
| 9 | `IC.CORDR.DR.INT.CATEG` | `CorrAcctDr_DrIntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when debit interest is accrued. Validation Rules: 4 or 5 numeric characters. |
| 10 | `IC.CORDR.DR.INT.TR.AC` | `CorrAcctDr_DrIntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when debit interest is capitalised. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.CORDR.DR.INT.TR.PL` | `CorrAcctDr_DrIntTrPl` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated when debit interest is accrued. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 12 | `IC.CORDR.DR.INT.TAX.CODE` | `CorrAcctDr_DrIntTaxCode` |  |  |  |
| 13 | `IC.CORDR.DR.INT.TAX.RATE` | `CorrAcctDr_DrIntTaxRate` |  |  |  |
| 14 | `IC.CORDR.DR.INT.TAX.AMT` | `CorrAcctDr_DrIntTaxAmt` |  |  |  |
| 15 | `IC.CORDR.DR.INT.TAXCATEG` | `CorrAcctDr_DrIntTaxcateg` |  |  |  |
| 16 | `IC.CORDR.DR.INT.TAXTRSDR` | `CorrAcctDr_DrIntTaxtrsdr` |  |  |  |
| 17 | `IC.CORDR.DR.INT.TAXTRSCR` | `CorrAcctDr_DrIntTaxtrscr` |  |  |  |
| 18 | `IC.CORDR.INT.ADDON.CODE` | `CorrAcctDr_IntAddonCode` | TField |  | Where a Debit Interest Add-on charge is to be made on an Account, this code specifies the DEBIT.INT.ADDON record containing details of the calculation and processing of Interest Add-on charge. The Debit Interest Add-on charge is calculated as a percentage of the total value of Debit Interest shown in all occurrences of multivalue field DR.INT.AMT. The Debit Interest Add-on charge details used are those applicable on the capitalisation date. Validation Rules: 1-2 numeric characters. |
| 19 | `IC.CORDR.INT.ADDON.PERCT` | `CorrAcctDr_IntAddonPerct` | TField |  | Shows the Percentage applied to the Debit Interest amount to calculate the Debit Interest Add-on charge. Validation Rules: Up to 10 numeric characters plus a decimal point. Up to 6 integers. Up to 9 decimals. Standard rate format. |
| 20 | `IC.CORDR.INT.ADDON.FREE` | `CorrAcctDr_IntAddonFree` | TField |  | Shows the free amount deducted from the calculated interest add-on charge, if applicable. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.CORDR.ADDON.MIN.MAX` | `CorrAcctDr_AddonMinMax` | TField |  | After calculating the gross Debit Interest Add-on charge and subtracting the Free Amount, comparison is made with Minimum and Maximum charge amounts from the Debit Interest Addon record. If either the Minimum charge or the Maximum charge is substituted for the calculated charge, 'MINIMUM' or 'MAXIMUM' is recorded in this field. Validation Rules: 'MINIMUM', 'MAXIMUM' or nothing. |
| 22 | `IC.CORDR.UNADJ.INT.ADDON` | `CorrAcctDr_UnadjIntAddon` | TField |  | This field holds the unadjusted Debit Interest Addon amount when an adjustment relating to the Maximum Legal Rate is needed. This is used to store the actual Debit Interest Addon charge when differs from the applied Debit Interest Add-on charge. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 23 | `IC.CORDR.INT.ADDON.AMT` | `CorrAcctDr_IntAddonAmt` | TField |  | Shows the calculated Debit Interest Add-on Charge after Minimum or Maximum adjustment if appropriate. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 24 | `IC.CORDR.INT.ADDON.CATEG` | `CorrAcctDr_IntAddonCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Debit Interest Add-on charges. Validation Rules: 4 or 5 numeric characters. |
| 25 | `IC.CORDR.INT.ADDON.TRSDR` | `CorrAcctDr_IntAddonTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Debit Interest Add-on charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 26 | `IC.CORDR.INT.ADDON.TRSCR` | `CorrAcctDr_IntAddonTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Debit Interest Add-on charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 27 | `IC.CORDR.ADDON.TAX.CODE` | `CorrAcctDr_AddonTaxCode` | TField |  | Specifies the TAX record containing details of the calculation and processing of Tax applicable to the Debit Interest Add-on charge. The tax details used are those applicable on the capitalisation date. Validation Rules: Up to 2 numeric characters. |
| 28 | `IC.CORDR.ADDON.TAX.RATE` | `CorrAcctDr_AddonTaxRate` |  |  |  |
| 29 | `IC.CORDR.ADDON.TAX.AMT` | `CorrAcctDr_AddonTaxAmt` |  |  |  |
| 30 | `IC.CORDR.ADDON.TAXCATEG` | `CorrAcctDr_AddonTaxcateg` |  |  |  |
| 31 | `IC.CORDR.ADDON.TAXTRSDR` | `CorrAcctDr_AddonTaxtrsdr` |  |  |  |
| 32 | `IC.CORDR.ADDON.TAXTRSCR` | `CorrAcctDr_AddonTaxtrscr` |  |  |  |
| 33 | `IC.CORDR.GOV.MARGIN.DATE` | `CorrAcctDr_GovMarginDate` |  |  |  |
| 34 | `IC.CORDR.GV.NO.OF.DAYS` | `CorrAcctDr_GvNoOfDays` |  |  |  |
| 35 | `IC.CORDR.GV.VAL.BALANCE` | `CorrAcctDr_GvValBalance` |  |  |  |
| 36 | `IC.CORDR.GV.INT.RATE` | `CorrAcctDr_GvIntRate` |  |  |  |
| 37 | `IC.CORDR.GOV.MARGIN.AMT` | `CorrAcctDr_GovMarginAmt` |  |  |  |
| 38 | `IC.CORDR.GOV.MARGIN.CODE` | `CorrAcctDr_GovMarginCode` | TField |  | Where a Government Margin charge is to be made on an Account, this code specifies the GOVERNMENT.MARGIN record containing the details of the calculation and processing of Government Margin charges. The Government Margin charge is calculated as a percentage of the debit balance. (Shown in multivalue field GV.VAL.BALANCE). The Government Margin details used are those applicable on the capitalisation date. Validation Rules: 1-2 numeric characters. |
| 39 | `IC.CORDR.GOV.MARGIN.MIN.MAX` | `CorrAcctDr_GovMarginMinMax` | TField |  | After calculating the gross Government Margin charge, comparison is made with Minimum and Maximum charge amounts from the GOVERNMENT.MARGIN record. If either the Minimum charge or the Maximum charge is substituted for the calculated charge, 'MINIMUM' or "MAXIMUM' is recorded in this field. Validation Rules: 'MINIMUM', 'MAXIMUM' or nothing. |
| 40 | `IC.CORDR.GOV.MRG.TOT.AMT` | `CorrAcctDr_GovMrgTotAmt` | TField |  | Shows the total calculated Government Margin Charge. It is the sum of multivalue fields GOV.MARGIN.AMT adjusted to the Minimum or Maximum if appropriate. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 41 | `IC.CORDR.GOV.MRG.CATEG` | `CorrAcctDr_GovMrgCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Government Margin charges. Validation Rules: 4 or 5 numeric characters. |
| 42 | `IC.CORDR.GOV.MRG.TRSDR` | `CorrAcctDr_GovMrgTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Government Margin charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 43 | `IC.CORDR.GOV.MRG.TRSCR` | `CorrAcctDr_GovMrgTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Government Margin charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 44 | `IC.CORDR.HIGHEST.DR.CODE` | `CorrAcctDr_HighestDrCode` | TField |  | Where a Highest Debit charge is to be made on an Account, this code specifies the HIGHEST.DEBIT record containing details of the calculation and processing of the Highest Debit charge. The Highest Debit charge details used are those applicable on the capitalisation date. Validation Rules: 1-2 numeric characters. |
| 45 | `IC.CORDR.HIGHEST.DR.BAL` | `CorrAcctDr_HighestDrBal` | TField |  | Shows the Highest Debit Balance found during the application period and on which the Highest Debit Balance charge is based. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 46 | `IC.CORDR.HIGHEST.DR.PERC` | `CorrAcctDr_HighestDrPerc` | TField |  | Shows the Percentage applied to the Highest Debit amount to calculate the Highest Debit charge. Validation Rules: Up to 10 numeric characters plus a decimal point. Up to 6 integers. Up to 9 decimals. Standard rate format. |
| 47 | `IC.CORDR.HIGHEST.DR.FREE` | `CorrAcctDr_HighestDrFree` | TField |  | Shows the free amount by which the calculated Highest Debit charge is reduced. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 48 | `IC.CORDR.HIGH.DR.MIN.MAX` | `CorrAcctDr_HighDrMinMax` | TField |  | After calculating the gross Highest Debit charge and subtracting the Free Amount, comparison is made with Minimum and Maximum charge amounts from the Highest Debit record. If either the Minimum charge or the Maximum charge is substituted for the calculated charge, 'MINIMUM' or 'MAXIMUM' is recorded in this field. Validation Rules: 'MINIMUM', 'MAXIMUM' or nothing. |
| 49 | `IC.CORDR.UNADJ.HIGHEST.DR` | `CorrAcctDr_UnadjHighestDr` | TField |  | This field holds the unadjusted Highest Debit charge when an adjustment relating to the Maximum Legal Rate is needed. This is used to store the actual Highest Debit charge when differs from the applied Highest Debit charge. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 50 | `IC.CORDR.HIGHEST.DR.AMT` | `CorrAcctDr_HighestDrAmt` | TField |  | Shows the calculated Highest Debit Charge after Minimum or Maximum adjustment if appropriate. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 51 | `IC.CORDR.HIGH.DR.CATEG` | `CorrAcctDr_HighDrCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Highest Debit charges. Validation Rules: 4 or 5 numeric characters. |
| 52 | `IC.CORDR.HIGH.DR.TRSDR` | `CorrAcctDr_HighDrTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Highest Debit charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 53 | `IC.CORDR.HIGH.DR.TRSCR` | `CorrAcctDr_HighDrTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Highest Debit charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 54 | `IC.CORDR.HI.DR.TAX.CODE` | `CorrAcctDr_HiDrTaxCode` | TField |  | Specifies the TAX record containing details of the calculation and processing of Tax applicable to the Highest Debit charge. The tax details used are those applicable on the capitalisation date. Validation Rules: Up to 2 numeric characters. |
| 55 | `IC.CORDR.HI.DR.TAX.RATE` | `CorrAcctDr_HiDrTaxRate` |  |  |  |
| 56 | `IC.CORDR.HI.DR.TAX.AMT` | `CorrAcctDr_HiDrTaxAmt` |  |  |  |
| 57 | `IC.CORDR.HI.DR.TAXCATEG` | `CorrAcctDr_HiDrTaxcateg` |  |  |  |
| 58 | `IC.CORDR.HI.DR.TAXTRSDR` | `CorrAcctDr_HiDrTaxtrsdr` |  |  |  |
| 59 | `IC.CORDR.HI.DR.TAXTRSCR` | `CorrAcctDr_HiDrTaxtrscr` |  |  |  |
| 60 | `IC.CORDR.INT.STMT.CODE` | `CorrAcctDr_IntStmtCode` | TField |  | Where an Interest Statement charge is to be made on an Account, this code specifies the INTEREST.STATEMENT record containing details of the calculation and processing of Interest Statement charge. The Interest Statement charge details used are those applicable on the Capitalisation date. Validation Rules: 1-2 numeric characters. |
| 61 | `IC.CORDR.INT.STMT.AMT` | `CorrAcctDr_IntStmtAmt` | TField |  | Shows the Interest Statement Charge. This is a flat charge levied on each debit interest capitalisation date. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 62 | `IC.CORDR.INT.STMT.CATEG` | `CorrAcctDr_IntStmtCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Interest Statement charges. Validation Rules: 4 or 5 numeric characters. |
| 63 | `IC.CORDR.INT.STMT.TRSDR` | `CorrAcctDr_IntStmtTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Interest Statement charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 64 | `IC.CORDR.INT.STMT.TRSCR` | `CorrAcctDr_IntStmtTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Interest Statement charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 65 | `IC.CORDR.STMT.TAX.CODE` | `CorrAcctDr_StmtTaxCode` | TField |  | Specifies the TAX record containing details of the calculation and processing of Tax applicable to the Interest Statement charge. The tax details used are those applicable on the capitalisation date. Validation Rules: Up to 2 numeric characters. |
| 66 | `IC.CORDR.STMT.TAX.RATE` | `CorrAcctDr_StmtTaxRate` |  |  |  |
| 67 | `IC.CORDR.STMT.TAX.AMT` | `CorrAcctDr_StmtTaxAmt` |  |  |  |
| 68 | `IC.CORDR.STMT.TAXCATEG` | `CorrAcctDr_StmtTaxcateg` |  |  |  |
| 69 | `IC.CORDR.STMT.TAXTRSDR` | `CorrAcctDr_StmtTaxtrsdr` |  |  |  |
| 70 | `IC.CORDR.STMT.TAXTRSCR` | `CorrAcctDr_StmtTaxtrscr` |  |  |  |
| 71 | `IC.CORDR.LIQUIDITY.ACCOUNT` | `CorrAcctDr_LiquidityAccount` | TField |  | Where interest and charges are to be passed to an alternative Account, the number of the alternative ACCOUNT is shown by this field. Where interest and charges are to be passed to an alternative Account, the alternative account number should be entered in the INTEREST.LIQU.ACCT field on the original customer ACCOUNT record. Validation Rules: 2-16 numeric characters. |
| 72 | `IC.CORDR.COMPENS.ACCOUNT` | `CorrAcctDr_CompensAccount` |  |  |  |
| 73 | `IC.CORDR.INT.NO.BOOKING` | `CorrAcctDr_IntNoBooking` | TField |  | If interest and charges are to be calculated for information purposes only and not passed to the account, or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit or Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the Account record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 74 | `IC.CORDR.USED.MIDDLE.RATE` | `CorrAcctDr_UsedMiddleRate` | TField |  | The exchange rate used to convert the Account Currency into Local Currency during the Charge calculation process. Note : This is necessary where default charges specified in local currency are used. Validation Rules: Up to 10 numeric characters plus a decimal point. Up to 6 integers. Up to 9 decimals. Standard rate format. |
| 75 | `IC.CORDR.TOTAL.INTEREST` | `CorrAcctDr_TotalInterest` | TField |  | Amount of interest before Tax. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 76 | `IC.CORDR.TOTAL.CHARGE` | `CorrAcctDr_TotalCharge` | TField |  | Total of Interest Related Charges. Made up of the following: Debit Interest Add-on - a percentage of the amount of debit interest to be applied. Government Margin - an additional interest rate applied to each debit balance. Highest Debit - a percentage of the largest debit balance. Interest Statement - a charge for providing a detailed interest statement when debit interest is applied. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 77 | `IC.CORDR.TOTAL.TAX` | `CorrAcctDr_TotalTax` | TField |  | Total amount of Tax on Interest and all Charges (if applicable). Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 78 | `IC.CORDR.GRAND.TOTAL` | `CorrAcctDr_GrandTotal` | TField |  | Total amount to be debited to customer's account including debit interest, any interest related charges and tax (if applicable). Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 79 | `IC.CORDR.CORRECTION.NUMBER` | `CorrAcctDr_CorrectionNumber` | TField |  | Incremented every time an interest correction takes place |
| 80 | `IC.CORDR.APR` | `CorrAcctDr_Apr` | TField |  | This field stores the Annual Payment Rate (or the Taux Effectif Global in France). Validation Rules: 1-10 type R (standard rate format) characters plus a decimal point. |
| 81 | `IC.CORDR.DEFERRED.DATE` | `CorrAcctDr_DeferredDate` | TField |  | This field will hold the deferred application date of the debit interest in case pending debit interest processing was being performed on this account. |
| 82 | `IC.CORDR.LIQUIDITY.CCY` | `CorrAcctDr_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarally be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) characters or 1-3 numeric characters. |
| 83 | `IC.CORDR.ICA.POST.INTEREST` | `CorrAcctDr_IcaPostInterest` | TField |  | Indicates whether ICA interest is actually posted to this account, or is just calculated for information purposes. |
| 84 | `IC.CORDR.ICA.MAIN.ACCT` | `CorrAcctDr_IcaMainAcct` |  |  |  |
| 85 | `IC.CORDR.ICA.DIST.TYPE` | `CorrAcctDr_IcaDistType` |  |  |  |
| 86 | `IC.CORDR.ICA.DIST.RATIO` | `CorrAcctDr_IcaDistRatio` |  |  |  |
| 87 | `IC.CORDR.ICA.INT.CATEG` | `CorrAcctDr_IcaIntCateg` |  |  |  |
| 88 | `IC.CORDR.ICA.TR.AC` | `CorrAcctDr_IcaTrAc` |  |  |  |
| 89 | `IC.CORDR.ICA.TR.PL` | `CorrAcctDr_IcaTrPl` |  |  |  |
| 90 | `IC.CORDR.ICA.MAIN.INT` | `CorrAcctDr_IcaMainInt` |  |  |  |
| 91 | `IC.CORDR.ICA.SUB.INT` | `CorrAcctDr_IcaSubInt` |  |  |  |
| 92 | `IC.CORDR.DR.MIN.VALUE` | `CorrAcctDr_DrMinValue` | TField |  | Indicates that the minimum amount of credit interest has been applied. If the calculated amount of interest was less than the minimum value then this will be applied, assuming that the amount is not to be waived. |
| 93 | `IC.CORDR.DR.MIN.WAIVE` | `CorrAcctDr_DrMinWaive` | TField |  | Indicates whether credit interest is set to zero if it is less than the minimum value. Set to "YES" is interest below the minimum value is to be waived. |
| 94 | `IC.CORDR.UNADJ.TOTAL.INT` | `CorrAcctDr_UnadjTotalInt` | TField |  | The calculated total interest amount, this will differ from the total interest that is posted when a manual interest adjustment has been made |
| 95 | `IC.CORDR.INT.POST.DATE` | `CorrAcctDr_IntPostDate` | TField |  | The date that interest was posted to the account |
| 96 | `IC.CORDR.MANUAL.ADJ.AMT` | `CorrAcctDr_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 97 | `IC.CORDR.DEF.DR.INT` | `CorrAcctDr_DefDrInt` | TField |  | The deferred amount posted for debit interest. |
| 98 | `IC.CORDR.DEF.DR.TAX` | `CorrAcctDr_DefDrTax` | TField |  | The deferred amount posted for debit interest Tax. |
| 99 | `IC.CORDR.DEF.ADDON` | `CorrAcctDr_DefAddon` | TField |  | The deferred amount posted for deferred debit interest addon charge. |
| 100 | `IC.CORDR.DEF.ADDON.TAX` | `CorrAcctDr_DefAddonTax` | TField |  | The deferred amount posted for deferred debit interest addon charge Tax. |
| 101 | `IC.CORDR.DEF.HIGH.DR` | `CorrAcctDr_DefHighDr` | TField |  | The deferred amount posted for highest debit charge. |
| 102 | `IC.CORDR.DEF.HIGH.DR.TAX` | `CorrAcctDr_DefHighDrTax` | TField |  | The deferred amount posted for highest debit charge Tax. |
| 103 | `IC.CORDR.DEF.GOV.MAR` | `CorrAcctDr_DefGovMar` | TField |  | The deferred amount posted for government margin charge. |
| 104 | `IC.CORDR.DEF.GOV.MAR.TAX` | `CorrAcctDr_DefGovMarTax` | TField |  | The deferred amount posted for government margin charge Tax. |
| 105 | `IC.CORDR.DEF.INT.STMT` | `CorrAcctDr_DefIntStmt` | TField |  | The deferred amount posted for interest statement charge. |
| 106 | `IC.CORDR.DEF.INT.STMT.TAX` | `CorrAcctDr_DefIntStmtTax` | TField |  | The deferred amount posted for interest statement charge Tax. |
| 107 | `IC.CORDR.DEF.TOTAL.INT` | `CorrAcctDr_DefTotalInt` | TField |  | The total amount of deferred interest. |
| 108 | `IC.CORDR.DEF.TOTAL.CHARGE` | `CorrAcctDr_DefTotalCharge` | TField |  | The total amount of deferred debit charge. |
| 109 | `IC.CORDR.DEF.TOTAL.TAX` | `CorrAcctDr_DefTotalTax` | TField |  | The total amount of deferred Tax. |
| 110 | `IC.CORDR.DEF.WAIVE.ALL` | `CorrAcctDr_DefWaiveAll` | TField |  | YES indicates that all debit interest and tax was waived for this period, if set to YES then no debit interest or tax will apply to this period for back valued corrections. But it will be calculated. |
| 111 | `IC.CORDR.CORRECTION.ID` | `CorrAcctDr_CorrectionId` |  |  |  |
| 112 | `IC.CORDR.ADJ.INT.AMT` | `CorrAcctDr_AdjIntAmt` |  |  |  |
| 113 | `IC.CORDR.ADJ.TAX.AMT` | `CorrAcctDr_AdjTaxAmt` |  |  |  |
| 114 | `IC.CORDR.WITHHELD.INT.AMT` | `CorrAcctDr_WithheldIntAmt` |  |  |  |
| 115 | `IC.CORDR.DB.NETTING.AMT` | `CorrAcctDr_DbNettingAmt` | TField |  | This field will be updated if CR interest is netted with corresponding DR interest. |
| 116 | `IC.CORDR.CORRECTION.DATE` | `CorrAcctDr_CorrectionDate` | TField |  | This field will contain the period end date of the current capitalisation period. |
| 117 | `IC.CORDR.WAIVE.AMT` | `CorrAcctDr_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 118 | `IC.CORDR.WAIVE.RATE` | `CorrAcctDr_WaiveRate` | TField |  |  |
| 119 | `IC.CORDR.RESERVED.03` | `CorrAcctDr_Reserved03` | TField |  |  |
| 120 | `IC.CORDR.RESERVED.02` | `CorrAcctDr_Reserved02` | TField |  |  |
| 121 | `IC.CORDR.RESERVED.01` | `CorrAcctDr_Reserved01` | TField |  |  |
