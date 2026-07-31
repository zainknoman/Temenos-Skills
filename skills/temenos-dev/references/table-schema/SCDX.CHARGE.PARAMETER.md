# SCDX.CHARGE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SCDX.CHARGE.PARAMETER` in `SC_SctFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SD.CP.CHARGE.TAX.TYPE` | `ScdxChargeParameter_ChargeTaxType` |  |  |  |
| 2 | `SD.CP.CHARGE.TAX.DESC` | `ScdxChargeParameter_ChargeTaxDesc` |  |  |  |
| 3 | `SD.CP.CHARGE.TAX.CAT` | `ScdxChargeParameter_ChargeTaxCat` |  |  |  |
| 4 | `SD.CP.CHG.TAX.CR.CODE` | `ScdxChargeParameter_ChgTaxCrCode` |  |  |  |
| 5 | `SD.CP.CHG.TAX.DR.CODE` | `ScdxChargeParameter_ChgTaxDrCode` |  |  |  |
| 6 | `SD.CP.CHG.TAX.CUST.BROK` | `ScdxChargeParameter_ChgTaxCustBrok` |  |  |  |
| 7 | `SD.CP.PRIORITY` | `ScdxChargeParameter_Priority` |  |  |  |
| 8 | `SD.CP.CHARGE.TAX.OPERAND` | `ScdxChargeParameter_ChargeTaxOperand` |  |  |  |
| 9 | `SD.CP.TYPE` | `ScdxChargeParameter_Type` |  |  |  |
| 10 | `SD.CP.DERIVED.AMOUNT` | `ScdxChargeParameter_DerivedAmount` |  |  |  |
| 11 | `SD.CP.POST.LCY` | `ScdxChargeParameter_PostLcy` |  |  |  |
| 12 | `SD.CP.MARKET.FEES` | `ScdxChargeParameter_MarketFees` |  |  |  |
| 13 | `SD.CP.RESERVED.17` | `ScdxChargeParameter_Reserved17` |  |  |  |
| 14 | `SD.CP.RESERVED.16` | `ScdxChargeParameter_Reserved16` |  |  |  |
| 15 | `SD.CP.RESERVED.15` | `ScdxChargeParameter_Reserved15` |  |  |  |
| 16 | `SD.CP.RESERVED.14` | `ScdxChargeParameter_Reserved14` |  |  |  |
| 17 | `SD.CP.RESERVED.13` | `ScdxChargeParameter_Reserved13` |  |  |  |
| 18 | `SD.CP.RESERVED.12` | `ScdxChargeParameter_Reserved12` |  |  |  |
| 19 | `SD.CP.RESERVED.11` | `ScdxChargeParameter_Reserved11` |  |  |  |
| 20 | `SD.CP.ADDL.CRITERIA` | `ScdxChargeParameter_AddlCriteria` |  |  |  |
| 21 | `SD.CP.RESERVED.9` | `ScdxChargeParameter_Reserved9` | TField |  |  |
| 22 | `SD.CP.RESERVED.8` | `ScdxChargeParameter_Reserved8` | TField |  |  |
| 23 | `SD.CP.RESERVED.7` | `ScdxChargeParameter_Reserved7` | TField |  |  |
| 24 | `SD.CP.RESERVED.6` | `ScdxChargeParameter_Reserved6` | TField |  |  |
| 25 | `SD.CP.RESERVED.5` | `ScdxChargeParameter_Reserved5` | TField |  |  |
| 26 | `SD.CP.RESERVED.4` | `ScdxChargeParameter_Reserved4` | TField |  |  |
| 27 | `SD.CP.RESERVED.3` | `ScdxChargeParameter_Reserved3` | TField |  |  |
| 28 | `SD.CP.RESERVED.2` | `ScdxChargeParameter_Reserved2` | TField |  |  |
| 29 | `SD.CP.RESERVED.1` | `ScdxChargeParameter_Reserved1` | TField |  |  |
| 30 | `SD.CP.LOCAL.REF` | `ScdxChargeParameter_LocalRef` |  |  |  |
| 31 | `SD.CP.OVERRIDE` | `ScdxChargeParameter_Override` |  |  |  |
| 32 | `SD.CP.RECORD.STATUS` | `ScdxChargeParameter_RecordStatus` | String |  |  |
| 33 | `SD.CP.CURR.NO` | `ScdxChargeParameter_CurrNo` | String |  |  |
| 34 | `SD.CP.INPUTTER` | `ScdxChargeParameter_Inputter` |  |  |  |
| 35 | `SD.CP.DATE.TIME` | `ScdxChargeParameter_DateTime` |  |  |  |
| 36 | `SD.CP.AUTHORISER` | `ScdxChargeParameter_Authoriser` | String |  |  |
| 37 | `SD.CP.CO.CODE` | `ScdxChargeParameter_CoCode` | String |  |  |
| 38 | `SD.CP.DEPT.CODE` | `ScdxChargeParameter_DeptCode` | String |  |  |
| 39 | `SD.CP.AUDITOR.CODE` | `ScdxChargeParameter_AuditorCode` | String |  |  |
| 40 | `SD.CP.AUDIT.DATE.TIME` | `ScdxChargeParameter_AuditDateTime` | String |  |  |
| 41 | `SD.CP.SWIFT.QUAL.TR` | `ScdxChargeParameter_SwiftQualTr` |  |  |  |
