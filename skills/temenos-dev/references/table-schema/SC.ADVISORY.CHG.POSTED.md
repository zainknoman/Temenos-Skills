# SC.ADVISORY.CHG.POSTED — Table Schema

> Source: `INSERTS/I_F.SC.ADVISORY.CHG.POSTED` in `AM_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SCAD.POS.CUSTOMER` | `ScAdvisoryChgPosted_Customer` | TField |  | This field contains the customer number for which fees are being posted. Validation Rules: Its a noinput field. |
| 2 | `SCAD.POS.PERIOD.FROM` | `ScAdvisoryChgPosted_PeriodFrom` | TField |  | Identifies the Start of the Charge Period for Advisory Charges. Validation Rules: Noinput field. |
| 3 | `SCAD.POS.PERIOD.TO` | `ScAdvisoryChgPosted_PeriodTo` | TField |  | Identifies the End Period of the Advisory Charge. Validation Rules: Noinput field. |
| 4 | `SCAD.POS.AVG.ASSET.BAL` | `ScAdvisoryChgPosted_AvgAssetBal` | TField |  | Identifies the Average Asset Balance to be used in calculating the Advisory Charge. Validation Rules: Noinput field. |
| 5 | `SCAD.POS.INT.MONTHS` | `ScAdvisoryChgPosted_IntMonths` | TField |  | Indentifies the Period of the Advisory Charge in Months. Validation Rules: Noinput field. |
| 6 | `SCAD.POS.CHARGES.LCY` | `ScAdvisoryChgPosted_ChargesLcy` | TField |  | Identifies the system calculated Advisory Charge in Local Currency, for this portfolio. Updated based on both LocalFeesLcy and TxnBasedFee fields Validation Rules: Noinput field. |
| 7 | `SCAD.POS.PREV.CHGS.LCY` | `ScAdvisoryChgPosted_PrevChgsLcy` | TField |  | This field contains the charges that were present before the backvalue transaction that resulted in the recalculation of fees. Validation Rules: Noinput field. |
| 8 | `SCAD.POS.DIFFERENCE.LCY` | `ScAdvisoryChgPosted_DifferenceLcy` | TField |  | This field contains the difference between the previously posted charges and the new charges that have been recalculated. Validation Rules: Noinput field. |
| 9 | `SCAD.POS.ACCOUNT.NO` | `ScAdvisoryChgPosted_AccountNo` | TField | Yes | Identifies the Customer Account to be used to post Advisory Charges. Defaulted from the SEC.ACC.MASTER-SAFEKEEP.CHRG.ACC Validation Rules: Mandatory Input. |
| 10 | `SCAD.POS.ACCOUNT.CCY` | `ScAdvisoryChgPosted_AccountCcy` | TField |  | Identifies the Currency of the Account to be used to post Advisory Charges. Validation Rules: Noinput field. |
| 11 | `SCAD.POS.ACY.LCY.RATE` | `ScAdvisoryChgPosted_AcyLcyRate` | TField |  | Identifies the Exchange Rate between : Account Currency and Local Currency. Validation Rules: Noinput field. |
| 12 | `SCAD.POS.CHARGES.AC.CCY` | `ScAdvisoryChgPosted_ChargesAcCcy` | TField |  | Identifies the resultant Customer Advisory Charge. Validation Rules: Noinput field. |
| 13 | `SCAD.POS.PREV.CHG.AC.CCY` | `ScAdvisoryChgPosted_PrevChgAcCcy` | TField |  | The field contains the charges before the charges were recalculated due to a back-value transaction Validation Rules: Noinput field. |
| 14 | `SCAD.POS.DIFFERENCE.AC.CCY` | `ScAdvisoryChgPosted_DifferenceAcCcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `SCAD.POS.LOCAL.FEES.LCY` | `ScAdvisoryChgPosted_LocalFeesLcy` | TField |  | Identifies the Advisory Charge in Local Currency Validation Rules: Noinput field. |
| 16 | `SCAD.POS.DISC.AMOUNT.LCY` | `ScAdvisoryChgPosted_DiscAmountLcy` | TField | No | Identifies the Discount Amount to be applied to the the calculated Advisory Charge. Automatically calculated by the system. Validation Rules: Optional Input. |
| 17 | `SCAD.POS.CHARGES.TAX.AMT` | `ScAdvisoryChgPosted_ChargesTaxAmt` | TField |  | Identifies the Tax applied to the Advisory Charge. Validation Rules: Noinput field. |
| 18 | `SCAD.POS.CHARGES.TAX.LCY` | `ScAdvisoryChgPosted_ChargesTaxLcy` | TField |  | Identifies the Tax applied to the Advisory Charge in Local Currency. Validation Rules: Noinput field. |
| 19 | `SCAD.POS.CHARGE.CODE` | `ScAdvisoryChgPosted_ChargeCode` | TField |  | Identifies the Charge Code or Group to be used for Advisory Charges. Defaulted from SCPM.GROUP.CONDITION - Tax.Comm.Code Validation Rules: Noinput field. |
| 20 | `SCAD.POS.TAX.CODE` | `ScAdvisoryChgPosted_TaxCode` | TField |  | Identfies the Tax Code used in the calculation of the Tax Amount. Tax Code is extracted from above Charge Code. Validation Rules: Noinput Field. |
| 21 | `SCAD.POS.TAX.XRATE` | `ScAdvisoryChgPosted_TaxXrate` | TField |  | Identifies the Exchange Rate between the Tax Amount and the Local Currency. Validation Rules: Noinput field. |
| 22 | `SCAD.POS.VALUE.DATE` | `ScAdvisoryChgPosted_ValueDate` | TField |  | Date for posting of management fees. Defaults from SAFECUSTODY VALUES value date if process type field is set to'periodic' otherwise uses today's date. Can be amended by the user. Validation Rules: Standard T24 date field. |
| 23 | `SCAD.POS.PROCESS.STAGE` | `ScAdvisoryChgPosted_ProcessStage` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 20 characters may be entered. This is a no input, no copy field. |
| 24 | `SCAD.POS.PROCESS.TYPE` | `ScAdvisoryChgPosted_ProcessType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 20 characters may be entered. This is a no input, no copy field. |
| 25 | `SCAD.POS.SYS.GENERATED` | `ScAdvisoryChgPosted_SysGenerated` | TField |  | Specifies whether the record was modified after being generated. The status is automatically updated. Validation Rules: Noinput field. |
| 26 | `SCAD.POS.POST.CHARGES` | `ScAdvisoryChgPosted_PostCharges` | TField |  | Y/N flag showing whether the advisory fees are ready for posting. Validation Rules: Noinput field. |
| 27 | `SCAD.POS.REASON.NARR` | `ScAdvisoryChgPosted_ReasonNarr` |  |  |  |
| 28 | `SCAD.POS.DELIVERY.KEY` | `ScAdvisoryChgPosted_DeliveryKey` |  |  |  |
| 29 | `SCAD.POS.ACCRUAL.KEY` | `ScAdvisoryChgPosted_AccrualKey` | TField |  | System-maintained field populated only when SAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL is set to DAILY. Recorded tosupport the reversal of accounting entries following fee reversal after the fee-realisation date. |
| 30 | `SCAD.POS.ADJUST.FEES` | `ScAdvisoryChgPosted_AdjustFees` | TField |  |  |
| 31 | `SCAD.POS.ADJUST.VALUE.DATE` | `ScAdvisoryChgPosted_AdjustValueDate` | TField |  |  |
| 32 | `SCAD.POS.DISCOUNT.PL` | `ScAdvisoryChgPosted_DiscountPl` | TField |  |  |
| 33 | `SCAD.POS.RESERVED6` | `ScAdvisoryChgPosted_Reserved6` | TField |  |  |
| 34 | `SCAD.POS.RESERVED5` | `ScAdvisoryChgPosted_Reserved5` | TField |  |  |
| 35 | `SCAD.POS.TXN.BASED.FEE` | `ScAdvisoryChgPosted_TxnBasedFee` | TField |  | Holds the calculated transaction based fee for the period. Validation Rules CHARGES.LCY field value will be adjusted by amending TXN.BASED.FEE field |
| 36 | `SCAD.POS.TXN.COUNT` | `ScAdvisoryChgPosted_TxnCount` | TField |  | Holds the no.of.transaction for the period. Validation Rules This is NOINPUT field. |
| 37 | `SCAD.POS.RESERVED2` | `ScAdvisoryChgPosted_Reserved2` |  |  |  |
| 38 | `SCAD.POS.RESERVED1` | `ScAdvisoryChgPosted_Reserved1` | TField |  |  |
| 39 | `SCAD.POS.LOCAL.REF` | `ScAdvisoryChgPosted_LocalRef` |  |  |  |
| 40 | `SCAD.POS.STATEMENT.NOS` | `ScAdvisoryChgPosted_StatementNos` |  |  |  |
| 41 | `SCAD.POS.OVERRIDE` | `ScAdvisoryChgPosted_Override` |  |  |  |
| 42 | `SCAD.POS.RECORD.STATUS` | `ScAdvisoryChgPosted_RecordStatus` | String |  |  |
| 43 | `SCAD.POS.CURR.NO` | `ScAdvisoryChgPosted_CurrNo` | String |  |  |
| 44 | `SCAD.POS.INPUTTER` | `ScAdvisoryChgPosted_Inputter` |  |  |  |
| 45 | `SCAD.POS.DATE.TIME` | `ScAdvisoryChgPosted_DateTime` |  |  |  |
| 46 | `SCAD.POS.AUTHORISER` | `ScAdvisoryChgPosted_Authoriser` | String |  |  |
| 47 | `SCAD.POS.CO.CODE` | `ScAdvisoryChgPosted_CoCode` | String |  |  |
| 48 | `SCAD.POS.DEPT.CODE` | `ScAdvisoryChgPosted_DeptCode` | String |  |  |
| 49 | `SCAD.POS.AUDITOR.CODE` | `ScAdvisoryChgPosted_AuditorCode` | String |  |  |
| 50 | `SCAD.POS.AUDIT.DATE.TIME` | `ScAdvisoryChgPosted_AuditDateTime` | String |  |  |
