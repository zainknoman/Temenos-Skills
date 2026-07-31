# SWAP.BALANCES — Table Schema

> Source: `INSERTS/I_F.SWAP.BALANCES` in `SW_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SW.BAL.CURRENCY` | `SwapBalances_Currency` | TField |  | This field denotes the currency code of the associated Swap leg. Validation Rules: 3 Alpha-numeric currency code (type CCY). (No-input field. Automatically updated). Must be a valid CURRENCY code. |
| 2 | `SW.BAL.NOTIONAL` | `SwapBalances_Notional` | TField |  | This field indicates whether the outstanding principal is notional or real. o "Y" signifies a Notional principal amount. o "NO" signifies a Real principal amount. The principal amount will remain notional until a PX (Principal Exchange) schedule has been processed on the Swap leg. This field is automatically updated. Validation Rules: 2 Alphanumric characters. (No-input field. Valid types : "Y"_"NO"). |
| 3 | `SW.BAL.PRINCIPAL` | `SwapBalances_Principal` |  |  |  |
| 4 | `SW.BAL.PRIN.DATE` | `SwapBalances_PrinDate` |  |  |  |
| 5 | `SW.BAL.EFFECTIVE.DATE` | `SwapBalances_EffectiveDate` |  |  |  |
| 6 | `SW.BAL.INTEREST.KEY` | `SwapBalances_InterestKey` |  |  |  |
| 7 | `SW.BAL.INTEREST.RATE` | `SwapBalances_InterestRate` |  |  |  |
| 8 | `SW.BAL.MKT.INT.RATE` | `SwapBalances_MktIntRate` |  |  |  |
| 9 | `SW.BAL.INTEREST.AMOUNT` | `SwapBalances_InterestAmount` | TField |  | This field records the total amount of unpaid interest due (accrued) for the current interest period. As interest is accrued, the details of each accrual are stored in the multivalue accrual fields (ACCR.FROM.DATE - ACCR.ACT.AMT). This field contains the total of accrued interest in the current period. This is equal to the sum of the multivalues in the ACCR.AMT field whose corresponding ACCR.FROM.DATE is greater than or equal to the START.INT.PERIOD date. Validation Rules: 1 to 19 Numeric characters (type AMT). (No-input field). |
| 10 | `SW.BAL.MKT.INT.AMOUNT` | `SwapBalances_MktIntAmount` | TField |  | It contains the Interest Amount of the Market Exchange for the current period As interest is accrued, the details of each accrual are stored in the multivalue accrual fields (ACCR.FROM.DATE - MKT.ACT.AMT). This field contains the total of accrued interest in the current period. This is equal to the sum of the multivalues in the MKT.ACCR.AMT field whose corresponding ACCR.FROM.DATE is greater than or equal to the START.INT.PERIOD date. Validation Rules: 1 to 19 Numeric characters (type AMT). |
| 11 | `SW.BAL.START.INT.PERIOD` | `SwapBalances_StartIntPeriod` | TField |  | Identifies the start date of the current interest period. This field records the date from which interest will be accrued for the current interest period. The end of this period is defined in theEND.INT.PERIOD field. This field is cycled automatically by the end of day batch processing whenever an interest payment is made. The START.INT.PERDIO date will then become equal to the END.INT.PERIOD date of the period processed. Validation Rules: 11 Numeric Character field (standard date format). (No-input field). |
| 12 | `SW.BAL.END.INT.PERIOD` | `SwapBalances_EndIntPeriod` | TField |  | Identifies the end date of current interest period. This field defines the date on which the interest accrued in the current interest period is to be settled. Accruals for the current interest period commence on the date held in the START.INT.PERIOD field. The date in this field will be cycled automatically by the end of day batch process whenever an interest payment is made. It is updated with the next interest payment date as defined on the Swap contract. The old date from this field then becomes the START.INT.PERIOD date for the coming period. Validation Rules: 11 Numeric Character field (standard date format). (No-input field). |
| 13 | `SW.BAL.TOT.INT.AMT` | `SwapBalances_TotIntAmt` | TField |  | This represents the Total Interest Amount Payable/Receivable on the Asset/Liability Leg of the SWAP Contract from value date till maturity date. This is different from the field Interest.Amount of the SWAP.BALANCES which holds the interest amount for the current period only. Validation Rules: 1 to 19 Numeric characters (type AMT). |
| 14 | `SW.BAL.TOT.MKT.INT.AMT` | `SwapBalances_TotMktIntAmt` | TField |  | This field contains the Total Interest Amount(Net interest) of the Market Exchange. Validation Rules: 1 to 19 Numeric characters (type AMT). |
| 15 | `SW.BAL.ACCR.FROM.DATE` | `SwapBalances_AccrFromDate` |  |  |  |
| 16 | `SW.BAL.ACCR.TO.DATE` | `SwapBalances_AccrToDate` |  |  |  |
| 17 | `SW.BAL.ACCR.DAYS` | `SwapBalances_AccrDays` |  |  |  |
| 18 | `SW.BAL.ACCR.PRIN` | `SwapBalances_AccrPrin` |  |  |  |
| 19 | `SW.BAL.ACCR.RATE` | `SwapBalances_AccrRate` |  |  |  |
| 20 | `SW.BAL.ACCR.AMT` | `SwapBalances_AccrAmt` |  |  |  |
| 21 | `SW.BAL.ACCR.ACT.AMT` | `SwapBalances_AccrActAmt` |  |  |  |
| 22 | `SW.BAL.MKT.ACCR.RATE` | `SwapBalances_MktAccrRate` |  |  |  |
| 23 | `SW.BAL.MKT.ACCR.AMT` | `SwapBalances_MktAccrAmt` |  |  |  |
| 24 | `SW.BAL.MKT.ACT.AMT` | `SwapBalances_MktActAmt` |  |  |  |
| 25 | `SW.BAL.AMORT.SCHEDULE` | `SwapBalances_AmortSchedule` |  |  |  |
| 26 | `SW.BAL.AMORT.AMOUNT` | `SwapBalances_AmortAmount` |  |  |  |
| 27 | `SW.BAL.AMORT.START` | `SwapBalances_AmortStart` |  |  |  |
| 28 | `SW.BAL.AMORT.END` | `SwapBalances_AmortEnd` |  |  |  |
| 29 | `SW.BAL.AMORT.TO.DATE` | `SwapBalances_AmortToDate` |  |  |  |
| 30 | `SW.BAL.SCHEDULE.TYPE` | `SwapBalances_ScheduleType` |  |  |  |
| 31 | `SW.BAL.CHARGE.CODE` | `SwapBalances_ChargeCode` |  |  |  |
| 32 | `SW.BAL.SCHEDULE.DATE` | `SwapBalances_ScheduleDate` |  |  |  |
| 33 | `SW.BAL.PROCESS.DATE` | `SwapBalances_ProcessDate` |  |  |  |
| 34 | `SW.BAL.PERIOD.START` | `SwapBalances_PeriodStart` |  |  |  |
| 35 | `SW.BAL.PERIOD.END` | `SwapBalances_PeriodEnd` |  |  |  |
| 36 | `SW.BAL.SCHED.EFF.DATE` | `SwapBalances_SchedEffDate` |  |  |  |
| 37 | `SW.BAL.CCY.AMOUNT` | `SwapBalances_CcyAmount` |  |  |  |
| 38 | `SW.BAL.MKT.CCY.AMT` | `SwapBalances_MktCcyAmt` |  |  |  |
| 39 | `SW.BAL.RESET.RATE` | `SwapBalances_ResetRate` |  |  |  |
| 40 | `SW.BAL.LCL.AMOUNT` | `SwapBalances_LclAmount` |  |  |  |
| 41 | `SW.BAL.AMOUNT.DIFF` | `SwapBalances_AmountDiff` |  |  |  |
| 42 | `SW.BAL.VALUE.DATE` | `SwapBalances_ValueDate` |  |  |  |
| 43 | `SW.BAL.CRB.VALUE.DATE` | `SwapBalances_CrbValueDate` | TField |  | Identifies the CRB recorded value date for the contract. Validation Rules: 11 Character field (standard date format). (No-input field). |
| 44 | `SW.BAL.CRB.MATURITY.DATE` | `SwapBalances_CrbMaturityDate` | TField |  | Identifies the CRB recorded maturity date of the contract. Validation Rules: 11 Character field (standard date format). (No-input field). |
| 45 | `SW.BAL.CRB.INTEREST.DATE` | `SwapBalances_CrbInterestDate` | TField |  | Identifies the CRB recorded next interest date of the contract. Validation Rules: 11 Character field (standard date format). (No-input field). |
| 46 | `SW.BAL.CONSOL.KEY` | `SwapBalances_ConsolKey` | TField |  | Identifies the associated CRB consol key. This key is the reference to the CONSOLIDATE.ASST.LIAB file. Validation Rules: 1 to 16 Alpha-numeric characters. (No-input field). |
| 47 | `SW.BAL.INITIAL.XRATE` | `SwapBalances_InitialXrate` | TField |  | This field is populated when a 'PX' schedule is processed and the contract must be OFF balance sheet. It will hold the exchange rate between the leg currency and the local currency and is used to derive the local currency equivalent of the base currency of the swap contract. Validation Rules: Standard T24 rate field. |
| 48 | `SW.BAL.OUTS.PRIN.LCY` | `SwapBalances_OutsPrinLcy` | TField |  | It holds the principal outstanding in local currency. All principal movements will update this field. Validation Rules: 1-19 type AMT (standard amount format) characters plus a decimal point. |
| 49 | `SW.BAL.CCY.REVAL.PL` | `SwapBalances_CcyRevalPl` | TField |  | This field holds the net amount which has been posted as unrealised P&amp;L in local currency. The amount is derived by the formula:- Principal outstanding * (current.xrate - initial.xrate) Validation Rules: 1-19 type AMT (standard amount format) characters plus a decimal point. |
| 50 | `SW.BAL.NPV` | `SwapBalances_Npv` | TField |  | The Net Present Value of this leg. Validation Rules: 1-19 Type AMT numeric characters |
| 51 | `SW.BAL.NPV.LCY` | `SwapBalances_NpvLcy` | TField |  | The Net Present Value local equivalent of this leg. Validation Rules: 1-19 Type AMT numeric characters |
| 52 | `SW.BAL.POSITION.DATE` | `SwapBalances_PositionDate` |  |  |  |
| 53 | `SW.BAL.POSITION.FCY` | `SwapBalances_PositionFcy` |  |  |  |
| 54 | `SW.BAL.POSITION.LCY` | `SwapBalances_PositionLcy` |  |  |  |
| 55 | `SW.BAL.CONF.SENT` | `SwapBalances_ConfSent` | TField |  | This field indicates that the contract initiation activity is done and confirmation is generated for this leg. Validation rules: System generated field. When confirmation is sent, it would default to Y. |
| 56 | `SW.BAL.OLD.OUTS.PRIN.LCY` | `SwapBalances_OldOutsPrinLcy` | TField |  | It holds the principal outstanding in local currency as on the previous day. Value available in the field OUTS.PRIN.LCY is moved to this field before SWAP Currency Revaluation is done. Used for reports. Validation Rules: 1-19 type AMT (standard amount format) characters plus a decimal point. |
| 57 | `SW.BAL.NPV.BEF.ACC.ADJ` | `SwapBalances_NpvBefAccAdj` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 58 | `SW.BAL.NPV.BEF.ADJ.LCY` | `SwapBalances_NpvBefAdjLcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 59 | `SW.BAL.NPV.INC.TDY.IP` | `SwapBalances_NpvInclTodayIp` |  |  |  |
| 60 | `SW.BAL.NPV.INC.TDY.IPLCY` | `SwapBalances_NpvInclTodayIpLcy` |  |  |  |
| 61 | `SW.BAL.CCY.REVAL.FCY` | `SwapBalances_CcyRevalFcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 62 | `SW.BAL.PO.SENT` | `SwapBalances_PoSent` | TField |  |  |
| 63 | `SW.BAL.DP.PAYMENT.DT` | `SwapBalances_DpPaymentDt` | TField |  | Contains the payment delay date of recently processed interest payment schedule. This is a technical field for processing DP schedules. |
| 64 | `SW.BAL.DP.PAYMENT.AMT` | `SwapBalances_DpPaymentAmt` | TField |  | Contains the recently processed interest payment amount. This is a technical field for processing DP schedules. |
| 65 | `SW.BAL.DP.FINAL.RATE` | `SwapBalances_DpFinalRate` | TField |  | This field holds YES or NO based on the final rate availability of the recently processed interest payment schedule defined with payment delay. This is a technical field for processing DP schedules. |
| 66 | `SW.BAL.DP.MSG.GENERATED` | `SwapBalances_DpMsgGenerated` | TField |  | This field holds YES or NO based on the whether the message is generated for the recently processed interest payment schedule defined with payment delay. This is a technical field for processing the DP schedules. |
| 67 | `SW.BAL.DP.ADJ.AMT` | `SwapBalances_DpAdjAmt` | TField |  | This field contains adjustment accrual amount. It is the difference between the previous DP.PAYMENT.AMT and the current DP.PAYMENT.AMT due to rate change. This is a technical field for processing DP schedules. |
| 68 | `SW.BAL.RESERVED.14` | `SwapBalances_Reserved14` | TField |  |  |
| 69 | `SW.BAL.RESERVED.13` | `SwapBalances_Reserved13` | TField |  |  |
| 70 | `SW.BAL.RESERVED.12` | `SwapBalances_Reserved12` | TField |  |  |
| 71 | `SW.BAL.RESERVED.11` | `SwapBalances_Reserved11` | TField |  |  |
| 72 | `SW.BAL.RESERVED.10` | `SwapBalances_Reserved10` | TField |  |  |
| 73 | `SW.BAL.RESERVED.9` | `SwapBalances_Reserved9` | TField |  |  |
| 74 | `SW.BAL.RESERVED.8` | `SwapBalances_Reserved8` | TField |  |  |
| 75 | `SW.BAL.RESERVED.7` | `SwapBalances_Reserved7` | TField |  |  |
| 76 | `SW.BAL.RESERVED.6` | `SwapBalances_Reserved6` | TField |  |  |
| 77 | `SW.BAL.RESERVED.5` | `SwapBalances_Reserved5` | TField |  |  |
| 78 | `SW.BAL.RESERVED.4` | `SwapBalances_Reserved4` | TField |  |  |
| 79 | `SW.BAL.RESERVED.3` | `SwapBalances_Reserved3` | TField |  |  |
| 80 | `SW.BAL.RESERVED.2` | `SwapBalances_Reserved2` | TField |  |  |
| 81 | `SW.BAL.RESERVED.1` | `SwapBalances_Reserved1` | TField |  |  |
