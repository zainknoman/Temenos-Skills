# USCORE.ACCOUNT.HISTORY — Table Schema

> Source: `INSERTS/I_F.USCORE.ACCOUNT.HISTORY` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.AH.CUSTOMER.NO` | `UscoreAccountHistory_CustomerNo` |  |  |  |
| 2 | `US.AH.CUSTOMER.NAME` | `UscoreAccountHistory_CustomerName` |  |  |  |
| 3 | `US.AH.PRODUCT.LINE` | `UscoreAccountHistory_ProductLine` |  |  |  |
| 4 | `US.AH.PRODUCT.TYPE` | `UscoreAccountHistory_ProductType` |  |  |  |
| 5 | `US.AH.ORIGINAL.LOAN.AMT` | `UscoreAccountHistory_OriginalLoanAmt` |  |  |  |
| 6 | `US.AH.DATE.OPENED` | `UscoreAccountHistory_DateOpened` |  |  |  |
| 7 | `US.AH.MATURITY.DATE` | `UscoreAccountHistory_MaturityDate` |  |  |  |
| 8 | `US.AH.TERM` | `UscoreAccountHistory_Term` |  |  |  |
| 9 | `US.AH.ROLLOVER.DATE` | `UscoreAccountHistory_RolloverDate` |  |  |  |
| 10 | `US.AH.INTEREST.METHOD` | `UscoreAccountHistory_InterestMethod` |  |  |  |
| 11 | `US.AH.INTEREST.BASE` | `UscoreAccountHistory_InterestBase` |  |  |  |
| 12 | `US.AH.INTEREST.RATE` | `UscoreAccountHistory_InterestRate` |  |  |  |
| 13 | `US.AH.RATE.INDICATOR` | `UscoreAccountHistory_RateIndicator` |  |  |  |
| 14 | `US.AH.MARGIN` | `UscoreAccountHistory_Margin` |  |  |  |
| 15 | `US.AH.COLLATERAL.CODE` | `UscoreAccountHistory_CollateralCode` |  |  |  |
| 16 | `US.AH.LAST.TXN.DATE` | `UscoreAccountHistory_LastTxnDate` |  |  |  |
| 17 | `US.AH.LAST.POSTING.DATE` | `UscoreAccountHistory_LastPostingDate` |  |  |  |
| 18 | `US.AH.LAST.ACTIVITY.DATE` | `UscoreAccountHistory_LastActivityDate` |  |  |  |
| 19 | `US.AH.LAST.OD.DATE` | `UscoreAccountHistory_LastOdDate` |  |  |  |
| 20 | `US.AH.LAST.STMT.DATE` | `UscoreAccountHistory_LastStmtDate` |  |  |  |
| 21 | `US.AH.STATEMENT.FREQ` | `UscoreAccountHistory_StatementFreq` |  |  |  |
| 22 | `US.AH.LAST.INT.PAY.DATE` | `UscoreAccountHistory_LastIntPayDate` |  |  |  |
| 23 | `US.AH.LAST.INT.PAY.AMT` | `UscoreAccountHistory_LastIntPayAmt` |  |  |  |
| 24 | `US.AH.LAST.CREDIT.DATE` | `UscoreAccountHistory_LastCreditDate` |  |  |  |
| 25 | `US.AH.LAST.CREDIT.AMT` | `UscoreAccountHistory_LastCreditAmt` |  |  |  |
| 26 | `US.AH.ACCOUNT.STATUS` | `UscoreAccountHistory_AccountStatus` |  |  |  |
| 27 | `US.AH.NON.ACCRUAL` | `UscoreAccountHistory_NonAccrual` |  |  |  |
| 28 | `US.AH.SOLD.LOAN` | `UscoreAccountHistory_SoldLoan` |  |  |  |
| 29 | `US.AH.PARTICIPATION` | `UscoreAccountHistory_Participation` |  |  |  |
| 30 | `US.AH.INT.PAID.LAST.YEAR` | `UscoreAccountHistory_IntPaidLastYear` |  |  |  |
| 31 | `US.AH.YTD.INTEREST.PAID` | `UscoreAccountHistory_YtdInterestPaid` |  |  |  |
| 32 | `US.AH.YTD.NSF` | `UscoreAccountHistory_YtdNsf` |  |  |  |
| 33 | `US.AH.YTD.OD` | `UscoreAccountHistory_YtdOd` |  |  |  |
| 34 | `US.AH.LTD.OD` | `UscoreAccountHistory_LtdOd` |  |  |  |
| 35 | `US.AH.PAYMENT.FREQ` | `UscoreAccountHistory_PaymentFreq` |  |  |  |
| 36 | `US.AH.REGULAR.PAYMT.AMT` | `UscoreAccountHistory_RegularPaymtAmt` |  |  |  |
| 37 | `US.AH.IRA.PLAN.TYPE` | `UscoreAccountHistory_IraPlanType` |  |  |  |
| 38 | `US.AH.TAX.WITHHOLDING` | `UscoreAccountHistory_TaxWithholding` |  |  |  |
| 39 | `US.AH.PENALTY` | `UscoreAccountHistory_Penalty` |  |  |  |
| 40 | `US.AH.CHARGED.OFF.DATE` | `UscoreAccountHistory_ChargedOffDate` |  |  |  |
| 41 | `US.AH.CHARGED.OFF.BAL` | `UscoreAccountHistory_ChargedOffBal` |  |  |  |
| 42 | `US.AH.CHARGED.OFF.INT` | `UscoreAccountHistory_ChargedOffInt` |  |  |  |
| 43 | `US.AH.REBATABLE.INSURE` | `UscoreAccountHistory_RebatableInsure` |  |  |  |
| 44 | `US.AH.LATE.CHARGE.PAID` | `UscoreAccountHistory_LateChargePaid` |  |  |  |
| 45 | `US.AH.TIMES.PAST.DUE` | `UscoreAccountHistory_TimesPastDue` |  |  |  |
| 46 | `US.AH.CENSUS.TRACT` | `UscoreAccountHistory_CensusTract` |  |  |  |
| 47 | `US.AH.ESCROW.PAYEE` | `UscoreAccountHistory_EscrowPayee` |  |  |  |
| 48 | `US.AH.PAYMENT.AMOUNT` | `UscoreAccountHistory_PaymentAmount` |  |  |  |
| 49 | `US.AH.LAST.DISB.DATE` | `UscoreAccountHistory_LastDisbDate` |  |  |  |
| 50 | `US.AH.LAST.DISB.AMT` | `UscoreAccountHistory_LastDisbAmt` |  |  |  |
| 51 | `US.AH.REMARKS` | `UscoreAccountHistory_Remarks` |  |  |  |
| 52 | `US.AH.OFFICER` | `UscoreAccountHistory_Officer` |  |  |  |
| 53 | `US.AH.BRANCH` | `UscoreAccountHistory_Branch` |  |  |  |
| 54 | `US.AH.RESERVED.20` | `UscoreAccountHistory_Reserved20` |  |  |  |
| 55 | `US.AH.RESERVED.19` | `UscoreAccountHistory_Reserved19` |  |  |  |
| 56 | `US.AH.RESERVED.18` | `UscoreAccountHistory_Reserved18` |  |  |  |
| 57 | `US.AH.RESERVED.17` | `UscoreAccountHistory_Reserved17` |  |  |  |
| 58 | `US.AH.RESERVED.16` | `UscoreAccountHistory_Reserved16` |  |  |  |
| 59 | `US.AH.RESERVED.15` | `UscoreAccountHistory_Reserved15` |  |  |  |
| 60 | `US.AH.RESERVED.14` | `UscoreAccountHistory_Reserved14` |  |  |  |
| 61 | `US.AH.RESERVED.13` | `UscoreAccountHistory_Reserved13` |  |  |  |
| 62 | `US.AH.RESERVED.12` | `UscoreAccountHistory_Reserved12` |  |  |  |
| 63 | `US.AH.RESERVED.11` | `UscoreAccountHistory_Reserved11` |  |  |  |
| 64 | `US.AH.RESERVED.10` | `UscoreAccountHistory_Reserved10` |  |  |  |
| 65 | `US.AH.RESERVED.9` | `UscoreAccountHistory_Reserved9` |  |  |  |
| 66 | `US.AH.RESERVED.8` | `UscoreAccountHistory_Reserved8` |  |  |  |
| 67 | `US.AH.RESERVED.7` | `UscoreAccountHistory_Reserved7` |  |  |  |
| 68 | `US.AH.RESERVED.6` | `UscoreAccountHistory_Reserved6` |  |  |  |
| 69 | `US.AH.RESERVED.5` | `UscoreAccountHistory_Reserved5` |  |  |  |
| 70 | `US.AH.RESERVED.4` | `UscoreAccountHistory_Reserved4` |  |  |  |
| 71 | `US.AH.RESERVED.3` | `UscoreAccountHistory_Reserved3` |  |  |  |
| 72 | `US.AH.RESERVED.2` | `UscoreAccountHistory_Reserved2` |  |  |  |
| 73 | `US.AH.RESERVED.1` | `UscoreAccountHistory_Reserved1` |  |  |  |
