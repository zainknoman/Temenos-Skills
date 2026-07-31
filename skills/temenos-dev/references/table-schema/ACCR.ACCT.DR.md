# ACCR.ACCT.DR — Table Schema

> Source: `INSERTS/I_F.ACCR.ACCT.DR` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.ACRDR.PERIOD.FIRST.DATE` | `AccrAcctDr_PeriodFirstDate` | TField |  | Specifies the value date of the first balance on which the interest has been calculated. This is the day after the last debit interest application (Capitalisation) as stored in the CAP.DATE.DR.INT field in the ACCOUNT record. Validation Rules: 9 date characters DD MMM YYYY. |
| 2 | `IC.ACRDR.PERIOD.LAST.DATE` | `AccrAcctDr_PeriodLastDate` | TField |  | Specifies the value date of the last balance on which the interest has been calculated. Interest is calculated on the value dated balances stored in the ACCT.ACTIVITY file, taking into account all entries over the Account up to and including the last end of day processing. The calculation includes all balances from the day after the last debit interest capitalisation, as stored in the ACCOUNT record (in the CAP.DATE.DR.INT field) up to and including the month end accrual date specified in the MTH.END.UPTO.DAY field in the ACCOUNT.ACCRUAL file. Validation Rules: 9 date characters DD MMM YYYY. |
| 3 | `IC.ACRDR.DR.INT.DATE` | `AccrAcctDr_DrIntDate` |  |  |  |
| 4 | `IC.ACRDR.DR.NO.OF.DAYS` | `AccrAcctDr_DrNoOfDays` |  |  |  |
| 5 | `IC.ACRDR.DR.VAL.BALANCE` | `AccrAcctDr_DrValBalance` |  |  |  |
| 6 | `IC.ACRDR.DR.INT.RATE` | `AccrAcctDr_DrIntRate` |  |  |  |
| 7 | `IC.ACRDR.UNADJ.DR.INT` | `AccrAcctDr_UnadjDrInt` |  |  |  |
| 8 | `IC.ACRDR.DR.INT.AMT` | `AccrAcctDr_DrIntAmt` |  |  |  |
| 9 | `IC.ACRDR.DR.INT.CATEG` | `AccrAcctDr_DrIntCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated when debit interest is accrued. Validation Rules: 4 or 5 numeric characters. |
| 10 | `IC.ACRDR.DR.INT.TR.AC` | `AccrAcctDr_DrIntTrAc` | TField |  | Identifies the Transaction code to be assigned to Account entries generated when debit interest is capitalised. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 11 | `IC.ACRDR.DR.INT.TR.PL` | `AccrAcctDr_DrIntTrPl` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated when debit interest is accrued. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 12 | `IC.ACRDR.DR.INT.TAX.CODE` | `AccrAcctDr_DrIntTaxCode` |  |  |  |
| 13 | `IC.ACRDR.DR.INT.TAX.RATE` | `AccrAcctDr_DrIntTaxRate` |  |  |  |
| 14 | `IC.ACRDR.DR.INT.TAX.AMT` | `AccrAcctDr_DrIntTaxAmt` |  |  |  |
| 15 | `IC.ACRDR.DR.INT.TAXCATEG` | `AccrAcctDr_DrIntTaxcateg` |  |  |  |
| 16 | `IC.ACRDR.DR.INT.TAXTRSDR` | `AccrAcctDr_DrIntTaxtrsdr` |  |  |  |
| 17 | `IC.ACRDR.DR.INT.TAXTRSCR` | `AccrAcctDr_DrIntTaxtrscr` |  |  |  |
| 18 | `IC.ACRDR.INT.ADDON.CODE` | `AccrAcctDr_IntAddonCode` | TField |  | Where a Debit Interest Addon charge is to be made on an Account, this code specifies the DEBIT.INT.ADDON record containing details of the calculation and processing of Interest Addon charge. The Debit Interest Addon charge is calculated as a percentage of the total value of Debit Interest shown in all occurrences of multivalue field DR.INT.AMT. The Debit Interest Addon charge details used are those applicable on the accrual month end date. Validation Rules: 1-2 numeric characters. |
| 19 | `IC.ACRDR.INT.ADDON.PERCT` | `AccrAcctDr_IntAddonPerct` | TField |  | Shows the Percentage which will be applied to the Debit Interest amount to calculate the Debit Interest Addon charge. Validation Rules: Up to 10 numeric characters plus a decimal point. Up to 6 integers. Up to 9 decimals. Standard rate format. |
| 20 | `IC.ACRDR.INT.ADDON.FREE` | `AccrAcctDr_IntAddonFree` | TField |  | Shows the free amount to be deducted from the calculated interest addon charge, if applicable. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 21 | `IC.ACRDR.ADDON.MIN.MAX` | `AccrAcctDr_AddonMinMax` | TField |  | After calculating the gross Debit Interest Addon charge and subtracting the Free Amount, comparison is made with Minimum and Maximum charge amounts from the Debit Interest Addon record. If either the Minimum charge or the Maximum charge is substituted for the calculated charge, 'MINIMUM' or 'MAXIMUM' is recorded in this field. Validation Rules: 'MINIMUM', 'MAXIMUM' or nothing. |
| 22 | `IC.ACRDR.UNADJ.INT.ADDON` | `AccrAcctDr_UnadjIntAddon` | TField |  | This field holds the unadjusted Debit Interest Addon amount when an adjustment relating to the Maximum Legal Rate is needed. This is used to store the actual Debit Interest Addon charge when differs from the applied Debit Interest Addon charge. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 23 | `IC.ACRDR.INT.ADDON.AMT` | `AccrAcctDr_IntAddonAmt` | TField |  | Shows the calculated Debit Interest Addon Charge after Minimum or Maximum adjustment if appropriate. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 24 | `IC.ACRDR.INT.ADDON.CATEG` | `AccrAcctDr_IntAddonCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Debit Interest Addon charges. Validation Rules: 4 or 5 numeric characters. |
| 25 | `IC.ACRDR.INT.ADDON.TRSDR` | `AccrAcctDr_IntAddonTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Debit Interest Addon charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 26 | `IC.ACRDR.INT.ADDON.TRSCR` | `AccrAcctDr_IntAddonTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Debit Interest Addon charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 27 | `IC.ACRDR.ADDON.TAX.CODE` | `AccrAcctDr_AddonTaxCode` | TField |  | Not used in ACCR.ACCT.DR records. Validation Rules: Null. |
| 28 | `IC.ACRDR.ADDON.TAX.RATE` | `AccrAcctDr_AddonTaxRate` |  |  |  |
| 29 | `IC.ACRDR.ADDON.TAX.AMT` | `AccrAcctDr_AddonTaxAmt` |  |  |  |
| 30 | `IC.ACRDR.ADDON.TAXCATEG` | `AccrAcctDr_AddonTaxcateg` |  |  |  |
| 31 | `IC.ACRDR.ADDON.TAXTRSDR` | `AccrAcctDr_AddonTaxtrsdr` |  |  |  |
| 32 | `IC.ACRDR.ADDON.TAXTRSCR` | `AccrAcctDr_AddonTaxtrscr` |  |  |  |
| 33 | `IC.ACRDR.GOV.MARGIN.DATE` | `AccrAcctDr_GovMarginDate` |  |  |  |
| 34 | `IC.ACRDR.GV.NO.OF.DAYS` | `AccrAcctDr_GvNoOfDays` |  |  |  |
| 35 | `IC.ACRDR.GV.VAL.BALANCE` | `AccrAcctDr_GvValBalance` |  |  |  |
| 36 | `IC.ACRDR.GV.INT.RATE` | `AccrAcctDr_GvIntRate` |  |  |  |
| 37 | `IC.ACRDR.GOV.MARGIN.AMT` | `AccrAcctDr_GovMarginAmt` |  |  |  |
| 38 | `IC.ACRDR.GOV.MARGIN.CODE` | `AccrAcctDr_GovMarginCode` | TField |  | Where a Government Margin charge is to be made on an Account, this code specifies the GOVERNMENT.MARGIN record containing the details of the calculation and processing of Government Margin charges. The Government Margin charge is calculated as a percentage of the debit balance. (Shown in multivalue field GV.VAL.BALANCE). The Government Margin details to be used are those applicable on the accrual month end date. Validation Rules: 1-2 numeric characters. |
| 39 | `IC.ACRDR.GOV.MARGIN.MIN.MAX` | `AccrAcctDr_GovMarginMinMax` | TField |  | After calculating the gross Government Margin charge, comparison is made with Minimum and Maximum charge amounts from the GOVERNMENT.MARGIN record. If either the Minimum charge or the Maximum charge is substituted for the calculated charge, 'MINIMUM' or "MAXIMUM' is recorded in this field. Validation Rules: 'MINIMUM', 'MAXIMUM' or nothing. |
| 40 | `IC.ACRDR.GOV.MRG.TOT.AMT` | `AccrAcctDr_GovMrgTotAmt` | TField |  | Shows the total calculated Government Margin Charge. It is the sum of multivalue fields GOV.MARGIN.AMT adjusted to the Minimum or Maximum if appropriate. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 41 | `IC.ACRDR.GOV.MRG.CATEG` | `AccrAcctDr_GovMrgCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Government Margin charges. Validation Rules: 4 or 5 numeric characters. |
| 42 | `IC.ACRDR.GOV.MRG.TRSDR` | `AccrAcctDr_GovMrgTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Government Margin charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 43 | `IC.ACRDR.GOV.MRG.TRSCR` | `AccrAcctDr_GovMrgTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Government Margin charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 44 | `IC.ACRDR.HIGHEST.DR.CODE` | `AccrAcctDr_HighestDrCode` | TField |  | Where a Highest Debit charge is to be made on an Account, this code specifies the HIGHEST.DEBIT record containing details of the calculation and processing of the Highest Debit charge. The Highest Debit charge details to be used are those applicable on the accrual month end date. Validation Rules: 1-2 numeric characters. |
| 45 | `IC.ACRDR.HIGHEST.DR.BAL` | `AccrAcctDr_HighestDrBal` | TField |  | Shows the Highest Debit Balance found during the calculation period and on which the Highest Debit Balance charge will be based. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 46 | `IC.ACRDR.HIGHEST.DR.PERC` | `AccrAcctDr_HighestDrPerc` | TField |  | Shows the Percentage which will be applied to the Highest Debit amount to calculate the Highest Debit charge. Validation Rules: Up to 10 numeric characters plus a decimal point. Up to 6 integers. Up to 9 decimals. Standard rate format. |
| 47 | `IC.ACRDR.HIGHEST.DR.FREE` | `AccrAcctDr_HighestDrFree` | TField |  | Shows the free amount by which the calculated Highest Debit charge will be reduced. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 48 | `IC.ACRDR.HIGH.DR.MIN.MAX` | `AccrAcctDr_HighDrMinMax` | TField |  | After calculating the gross Highest Debit charge and subtracting the Free Amount, comparison is made with Minimum and Maximum charge amounts from the Highest Debit record. If either the Minimum charge or the Maximum charge is substituted for the calculated charge, 'MINIMUM' or 'MAXIMUM' is recorded in this field. Validation Rules: 'MINIMUM', 'MAXIMUM' or nothing. |
| 49 | `IC.ACRDR.UNADJ.HIGHEST.DR` | `AccrAcctDr_UnadjHighestDr` | TField |  | This field holds the unadjusted Highest Debit charge when an adjustment relating to the Maximum Legal Rate is needed. This is used to store the actual Highest Debit charge when differs from the applied Highest Debit charge. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 50 | `IC.ACRDR.HIGHEST.DR.AMT` | `AccrAcctDr_HighestDrAmt` | TField |  | Shows the calculated Highest Debit Charge after Minimum or Maximum adjustment if appropriate. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 51 | `IC.ACRDR.HIGH.DR.CATEG` | `AccrAcctDr_HighDrCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Highest Debit charges. Validation Rules: 4 or 5 numeric characters. |
| 52 | `IC.ACRDR.HIGH.DR.TRSDR` | `AccrAcctDr_HighDrTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Highest Debit charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 53 | `IC.ACRDR.HIGH.DR.TRSCR` | `AccrAcctDr_HighDrTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Highest Debit charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 54 | `IC.ACRDR.HI.DR.TAX.CODE` | `AccrAcctDr_HiDrTaxCode` | TField |  | Not used in ACCR.ACCT.DR records. Validation Rules: Null. |
| 55 | `IC.ACRDR.HI.DR.TAX.RATE` | `AccrAcctDr_HiDrTaxRate` |  |  |  |
| 56 | `IC.ACRDR.HI.DR.TAX.AMT` | `AccrAcctDr_HiDrTaxAmt` |  |  |  |
| 57 | `IC.ACRDR.HI.DR.TAXCATEG` | `AccrAcctDr_HiDrTaxcateg` |  |  |  |
| 58 | `IC.ACRDR.HI.DR.TAXTRSDR` | `AccrAcctDr_HiDrTaxtrsdr` |  |  |  |
| 59 | `IC.ACRDR.HI.DR.TAXTRSCR` | `AccrAcctDr_HiDrTaxtrscr` |  |  |  |
| 60 | `IC.ACRDR.INT.STMT.CODE` | `AccrAcctDr_IntStmtCode` | TField |  | Where an Interest Statement charge is to be made on an Account, this code specifies the INTEREST.STATEMENT record containing details of the calculation and processing of Interest Statement charge. The Interest Statement charge details to be used are those applicable on the accrual monthend date. Validation Rules: 1-2 numeric characters. |
| 61 | `IC.ACRDR.INT.STMT.AMT` | `AccrAcctDr_IntStmtAmt` | TField |  | Shows the Interest Statement Charge. This is a flat charge levied on each debit interest capitalisation date. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 62 | `IC.ACRDR.INT.STMT.CATEG` | `AccrAcctDr_IntStmtCateg` | TField |  | Identifies the Category code to be assigned to Profit and Loss entries generated for Interest Statement charges. Validation Rules: 4 or 5 numeric characters. |
| 63 | `IC.ACRDR.INT.STMT.TRSDR` | `AccrAcctDr_IntStmtTrsdr` | TField |  | Identifies the Transaction code to be assigned to Account entries generated for Interest Statement charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 64 | `IC.ACRDR.INT.STMT.TRSCR` | `AccrAcctDr_IntStmtTrscr` | TField |  | Identifies the Transaction code to be assigned to Profit and Loss entries generated for Interest Statement charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 65 | `IC.ACRDR.STMT.TAX.CODE` | `AccrAcctDr_StmtTaxCode` | TField |  | Not used in ACCR.ACCT.DR records. Validation Rules: Null. |
| 66 | `IC.ACRDR.STMT.TAX.RATE` | `AccrAcctDr_StmtTaxRate` |  |  |  |
| 67 | `IC.ACRDR.STMT.TAX.AMT` | `AccrAcctDr_StmtTaxAmt` |  |  |  |
| 68 | `IC.ACRDR.STMT.TAXCATEG` | `AccrAcctDr_StmtTaxcateg` |  |  |  |
| 69 | `IC.ACRDR.STMT.TAXTRSDR` | `AccrAcctDr_StmtTaxtrsdr` |  |  |  |
| 70 | `IC.ACRDR.STMT.TAXTRSCR` | `AccrAcctDr_StmtTaxtrscr` |  |  |  |
| 71 | `IC.ACRDR.LIQUIDITY.ACCOUNT` | `AccrAcctDr_LiquidityAccount` | TField |  | Where interest and charges are to be passed to an alternative Account, the number of the alternative ACCOUNT is shown by this field. Where interest and charges are to be passed to an alternative Account, the alternative account number should be entered in the INTEREST LIQU ACCT Field on the original customer ACCOUNT record. Validation Rules: Standard account format. |
| 72 | `IC.ACRDR.COMPENS.ACCOUNT` | `AccrAcctDr_CompensAccount` |  |  |  |
| 73 | `IC.ACRDR.INT.NO.BOOKING` | `AccrAcctDr_IntNoBooking` | TField |  | If interest and charges are to be calculated for information purposes only and not passed to the account, or if accrued interest is to be suspended and not posted to Profit and Loss, this is shown by this field. The information in this field comes from the equivalent field in the ACCOUNT record. If this field contains 'SUSPENSE', interest will be booked to the Customer's Account but no Profit or Loss entries will be generated, instead, the amount which would have been accrued will be stored in a Suspense Amount field in the Account record. If this field contains 'Y', interest is calculated for information only, no entries will be posted either to Profit and Loss or to the Customer's Account. e.g. for Nostro Accounts. Validation Rules: 'SUSPENSE', 'Y' or nothing. |
| 74 | `IC.ACRDR.USED.MIDDLE.RATE` | `AccrAcctDr_UsedMiddleRate` | TField |  | The exchange rate used to convert the Account Currency into Local Currency during the Charge calculation process. Note: This is necessary where default charges specified in local currency are used. Validation Rules: Up to 10 numeric characters plus a decimal point. Up to 6 integers. Up to 9 decimals. Standard rate format. |
| 75 | `IC.ACRDR.TOTAL.INTEREST` | `AccrAcctDr_TotalInterest` | TField |  | Total interest calculated. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 76 | `IC.ACRDR.TOTAL.CHARGE` | `AccrAcctDr_TotalCharge` | TField |  | Total of Interest Related Charges. Made up of the following: Debit Interest Addon - a percentage of the amount of debit interest to be applied. Government Margin - an additional interest rate applied to each debit balance. Highest Debit - a percentage of the largest debit balance. Interest Statement - a charge for providing a detailed interest statement when debit interest is applied. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 77 | `IC.ACRDR.TOTAL.TAX` | `AccrAcctDr_TotalTax` | TField |  | Not used in ACCR.ACCT.DR records. Validation Rules: Null. |
| 78 | `IC.ACRDR.GRAND.TOTAL` | `AccrAcctDr_GrandTotal` | TField |  | Total debit interest and interest related charges accrued since the last capitalisation. Validation Rules: Up to 14 numeric characters plus a decimal point. Standard amount format. |
| 79 | `IC.ACRDR.CORRECTION.NUMBER` | `AccrAcctDr_CorrectionNumber` | TField |  | Sequential number of corrected record generated after back-valued entries, rate changes or condition changes. Validation Rules: Field not used. Just to keep the file layout same as STMT.ACCT.DR. |
| 80 | `IC.ACRDR.APR` | `AccrAcctDr_Apr` | TField |  | This field stores the Annual Payment Rate (or the Taux Effectif Global in France). Validation Rules: 1-10 type R (standard rate format) characters plus a decimal point. |
| 81 | `IC.ACRDR.DEFERRED.DATE` | `AccrAcctDr_DeferredDate` | TField |  | This field will hold the deferred application date of the debit interest in case pending debit interest processing was being performed on this account. |
| 82 | `IC.ACRDR.LIQUIDITY.CCY` | `AccrAcctDr_LiquidityCcy` | TField |  | Identifies the currency of the liquidity account which may be present on this file. The currency may not necessarily be the currency of the main account. Validation Rules: 3 type SSS (uppercase alpha) characters or 1-3 numeric characters. |
| 83 | `IC.ACRDR.ICA.POST.INTEREST` | `AccrAcctDr_IcaPostInterest` | TField |  | Not used in ACCR.ACCT.DR records. Validation Rules: Null. |
| 84 | `IC.ACRDR.ICA.MAIN.ACCT` | `AccrAcctDr_IcaMainAcct` |  |  |  |
| 85 | `IC.ACRDR.ICA.DIST.TYPE` | `AccrAcctDr_IcaDistType` |  |  |  |
| 86 | `IC.ACRDR.ICA.DIST.RATIO` | `AccrAcctDr_IcaDistRatio` |  |  |  |
| 87 | `IC.ACRDR.ICA.INT.CATEG` | `AccrAcctDr_IcaIntCateg` |  |  |  |
| 88 | `IC.ACRDR.ICA.TR.AC` | `AccrAcctDr_IcaTrAc` |  |  |  |
| 89 | `IC.ACRDR.ICA.TR.PL` | `AccrAcctDr_IcaTrPl` |  |  |  |
| 90 | `IC.ACRDR.ICA.MAIN.INT` | `AccrAcctDr_IcaMainInt` |  |  |  |
| 91 | `IC.ACRDR.ICA.SUB.INT` | `AccrAcctDr_IcaSubInt` |  |  |  |
| 92 | `IC.ACRDR.DR.MIN.VALUE` | `AccrAcctDr_DrMinValue` | TField |  | If relevant the minimum amount of debit interest to apply if the calculated amount of interest is less than the minimum value and CR.MIN.WAIVE is not set to "YES". |
| 93 | `IC.ACRDR.DR.MIN.WAIVE` | `AccrAcctDr_DrMinWaive` | TField |  | If set to "YES" and the amount of interest calculated is less than the DR.MIN.VALUE then no interest will be booked. |
| 94 | `IC.ACRDR.UNADJ.TOTAL.INT` | `AccrAcctDr_UnadjTotalInt` | TField |  | The calculated total interest acount which could differ from the total interest amounts if interest has been manually adjusted for this period. |
| 95 | `IC.ACRDR.INT.POST.DATE` | `AccrAcctDr_IntPostDate` | TField |  | Not used in ACCR.ACCT.DR records. Validation Rules: Null. |
| 96 | `IC.ACRDR.MANUAL.ADJ.AMT` | `AccrAcctDr_ManualAdjAmt` | TField |  | The manual accrual adjustment amount for the period. |
| 97 | `IC.ACRDR.DEF.DR.INT` | `AccrAcctDr_DefDrInt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 98 | `IC.ACRDR.DEF.DR.TAX` | `AccrAcctDr_DefDrTax` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 99 | `IC.ACRDR.DEF.ADDON` | `AccrAcctDr_DefAddon` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 100 | `IC.ACRDR.DEF.ADDON.TAX` | `AccrAcctDr_DefAddonTax` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 101 | `IC.ACRDR.DEF.HIGH.DR` | `AccrAcctDr_DefHighDr` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 102 | `IC.ACRDR.DEF.HIGH.DR.TAX` | `AccrAcctDr_DefHighDrTax` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 103 | `IC.ACRDR.DEF.GOV.MAR` | `AccrAcctDr_DefGovMar` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 104 | `IC.ACRDR.DEF.GOV.MAR.TAX` | `AccrAcctDr_DefGovMarTax` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 105 | `IC.ACRDR.DEF.INT.STMT` | `AccrAcctDr_DefIntStmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 106 | `IC.ACRDR.DEF.INT.STMT.TAX` | `AccrAcctDr_DefIntStmtTax` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 107 | `IC.ACRDR.DEF.TOTAL.INT` | `AccrAcctDr_DefTotalInt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 108 | `IC.ACRDR.DEF.TOTAL.CHARGE` | `AccrAcctDr_DefTotalCharge` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 109 | `IC.ACRDR.DEF.TOTAL.TAX` | `AccrAcctDr_DefTotalTax` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 110 | `IC.ACRDR.DEF.WAIVE.ALL` | `AccrAcctDr_DefWaiveAll` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 111 | `IC.ACRDR.CORRECTION.ID` | `AccrAcctDr_CorrectionId` |  |  |  |
| 112 | `IC.ACRDR.ADJ.INT.AMT` | `AccrAcctDr_AdjIntAmt` |  |  |  |
| 113 | `IC.ACRDR.ADJ.TAX.AMT` | `AccrAcctDr_AdjTaxAmt` |  |  |  |
| 114 | `IC.ACRDR.WITHHELD.INT.AMT` | `AccrAcctDr_WithheldIntAmt` |  |  |  |
| 115 | `IC.ACRDR.DB.NETTING.AMT` | `AccrAcctDr_DbNettingAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 116 | `IC.ACRDR.CORRECTION.DATE` | `AccrAcctDr_CorrectionDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 117 | `IC.ACRDR.WAIVE.AMT` | `AccrAcctDr_WaiveAmt` | TField |  | The minimum waive amount in the currency of the account if the waive currency is different to the currency of the account Validation Rules: Standard amount format. |
| 118 | `IC.ACRDR.WAIVE.RATE` | `AccrAcctDr_WaiveRate` | TField |  |  |
| 119 | `IC.ACRDR.RESERVED.03` | `AccrAcctDr_Reserved03` | TField |  |  |
| 120 | `IC.ACRDR.RESERVED.02` | `AccrAcctDr_Reserved02` | TField |  |  |
| 121 | `IC.ACRDR.RESERVED.01` | `AccrAcctDr_Reserved01` | TField |  |  |
