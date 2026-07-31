# MD.BALANCES — Table Schema

> Source: `INSERTS/I_F.MD.BALANCES` in `MD_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.BAL.PRIN.BALANCE` | `MdBalances_PrinBalance` |  |  |  |
| 2 | `MD.BAL.PRIN.PART.BAL` | `MdBalances_PrinPartBal` |  |  |  |
| 3 | `MD.BAL.PRIN.EFF.DATE` | `MdBalances_PrinEffDate` |  |  |  |
| 4 | `MD.BAL.CHARGE.DATE` | `MdBalances_ChargeDate` |  |  |  |
| 5 | `MD.BAL.CHARGE.CURR` | `MdBalances_ChargeCurr` |  |  |  |
| 6 | `MD.BAL.CHARGE.ACCOUNT` | `MdBalances_ChargeAccount` |  |  |  |
| 7 | `MD.BAL.CHARGE.AMT` | `MdBalances_ChargeAmt` |  |  |  |
| 8 | `MD.BAL.REFUNDED.AMT` | `MdBalances_RefundedAmt` |  |  |  |
| 9 | `MD.BAL.CHARGE.SEQ` | `MdBalances_ChargeSeq` |  |  |  |
| 10 | `MD.BAL.CHARGE.CODE` | `MdBalances_ChargeCode` |  |  |  |
| 11 | `MD.BAL.CHG.TAX.CODE` | `MdBalances_ChgTaxCode` |  |  |  |
| 12 | `MD.BAL.CHRG.TAX.AMT` | `MdBalances_ChrgTaxAmt` |  |  |  |
| 13 | `MD.BAL.TOT.CHARGE.CCY` | `MdBalances_TotChargeCcy` |  |  |  |
| 14 | `MD.BAL.TOT.CHARGE.AMT` | `MdBalances_TotChargeAmt` |  |  |  |
| 15 | `MD.BAL.TOT.CHRG.TAX` | `MdBalances_TotChrgTax` |  |  |  |
| 16 | `MD.BAL.CURRENCY` | `MdBalances_Currency` | TField |  | Currency in which the Commission is collected, this is invariably the Deal currency. Validation Rules: Deal currency. System maintained. |
| 17 | `MD.BAL.START.CSN.PERIOD` | `MdBalances_StartCsnPeriod` | TField |  | This denotes the date from which the commission is calculated for the current cycle. Validation Rules: System Maintained. |
| 18 | `MD.BAL.END.CSN.PERIOD` | `MdBalances_EndCsnPeriod` | TField |  | This field denotes the start date of the next commission cycle. Validation Rules: System maintained. |
| 19 | `MD.BAL.COMM.BASE.AMT` | `MdBalances_CommBaseAmt` | TField |  | principal amount on which commission is calculated Incase commission rate is defined. If In case of fixed commission fixed amount is defined. |
| 20 | `MD.BAL.COMM.BASE.DATE` | `MdBalances_CommBaseDate` | TField |  | COMM.BASE.DATE This field represents the date from which the next cycle should commence when the commission is scheduled with a frequency. This ensures apt roll over of the commission period Validation Rules: System Maintained. |
| 21 | `MD.BAL.COMMISSION.AMOUNT` | `MdBalances_CommissionAmount` | TField |  | COMMISSION.AMOUNT This field holds the total amount of commission for the current commission schedule, i.e. from the START.CSN.PERIOD to END.CSN.PERIOD. Validation Rules: System Maintained. |
| 22 | `MD.BAL.CSN.ACCRUED.TODATE` | `MdBalances_CsnAccruedTodate` | TField |  | CSN.ACCRUED.TODATE The amount of commission that has been accrued (END Type) or the balance amount of commission to be amortized (BEGIN Type). Validation Rules: System Maintained. |
| 23 | `MD.BAL.ACCR.FROM.DATE` | `MdBalances_AccrFromDate` |  |  |  |
| 24 | `MD.BAL.ACCR.TO.DATE` | `MdBalances_AccrToDate` |  |  |  |
| 25 | `MD.BAL.ACCR.DAYS` | `MdBalances_AccrDays` |  |  |  |
| 26 | `MD.BAL.ACCR.PRIN` | `MdBalances_AccrPrin` |  |  |  |
| 27 | `MD.BAL.ACCR.RATE` | `MdBalances_AccrRate` |  |  |  |
| 28 | `MD.BAL.ACCR.AMT` | `MdBalances_AccrAmt` |  |  |  |
| 29 | `MD.BAL.ACCR.ACT.AMT` | `MdBalances_AccrActAmt` |  |  |  |
| 30 | `MD.BAL.PAST.SCHED.DATE` | `MdBalances_PastSchedDate` |  |  |  |
| 31 | `MD.BAL.PAST.SCHED.AMT` | `MdBalances_PastSchedAmt` |  |  |  |
| 32 | `MD.BAL.PAST.SCHED.TYPE` | `MdBalances_PastSchedType` |  |  |  |
| 33 | `MD.BAL.COMM.ACCOUNT` | `MdBalances_CommAccount` |  |  |  |
| 34 | `MD.BAL.PAST.PART.COMM` | `MdBalances_PastPartComm` |  |  |  |
| 35 | `MD.BAL.PAST.TAX.CODE` | `MdBalances_PastTaxCode` |  |  |  |
| 36 | `MD.BAL.PAST.TAX.AMT` | `MdBalances_PastTaxAmt` |  |  |  |
| 37 | `MD.BAL.PAST.PART.TAX` | `MdBalances_PastPartTax` |  |  |  |
| 38 | `MD.BAL.PAST.PROCESS.DT` | `MdBalances_PastProcessDt` |  |  |  |
| 39 | `MD.BAL.PART.COMM.AMT` | `MdBalances_PartCommAmt` | TField |  | PART.COMM.AMT Holds the total amount of commission relating to the Participants' for the Deal. Validation Rules: System Maintained. |
| 40 | `MD.BAL.COMM.TAX.AMT` | `MdBalances_CommTaxAmt` | TField |  | COMM.TAX.AMT Represents the total amount of Tax on Commission relating to the Leader on the Deal. Validation Rules: System Maintained. |
| 41 | `MD.BAL.PART.TAX.AMT` | `MdBalances_PartTaxAmt` | TField |  | PART.TAX.AMT Represents the Tax on commission relating to the Participants' on the Deal. Validation Rules: System Maintained. |
| 42 | `MD.BAL.RECALC.COMM.FLG` | `MdBalances_RecalcCommFlg` | TField |  | This field is set to YES, if commission amount is less than MIN.COMM.AMT of MD.TXN.TYPE.CONDITION and MIN.DAYS of MD.TXN.TYPE.CONDITION less than contract period. |
| 43 | `MD.BAL.NEW.CSN.RATE` | `MdBalances_NewCsnRate` | TField |  | whenever we change the rate through MD.CSN.RATE.CHANGE, this will get updated with new commission rate. |
| 44 | `MD.BAL.PART.AMT.CHG` | `MdBalances_PartAmtChg` | TField |  | represents the participant amount. |
| 45 | `MD.BAL.RATE.REVISION.DATE` | `MdBalances_RateRevisionDate` |  |  |  |
| 46 | `MD.BAL.CSN.RATE` | `MdBalances_CsnRate` |  |  |  |
| 47 | `MD.BAL.EXCESS.COMMISSION` | `MdBalances_ExcessCommission` | TField |  | This field holds the excess commission collected from the customer on account of rate change or principal movements when RETURN.COMM field is set to 'NO'. This field will reflect the cumulative excess commission amount resultant from events on various dates during the life of the contract but not returned to the customer. |
| 48 | `MD.BAL.LAST.BS.DATE` | `MdBalances_LastBsDate` | TField |  | Holds the date of last contingent BUY or SELL movement for Syndicated Guarantee done through SL.BUY.SELL application. System maintained field. |
| 49 | `MD.BAL.CSN.RF.REAL` | `MdBalances_CsnRfReal` | TField |  | Holds the realised commission amount refunded. |
| 50 | `MD.BAL.CSN.RF.UNREAL` | `MdBalances_CsnRfUnreal` | TField |  | Holds the unrealised (unamortised) commission amount refunded. |
| 51 | `MD.BAL.TOT.CSN.AMOUNT` | `MdBalances_TotCsnAmount` | TField |  | Holds the total commission amount collected. |
| 52 | `MD.BAL.CLAIM.SETTLE.AMT` | `MdBalances_ClaimSettleAmt` | TField |  | Holds the claimed commission amount settled. |
| 53 | `MD.BAL.CLAIM.WOF.AMT` | `MdBalances_ClaimWofAmt` | TField |  | Holds the claimed commission amount written off. |
| 54 | `MD.BAL.NEXT.SETTLE.ID` | `MdBalances_NextSettleId` | TField |  | Holds the next sequence number of MD.FEE.SETTLEMENT record ID. |
| 55 | `MD.BAL.CSN.EXCH.RATE` | `MdBalances_CsnExchRate` | TField |  | Records the exchange rate involved in guarantees In a guarantee if deal currency and Csn Account is inputed in foreign currency the corresponding exchange rate details will be updated in this field. While reversing the same guarantee system will take this exchange rate for reversal entries. Format : Deal currency - exchange rate * Csn Account Currency - exchange rate between deal and account currency Example : GBP-2.1*EUR-0.6667 Validation Rules: System Maintained. |
| 56 | `MD.BAL.CSN.PERIOD` | `MdBalances_CsnPeriod` | TField |  | Holds the period defined for applying the commission rate. Validation Rules: System Maintained. |
| 57 | `MD.BAL.CSN.CALC.ST.DT` | `MdBalances_CsnCalcStDt` |  |  |  |
| 58 | `MD.BAL.PRIN.AMT` | `MdBalances_PrinAmt` |  |  |  |
| 59 | `MD.BAL.CSN.CALC.END.DT` | `MdBalances_CsnCalcEndDt` |  |  |  |
| 60 | `MD.BAL.DEAL.CURRENCY` | `MdBalances_BalDealCurrency` |  |  |  |
| 61 | `MD.BAL.PRINCIPAL.AMT` | `MdBalances_BalPrincipalAmt` |  |  |  |
