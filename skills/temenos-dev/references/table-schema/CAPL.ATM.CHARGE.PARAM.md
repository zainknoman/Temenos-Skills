# CAPL.ATM.CHARGE.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.ATM.CHARGE.PARAM` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ATM.CHRG.SHORT.DESCRP` | `CAPLAtmChargeParam_ShortDescrp` |  |  |  |
| 2 | `ATM.CHRG.DESCRIPTION` | `CAPLAtmChargeParam_Description` |  |  |  |
| 3 | `ATM.CHRG.CATEGORY.ACCOUNT` | `CAPLAtmChargeParam_CategoryAccount` |  |  |  |
| 4 | `ATM.CHRG.TXN.CODE.CR` | `CAPLAtmChargeParam_TxnCodeCr` |  |  |  |
| 5 | `ATM.CHRG.TXN.CODE.DR` | `CAPLAtmChargeParam_TxnCodeDr` |  |  |  |
| 6 | `ATM.CHRG.CALCULATION.BASIS` | `CAPLAtmChargeParam_CalculationBasis` |  |  |  |
| 7 | `ATM.CHRG.AC.CHARGE.REQ` | `CAPLAtmChargeParam_AcChargeReq` |  |  |  |
| 8 | `ATM.CHRG.NETWORK.ID` | `CAPLAtmChargeParam_NetworkId` |  |  |  |
| 9 | `ATM.CHRG.CURRENCY` | `CAPLAtmChargeParam_Currency` |  |  |  |
| 10 | `ATM.CHRG.FLAT.AMT` | `CAPLAtmChargeParam_FlatAmt` |  |  |  |
| 11 | `ATM.CHRG.CALC.TYPE` | `CAPLAtmChargeParam_CalcType` |  |  |  |
| 12 | `ATM.CHRG.PERCENTAGE` | `CAPLAtmChargeParam_Percentage` |  |  |  |
| 13 | `ATM.CHRG.UNIT.CHARGE` | `CAPLAtmChargeParam_UnitCharge` |  |  |  |
| 14 | `ATM.CHRG.UPTO.AMT` | `CAPLAtmChargeParam_UptoAmt` |  |  |  |
| 15 | `ATM.CHRG.MIN.AMT` | `CAPLAtmChargeParam_MinAmt` |  |  |  |
| 16 | `ATM.CHRG.MAX.AMT` | `CAPLAtmChargeParam_MaxAmt` |  |  |  |
| 17 | `ATM.CHRG.FT.TXN.TYPE` | `CAPLAtmChargeParam_FtTxnType` |  |  |  |
| 18 | `ATM.CHRG.DEFAULT.CCY` | `CAPLAtmChargeParam_DefaultCcy` |  |  |  |
| 19 | `ATM.CHRG.CHARGE.ROUTINE` | `CAPLAtmChargeParam_ChargeRoutine` |  |  |  |
| 20 | `ATM.CHRG.FT.DEF.CHARGE` | `CAPLAtmChargeParam_FtDefCharge` |  |  |  |
| 21 | `ATM.CHRG.CHARGE.AMT` | `CAPLAtmChargeParam_ChargeAmt` |  |  |  |
| 22 | `ATM.CHRG.FT.DEF.COMMISION` | `CAPLAtmChargeParam_FtDefCommision` |  |  |  |
| 23 | `ATM.CHRG.COMMISSION.AMT` | `CAPLAtmChargeParam_CommissionAmt` |  |  |  |
| 24 | `ATM.CHRG.LOCAL.REF` | `CAPLAtmChargeParam_LocalRef` |  |  |  |
| 25 | `ATM.CHRG.RESERVED.10` | `CAPLAtmChargeParam_Reserved10` |  |  |  |
| 26 | `ATM.CHRG.RESERVED.9` | `CAPLAtmChargeParam_Reserved9` |  |  |  |
| 27 | `ATM.CHRG.RESERVED.8` | `CAPLAtmChargeParam_Reserved8` |  |  |  |
| 28 | `ATM.CHRG.RESERVED.7` | `CAPLAtmChargeParam_Reserved7` |  |  |  |
| 29 | `ATM.CHRG.RESERVED.6` | `CAPLAtmChargeParam_Reserved6` |  |  |  |
| 30 | `ATM.CHRG.RESERVED.5` | `CAPLAtmChargeParam_Reserved5` |  |  |  |
| 31 | `ATM.CHRG.RESERVED.4` | `CAPLAtmChargeParam_Reserved4` |  |  |  |
| 32 | `ATM.CHRG.RESERVED.3` | `CAPLAtmChargeParam_Reserved3` |  |  |  |
| 33 | `ATM.CHRG.RESERVED.2` | `CAPLAtmChargeParam_Reserved2` |  |  |  |
| 34 | `ATM.CHRG.RESERVED.1` | `CAPLAtmChargeParam_Reserved1` |  |  |  |
| 35 | `ATM.CHRG.OVERRIDE` | `CAPLAtmChargeParam_Override` |  |  |  |
| 36 | `ATM.CHRG.RECORD.STATUS` | `CAPLAtmChargeParam_RecordStatus` |  |  |  |
| 37 | `ATM.CHRG.CURR.NO` | `CAPLAtmChargeParam_CurrNo` |  |  |  |
| 38 | `ATM.CHRG.INPUTTER` | `CAPLAtmChargeParam_Inputter` |  |  |  |
| 39 | `ATM.CHRG.DATE.TIME` | `CAPLAtmChargeParam_DateTime` |  |  |  |
| 40 | `ATM.CHRG.AUTHORISER` | `CAPLAtmChargeParam_Authoriser` |  |  |  |
| 41 | `ATM.CHRG.CO.CODE` | `CAPLAtmChargeParam_CoCode` |  |  |  |
| 42 | `ATM.CHRG.DEPT.CODE` | `CAPLAtmChargeParam_DeptCode` |  |  |  |
| 43 | `ATM.CHRG.AUDITOR.CODE` | `CAPLAtmChargeParam_AuditorCode` |  |  |  |
| 44 | `ATM.CHRG.AUDIT.DATE.TIME` | `CAPLAtmChargeParam_AuditDateTime` |  |  |  |
