# AA.PRICING.ADJUSTMENTS — Table Schema

> Source: `INSERTS/I_F.AA.PRICING.ADJUSTMENTS` in `AA_PricingAdjustments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRICADJ.ACTIVITY` | `AaSimPricingAdjustments_Activity` |  |  |  |
| 2 | `AA.PRICADJ.ACTION` | `AaSimPricingAdjustments_Action` |  |  |  |
| 3 | `AA.PRICADJ.PRICING.PROPERTY` | `AaSimPricingAdjustments_PricingProperty` |  |  |  |
| 4 | `AA.PRICADJ.ADJUST.TYPE` | `AaSimPricingAdjustments_AdjustType` |  |  |  |
| 5 | `AA.PRICADJ.ADJUSTMENT` | `AaSimPricingAdjustments_Adjustment` |  |  |  |
| 6 | `AA.PRICADJ.RESERVED.10` | `AaSimPricingAdjustments_Reserved10` |  |  |  |
| 7 | `AA.PRICADJ.RESERVED.9` | `AaSimPricingAdjustments_Reserved9` |  |  |  |
| 11 | `AA.PRICADJ.ADJUST.REASON` | `AaSimPricingAdjustments_AdjustReason` |  |  |  |
| 12 | `AA.PRICADJ.ADJUST.EXPIRY.DATE` | `AaSimPricingAdjustments_AdjustExpiryDate` |  |  |  |
| 15 | `AA.PRICADJ.RESERVED.8` | `AaSimPricingAdjustments_Reserved8` |  |  |  |
| 16 | `AA.PRICADJ.RESERVED.7` | `AaSimPricingAdjustments_Reserved7` |  |  |  |
| 17 | `AA.PRICADJ.RESERVED.6` | `AaSimPricingAdjustments_Reserved6` |  |  |  |
| 18 | `AA.PRICADJ.SYS.RESERVE2` | `AaSimPricingAdjustments_SysReserve2` |  |  |  |
| 19 | `AA.PRICADJ.SYS.RESERVE1` | `AaSimPricingAdjustments_SysReserve1` |  |  |  |
| 20 | `AA.PRICADJ.DEFAULT.ATTR.OPTION` | `AaSimPricingAdjustments_DefaultAttrOption` |  |  |  |
| 21 | `AA.PRICADJ.DEFAULT.NEGOTIABLE` | `AaSimPricingAdjustments_DefaultNegotiable` |  |  |  |
| 22 | `AA.PRICADJ.NR.ATTRIBUTE` | `AaSimPricingAdjustments_NrAttribute` |  |  |  |
| 23 | `AA.PRICADJ.NR.OPTIONS` | `AaSimPricingAdjustments_NrOptions` |  |  |  |
| 24 | `AA.PRICADJ.NR.ATTRIBUTE.RULE` | `AaSimPricingAdjustments_NrAttributeRule` |  |  |  |
| 25 | `AA.PRICADJ.NR.VALUE.SOURCE` | `AaSimPricingAdjustments_NrValueSource` |  |  |  |
| 26 | `AA.PRICADJ.NR.STD.COMP` | `AaSimPricingAdjustments_NrStdComp` |  |  |  |
| 27 | `AA.PRICADJ.NR.TYPE` | `AaSimPricingAdjustments_NrType` |  |  |  |
| 28 | `AA.PRICADJ.NR.VALUE` | `AaSimPricingAdjustments_NrValue` |  |  |  |
| 29 | `AA.PRICADJ.NR.MESSAGE` | `AaSimPricingAdjustments_NrMessage` |  |  |  |
| 30 | `AA.PRICADJ.NEGOTIATED.FLDS` | `AaSimPricingAdjustments_NegotiatedFlds` |  |  |  |
| 31 | `AA.PRICADJ.ID.COMP.1` | `AaSimPricingAdjustments_IdComp1` |  |  |  |
| 32 | `AA.PRICADJ.ID.COMP.2` | `AaSimPricingAdjustments_IdComp2` |  |  |  |
| 33 | `AA.PRICADJ.ID.COMP.3` | `AaSimPricingAdjustments_IdComp3` |  |  |  |
| 34 | `AA.PRICADJ.ID.COMP.4` | `AaSimPricingAdjustments_IdComp4` |  |  |  |
| 35 | `AA.PRICADJ.ID.COMP.5` | `AaSimPricingAdjustments_IdComp5` |  |  |  |
| 36 | `AA.PRICADJ.ID.COMP.6` | `AaSimPricingAdjustments_IdComp6` |  |  |  |
| 37 | `AA.PRICADJ.RESERVED2.ID` | `AaSimPricingAdjustments_Reserved2Id` |  |  |  |
| 38 | `AA.PRICADJ.TARGET.PRODUCT` | `AaSimPricingAdjustments_TargetProduct` |  |  |  |
| 39 | `AA.PRICADJ.RECORD.STATUS` | `AaSimPricingAdjustments_RecordStatus` |  |  |  |
| 40 | `AA.PRICADJ.CURR.NO` | `AaSimPricingAdjustments_CurrNo` |  |  |  |
| 41 | `AA.PRICADJ.INPUTTER` | `AaSimPricingAdjustments_Inputter` |  |  |  |
| 42 | `AA.PRICADJ.DATE.TIME` | `AaSimPricingAdjustments_DateTime` |  |  |  |
| 43 | `AA.PRICADJ.AUTHORISER` | `AaSimPricingAdjustments_Authoriser` |  |  |  |
| 44 | `AA.PRICADJ.CO.CODE` | `AaSimPricingAdjustments_CoCode` |  |  |  |
| 45 | `AA.PRICADJ.DEPT.CODE` | `AaSimPricingAdjustments_DeptCode` |  |  |  |
| 46 | `AA.PRICADJ.AUDITOR.CODE` | `AaSimPricingAdjustments_AuditorCode` |  |  |  |
| 47 | `AA.PRICADJ.AUDIT.DATE.TIME` | `AaSimPricingAdjustments_AuditDateTime` |  |  |  |
