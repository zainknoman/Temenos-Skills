# USCORE.ARRANGEMENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.USCORE.ARRANGEMENT.DETAILS` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.ARR.DETS.PRODUCT.LINE` | `UscoreArrangementDetails_ProductLine` | TField |  | Valid AA.PRODUCT.LINE Id. |
| 2 | `USCORE.ARR.DETS.BALANCE.TYPE` | `UscoreArrangementDetails_BalanceType` | TField |  | Whether interest calculated on Daily Balance or on Average Daily Balance. Alpha Numeric with 7 characters |
| 3 | `USCORE.ARR.DETS.STATEMENT.FROM` | `UscoreArrangementDetails_StatementFrom` | TField |  | Statement Period Start Date.Date type field with length of 11 characters |
| 4 | `USCORE.ARR.DETS.STATEMENT.TO` | `UscoreArrangementDetails_StatementTo` | TField |  | Statement Period End Date.Date type field with length of 11 characters |
| 5 | `USCORE.ARR.DETS.AVG.BALANCE` | `UscoreArrangementDetails_AvgBalance` | TField |  | Avarage Balance for statement period. AMT field with 18 characters |
| 6 | `USCORE.ARR.DETS.INTEREST.EARNED` | `UscoreArrangementDetails_InterestEarned` | TField |  | Interest earned during this period (either accrued/capitalised). AMT field with 18 characters. |
| 7 | `USCORE.ARR.DETS.DAYS.IN.PERIOD` | `UscoreArrangementDetails_DaysInPeriod` | TField |  | Total number of days in this period. Numeric value with 5 characters. |
| 8 | `USCORE.ARR.DETS.APYE` | `UscoreArrangementDetails_Apye` | TField |  | Update the calculated APYE value. Rate value with 4 characters. |
| 9 | `USCORE.ARR.DETS.CURRENT.BALANCE` | `UscoreArrangementDetails_CurrentBalance` | TField |  | Current Outstanding Balance for the Account. |
| 10 | `USCORE.ARR.DETS.INTEREST.YTD` | `UscoreArrangementDetails_InterestYtd` | TField |  | This field contains the interest accrued for the account from Year start to date. |
| 11 | `USCORE.ARR.DETS.FEES.AMOUNT` | `UscoreArrangementDetails_FeesAmount` | TField |  | This field contains the charge amount of lending contract. |
| 12 | `USCORE.ARR.DETS.UNAMORT.AMOUNT` | `UscoreArrangementDetails_UnamortAmount` | TField |  | This field contains the unamortized fees amount of lending contract. |
| 13 | `USCORE.ARR.DETS.TOTALINT.YTD` | `UscoreArrangementDetails_TotalintYtd` | TField |  |  |
| 14 | `USCORE.ARR.DETS.INT.PAID.YTD` | `UscoreArrangementDetails_IntPaidYtd` | TField |  | This field contains interest paid on a loan and not the accrued interest till the date . |
| 15 | `USCORE.ARR.DETS.INT.PAID.LYEAR` | `UscoreArrangementDetails_IntPaidLyear` | TField |  | This field contains interest paid on a loan for last year. |
| 16 | `USCORE.ARR.DETS.LATE.FEES` | `UscoreArrangementDetails_LateFees` | TField |  | This field contains late charges paid for a loan till the date. |
| 17 | `USCORE.ARR.DETS.OD.STATUS` | `UscoreArrangementDetails_OdStatus` |  |  |  |
| 18 | `USCORE.ARR.DETS.OD.STATUS.COUNT` | `UscoreArrangementDetails_OdStatusCount` |  |  |  |
| 19 | `USCORE.ARR.DETS.OVERDRAFT.BAL` | `UscoreArrangementDetails_OverdraftBal` | TField |  |  |
| 20 | `USCORE.ARR.DETS.UNUSED.AMT` | `UscoreArrangementDetails_UnusedAmt` | TField |  | Shows the un advanced amount for loans. Amount 19 Characters. Standard Amount Format with 2 decimals. |
| 21 | `USCORE.ARR.DETS.LOAN.TO.VALUE` | `UscoreArrangementDetails_LoanToValue` | TField |  | shows the loan to value for third party system Amount 19 Characters. Standard Amount Format with 2 decimals. |
| 22 | `USCORE.ARR.DETS.ACCR.UNPAID.INT` | `UscoreArrangementDetails_AccrUnpaidInt` | TField |  | Shows the Accrued unpaid interest amount for accounts and deposits. Amount 19 Characters. Standard Amount Format with 2 decimals. |
| 23 | `USCORE.ARR.DETS.INTTAX.WITHHELD.C.YR` | `UscoreArrangementDetails_InttaxWithheldCYr` | TField |  | Not in Use. |
| 24 | `USCORE.ARR.DETS.INTTAX.WITHHELD.L.YR` | `UscoreArrangementDetails_InttaxWithheldLYr` | TField |  | Not in Use. |
| 25 | `USCORE.ARR.DETS.LAST.INT.PAYMENT.DATE` | `UscoreArrangementDetails_LastIntPaymentDate` | TField |  | Shows the Last interest paid date for deposits and accounts. Amount 19 Characters. Standard Amount Format with 2 decimals. |
| 26 | `USCORE.ARR.DETS.NEXT.INT.PAYMENT.DATE` | `UscoreArrangementDetails_NextIntPaymentDate` | TField |  | Shows the next interest payment date for deposits and accounts. Amount 19 Characters. Standard Amount Format with 2 decimals. |
| 27 | `USCORE.ARR.DETS.ESCROWINT.PAID.YTD` | `UscoreArrangementDetails_EscrowintPaidYtd` | TField |  |  |
| 28 | `USCORE.ARR.DETS.ESCROWINT.PAID.LYEAR` | `UscoreArrangementDetails_EscrowintPaidLyear` | TField |  |  |
| 29 | `USCORE.ARR.DETS.ESCROWTAX.PAID.YTD` | `UscoreArrangementDetails_EscrowtaxPaidYtd` | TField |  |  |
| 30 | `USCORE.ARR.DETS.ESCROWTAX.PAID.LYEAR` | `UscoreArrangementDetails_EscrowtaxPaidLyear` | TField |  |  |
| 31 | `USCORE.ARR.DETS.NO.OF.PAYMENTS` | `UscoreArrangementDetails_NoOfPayments` | TField |  |  |
| 32 | `USCORE.ARR.DETS.LAST.PAYMENT.DATE` | `UscoreArrangementDetails_LastPaymentDate` | TField |  |  |
| 33 | `USCORE.ARR.DETS.INT.PAID.TO.DATE` | `UscoreArrangementDetails_IntPaidToDate` | TField |  |  |
| 34 | `USCORE.ARR.DETS.APY` | `UscoreArrangementDetails_Apy` | TField |  | APY will be calculated during deposit creation, apply payment, renewal, roll over and updated here. Will be updated only for deposits |
| 35 | `USCORE.ARR.DETS.EARLY.REDEM.INT` | `UscoreArrangementDetails_EarlyRedemInt` | TField |  |  |
| 36 | `USCORE.ARR.DETS.EARLY.REDEM.INT.TAX` | `UscoreArrangementDetails_EarlyRedemIntTax` | TField |  |  |
| 37 | `USCORE.ARR.DETS.TIER.APY` | `UscoreArrangementDetails_TierApy` |  |  |  |
| 38 | `USCORE.ARR.DETS.STATE.WHT.C.YR` | `UscoreArrangementDetails_StateWhtCYr` | TField |  | Current year State withhold amount. |
| 39 | `USCORE.ARR.DETS.STATE.WHT.L.YR` | `UscoreArrangementDetails_StateWhtLYr` | TField |  | Last year State withhold amount. |
| 40 | `USCORE.ARR.DETS.FED.WHT.C.YR` | `UscoreArrangementDetails_FedWhtCYr` | TField |  | Current year Fed withhold amount. |
| 41 | `USCORE.ARR.DETS.FED.WHT.L.YR` | `UscoreArrangementDetails_FedWhtLYr` | TField |  | Last year Fed withhold amount. |
| 42 | `USCORE.ARR.DETS.REGCC.FROM.DATE` | `UscoreArrangementDetails_RegccFromDate` |  |  |  |
| 43 | `USCORE.ARR.DETS.REGCC.AMOUNT` | `UscoreArrangementDetails_RegccAmount` |  |  |  |
| 44 | `USCORE.ARR.DETS.VD.CUMUL.BAL` | `UscoreArrangementDetails_VdCumulBal` | TField |  | Current month Cumulative balance. |
| 45 | `USCORE.ARR.DETS.VD.AVG.BALANCE` | `UscoreArrangementDetails_VdAvgBalance` | TField |  | Month to date average balance. It is calculated as Cumulative balance divided by the number of days in the month. |
| 46 | `USCORE.ARR.DETS.FV.DATE` | `UscoreArrangementDetails_FvDate` |  |  |  |
| 47 | `USCORE.ARR.DETS.FV.BALANCE` | `UscoreArrangementDetails_FvBalance` |  |  |  |
| 48 | `USCORE.ARR.DETS.VD.AVG.BAL.M01` | `UscoreArrangementDetails_VdAvgBalM01` | TField |  | Month to date average balance corresponding to the month of January. |
| 49 | `USCORE.ARR.DETS.VD.AVG.BAL.M02` | `UscoreArrangementDetails_VdAvgBalM02` | TField |  | Month to date average balance corresponding to the month of February. |
| 50 | `USCORE.ARR.DETS.VD.AVG.BAL.M03` | `UscoreArrangementDetails_VdAvgBalM03` | TField |  | Month to date average balance corresponding to the month of March. |
| 51 | `USCORE.ARR.DETS.VD.AVG.BAL.M04` | `UscoreArrangementDetails_VdAvgBalM04` | TField |  | Month to date average balance corresponding to the month of April. |
| 52 | `USCORE.ARR.DETS.VD.AVG.BAL.M05` | `UscoreArrangementDetails_VdAvgBalM05` | TField |  | Month to date average balance corresponding to the month of May. |
| 53 | `USCORE.ARR.DETS.VD.AVG.BAL.M06` | `UscoreArrangementDetails_VdAvgBalM06` | TField |  | Month to date average balance corresponding to the month of June. |
| 54 | `USCORE.ARR.DETS.VD.AVG.BAL.M07` | `UscoreArrangementDetails_VdAvgBalM07` | TField |  | Month to date average balance corresponding to the month of July. |
| 55 | `USCORE.ARR.DETS.VD.AVG.BAL.M08` | `UscoreArrangementDetails_VdAvgBalM08` | TField |  | Month to date average balance corresponding to the month of August. |
| 56 | `USCORE.ARR.DETS.VD.AVG.BAL.M09` | `UscoreArrangementDetails_VdAvgBalM09` | TField |  | Month to date average balance corresponding to the month of September. |
| 57 | `USCORE.ARR.DETS.VD.AVG.BAL.M10` | `UscoreArrangementDetails_VdAvgBalM10` | TField |  | Month to date average balance corresponding to the month of October. |
| 58 | `USCORE.ARR.DETS.VD.AVG.BAL.M11` | `UscoreArrangementDetails_VdAvgBalM11` | TField |  | Month to date average balance corresponding to the month of November. |
| 59 | `USCORE.ARR.DETS.VD.AVG.BAL.M12` | `UscoreArrangementDetails_VdAvgBalM12` | TField |  | Month to date average balance corresponding to the month of December. |
| 60 | `USCORE.ARR.DETS.DQ.AMOUNT` | `UscoreArrangementDetails_DqAmount` | TField |  | Amount due in bills from the delinquent date. |
| 61 | `USCORE.ARR.DETS.OUTST.PRINCIPAL` | `UscoreArrangementDetails_OutstPrincipal` | TField |  | Outstanding Principal Amount. |
| 62 | `USCORE.ARR.DETS.OUTST.INTEREST` | `UscoreArrangementDetails_OutstInterest` | TField |  | Outstanding Interest Amount. |
| 63 | `USCORE.ARR.DETS.OUTST.FEES` | `UscoreArrangementDetails_OutstFees` | TField |  | Outstanding Fee amount. |
| 64 | `USCORE.ARR.DETS.OUTST.LATEFEE` | `UscoreArrangementDetails_OutstLatefee` | TField |  | Outstanding Late fee amount, based on the late fee property configured in USLEND.PARAMETER. |
| 65 | `USCORE.ARR.DETS.CLOSURE.DATE` | `UscoreArrangementDetails_ClosureDate` | TField |  | Date when an account was CLosed. |
| 66 | `USCORE.ARR.DETS.LAST.PAID.DATE` | `UscoreArrangementDetails_LastPaidDate` | TField |  | Loan last repaid date. |
| 67 | `USCORE.ARR.DETS.LAST.PAID.AMT` | `UscoreArrangementDetails_LastPaidAmt` | TField |  | Loan amount repaid in LAST.PAID.DATE. |
| 68 | `USCORE.ARR.DETS.SCH.PAYMENT.AMT` | `UscoreArrangementDetails_SchPaymentAmt` | TField |  | Amount to be repaid every month. |
| 69 | `USCORE.ARR.DETS.PARTIAL.AMT` | `UscoreArrangementDetails_PartialAmt` | TField |  | Due amount from bills partially paid. |
| 70 | `USCORE.ARR.DETS.PAYMENT.FREQ` | `UscoreArrangementDetails_PaymentFreq` | TField |  | Payment frequency. 35 chars |
| 71 | `USCORE.ARR.DETS.CHGOFF.AMOUNT` | `UscoreArrangementDetails_ChgoffAmount` | TField |  |  |
| 72 | `USCORE.ARR.DETS.CHGOFF.REASON` | `UscoreArrangementDetails_ChgoffReason` | TField |  | Charge off reason. Reserved for later use 35 chars |
