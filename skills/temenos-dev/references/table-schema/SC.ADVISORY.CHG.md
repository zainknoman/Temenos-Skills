# SC.ADVISORY.CHG — Table Schema

> Source: `INSERTS/I_F.SC.ADVISORY.CHG` in `SC_ScfAdvisoryFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ADC.CUSTOMER` | `ScAdvisoryChg_Customer` | TField |  | Identifies the Customer Number of the Portfolio. Validation Rules: Noinput field. |
| 2 | `SC.ADC.PERIOD.FROM` | `ScAdvisoryChg_PeriodFrom` | TField |  | Identifies the Start of the Charge Period for Advisory Charges. Validation Rules: Noinput field. |
| 3 | `SC.ADC.PERIOD.TO` | `ScAdvisoryChg_PeriodTo` | TField |  | Identifies the End Period of the Advisory Charge. Validation Rules: Noinput field. |
| 4 | `SC.ADC.AVG.ASSET.BAL` | `ScAdvisoryChg_AvgAssetBal` | TField |  | Identifies the Average Asset Balance to be used in calculating the Advisory Charge. Validation Rules: Noinput field. |
| 5 | `SC.ADC.INT.MONTHS` | `ScAdvisoryChg_IntMonths` | TField |  | Identifies the Period of the Advisory Charge in Months. Validation Rules: Noinput field. |
| 6 | `SC.ADC.CHARGES.LCY` | `ScAdvisoryChg_ChargesLcy` | TField |  | Identifies the system calculated Advisory Charge in Local Currency, for this portfolio. Updated based on both LocalFeesLcy and TxnBasedFee fields Validation Rules: Noinput field. |
| 7 | `SC.ADC.ACCOUNT.NO` | `ScAdvisoryChg_AccountNo` | TField | Yes | Identfies the Customer Account to be used to post Advisory Charges. Defaulted from the Sec.Acc.Master - Safekeep.Chrg.Acc Validation Rules: Mandatory Input. |
| 8 | `SC.ADC.ACCOUNT.CCY` | `ScAdvisoryChg_AccountCcy` | TField |  | Identifies the Currency of the Account to be used to post Advisory Charges. Validation Rules: Noinput field. |
| 9 | `SC.ADC.ACY.LCY.RATE` | `ScAdvisoryChg_AcyLcyRate` | TField |  | Identifies the Exchange Rate between : Account Currency and Local Currency. Validation Rules: Noinput field. |
| 10 | `SC.ADC.CHARGES.AC.CCY` | `ScAdvisoryChg_ChargesAcCcy` | TField |  | Identifies the resultant Customer Advisory Charge. Validation Rules: Noinput field. |
| 11 | `SC.ADC.LOCAL.FEES.LCY` | `ScAdvisoryChg_LocalFeesLcy` | TField |  | Identifies the Advisory Charge in Local Currency Validation Rules: Noinput field. |
| 12 | `SC.ADC.DISC.AMOUNT.LCY` | `ScAdvisoryChg_DiscAmountLcy` | TField | No | Identifies the Discount Amount to be applied to the the calculated Advisory Charge. Automatically calculated by the system. Validation Rules: Optional Input. |
| 13 | `SC.ADC.CHARGES.TAX.AMT` | `ScAdvisoryChg_ChargesTaxAmt` | TField |  | Identifies the Tax applied to the Advisory Charge. Validation Rules: Noinput field. |
| 14 | `SC.ADC.CHARGES.TAX.LCY` | `ScAdvisoryChg_ChargesTaxLcy` | TField |  | Identifies the Tax applied to the Advisory Charge in Local Currency. Validation Rules: Noinput field. |
| 15 | `SC.ADC.CHARGE.CODE` | `ScAdvisoryChg_ChargeCode` | TField |  | Identifies the Charge Code or Group to be used for Advisory Charges. Defaulted from SCPM.GROUP.CONDITION - Tax.Comm.Code Validation Rules: Noinput field. |
| 16 | `SC.ADC.TAX.CODE` | `ScAdvisoryChg_TaxCode` | TField |  | Identfies the Tax Code used in the calculation of the Tax Amount. Tax Code is extracted from above Charge Code. Validation Rules: Noinput Field. |
| 17 | `SC.ADC.TAX.XRATE` | `ScAdvisoryChg_TaxXrate` | TField |  | Identifies the Exchange Rate between the Tax Amount and the Local Currency. Validation Rules: Noinput field. |
| 18 | `SC.ADC.VALUE.DATE` | `ScAdvisoryChg_ValueDate` | TField |  | Date for posting of management fees. Defaults from SAFECUSTODY VALUES value date if process type field is set to'periodic' otherwise uses today's date. Can be amended by the user. Validation Rules: Standard T24 date field. |
| 19 | `SC.ADC.PROCESS.STAGE` | `ScAdvisoryChg_ProcessStage` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 20 characters may be entered. This is a no input, no copy field. |
| 20 | `SC.ADC.PROCESS.TYPE` | `ScAdvisoryChg_ProcessType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 20 characters may be entered. This is a no input, no copy field. |
| 21 | `SC.ADC.POST.CHARGES` | `ScAdvisoryChg_PostCharges` | TField |  | Y/N flag showing whether the advisory fees are ready for posting. |
| 22 | `SC.ADC.REASON.NARR` | `ScAdvisoryChg_ReasonNarr` |  |  |  |
| 23 | `SC.ADC.GRP.PORT.NO` | `ScAdvisoryChg_GrpPortNo` | TField |  | Primary portfolio id for the group to which this portfolio belongs |
| 24 | `SC.ADC.GRP.ASSET.BAL` | `ScAdvisoryChg_GrpAssetBal` | TField |  | Asset balance for the group to which this portfolio belongs |
| 25 | `SC.ADC.GRP.LCY.FEE` | `ScAdvisoryChg_GrpLcyFee` | TField |  | Local fee total for the group to which this portfolio belongs |
| 26 | `SC.ADC.DELIVERY.KEY` | `ScAdvisoryChg_DeliveryKey` |  |  |  |
| 27 | `SC.ADC.LOCAL.REF` | `ScAdvisoryChg_LocalRef` |  |  |  |
| 28 | `SC.ADC.MTH.END.DATE` | `ScAdvisoryChg_MthEndDate` |  |  |  |
| 29 | `SC.ADC.MTH.LOCAL.LCY` | `ScAdvisoryChg_MthLocalLcy` |  |  |  |
| 30 | `SC.ADC.MTH.XRATE` | `ScAdvisoryChg_MthXrate` |  |  |  |
| 31 | `SC.ADC.MTH.LOCAL.ACY` | `ScAdvisoryChg_MthLocalAcy` |  |  |  |
| 32 | `SC.ADC.ACCRUAL.KEY` | `ScAdvisoryChg_AccrualKey` | TField |  | System-maintained field populated only when SAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL is set to DAILY. Recorded tosupport the reversal of accounting entries following fee reversal after the fee-realisation date. |
| 33 | `SC.ADC.DISCOUNT.PL` | `ScAdvisoryChg_DiscountPl` | TField |  | Description Profit loss category for discount posting. Defaulted from SAFECUSTODY.VALUES but can be overridden. |
| 34 | `SC.ADC.ACT.CHARGES` | `ScAdvisoryChg_ActCharges` | TField |  | This field will hold the actual charges calculated by the system Validation Rules: This is a NOINPUT field. |
| 35 | `SC.ADC.RESERVED3` | `ScAdvisoryChg_Reserved3` |  |  |  |
| 36 | `SC.ADC.TXN.BASED.FEE` | `ScAdvisoryChg_TxnBasedFee` | TField |  | Holds the calculated transaction based fee for the period. Validation Rules CHARGES.LCY field value will be adjusted by amending TXN.BASED.FEE field |
| 37 | `SC.ADC.TXN.COUNT` | `ScAdvisoryChg_TxnCount` | TField |  | Holds the no.of.transaction for the period. Validation Rules This is NOINPUT field. |
| 38 | `SC.ADC.STATEMENT.NOS` | `ScAdvisoryChg_StatementNos` |  |  |  |
| 39 | `SC.ADC.OVERRIDE` | `ScAdvisoryChg_Override` |  |  |  |
| 40 | `SC.ADC.RECORD.STATUS` | `ScAdvisoryChg_RecordStatus` | String |  |  |
| 41 | `SC.ADC.CURR.NO` | `ScAdvisoryChg_CurrNo` | String |  |  |
| 42 | `SC.ADC.INPUTTER` | `ScAdvisoryChg_Inputter` |  |  |  |
| 43 | `SC.ADC.DATE.TIME` | `ScAdvisoryChg_DateTime` |  |  |  |
| 44 | `SC.ADC.AUTHORISER` | `ScAdvisoryChg_Authoriser` | String |  |  |
| 45 | `SC.ADC.CO.CODE` | `ScAdvisoryChg_CoCode` | String |  |  |
| 46 | `SC.ADC.DEPT.CODE` | `ScAdvisoryChg_DeptCode` | String |  |  |
| 47 | `SC.ADC.AUDITOR.CODE` | `ScAdvisoryChg_AuditorCode` | String |  |  |
| 48 | `SC.ADC.AUDIT.DATE.TIME` | `ScAdvisoryChg_AuditDateTime` | String |  |  |
