# AA.FEES — Table Schema

> Source: `INSERTS/I_F.AA.FEES` in `AA_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.FEE.DESCRIPTION` | `AaSimFee_FeeActivity` |  |  |  |
| 2 | `AA.FEE.RESERVED` | `AaSimFee_FeeAction` |  |  |  |
| 3 | `AA.FEE.PROPERTY` | `AaSimFee_FeeProperty` |  |  |  |
| 4 | `AA.FEE.TYPE` | `AaSimFee_FeeType` |  |  |  |
| 5 | `AA.FEE.CONTEXT.EXPRESSION` | `AaSimFee_FeeContextExpression` |  |  |  |
| 6 | `AA.FEE.RESERVED.9` | `AaSimFee_FeeReserved9` |  |  |  |
| 7 | `AA.FEE.RESERVED.8` | `AaSimFee_FeeReserved8` |  |  |  |
| 8 | `AA.FEE.RESERVED.7` | `AaSimFee_FeeReserved7` |  |  |  |
| 9 | `AA.FEE.RESERVED.6` | `AaSimFee_FeeReserved6` |  |  |  |
| 10 | `AA.FEE.RESERVED.5` | `AaSimFee_FeeReserved5` |  |  |  |
| 11 | `AA.FEE.RESERVED.4` | `AaSimFee_FeeReserved4` |  |  |  |
| 12 | `AA.FEE.RESERVED.3` | `AaSimFee_FeeReserved3` |  |  |  |
| 13 | `AA.FEE.RESERVED.2` | `AaSimFee_FeeReserved2` |  |  |  |
| 14 | `AA.FEE.RESERVED.1` | `AaSimFee_FeeReserved1` |  |  |  |
| 15 | `AA.FEE.TIERS` | `AaSimFee_FeeTiers` |  |  |  |
| 16 | `AA.FEE.TIER.VALUE.TYPE` | `AaSimFee_FeeTierValueType` |  |  |  |
| 17 | `AA.FEE.CALC.VALUE` | `AaSimFee_FeeCalcValue` |  |  |  |
| 18 | `AA.FEE.TIER.START` | `AaSimFee_FeeTierStart` |  |  |  |
| 19 | `AA.FEE.MIN.AMOUNT` | `AaSimFee_FeeMinAmount` |  |  |  |
| 20 | `AA.FEE.MAX.AMOUNT` | `AaSimFee_FeeMaxAmount` |  |  |  |
| 21 | `AA.FEE.CURRENCY` | `AaSimFee_FeeCurrency` |  |  |  |
| 22 | `AA.FEE.ROUNDING.RULE` | `AaSimFee_FeeRoundingRule` |  |  |  |
| 23 | `AA.FEE.INTERNAL.BOOKING` | `AaSimFee_FeeInternalBooking` |  |  |  |
| 24 | `AA.FEE.LOCAL.REF` | `AaSimFee_FeeLocalRef` |  |  |  |
| 25 | `AA.FEE.PR.ATTRIBUTE` | `AaSimFee_FeePrAttribute` |  |  |  |
| 26 | `AA.FEE.PR.VALUE` | `AaSimFee_FeePrValue` |  |  |  |
| 27 | `AA.FEE.PR.BRK.RES` | `AaSimFee_FeePrBrkRes` |  |  |  |
| 28 | `AA.FEE.PR.BRK.MSG` | `AaSimFee_FeePrBrkMsg` |  |  |  |
| 29 | `AA.FEE.PR.BRK.CHARGE` | `AaSimFee_FeePrBrkCharge` |  |  |  |
| 30 | `AA.FEE.PR.RESERVED.3` | `AaSimFee_FeePrReserved3` |  |  |  |
| 31 | `AA.FEE.PR.RESERVED.2` | `AaSimFee_FeePrReserved2` |  |  |  |
| 32 | `AA.FEE.PR.RESERVED.1` | `AaSimFee_FeePrReserved1` |  |  |  |
| 33 | `AA.FEE.PR.APP.METHOD` | `AaSimFee_FeePrAppMethod` |  |  |  |
| 34 | `AA.FEE.PR.APP.PERIOD` | `AaSimFee_FeePrAppPeriod` |  |  |  |
| 35 | `AA.FEE.SYS.RESERVE7` | `AaSimFee_FeeSysReserve7` |  |  |  |
| 36 | `AA.FEE.SYS.RESERVE6` | `AaSimFee_FeeSysReserve6` |  |  |  |
| 37 | `AA.FEE.OWNING.COMPANY` | `AaSimFee_FeeOwningCompany` |  |  |  |
| 38 | `AA.FEE.API.ATTRIBUTE` | `AaSimFee_FeeApiAttribute` |  |  |  |
| 39 | `AA.FEE.SYS.RESERVE3` | `AaSimFee_FeeSysReserve3` |  |  |  |
| 40 | `AA.FEE.SYS.RESERVE2` | `AaSimFee_FeeSysReserve2` |  |  |  |
| 41 | `AA.FEE.SYS.RESERVE1` | `AaSimFee_FeeSysReserve1` |  |  |  |
| 42 | `AA.FEE.DEFAULT.ATTR.OPTION` | `AaSimFee_FeeDefaultAttrOption` |  |  |  |
| 43 | `AA.FEE.DEFAULT.NEGOTIABLE` | `AaSimFee_FeeDefaultNegotiable` |  |  |  |
| 44 | `AA.FEE.NR.ATTRIBUTE` | `AaSimFee_FeeNrAttribute` |  |  |  |
| 45 | `AA.FEE.NR.OPTIONS` | `AaSimFee_FeeNrOptions` |  |  |  |
| 46 | `AA.FEE.NR.ATTRIBUTE.RULE` | `AaSimFee_FeeNrAttributeRule` |  |  |  |
| 47 | `AA.FEE.NR.VALUE.SOURCE` | `AaSimFee_FeeNrValueSource` |  |  |  |
| 48 | `AA.FEE.NR.STD.COMP` | `AaSimFee_FeeNrStdComp` |  |  |  |
| 49 | `AA.FEE.NR.TYPE` | `AaSimFee_FeeNrType` |  |  |  |
| 50 | `AA.FEE.NR.VALUE` | `AaSimFee_FeeNrValue` |  |  |  |
| 51 | `AA.FEE.NR.MESSAGE` | `AaSimFee_FeeNrMessage` |  |  |  |
| 52 | `AA.FEE.CHANGED.FIELDS` | `AaSimFee_FeeChangedFields` |  |  |  |
| 53 | `AA.FEE.NEGOTIATED.FLDS` | `AaSimFee_FeeNegotiatedFlds` |  |  |  |
| 54 | `AA.FEE.ID.COMP.1` | `AaSimFee_FeeIdComp1` |  |  |  |
| 55 | `AA.FEE.ID.COMP.2` | `AaSimFee_FeeIdComp2` |  |  |  |
| 56 | `AA.FEE.ID.COMP.3` | `AaSimFee_FeeIdComp3` |  |  |  |
| 57 | `AA.FEE.ID.COMP.4` | `AaSimFee_FeeIdComp4` |  |  |  |
| 58 | `AA.FEE.ID.COMP.5` | `AaSimFee_FeeIdComp5` |  |  |  |
| 59 | `AA.FEE.ID.COMP.6` | `AaSimFee_FeeIdComp6` |  |  |  |
| 60 | `AA.FEE.RESERVED2.ID` | `AaSimFee_FeeReserved2Id` |  |  |  |
| 61 | `AA.FEE.TARGET.PRODUCT` | `AaSimFee_FeeTargetProduct` |  |  |  |
| 62 | `AA.FEE.STMT.NOS` | `AaSimFee_FeeStmtNos` |  |  |  |
| 63 | `AA.FEE.OVERRIDE` | `AaSimFee_FeeOverride` |  |  |  |
| 64 | `AA.FEE.RECORD.STATUS` | `AaSimFee_FeeRecordStatus` |  |  |  |
| 65 | `AA.FEE.CURR.NO` | `AaSimFee_FeeCurrNo` |  |  |  |
| 66 | `AA.FEE.INPUTTER` | `AaSimFee_FeeInputter` |  |  |  |
| 67 | `AA.FEE.DATE.TIME` | `AaSimFee_FeeDateTime` |  |  |  |
| 68 | `AA.FEE.AUTHORISER` | `AaSimFee_FeeAuthoriser` |  |  |  |
| 69 | `AA.FEE.CO.CODE` | `AaSimFee_FeeCoCode` |  |  |  |
| 70 | `AA.FEE.DEPT.CODE` | `AaSimFee_FeeDeptCode` |  |  |  |
| 71 | `AA.FEE.AUDITOR.CODE` | `AaSimFee_FeeAuditorCode` |  |  |  |
| 72 | `AA.FEE.AUDIT.DATE.TIME` | `AaSimFee_FeeAuditDateTime` |  |  |  |
| 73 | `AA.FEE.PER.UNIT` | `AaSimFee_FeePerUnit` |  |  |  |
| 74 | `AA.FEE.CHARGE.CURRENCY` | `AaSimFee_FeeChargeCurrency` |  |  |  |
