# ESCROW.ANALYSIS.DETAILS — Table Schema

> Source: `INSERTS/I_F.ESCROW.ANALYSIS.DETAILS` in `ESCROW_Analysis.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.AD.ANALYSIS.TYPE` | `EscrowAnalysisDetails_AnalysisType` | TField |  | Records the type of analysis Ex: INITIAL, TEST, PAYOFF, SHORT.YEAR and ANNUAL |
| 2 | `ESCROW.AD.ESCROW.BALANCE` | `EscrowAnalysisDetails_EscrowBalance` | TField |  | Records current ESCROW balance during analysis |
| 3 | `ESCROW.AD.TOT.DISBURSE.NEXT.YR` | `EscrowAnalysisDetails_TotDisburseNextYr` | TField |  | Total disbursement amount for next year for the account |
| 4 | `ESCROW.AD.NO.OF.INSTALMENTS` | `EscrowAnalysisDetails_NoOfInstalments` | TField |  | This field will store the number of projected ESCROW installment does the account number has. |
| 5 | `ESCROW.AD.NEW.INSTAL.AMT` | `EscrowAnalysisDetails_NewInstalAmt` | TField |  | The escrow installment amount effective after the analysis date plus the payment effective period. |
| 6 | `ESCROW.AD.NEW.AMT.EFF.DATE` | `EscrowAnalysisDetails_NewAmtEffDate` | TField |  | The date that indicates the first time the new escrow installment amount is expected. This is derived by the using the escrow analysis date and adding to it the payment effective period from the escrow parameter. |
| 7 | `ESCROW.AD.TOT.PYMT.AMOUNT` | `EscrowAnalysisDetails_TotPymtAmount` | TField |  |  |
| 8 | `ESCROW.AD.REPAYMENT.FREQUENCY` | `EscrowAnalysisDetails_RepaymentFrequency` | TField |  |  |
| 9 | `ESCROW.AD.ESCROW.ACTIVITY` | `EscrowAnalysisDetails_EscrowActivity` | TField |  | This field will record the analysis escrow activity id. |
| 10 | `ESCROW.AD.PERIOD.START.DATE` | `EscrowAnalysisDetails_PeriodStartDate` | TField |  | The date that notes the beginning of the escrow processing period. For initial analysis this will be the loan's opening date, for all other analyses it will be based on the date of analysis plus the payment effective period in the escrow parameter. |
| 11 | `ESCROW.AD.PERIOD.END.DATE` | `EscrowAnalysisDetails_PeriodEndDate` | TField |  | The date that notes the termination of the escrow processing period. For initial analysis this will be one year from the opening date. For all other analyses it will be one year from the payment effective period. |
| 12 | `ESCROW.AD.ACCOUNT.ID` | `EscrowAnalysisDetails_AccountId` | TField |  | Customer's account number that is undergoing escrow processing |
| 13 | `ESCROW.AD.STATEMENT.DATE` | `EscrowAnalysisDetails_StatementDate` | TField |  | Customer's account number that is undergoing escrow processing |
| 14 | `ESCROW.AD.ACTIVITY.DESC` | `EscrowAnalysisDetails_ActivityDesc` | TField |  | This field records the escrow analysis activity description. |
| 15 | `ESCROW.AD.CUSTOMER` | `EscrowAnalysisDetails_Customer` |  |  |  |
| 16 | `ESCROW.AD.CUSTOMER.ADDRESS` | `EscrowAnalysisDetails_CustomerAddress` |  |  |  |
| 17 | `ESCROW.AD.CUSTOMER.CITY` | `EscrowAnalysisDetails_CustomerCity` |  |  |  |
| 18 | `ESCROW.AD.CUSTOMER.STATE` | `EscrowAnalysisDetails_CustomerState` |  |  |  |
| 19 | `ESCROW.AD.CUSTOMER.ZIP` | `EscrowAnalysisDetails_CustomerZip` |  |  |  |
| 20 | `ESCROW.AD.CUSTOMER.NAME` | `EscrowAnalysisDetails_CustomerName` |  |  |  |
| 21 | `ESCROW.AD.RESERVED.29` | `EscrowAnalysisDetails_Reserved29` |  |  |  |
| 22 | `ESCROW.AD.RESERVED.28` | `EscrowAnalysisDetails_Reserved28` |  |  |  |
| 23 | `ESCROW.AD.RESERVED.27` | `EscrowAnalysisDetails_Reserved27` |  |  |  |
| 24 | `ESCROW.AD.RESERVED.26` | `EscrowAnalysisDetails_Reserved26` |  |  |  |
| 25 | `ESCROW.AD.PAYEE` | `EscrowAnalysisDetails_Payee` |  |  |  |
| 26 | `ESCROW.AD.PAYEE.NAME` | `EscrowAnalysisDetails_PayeeName` |  |  |  |
| 27 | `ESCROW.AD.REFERENCE.NO` | `EscrowAnalysisDetails_ReferenceNo` |  |  |  |
| 28 | `ESCROW.AD.DISBURSE.FQU.PRD` | `EscrowAnalysisDetails_DisburseFquPrd` |  |  |  |
| 29 | `ESCROW.AD.NXT.DISBURSE.DATE` | `EscrowAnalysisDetails_NxtDisburseDate` |  |  |  |
| 30 | `ESCROW.AD.NXT.DISBURSE.AMT` | `EscrowAnalysisDetails_NxtDisburseAmt` |  |  |  |
| 31 | `ESCROW.AD.ANNUAL.DISBURSE.AMT` | `EscrowAnalysisDetails_AnnualDisburseAmt` |  |  |  |
| 32 | `ESCROW.AD.RESERVED.24` | `EscrowAnalysisDetails_Reserved24` |  |  |  |
| 33 | `ESCROW.AD.RESERVED.23` | `EscrowAnalysisDetails_Reserved23` |  |  |  |
| 34 | `ESCROW.AD.RESERVED.22` | `EscrowAnalysisDetails_Reserved22` |  |  |  |
| 35 | `ESCROW.AD.RESERVED.21` | `EscrowAnalysisDetails_Reserved21` |  |  |  |
| 36 | `ESCROW.AD.TOT.PAYEE.DISBURSEMENT` | `EscrowAnalysisDetails_TotPayeeDisbursement` | TField |  | Sum of the annual disbursements for all payees at the time of analysis. |
| 37 | `ESCROW.AD.PAYMENT.DATE` | `EscrowAnalysisDetails_PaymentDate` |  |  |  |
| 38 | `ESCROW.AD.PAYMENT.DESC` | `EscrowAnalysisDetails_PaymentDesc` |  |  |  |
| 39 | `ESCROW.AD.PAYEE.REF.NO` | `EscrowAnalysisDetails_PayeeRefNo` |  |  |  |
| 40 | `ESCROW.AD.ESCROW.BILL.TYPE` | `EscrowAnalysisDetails_EscrowBillType` |  |  |  |
| 41 | `ESCROW.AD.EST.PAYMENT.AMT` | `EscrowAnalysisDetails_EstPaymentAmt` |  |  |  |
| 42 | `ESCROW.AD.ACT.PAYMENT.AMT` | `EscrowAnalysisDetails_ActPaymentAmt` |  |  |  |
| 43 | `ESCROW.AD.PAYMENT.INDICATOR` | `EscrowAnalysisDetails_PaymentIndicator` |  |  |  |
| 44 | `ESCROW.AD.EST.BALANCE` | `EscrowAnalysisDetails_EstBalance` |  |  |  |
| 45 | `ESCROW.AD.ACT.BALANCE` | `EscrowAnalysisDetails_ActBalance` |  |  |  |
| 46 | `ESCROW.AD.AA.BILL.REF` | `EscrowAnalysisDetails_AaBillRef` |  |  |  |
| 47 | `ESCROW.AD.RESERVED.20` | `EscrowAnalysisDetails_Reserved20` |  |  |  |
| 48 | `ESCROW.AD.RESERVED.19` | `EscrowAnalysisDetails_Reserved19` |  |  |  |
| 49 | `ESCROW.AD.RESERVED.18` | `EscrowAnalysisDetails_Reserved18` |  |  |  |
| 50 | `ESCROW.AD.RESERVED.17` | `EscrowAnalysisDetails_Reserved17` |  |  |  |
| 51 | `ESCROW.AD.RESERVED.16` | `EscrowAnalysisDetails_Reserved16` |  |  |  |
| 52 | `ESCROW.AD.EST.TOT.PAYMENTS` | `EscrowAnalysisDetails_EstTotPayments` | TField |  | Sum of all the estimated escrow payments that are made in the prior escrow analysis period. |
| 53 | `ESCROW.AD.ACT.TOT.PAYMENTS` | `EscrowAnalysisDetails_ActTotPayments` | TField |  | Sum of all the actual escrow payments that are made in the prior escrow analysis period. |
| 54 | `ESCROW.AD.EST.TOT.DISBURSEMENTS` | `EscrowAnalysisDetails_EstTotDisbursements` | TField |  | Sum of all the estimated escrow disbursements that are made in the prior escrow analysis period. |
| 55 | `ESCROW.AD.ACT.TOT.DISBURSEMENTS` | `EscrowAnalysisDetails_ActTotDisbursements` | TField |  | Sum of all the actual escrow disbursements that are made in the prior escrow analysis period. |
| 56 | `ESCROW.AD.PROJ.ESCROW.BALANCE` | `EscrowAnalysisDetails_ProjEscrowBalance` | TField |  | The amount that is forecasted to be in the escrow balance as the analysis period begins. |
| 57 | `ESCROW.AD.PROJ.PAYMENT.DATE` | `EscrowAnalysisDetails_ProjPaymentDate` |  |  |  |
| 58 | `ESCROW.AD.PROJ.PAYMENT.DESC` | `EscrowAnalysisDetails_ProjPaymentDesc` |  |  |  |
| 59 | `ESCROW.AD.PROJ.PAYEE.REF.NO` | `EscrowAnalysisDetails_ProjPayeeRefNo` |  |  |  |
| 60 | `ESCROW.AD.PROJ.ESCROW.BILL.TYPE` | `EscrowAnalysisDetails_ProjEscrowBillType` |  |  |  |
| 61 | `ESCROW.AD.PROJ.PAYMENT.AMOUNT` | `EscrowAnalysisDetails_ProjPaymentAmount` |  |  |  |
| 62 | `ESCROW.AD.PROJ.BALANCE` | `EscrowAnalysisDetails_ProjBalance` |  |  |  |
| 63 | `ESCROW.AD.RESERVED.15` | `EscrowAnalysisDetails_Reserved15` |  |  |  |
| 64 | `ESCROW.AD.RESERVED.14` | `EscrowAnalysisDetails_Reserved14` |  |  |  |
| 65 | `ESCROW.AD.RESERVED.13` | `EscrowAnalysisDetails_Reserved13` |  |  |  |
| 66 | `ESCROW.AD.RESERVED.12` | `EscrowAnalysisDetails_Reserved12` |  |  |  |
| 67 | `ESCROW.AD.RESERVED.11` | `EscrowAnalysisDetails_Reserved11` |  |  |  |
| 68 | `ESCROW.AD.TOTAL.PAYMENTS` | `EscrowAnalysisDetails_TotalPayments` | TField |  | Sum of all the escrow payments that are made in the escrow analysis period. |
| 69 | `ESCROW.AD.TOTAL.DISBURSEMENTS` | `EscrowAnalysisDetails_TotalDisbursements` | TField |  | Sum of all the escrow disbursements that are made in the escrow analysis period. |
| 70 | `ESCROW.AD.MINIMUM.BALANCE` | `EscrowAnalysisDetails_MinimumBalance` | TField |  | The minimum amount calculated when all payments and disbursements are analyzed chronologically from prior period projected figures. |
| 71 | `ESCROW.AD.REQUIRED.BALANCE` | `EscrowAnalysisDetails_RequiredBalance` | TField |  | The minimum amount calculated when all payments and disbursements are analyzed chronologically and the product of the escrow installment amount multiplied by the cushion amount is then added to this minimum amount. |
| 72 | `ESCROW.AD.ACT.MINIMUM.BALANCE` | `EscrowAnalysisDetails_ActMinimumBalance` | TField |  | The minimum amount calculated when all payments and disbursements are analyzed chronologically from prior period historical figures. |
| 73 | `ESCROW.AD.CUSHION.AMOUNT` | `EscrowAnalysisDetails_CushionAmount` | TField |  | Cushion amount is the product of the newly calculated escrow installment amount multiplied by the cushion period in the ESCROW.PARAMETER or, if populated in the ESCROW.ACCOUNT, cushion period value. |
| 74 | `ESCROW.AD.INITIAL.AMOUNT` | `EscrowAnalysisDetails_InitialAmount` | TField |  | The is the amount that is calculated by using the following steps: 1) Determine the minimum running balance including both incoming payments and outgoing disbursements 2) Add the cushion amount to the minimum amount in step one 3) This sum is the initial amount that is to be deposited into the escrow balance |
| 75 | `ESCROW.AD.SHORTAGE.SURPLUS` | `EscrowAnalysisDetails_ShortageSurplus` | TField |  | The amount determined by the calculation where balance is either insufficient or in excess of the required balance under escrow processing regulations. |
| 76 | `ESCROW.AD.ACTION` | `EscrowAnalysisDetails_Action` | TField |  | This is the outcome of the escrow analysis and it reflects whether the analysis calculates a surplus or shortage, if the surplus or shortage is above or below the threshold, and the setting for that category in escrow parameter. |
| 77 | `ESCROW.AD.CURR.PI.PAYMENT.AMOUNT` | `EscrowAnalysisDetails_CurrPiPaymentAmount` | TField |  | The sum of both principal and interest portions of the loan payment on the analysis date. |
| 78 | `ESCROW.AD.CURR.ESCROW.PAYMENT` | `EscrowAnalysisDetails_CurrEscrowPayment` | TField |  | The escrow installment amount effective at the time of the analysis and to the payment effective period. |
| 79 | `ESCROW.AD.CURR.TOTAL.PYMT.AMOUNT` | `EscrowAnalysisDetails_CurrTotalPymtAmount` | TField |  | The sum of the principal, interest, and escrow portions of the loan on the analysis date. |
| 80 | `ESCROW.AD.PROJ.PI.PAYMENT.AMOUNT` | `EscrowAnalysisDetails_ProjPiPaymentAmount` | TField |  | The projected sum of both principal and interest portions of the loan payment on the analysis date. |
| 81 | `ESCROW.AD.PROJ.ESCROW.PAYMENT` | `EscrowAnalysisDetails_ProjEscrowPayment` | TField |  | The projected escrow installment amount calculated at the time of the analysis but effective only after the payment effective period. |
| 82 | `ESCROW.AD.PROJ.TOTAL.PYMT.AMOUNT` | `EscrowAnalysisDetails_ProjTotalPymtAmount` | TField |  | The projected sum of the principal, interest, and escrow portions of the loan payment on the analysis date. |
| 83 | `ESCROW.AD.ADJUST.ACTIVITY` | `EscrowAnalysisDetails_AdjustActivity` | TField |  | This activity is the subsequent processing that stems from the action value. An example is when a shortage is realized in the analysis and the shortage is made up by increasing the escrow payment. This activity would be ESCROW-INCREASE-INSTALMENT.AMOUNT. |
| 84 | `ESCROW.AD.RESERVED.10` | `EscrowAnalysisDetails_Reserved10` | TField |  |  |
| 85 | `ESCROW.AD.RESERVED.9` | `EscrowAnalysisDetails_Reserved9` | TField |  |  |
| 86 | `ESCROW.AD.RESERVED.8` | `EscrowAnalysisDetails_Reserved8` | TField |  |  |
| 87 | `ESCROW.AD.RESERVED.7` | `EscrowAnalysisDetails_Reserved7` | TField |  |  |
| 88 | `ESCROW.AD.RESERVED.6` | `EscrowAnalysisDetails_Reserved6` | TField |  |  |
| 89 | `ESCROW.AD.RESERVED.5` | `EscrowAnalysisDetails_Reserved5` | TField |  |  |
| 90 | `ESCROW.AD.RESERVED.4` | `EscrowAnalysisDetails_Reserved4` | TField |  |  |
| 91 | `ESCROW.AD.RESERVED.3` | `EscrowAnalysisDetails_Reserved3` | TField |  |  |
| 92 | `ESCROW.AD.RESERVED.2` | `EscrowAnalysisDetails_Reserved2` | TField |  |  |
| 93 | `ESCROW.AD.RESERVED.1` | `EscrowAnalysisDetails_Reserved1` | TField |  |  |
