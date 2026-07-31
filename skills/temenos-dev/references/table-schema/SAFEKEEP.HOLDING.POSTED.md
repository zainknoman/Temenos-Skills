# SAFEKEEP.HOLDING.POSTED — Table Schema

> Source: `INSERTS/I_F.SAFEKEEP.HOLDING.POSTED` in `AM_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SHD.POS.CUSTOMER` | `SafekeepHoldingPosted_Customer` | TField |  | This field contains the customer number for which fees are being posted. Validation Rules: Its a noinput field. |
| 2 | `SHD.POS.PERIOD.FROM` | `SafekeepHoldingPosted_PeriodFrom` | TField |  | Identifies the Start of the Charge Period for Safekeeping Charges. Validation Rules: Noinput field. |
| 3 | `SHD.POS.PERIOD.TO` | `SafekeepHoldingPosted_PeriodTo` | TField |  | Identifies the End Period of the Safekeeping Charge. Validation Rules: Noinput field. |
| 4 | `SHD.POS.AVG.CLOSING.BAL` | `SafekeepHoldingPosted_AvgClosingBal` | TField |  | Identifies the Average Closing Balance to be used in calculating the Safekeeping Charge. Validation Rules: Noinput field. |
| 5 | `SHD.POS.INT.MONTHS` | `SafekeepHoldingPosted_IntMonths` | TField |  | Indentifies the Period of the Safekeeping Charge in Months. Validation Rules: Noinput field. |
| 6 | `SHD.POS.CHARGES.LCY` | `SafekeepHoldingPosted_ChargesLcy` | TField |  | Identifies the system calculated Safekeeping Charge in Local Currency, for this portfolio. Validation Rules: Noinput field. |
| 7 | `SHD.POS.PREV.CHGS.LCY` | `SafekeepHoldingPosted_PrevChgsLcy` | TField |  | This field contains the charges that were present before the backvalue transaction that resulted in the recalculation of fees in local currency . Validation Rules: Noinput field. |
| 8 | `SHD.POS.DIFFERENCE.LCY` | `SafekeepHoldingPosted_DifferenceLcy` | TField |  | This field contains the difference between the previously posted charges and the new charges that have been recalculated. Validation Rules: Noinput field. |
| 9 | `SHD.POS.ACCOUNT.NO` | `SafekeepHoldingPosted_AccountNo` | TField | Yes | Identfies the Customer Account to be used to post Safekeeping Charges. Defaulted from the Sec.Acc.Master - Safekeep.Chrg.Acc Validation Rules: Mandatory Input |
| 10 | `SHD.POS.ACCOUNT.CCY` | `SafekeepHoldingPosted_AccountCcy` | TField |  | Identifies the Currency of the Account to be used to post Safekeeping Charges. Validation Rules: Noinput field. |
| 11 | `SHD.POS.CHARGES.AC.CCY` | `SafekeepHoldingPosted_ChargesAcCcy` | TField |  | Identifies the resultant Customer Safekeeping Charge. Validation Rules: Noinput field. |
| 12 | `SHD.POS.PREV.CHG.AC.CCY` | `SafekeepHoldingPosted_PrevChgAcCcy` | TField |  | This field contains the charges that were calculated prior to backvalue transaction that resulted in recalculation of safekeeping fees in the account currency. Validation Rules: Noinput field. |
| 13 | `SHD.POS.DIFFERENCE.AC.CCY` | `SafekeepHoldingPosted_DifferenceAcCcy` | TField |  | This field contains the difference between the previously calculated charges and the new calculate safekeeping charges in the account currency. Validation Rules: Noinput field. |
| 14 | `SHD.POS.ACY.LCY.RATE` | `SafekeepHoldingPosted_AcyLcyRate` | TField |  | Identifies the Exchange Rate between : Account Currency and Local Currency. Validation Rules: Noinput field. |
| 15 | `SHD.POS.LOCAL.CHG.LCY` | `SafekeepHoldingPosted_LocalChgLcy` | TField |  | Identifies the Safekeeping Charge in Local Currency Will be automatically calculated by the system. Any modification to this amount will update the SC.FEES.MODIFY file. Validation Rules: Any input must be numeric and cannot be less than zero. |
| 16 | `SHD.POS.FOREIGN.CHG.LCY` | `SafekeepHoldingPosted_ForeignChgLcy` | TField | No | Identifies the Securities Holding Depository Charge, in Local Currency Validation Rules: Optional Input. |
| 17 | `SHD.POS.DISC.AMOUNT.LCY` | `SafekeepHoldingPosted_DiscAmountLcy` | TField | No | Identifies the Discount Amount to be applied to the the calculated Safekeeping Charge. Automatically calculated by the system. Validation Rules: Optional Input. |
| 18 | `SHD.POS.CHARGES.TAX.AMT` | `SafekeepHoldingPosted_ChargesTaxAmt` | TField |  | Identifies the Tax applied to the Safekeeping Charge. Validation Rules: Noinput field. |
| 19 | `SHD.POS.CHARGES.TAX.LCY` | `SafekeepHoldingPosted_ChargesTaxLcy` | TField |  | Identifies the Tax applied to the Safekeeping Charge in Local Currency. Validation Rules: Noinput field. |
| 20 | `SHD.POS.CHARGE.CODE` | `SafekeepHoldingPosted_ChargeCode` | TField |  | Identifies the Charge Code or Group to be used for Safekeeping Charge. Defaulted from SCSK.GROUP.CONDITION - Tax.Comm.Code Validation Rules: Noinput field. |
| 21 | `SHD.POS.TAX.CODE` | `SafekeepHoldingPosted_TaxCode` | TField |  | Identfies the Tax Code used in the calculation of the Tax Amount. Tax Code is extracted from above Charge Code. Validation Rules: Noinput Field. |
| 22 | `SHD.POS.TAX.XRATE` | `SafekeepHoldingPosted_TaxXrate` | TField |  | Identifies the Exchange Rate between the Tax Amount and the Local Currency. Validation Rules: Noinput field. |
| 23 | `SHD.POS.VALUE.DATE` | `SafekeepHoldingPosted_ValueDate` | TField |  | Value Date of Safecustody Fees posting. Defaulted from SAFECUSTODY VALUES value date if process type field is set to 'periodic' otherwise uses today's date. Can be amended by the user. Validation Rules: Standard T24 date field. |
| 24 | `SHD.POS.PROCESS.STAGE` | `SafekeepHoldingPosted_ProcessStage` | TField |  | This field contains the stage the SAFEKEEP.HOLDING record has reached. It will either be 'CALCULATED' if the Safecustody fees have been calculated but not posted or 'POSTED' once the fees have been debited from the portfolio (or suspense) account. Validation Rules: No input field automatically updated by the system. |
| 25 | `SHD.POS.PROCESS.TYPE` | `SafekeepHoldingPosted_ProcessType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 26 | `SHD.POS.SYS.GENERATED` | `SafekeepHoldingPosted_SysGenerated` | TField |  | This field contains only two values YES/NO which specifies whether the record was system generated or modified bya backvalue recalculation. Validation Rules: Noinput field. |
| 27 | `SHD.POS.POST.CHARGES` | `SafekeepHoldingPosted_PostCharges` | TField |  | Y/N flag showing if the safecustody fees are ready for posting. |
| 28 | `SHD.POS.REASON.NARR` | `SafekeepHoldingPosted_ReasonNarr` |  |  |  |
| 29 | `SHD.POS.DELIVERY.KEY` | `SafekeepHoldingPosted_DeliveryKey` |  |  |  |
| 30 | `SHD.POS.ACCRUAL.KEY` | `SafekeepHoldingPosted_AccrualKey` | TField |  | System-maintained field populated only when SAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL is set to DAILY. Recorded tosupport the reversal of accounting entries following fee reversal after the fee-realisation date. |
| 31 | `SHD.POS.ADJUST.FEES` | `SafekeepHoldingPosted_AdjustFees` | TField |  |  |
| 32 | `SHD.POS.ADJUST.VALUE.DATE` | `SafekeepHoldingPosted_AdjustValueDate` | TField |  |  |
| 33 | `SHD.POS.DISCOUNT.PL` | `SafekeepHoldingPosted_DiscountPl` | TField |  |  |
| 34 | `SHD.POS.RESERVED6` | `SafekeepHoldingPosted_Reserved6` |  |  |  |
| 35 | `SHD.POS.RESERVED5` | `SafekeepHoldingPosted_Reserved5` |  |  |  |
| 36 | `SHD.POS.RESERVED4` | `SafekeepHoldingPosted_Reserved4` | TField |  |  |
| 37 | `SHD.POS.RESERVED3` | `SafekeepHoldingPosted_Reserved3` | TField |  |  |
| 38 | `SHD.POS.RESERVED2` | `SafekeepHoldingPosted_Reserved2` | TField |  |  |
| 39 | `SHD.POS.RESERVED1` | `SafekeepHoldingPosted_Reserved1` | TField |  |  |
| 40 | `SHD.POS.LOCAL.REF` | `SafekeepHoldingPosted_LocalRef` |  |  |  |
| 41 | `SHD.POS.STATEMENT.NOS` | `SafekeepHoldingPosted_StatementNos` |  |  |  |
| 42 | `SHD.POS.OVERRIDE` | `SafekeepHoldingPosted_Override` |  |  |  |
| 43 | `SHD.POS.RECORD.STATUS` | `SafekeepHoldingPosted_RecordStatus` | String |  |  |
| 44 | `SHD.POS.CURR.NO` | `SafekeepHoldingPosted_CurrNo` | String |  |  |
| 45 | `SHD.POS.INPUTTER` | `SafekeepHoldingPosted_Inputter` |  |  |  |
| 46 | `SHD.POS.DATE.TIME` | `SafekeepHoldingPosted_DateTime` |  |  |  |
| 47 | `SHD.POS.AUTHORISER` | `SafekeepHoldingPosted_Authoriser` | String |  |  |
| 48 | `SHD.POS.CO.CODE` | `SafekeepHoldingPosted_CoCode` | String |  |  |
| 49 | `SHD.POS.DEPT.CODE` | `SafekeepHoldingPosted_DeptCode` | String |  |  |
| 50 | `SHD.POS.AUDITOR.CODE` | `SafekeepHoldingPosted_AuditorCode` | String |  |  |
| 51 | `SHD.POS.AUDIT.DATE.TIME` | `SafekeepHoldingPosted_AuditDateTime` | String |  |  |
