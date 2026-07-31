# SAFECUSTODY.VALUES — Table Schema

> Source: `INSERTS/I_F.SAFECUSTODY.VALUES` in `SC_ScfConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SCV.CHARGE.TYPE` | `SafecustodyValues_ChargeType` |  |  |  |
| 2 | `SC.SCV.DEBIT.TXN.CODE` | `SafecustodyValues_DebitTxnCode` |  |  |  |
| 3 | `SC.SCV.CREDIT.TXN.CODE` | `SafecustodyValues_CreditTxnCode` |  |  |  |
| 4 | `SC.SCV.CR.CATEG.CODE` | `SafecustodyValues_CrCategCode` |  |  |  |
| 5 | `SC.SCV.REV.CATEG.CODE` | `SafecustodyValues_RevCategCode` |  |  |  |
| 6 | `SC.SCV.REV.CUT.OFF` | `SafecustodyValues_RevCutOff` |  |  |  |
| 7 | `SC.SCV.COMPANY.CALC` | `SafecustodyValues_CompanyCalc` |  |  |  |
| 8 | `SC.SCV.COMPANY.POST` | `SafecustodyValues_CompanyPost` |  |  |  |
| 9 | `SC.SCV.CHARGE.FREQ` | `SafecustodyValues_ChargeFreq` |  |  |  |
| 10 | `SC.SCV.ACCRUAL.CATEG` | `SafecustodyValues_AccrualCateg` |  |  |  |
| 11 | `SC.SCV.LAST.RUN.DATE` | `SafecustodyValues_LastRunDate` |  |  |  |
| 12 | `SC.SCV.POST.CHARGES` | `SafecustodyValues_PostCharges` |  |  |  |
| 13 | `SC.SCV.VALUE.DATE` | `SafecustodyValues_ValueDate` |  |  |  |
| 14 | `SC.SCV.EXT.RECORD.BY` | `SafecustodyValues_ExtRecordBy` |  |  |  |
| 15 | `SC.SCV.MAN.ACC.CALC` | `SafecustodyValues_ManAccCalc` |  |  |  |
| 16 | `SC.SCV.INT.ROUND.UP` | `SafecustodyValues_IntRoundUp` |  |  |  |
| 17 | `SC.SCV.CALC.TYPE` | `SafecustodyValues_CalcType` |  |  |  |
| 18 | `SC.SCV.PERIOD.START` | `SafecustodyValues_PeriodStart` |  |  |  |
| 19 | `SC.SCV.PERIOD.END` | `SafecustodyValues_PeriodEnd` |  |  |  |
| 20 | `SC.SCV.NO.OF.MONTHS` | `SafecustodyValues_NoOfMonths` |  |  |  |
| 21 | `SC.SCV.DELIV.START` | `SafecustodyValues_DelivStart` |  |  |  |
| 22 | `SC.SCV.DELIV.END` | `SafecustodyValues_DelivEnd` |  |  |  |
| 23 | `SC.SCV.DEF.VALUE.DATE` | `SafecustodyValues_DefValueDate` |  |  |  |
| 24 | `SC.SCV.VAL.WORKING.DAY` | `SafecustodyValues_ValWorkingDay` |  |  |  |
| 25 | `SC.SCV.PERFORM.ACCRUAL` | `SafecustodyValues_PerformAccrual` |  |  |  |
| 26 | `SC.SCV.DAILY.EXTRACT` | `SafecustodyValues_DailyExtract` |  |  |  |
| 27 | `SC.SCV.FEE.GROUP` | `SafecustodyValues_FeeGroup` |  |  |  |
| 28 | `SC.SCV.DAILY.ACCR.TYPE` | `SafecustodyValues_DailyAccrType` |  |  |  |
| 29 | `SC.SCV.DAILY.POST.DATE` | `SafecustodyValues_DailyPostDate` |  |  |  |
| 30 | `SC.SCV.DAY.BASIS` | `SafecustodyValues_DayBasis` |  |  |  |
| 31 | `SC.SCV.OTHER.ASSET` | `SafecustodyValues_OtherAsset` |  |  |  |
| 32 | `SC.SCV.SEL.FIELD` | `SafecustodyValues_SelField` |  |  |  |
| 33 | `SC.SCV.OPERATION` | `SafecustodyValues_Operation` |  |  |  |
| 34 | `SC.SCV.FIELD.VALUE` | `SafecustodyValues_FieldValue` |  |  |  |
| 35 | `SC.SCV.INCL.NO.POSN` | `SafecustodyValues_InclNoPosn` |  |  |  |
| 36 | `SC.SCV.CALC.ZERO.BASIS` | `SafecustodyValues_CalcZeroBasis` |  |  |  |
| 37 | `SC.SCV.GROUP.ACCRUAL` | `SafecustodyValues_GroupAccrual` |  |  |  |
| 38 | `SC.SCV.DISCOUNT.PL` | `SafecustodyValues_DiscountPl` |  |  |  |
| 39 | `SC.SCV.COUNTRY.CHECK` | `SafecustodyValues_CountryCheck` |  |  |  |
| 40 | `SC.SCV.DAILY.FEE.ESTIMATE` | `SafecustodyValues_DailyFeeEstimate` |  |  |  |
| 41 | `SC.SCV.POST.FEES.ON.SALE` | `SafecustodyValues_PostFeesOnSale` |  |  |  |
| 42 | `SC.SCV.DEP.CHG.CR.CODE` | `SafecustodyValues_DepChgCrCode` | TField | Yes | Specifies the transaction code to be used in respect of Depository charges. Validation Rules: 1-10(Max Value) numeric characters Transaction Code.(Mandatory Input) The Maximum value is specified in EB.OBJECT for TRANSACTION. Must exist on the TRANSACTION table. |
| 43 | `SC.SCV.DEP.CHG.CATEG.CODE` | `SafecustodyValues_DepChgCategCode` | TField | Yes | Specifies the category code to which the Depository charge is to be posted. Validation Rules: 5 numeric characters. (Mandatory Input) Must exist on the CATEGORY table. Must be in the range 50000 to 59999 |
| 44 | `SC.SCV.PRODUCT.CATEGORY` | `SafecustodyValues_ProductCategory` | TField |  | Allow the specification of the product category under which the accounting entries will be raised. If notspecified will default to 22000. NOINPUT field, reserved for future use. |
| 45 | `SC.SCV.ADV.EXCL.EXT.POS` | `SafecustodyValues_AdvExclExtPos` | TField |  | 3 character alpha numeric input Field to determine whether advisory charges are to be excluded for external positions. Value of YES will excludefrom calculation. |
| 46 | `SC.SCV.CLOSURE.DAYS` | `SafecustodyValues_ClosureDays` | TField |  | When the portfolio is closed in middle of a month, for average balance calculation will consider the no of daysuntil the month end if the field is set. If this is set as ALL, this is applicable for both safe keeping and advisory other wise this will be applicablefor the individual fees definition. Validation Rules: Allowed values will be SC, IC, ALL or Blank |
| 47 | `SC.SCV.RESERVED07` | `SafecustodyValues_Reserved07` |  |  |  |
| 48 | `SC.SCV.RESERVED06` | `SafecustodyValues_Reserved06` |  |  |  |
| 49 | `SC.SCV.RESERVED05` | `SafecustodyValues_Reserved05` | TField |  |  |
| 50 | `SC.SCV.RESERVED04` | `SafecustodyValues_Reserved04` | TField |  |  |
| 51 | `SC.SCV.RESERVED03` | `SafecustodyValues_Reserved03` | TField |  |  |
| 52 | `SC.SCV.RESERVED02` | `SafecustodyValues_Reserved02` | TField |  |  |
| 53 | `SC.SCV.RESERVED01` | `SafecustodyValues_Reserved01` | TField |  |  |
| 54 | `SC.SCV.LOCAL.REF` | `SafecustodyValues_LocalRef` |  |  |  |
| 55 | `SC.SCV.OVERRIDE` | `SafecustodyValues_Override` |  |  |  |
| 56 | `SC.SCV.RECORD.STATUS` | `SafecustodyValues_RecordStatus` | String |  |  |
| 57 | `SC.SCV.CURR.NO` | `SafecustodyValues_CurrNo` | String |  |  |
| 58 | `SC.SCV.INPUTTER` | `SafecustodyValues_Inputter` |  |  |  |
| 59 | `SC.SCV.DATE.TIME` | `SafecustodyValues_DateTime` |  |  |  |
| 60 | `SC.SCV.AUTHORISER` | `SafecustodyValues_Authoriser` | String |  |  |
| 61 | `SC.SCV.CO.CODE` | `SafecustodyValues_CoCode` | String |  |  |
| 62 | `SC.SCV.DEPT.CODE` | `SafecustodyValues_DeptCode` | String |  |  |
| 63 | `SC.SCV.AUDITOR.CODE` | `SafecustodyValues_AuditorCode` | String |  |  |
| 64 | `SC.SCV.AUDIT.DATE.TIME` | `SafecustodyValues_AuditDateTime` | String |  |  |
