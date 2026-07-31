# MDI.LOAN.PROD.SUMM.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.LOAN.PROD.SUMM.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.LOAN.PROD.ITEM.REQ` | `MdiLoanProdSummWork_ItemReq` |  |  |  |
| 2 | `MDI.LOAN.PROD.ITEM.SENT` | `MdiLoanProdSummWork_ItemSent` |  |  |  |
| 3 | `MDI.LOAN.PROD.MORE.FLAG` | `MdiLoanProdSummWork_MoreFlag` |  |  |  |
| 4 | `MDI.LOAN.PROD.PAN.NO` | `MdiLoanProdSummWork_PanNo` |  |  |  |
| 5 | `MDI.LOAN.PROD.MEMBER.NO` | `MdiLoanProdSummWork_MemberNo` |  |  |  |
| 6 | `MDI.LOAN.PROD.LOANPROD.TYPE` | `MdiLoanProdSummWork_LoanprodType` |  |  |  |
| 7 | `MDI.LOAN.PROD.LOANPROD.ID` | `MdiLoanProdSummWork_LoanprodId` |  |  |  |
| 8 | `MDI.LOAN.PROD.CURR.BALANCE` | `MdiLoanProdSummWork_CurrBalance` |  |  |  |
| 9 | `MDI.LOAN.PROD.NEXT.DUE.DATE` | `MdiLoanProdSummWork_NextDueDate` |  |  |  |
| 10 | `MDI.LOAN.PROD.CUSTOMER.TYPE` | `MdiLoanProdSummWork_CustomerType` |  |  |  |
| 11 | `MDI.LOAN.PROD.LOANRATE` | `MdiLoanProdSummWork_Loanrate` |  |  |  |
| 12 | `MDI.LOAN.PROD.LOAN.LEVEL` | `MdiLoanProdSummWork_LoanLevel` |  |  |  |
| 13 | `MDI.LOAN.PROD.PAY.TYPE` | `MdiLoanProdSummWork_PayType` |  |  |  |
| 14 | `MDI.LOAN.PROD.LOAN.PAYMENT` | `MdiLoanProdSummWork_LoanPayment` |  |  |  |
| 15 | `MDI.LOAN.PROD.OPEN.DATE` | `MdiLoanProdSummWork_OpenDate` |  |  |  |
| 16 | `MDI.LOAN.PROD.MATURITY.DATE` | `MdiLoanProdSummWork_MaturityDate` |  |  |  |
| 17 | `MDI.LOAN.PROD.LENTH.OF.INT` | `MdiLoanProdSummWork_LenthOfInt` |  |  |  |
| 18 | `MDI.LOAN.PROD.FREQ.OF.INT` | `MdiLoanProdSummWork_FreqOfInt` |  |  |  |
| 19 | `MDI.LOAN.PROD.AMORT.PERIOD` | `MdiLoanProdSummWork_AmortPeriod` |  |  |  |
| 20 | `MDI.LOAN.PROD.PAY.LENTH` | `MdiLoanProdSummWork_PayLenth` |  |  |  |
| 21 | `MDI.LOAN.PROD.PAY.FREQ` | `MdiLoanProdSummWork_PayFreq` |  |  |  |
| 22 | `MDI.LOAN.PROD.DISBURSE.DATE` | `MdiLoanProdSummWork_DisburseDate` |  |  |  |
| 23 | `MDI.LOAN.PROD.ADVANCED.AMT` | `MdiLoanProdSummWork_AdvancedAmt` |  |  |  |
| 24 | `MDI.LOAN.PROD.IS.BLENDED` | `MdiLoanProdSummWork_IsBlended` |  |  |  |
| 25 | `MDI.LOAN.PROD.IS.PRIMEPLUS` | `MdiLoanProdSummWork_IsPrimeplus` |  |  |  |
| 26 | `MDI.LOAN.PROD.SCHEDULE` | `MdiLoanProdSummWork_Schedule` |  |  |  |
| 27 | `MDI.LOAN.PROD.DELIQ.DATE` | `MdiLoanProdSummWork_DeliqDate` |  |  |  |
| 28 | `MDI.LOAN.PROD.DELIQ.AMT` | `MdiLoanProdSummWork_DeliqAmt` |  |  |  |
| 29 | `MDI.LOAN.PROD.CURRENCY` | `MdiLoanProdSummWork_Currency` |  |  |  |
| 30 | `MDI.LOAN.PROD.ORIG.AMT` | `MdiLoanProdSummWork_OrigAmt` |  |  |  |
| 31 | `MDI.LOAN.PROD.LOAN.DESC` | `MdiLoanProdSummWork_LoanDesc` |  |  |  |
| 32 | `MDI.LOAN.PROD.ACCR.INT` | `MdiLoanProdSummWork_AccrInt` |  |  |  |
| 33 | `MDI.LOAN.PROD.INT.CHARGE.YTD` | `MdiLoanProdSummWork_IntChargeYtd` |  |  |  |
| 34 | `MDI.LOAN.PROD.INT.CHARGE.LY` | `MdiLoanProdSummWork_IntChargeLy` |  |  |  |
| 35 | `MDI.LOAN.PROD.REMAIN.AMORT` | `MdiLoanProdSummWork_RemainAmort` |  |  |  |
| 36 | `MDI.LOAN.PROD.END.BALANCE` | `MdiLoanProdSummWork_EndBalance` |  |  |  |
| 37 | `MDI.LOAN.PROD.TOT.PAID.AMT` | `MdiLoanProdSummWork_TotPaidAmt` |  |  |  |
| 38 | `MDI.LOAN.PROD.LOAN.FOREIGN.PERSON` | `MdiLoanProdSummWork_LoanForeignPerson` |  |  |  |
| 39 | `MDI.LOAN.PROD.INTEND.DESC` | `MdiLoanProdSummWork_IntendDesc` |  |  |  |
| 40 | `MDI.LOAN.PROD.SAVE.TAKE.BAL` | `MdiLoanProdSummWork_SaveTakeBal` |  |  |  |
| 41 | `MDI.LOAN.PROD.OUTS.BALDUE.PER` | `MdiLoanProdSummWork_OutsBalduePer` |  |  |  |
| 42 | `MDI.LOAN.PROD.PYMT.INCLUDES` | `MdiLoanProdSummWork_PymtIncludes` |  |  |  |
| 43 | `MDI.LOAN.PROD.LAST.MONTH.INT` | `MdiLoanProdSummWork_LastMonthInt` |  |  |  |
| 44 | `MDI.LOAN.PROD.RESERVED.9` | `MdiLoanProdSummWork_Reserved9` |  |  |  |
| 45 | `MDI.LOAN.PROD.RESERVED.8` | `MdiLoanProdSummWork_Reserved8` |  |  |  |
| 46 | `MDI.LOAN.PROD.RESERVED.7` | `MdiLoanProdSummWork_Reserved7` |  |  |  |
| 47 | `MDI.LOAN.PROD.RESERVED.6` | `MdiLoanProdSummWork_Reserved6` |  |  |  |
| 48 | `MDI.LOAN.PROD.RESERVED.5` | `MdiLoanProdSummWork_Reserved5` |  |  |  |
| 49 | `MDI.LOAN.PROD.RESERVED.4` | `MdiLoanProdSummWork_Reserved4` |  |  |  |
| 50 | `MDI.LOAN.PROD.RESERVED.3` | `MdiLoanProdSummWork_Reserved3` |  |  |  |
| 51 | `MDI.LOAN.PROD.RESERVED.2` | `MdiLoanProdSummWork_Reserved2` |  |  |  |
| 52 | `MDI.LOAN.PROD.RESERVED.1` | `MdiLoanProdSummWork_Reserved1` |  |  |  |
| 53 | `MDI.LOAN.PROD.LOCAL.REF` | `MdiLoanProdSummWork_LocalRef` |  |  |  |
