# SC.TRAIL.FEES.HOLDING — Table Schema

> Source: `INSERTS/I_F.SC.TRAIL.FEES.HOLDING` in `SC_ScfTrailerFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TFH.ISSUER` | `ScTrailFeesHolding_Issuer` | TField |  | Specifies the ISSUER for whom the holding is been created. Validation Rules: No input field. Updated by the system |
| 2 | `SC.TFH.PERIOD.START` | `ScTrailFeesHolding_PeriodStart` | TField |  | Specifies start date for which the holding record is been created. It is updated by system with the LAST.PAY.DATE set in corresponding SC.TRAIL.FEES.ARRANGEMENT record. Validation Rules: No input field. Updated by the system |
| 3 | `SC.TFH.PERIOD.END` | `ScTrailFeesHolding_PeriodEnd` | TField |  | Specifies end date for which the holding record is been created. It is updated by the system with the NEXT.PAY.DATE set in corresponding SC.TRAIL.FEES.ARRANGEMENT record. Validation Rules: No input field. Updated by the system |
| 4 | `SC.TFH.CALC.CCY` | `ScTrailFeesHolding_CalcCcy` |  |  |  |
| 5 | `SC.TFH.XRATE.CALC.PAY` | `ScTrailFeesHolding_XrateCalcPay` |  |  |  |
| 6 | `SC.TFH.AMT.IN.CALC.CCY` | `ScTrailFeesHolding_AmtInCalcCcy` |  |  |  |
| 7 | `SC.TFH.AMT.IN.PAY.CCY` | `ScTrailFeesHolding_AmtInPayCcy` |  |  |  |
| 8 | `SC.TFH.DIFF.AMT.CALC.CCY` | `ScTrailFeesHolding_DiffAmtCalcCcy` |  |  |  |
| 9 | `SC.TFH.DIFF.AMT.PAY.CCY` | `ScTrailFeesHolding_DiffAmtPayCcy` |  |  |  |
| 10 | `SC.TFH.ACT.CALC.AMT` | `ScTrailFeesHolding_ActCalcAmt` | TField |  | This field is updated by the system with the actual calculated trailer fee amount in pay currency for this payment period Validation Rules: This is a Noinput field and is defaulted by the system |
| 11 | `SC.TFH.RECALCULATED.AMT` | `ScTrailFeesHolding_RecalculatedAmt` | TField |  | This field holds the recalculated trailer fee amount when a back valuation process is triggered Validation Rules: This is a Noinput field and is defaulted by the system |
| 12 | `SC.TFH.RESERVED6` | `ScTrailFeesHolding_Reserved6` |  |  |  |
| 13 | `SC.TFH.PAYMENT.CCY` | `ScTrailFeesHolding_PaymentCcy` | TField |  | System defaults the currency of the account mentioned in PAYMENT.ACCOUNT field. Validation Rules: No input field. Updated by the system |
| 14 | `SC.TFH.XRATE.PAY.LCY` | `ScTrailFeesHolding_XratePayLcy` | TField |  | Specifies the exchange rate applicable between the payment currency and local currency. Validation Rules: This is a single value field. 1-10 numeric characters &amp; "." (1-6 integers and 1-9 decimal places). |
| 15 | `SC.TFH.PAYMENT.AMT` | `ScTrailFeesHolding_PaymentAmt` | TField |  | This field used to capture the payment amount received from the issuer. |
| 16 | `SC.TFH.DIFF.AMT` | `ScTrailFeesHolding_DiffAmt` | TField |  | This is the difference between the PAYMENT.AMT and the ACT.CALC.AMT which is expressed in Payment currency. This field is populated only when the payment is marked as �COMPLETE� Validation Rules: This is a single value and Noinput field. |
| 17 | `SC.TFH.NARRATIVE` | `ScTrailFeesHolding_Narrative` | TField |  | Multi Value No Input field which is used to store any comments or free format narrative concerning the customer or the transaction. Free Format narrative text. Up to 35 maximum characters per line. |
| 18 | `SC.TFH.THRESHOLD.AMT` | `ScTrailFeesHolding_ThresholdAmt` | TField |  | Specifies the Threshold amount and it gets defaulted from the corresponding issuer level arrangement. If the difference amount is within the threshold amount, single entry will be raised for the issuer receivable account against Profit &amp; Loss booked for the issuer. If the difference amount is not within the threshold amount then adjustment entries is raised against individual client level The functionality of this field is effective only if the payment is marked as �COMPLETE�. Validation Rules: This is a single value field which accepts numeric character |
| 19 | `SC.TFH.OUTS.UNSETT.AMT` | `ScTrailFeesHolding_OutsUnsettAmt` | TField |  | Specifies the outstanding amount that is due from the Issuer Validation Rules: This is a singe value and Noinput field which gets defaulted by the system. |
| 20 | `SC.TFH.SETTLED.AMT` | `ScTrailFeesHolding_SettledAmt` | TField |  | Specifies the total amount paid by the Issuer Validation Rules: This is a Noinput field which gets defaulted by the system. |
| 21 | `SC.TFH.SETT.STATUS` | `ScTrailFeesHolding_SettStatus` | TField |  | Specifies whether the payment made is partial or complete. If SETT.STATUS is marked as Complete, then there cannot be any further payments and adjustment entries will be raised (if there is any difference between the actual amount due and the received amount). System automatically marks the payment as COMPLETE, if the payment amount is exactly equal to the amount due. Validation Rules: This is a single value field and the valid input is �COMPLETE� |
| 22 | `SC.TFH.RECEIVABLE.ACCOUNT` | `ScTrailFeesHolding_ReceivableAccount` | TField |  | This field defaults the account from SC.TRAIL.FEES.ARRANGEMENT application. |
| 23 | `SC.TFH.TAX.CODE` | `ScTrailFeesHolding_TaxCode` |  |  |  |
| 24 | `SC.TFH.TAX.CALC.CCY` | `ScTrailFeesHolding_TaxCalcCcy` |  |  |  |
| 25 | `SC.TFH.TAX.PAY.CCY` | `ScTrailFeesHolding_TaxPayCcy` |  |  |  |
| 26 | `SC.TFH.TAX.PAY.LCY` | `ScTrailFeesHolding_TaxPayLcy` |  |  |  |
| 27 | `SC.TFH.DIFF.TAX` | `ScTrailFeesHolding_DiffTax` |  |  |  |
| 28 | `SC.TFH.ACT.TAX.PAY.CCY` | `ScTrailFeesHolding_ActTaxPayCcy` |  |  |  |
| 29 | `SC.TFH.RESERVED3` | `ScTrailFeesHolding_Reserved3` | TField |  |  |
| 30 | `SC.TFH.RESERVED4` | `ScTrailFeesHolding_Reserved4` | TField |  |  |
| 31 | `SC.TFH.RESERVED5` | `ScTrailFeesHolding_Reserved5` | TField |  |  |
| 32 | `SC.TFH.AMT.DUE.CALC.CCY` | `ScTrailFeesHolding_AmtDueCalcCcy` | TField |  | This field will not be updated anymore due to multiple calculated currencies Validation Rules: No input field. Updated by the system |
| 33 | `SC.TFH.AMT.DUE.PAY.CCY` | `ScTrailFeesHolding_AmtDuePayCcy` | TField |  | This field holds the amount expected from Issuer in payment currency. This is part of TAX.CODE multi value set Validation Rules: No input field. Updated by the system |
| 34 | `SC.TFH.INCL.EXCL` | `ScTrailFeesHolding_InclExcl` | TField |  | Field to hold values INCLUSIVE or EXCLUSIVE This field will be defaulted from SC.TRAIL.FEES.ARRANGEMENT record when SC.TRAIL.FEES.HOLDING is created on payment date Validation Rules: No input field. Updated by the system |
| 35 | `SC.TFH.FUND.ID` | `ScTrailFeesHolding_FundId` |  |  |  |
| 36 | `SC.TFH.AVG.RECAL.PRICE` | `ScTrailFeesHolding_AvgRecalPrice` |  |  |  |
| 37 | `SC.TFH.RECAL.WITH.AP` | `ScTrailFeesHolding_RecalWithAp` | TField |  | This field is to trigger recalculation and accepts value YES Validation Rules: Cannot amend the Value YES to blank after authorisation of record with value YES Not applicable for calculation formula except 1 and 4 RECAL.WITH.AP as YES and SETT.STATUS as COMPLETE, both cannot be done at the same time |
| 38 | `SC.TFH.RESERVED7` | `ScTrailFeesHolding_Reserved7` | TField |  |  |
| 39 | `SC.TFH.RESERVED8` | `ScTrailFeesHolding_Reserved8` | TField |  |  |
| 40 | `SC.TFH.RESERVED9` | `ScTrailFeesHolding_Reserved9` | TField |  |  |
| 41 | `SC.TFH.RESERVED10` | `ScTrailFeesHolding_Reserved10` | TField |  |  |
| 42 | `SC.TFH.RESERVED11` | `ScTrailFeesHolding_Reserved11` | TField |  |  |
| 43 | `SC.TFH.RESERVED12` | `ScTrailFeesHolding_Reserved12` | TField |  |  |
| 44 | `SC.TFH.RESERVED13` | `ScTrailFeesHolding_Reserved13` | TField |  |  |
| 45 | `SC.TFH.RESERVED14` | `ScTrailFeesHolding_Reserved14` | TField |  |  |
| 46 | `SC.TFH.RESERVED15` | `ScTrailFeesHolding_Reserved15` | TField |  |  |
| 47 | `SC.TFH.LOCAL.REF` | `ScTrailFeesHolding_LocalRef` |  |  |  |
| 48 | `SC.TFH.STMT.NOS` | `ScTrailFeesHolding_StmtNos` |  |  |  |
| 49 | `SC.TFH.OVERRIDE` | `ScTrailFeesHolding_Override` |  |  |  |
| 50 | `SC.TFH.RECORD.STATUS` | `ScTrailFeesHolding_RecordStatus` | String |  |  |
| 51 | `SC.TFH.CURR.NO` | `ScTrailFeesHolding_CurrNo` | String |  |  |
| 52 | `SC.TFH.INPUTTER` | `ScTrailFeesHolding_Inputter` |  |  |  |
| 53 | `SC.TFH.DATE.TIME` | `ScTrailFeesHolding_DateTime` |  |  |  |
| 54 | `SC.TFH.AUTHORISER` | `ScTrailFeesHolding_Authoriser` | String |  |  |
| 55 | `SC.TFH.CO.CODE` | `ScTrailFeesHolding_CoCode` | String |  |  |
| 56 | `SC.TFH.DEPT.CODE` | `ScTrailFeesHolding_DeptCode` | String |  |  |
| 57 | `SC.TFH.AUDITOR.CODE` | `ScTrailFeesHolding_AuditorCode` | String |  |  |
| 58 | `SC.TFH.AUDIT.DATE.TIME` | `ScTrailFeesHolding_AuditDateTime` | String |  |  |
