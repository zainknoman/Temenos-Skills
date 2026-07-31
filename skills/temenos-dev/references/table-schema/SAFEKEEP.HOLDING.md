# SAFEKEEP.HOLDING — Table Schema

> Source: `INSERTS/I_F.SAFEKEEP.HOLDING` in `SC_ScfSafekeepingFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SHD.CUSTOMER` | `SafekeepHolding_Customer` | TField |  | Identifies the Customer Number of the Portfolio. Validation Rules: Noinput field. |
| 2 | `SC.SHD.PERIOD.FROM` | `SafekeepHolding_PeriodFrom` | TField |  | Identifies the Start of the Charge Period for Safekeeping Charges. Validation Rules: Noinput field. |
| 3 | `SC.SHD.PERIOD.TO` | `SafekeepHolding_PeriodTo` | TField |  | Identifies the End Period of the Safekeeping Charge. Validation Rules: Noinput field. |
| 4 | `SC.SHD.AVG.CLOSING.BAL` | `SafekeepHolding_AvgClosingBal` | TField |  | Identifies the Average Security Balance to be used in calculating the Safekeeping Charge. The AVG.CLOSING.BAL is always reported in the reference currency of the portfolio. Validation Rules: Noinput field. |
| 5 | `SC.SHD.INT.MONTHS` | `SafekeepHolding_IntMonths` | TField |  | Indentifies the Period of the Safekeeping Charge in Months. Validation Rules: Noinput field. |
| 6 | `SC.SHD.CHARGES.LCY` | `SafekeepHolding_ChargesLcy` | TField |  | Identifies the system calculated Safekeeping Charge in Local Currency, for this portfolio. Validation Rules: Noinput field. |
| 7 | `SC.SHD.ACCOUNT.NO` | `SafekeepHolding_AccountNo` | TField | Yes | Identfies the Customer Account to be used to post Safekeeping Charges. Defaulted from the Sec.Acc.Master - Safekeep.Chrg.Acc Validation Rules: Mandatory Input. |
| 8 | `SC.SHD.ACCOUNT.CCY` | `SafekeepHolding_AccountCcy` | TField |  | Identifies the Currency of the Account to be used to post Safekeeping Charges. Validation Rules: Noinput field. |
| 9 | `SC.SHD.CHARGES.AC.CCY` | `SafekeepHolding_ChargesAcCcy` | TField |  | Identifies the resultant Customer Safekeeping Charge. Validation Rules: Noinput field. |
| 10 | `SC.SHD.ACY.LCY.RATE` | `SafekeepHolding_AcyLcyRate` | TField |  | Identifies the Exchange Rate between : Account Currency and Local Currency. Validation Rules: Noinput field. |
| 11 | `SC.SHD.LOCAL.CHG.LCY` | `SafekeepHolding_LocalChgLcy` | TField |  | Identifies the Safekeeping Charge in Local Currency Will be automatically calculated by the system. Any modification to this amount will update the SC.FEES.MODIFYfile. Validation Rules: Any input must be numeric and cannot be less than zero. |
| 12 | `SC.SHD.FOREIGN.CHG.LCY` | `SafekeepHolding_ForeignChgLcy` | TField | No | Identifies the Securities Holding Depository Charge, in Local Currency Validation Rules: Optional Input. |
| 13 | `SC.SHD.DISC.AMOUNT.LCY` | `SafekeepHolding_DiscAmountLcy` | TField | No | Identifies the Discount Amount to be applied to the the calculated Safekeeping Charge. Automatically calculated by the system. Validation Rules: Optional Input. |
| 14 | `SC.SHD.CHARGES.TAX.AMT` | `SafekeepHolding_ChargesTaxAmt` | TField |  | Identifies the Tax applied to the Safekeeping Charge. Validation Rules: Noinput field. |
| 15 | `SC.SHD.CHARGES.TAX.LCY` | `SafekeepHolding_ChargesTaxLcy` | TField |  | Identifies the Tax applied to the Safekeeping Charge in Local Currency. Validation Rules: Noinput field. |
| 16 | `SC.SHD.CHARGE.CODE` | `SafekeepHolding_ChargeCode` | TField |  | Identifies the Charge Code or Group to be used for Safekeeping Charge. Defaulted from SCSK.GROUP.CONDITION - Tax.Comm.Code Validation Rules: Noinput field. |
| 17 | `SC.SHD.TAX.CODE` | `SafekeepHolding_TaxCode` | TField |  | Identfies the Tax Code used in the calculation of the Tax Amount. Tax Code is extracted from above Charge Code. Validation Rules: Noinput Field. |
| 18 | `SC.SHD.TAX.XRATE` | `SafekeepHolding_TaxXrate` | TField |  | Identifies the Exchange Rate between the Tax Amount and the Local Currency. Validation Rules: Noinput field. |
| 19 | `SC.SHD.VALUE.DATE` | `SafekeepHolding_ValueDate` | TField |  | Value Date of Safecustody Fees posting. Defaulted from SAFECUSTODY VALUES value date if process type field is setto 'periodic' otherwise uses today's date. Can be amended by the user. Validation Rules: Standard T24 date field. |
| 20 | `SC.SHD.PROCESS.STAGE` | `SafekeepHolding_ProcessStage` | TField |  | This field contains the stage the SAFEKEEP.HOLDING record has reached. It will either be 'CALCULATED' if theSafecustody fees have been calculated but not posted or 'POSTED' once the fees have been debited from the portfolio(or suspense) account. Validation Rules: No input field automatically updated by the system. |
| 21 | `SC.SHD.PROCESS.TYPE` | `SafekeepHolding_ProcessType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 20 characters may be entered. This is a no input, no copy field. |
| 22 | `SC.SHD.POST.CHARGES` | `SafekeepHolding_PostCharges` | TField |  | Y/N flag showing if the safecustody fees are ready for posting. |
| 23 | `SC.SHD.REASON.NARR` | `SafekeepHolding_ReasonNarr` |  |  |  |
| 24 | `SC.SHD.GRP.PORT.NO` | `SafekeepHolding_GrpPortNo` | TField |  | Primary portfolio id for the group to which this portfolio belongs |
| 25 | `SC.SHD.GRP.ASSET.BAL` | `SafekeepHolding_GrpAssetBal` | TField |  | Asset balance for the group to which this portfolio belongs |
| 26 | `SC.SHD.GRP.LCY.FEE` | `SafekeepHolding_GrpLcyFee` | TField |  | Local fee total for the group to which this portfolio belongs |
| 27 | `SC.SHD.GRP.FCY.FEE` | `SafekeepHolding_GrpFcyFee` | TField |  | Foreign fee total for the group to which this portfolio belongs |
| 28 | `SC.SHD.MTH.END.DATE` | `SafekeepHolding_MthEndDate` |  |  |  |
| 29 | `SC.SHD.MTH.LOCAL.LCY` | `SafekeepHolding_MthLocalLcy` |  |  |  |
| 30 | `SC.SHD.MTH.FOREIGN.LCY` | `SafekeepHolding_MthForeignLcy` |  |  |  |
| 31 | `SC.SHD.MTH.XRATE` | `SafekeepHolding_MthXrate` |  |  |  |
| 32 | `SC.SHD.MTH.LOCAL.ACY` | `SafekeepHolding_MthLocalAcy` |  |  |  |
| 33 | `SC.SHD.MTH.FOREIGN.ACY` | `SafekeepHolding_MthForeignAcy` |  |  |  |
| 34 | `SC.SHD.ACCRUAL.KEY` | `SafekeepHolding_AccrualKey` | TField |  | System-maintained field populated only when SAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL is set to DAILY. Recorded tosupport the reversal of accounting entries following fee reversal after the fee-realisation date. |
| 35 | `SC.SHD.DISCOUNT.PL` | `SafekeepHolding_DiscountPl` | TField |  | Description Profit loss category for discount posting. Defaulted from SAFECUSTODY.VALUES but can be overridden. |
| 36 | `SC.SHD.ACT.CHARGES` | `SafekeepHolding_ActCharges` | TField |  | This field will hold the actual charges calculated by the system Validation Rules: This is a NOINPUT field. |
| 37 | `SC.SHD.RESERVED2` | `SafekeepHolding_Reserved2` |  |  |  |
| 38 | `SC.SHD.RESERVED1` | `SafekeepHolding_Reserved1` |  |  |  |
| 39 | `SC.SHD.LOCAL.REF` | `SafekeepHolding_LocalRef` |  |  |  |
| 40 | `SC.SHD.DELIVERY.KEY` | `SafekeepHolding_DeliveryKey` |  |  |  |
| 41 | `SC.SHD.STATEMENT.NOS` | `SafekeepHolding_StatementNos` |  |  |  |
| 42 | `SC.SHD.OVERRIDE` | `SafekeepHolding_Override` |  |  |  |
| 43 | `SC.SHD.RECORD.STATUS` | `SafekeepHolding_RecordStatus` | String |  |  |
| 44 | `SC.SHD.CURR.NO` | `SafekeepHolding_CurrNo` | String |  |  |
| 45 | `SC.SHD.INPUTTER` | `SafekeepHolding_Inputter` |  |  |  |
| 46 | `SC.SHD.DATE.TIME` | `SafekeepHolding_DateTime` |  |  |  |
| 47 | `SC.SHD.AUTHORISER` | `SafekeepHolding_Authoriser` | String |  |  |
| 48 | `SC.SHD.CO.CODE` | `SafekeepHolding_CoCode` | String |  |  |
| 49 | `SC.SHD.DEPT.CODE` | `SafekeepHolding_DeptCode` | String |  |  |
| 50 | `SC.SHD.AUDITOR.CODE` | `SafekeepHolding_AuditorCode` | String |  |  |
| 51 | `SC.SHD.AUDIT.DATE.TIME` | `SafekeepHolding_AuditDateTime` | String |  |  |
